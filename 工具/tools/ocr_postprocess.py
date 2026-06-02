import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


PROMO_TEXT_PATTERNS = (
    "公众号",
    "微信",
    "有机研",
    "45550060",
    "二维码",
)

IMAGE_TAG_PATTERN = re.compile(r'<(?:div[^>]*>\s*)?<img\s+[^>]*src="([^"]+)"[^>]*>\s*(?:</div>)?', re.I)
DOC_PAGE_PATTERN = re.compile(r"^doc_(\d+)\.md$", re.I)
BOX_PATTERN = re.compile(r"_(\d+)_(\d+)_(\d+)_(\d+)\.[^.]+$", re.I)
INLINE_MATH_PATTERN = re.compile(r"(?<!\$)\$(?!\$)([^\n$]*?)(?<!\$)\$(?!\$)")


@dataclass
class PostprocessResult:
    markdown: str
    manifest: dict


def sort_doc_pages(paths) -> list[Path]:
    return sorted((Path(path) for path in paths), key=_doc_page_key)


def _doc_page_key(path: Path) -> tuple[int, str]:
    match = DOC_PAGE_PATTERN.match(path.name)
    if match:
        return (int(match.group(1)), path.name)
    return (10**9, path.name)


def page_number(path: Path) -> int:
    match = DOC_PAGE_PATTERN.match(path.name)
    if not match:
        raise ValueError(f"Not a PaddleOCR page markdown file: {path}")
    return int(match.group(1)) + 1


def box_from_image_name(image_ref: str) -> tuple[int, int, int, int] | None:
    match = BOX_PATTERN.search(Path(image_ref).name)
    if not match:
        return None
    return tuple(int(part) for part in match.groups())


def is_rejected_image(image_ref: str, image_path: Path | None = None) -> tuple[bool, str]:
    lowered = image_ref.lower().replace("\\", "/")
    name = Path(lowered).name
    if "footer" in lowered:
        return True, "footer image"
    if "header" in lowered:
        return True, "header image"
    if name.startswith("layout_det_res_"):
        return True, "layout detection page image"
    if any(pattern.lower() in lowered for pattern in PROMO_TEXT_PATTERNS):
        return True, "promo or QR text in image path"

    box = box_from_image_name(image_ref)
    if box:
        x1, y1, x2, y2 = box
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        if "chart_box" not in lowered and (width < 120 or height < 70):
            return True, f"small low-information image ({width}x{height})"
        if y1 >= 1380:
            return True, "bottom margin watermark"

    if image_path and image_path.exists() and image_path.stat().st_size < 12_000:
        if "chart_box" not in lowered and not box:
            return True, "tiny image file"

    return False, ""


def _contains_promo_text(text: str) -> bool:
    return any(pattern in text for pattern in PROMO_TEXT_PATTERNS)


def normalize_latex_math(text: str) -> str:
    text = _merge_split_block_math_environments(text)
    text = _promote_multiline_math_environments(text)
    text = _repair_block_math_closing_dollars(text)
    text = _remove_stray_dollars_in_block_math(text)
    text = _repair_malformed_latex_fragments(text)
    text = _close_dangling_inline_math_starts(text)
    text = _balance_remaining_odd_inline_math(text)

    def replace_inline(match: re.Match) -> str:
        inner = match.group(1).strip()
        if not inner:
            return match.group(0)
        if _should_promote_to_block_math(inner):
            return f"\n\n$$\n{inner}\n$$\n\n"
        return f"${inner}$"

    normalized = INLINE_MATH_PATTERN.sub(replace_inline, text)
    return re.sub(r"\n{3,}", "\n\n", normalized)


def _remove_stray_dollars_in_block_math(text: str) -> str:
    parts = text.split("$$")
    for index in range(1, len(parts), 2):
        parts[index] = parts[index].replace("$", "")
    return "$$".join(parts)


def _repair_malformed_latex_fragments(text: str) -> str:
    text = _unwrap_single_argument_equation_fractions(text)
    text = _normalize_underlined_side_derivatives(text)
    return text


def _unwrap_single_argument_equation_fractions(text: str) -> str:
    pieces: list[str] = []
    cursor = 0
    search_from = 0
    marker = r"\frac{"

    while True:
        start = text.find(marker, search_from)
        if start == -1:
            break

        argument_start = start + len(r"\frac")
        argument_end = _find_balanced_group_end(text, argument_start)
        if argument_end is None:
            search_from = start + len(marker)
            continue

        after = _skip_latex_space(text, argument_end)
        inner = text[argument_start + 1 : argument_end - 1]
        has_denominator = after < len(text) and text[after] == "{"
        if not has_denominator and _looks_like_wrapped_equation_fraction(inner):
            pieces.append(text[cursor:start])
            pieces.append(inner)
            cursor = argument_end
            search_from = argument_end
            continue

        search_from = argument_start + 1

    if not pieces:
        return text
    pieces.append(text[cursor:])
    return "".join(pieces)


def _find_balanced_group_end(text: str, open_brace_index: int) -> int | None:
    if open_brace_index >= len(text) or text[open_brace_index] != "{":
        return None

    depth = 0
    index = open_brace_index
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    return None


def _skip_latex_space(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index


def _looks_like_wrapped_equation_fraction(inner: str) -> bool:
    if "=" not in inner:
        return False
    return bool(re.search(r"\\lim|\\to|\\prime|[_^]|\w\s*\(", inner))


def _normalize_underlined_side_derivatives(text: str) -> str:
    pattern = re.compile(r"\\underline\{([A-Za-z])\^\{\\prime\}\}_\{?([+-])\}?\(([^)]*)\)")
    return pattern.sub(r"\1_{\2}^{\\prime}(\3)", text)


def _balance_remaining_odd_inline_math(text: str) -> str:
    lines = []
    in_block_math = False
    for line in text.splitlines():
        if line.strip() == "$$":
            lines.append(line)
            in_block_math = not in_block_math
            continue
        if in_block_math:
            lines.append(line)
            continue
        positions = _single_dollar_positions(line)
        if len(positions) % 2 == 1:
            line = f"{line}$ %% 待确认：OCR 公式边界异常 %%"
        lines.append(line)
    return "\n".join(lines)


def _merge_split_block_math_environments(text: str) -> str:
    environment = r"(?:cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)"
    pattern = re.compile(
        rf"\$\$\n(.*?\\begin\{{{environment}\}}.*?)\n\$\$\s*\n\s*(.*?\\end\{{{environment}\}})\s*\$(?!\$)",
        re.S,
    )

    def replace(match: re.Match) -> str:
        first = match.group(1).rstrip()
        second = match.group(2).strip()
        return f"$$\n{first}\n{second}\n$$"

    previous = None
    while previous != text:
        previous = text
        text = pattern.sub(replace, text)
    return text


def _repair_block_math_closing_dollars(text: str) -> str:
    environment = r"(?:cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)"
    pattern = re.compile(
        rf"(?<!\$)\$\$\n(\\begin\{{{environment}\}}.*?\\end\{{{environment}\}}[^$\n]*?)\s*\$(?!\$)([^\n]*)",
        re.S,
    )

    def replace(match: re.Match) -> str:
        inner = match.group(1).strip()
        tail = match.group(2)
        return f"$$\n{inner}\n$$\n\n{tail.lstrip()}"

    return pattern.sub(replace, text)


def _promote_multiline_math_environments(text: str) -> str:
    environment = r"(?:cases|aligned|array|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)"
    pattern = re.compile(
        rf"(?<!\$)\$\s*(\\begin\{{{environment}\}}.*?\\end\{{{environment}\}})\s*\$(?!\$)",
        re.S,
    )

    def replace(match: re.Match) -> str:
        inner = match.group(1).strip()
        inner = re.sub(rf"(\\begin\{{{environment}\}})\s*\$", r"\1", inner)
        return f"\n\n$$\n{inner}\n$$\n\n"

    promoted = pattern.sub(replace, text)
    promoted = re.sub(r"[ \t]+\n", "\n", promoted)
    promoted = re.sub(r"(\$\$\n\n)[ \t]+", r"\1", promoted)
    return promoted


def _close_dangling_inline_math_starts(text: str) -> str:
    original_lines = text.splitlines()
    lines = []
    for line_number, line in enumerate(original_lines):
        single_dollar_positions = _single_dollar_positions(line)
        if len(single_dollar_positions) == 1:
            index = single_dollar_positions[0]
            tail = line[index + 1 :].strip()
            if tail and _looks_like_math_fragment(tail):
                tail = tail.rstrip("\\")
                suffix = "" if _next_nonblank_line_is_block_math(original_lines, line_number) else " %% 待确认：OCR 公式可能截断 %%"
                line = line[:index] + "$" + tail + f"${suffix}"
        lines.append(line)
    return "\n".join(lines)


def _single_dollar_positions(line: str) -> list[int]:
    return [
        index
        for index, char in enumerate(line)
        if char == "$"
        and (index == 0 or line[index - 1] != "$")
        and (index + 1 == len(line) or line[index + 1] != "$")
    ]


def _next_nonblank_line_is_block_math(lines: list[str], line_number: int) -> bool:
    for next_line in lines[line_number + 1 :]:
        stripped = next_line.strip()
        if not stripped:
            continue
        return stripped == "$$"
    return False


def _looks_like_math_fragment(text: str) -> bool:
    return bool(re.search(r"\\[A-Za-z]+|[_^{}=<>]|[A-Za-z]\s*\(", text))


def _should_promote_to_block_math(math_text: str) -> bool:
    if "\\begin{cases}" in math_text or "\\end{cases}" in math_text:
        return True
    if len(math_text) >= 120 and any(token in math_text for token in ("\\frac", "\\left", "\\right", "\\begin{aligned}")):
        return True
    return False


def _rewrite_or_remove_image(
    match: re.Match,
    final_stem: str,
    image_paths: dict[str, Path],
    manifest: dict,
    asset_prefix: str | None = None,
) -> str:
    image_ref = match.group(1)
    image_path = image_paths.get(image_ref) or image_paths.get(image_ref.replace("/", "\\"))
    reject, reason = is_rejected_image(image_ref, image_path)
    if reject:
        manifest["rejected_images"].append({"path": image_ref, "reason": reason})
        return ""

    asset_dir_ref = asset_prefix or f"{final_stem}-assets"
    asset_ref = f"{asset_dir_ref}/{Path(image_ref).name}"
    manifest["kept_images"].append({"source": image_ref, "asset": asset_ref})
    return f"![[{asset_ref}|550]]"


def postprocess_pages(
    page_texts: list[str],
    final_stem: str,
    image_paths: dict[str, Path] | None = None,
    asset_prefix: str | None = None,
) -> PostprocessResult:
    image_paths = image_paths or {}
    manifest = {
        "final_document": f"{final_stem}.md",
        "page_count": len(page_texts),
        "kept_images": [],
        "rejected_images": [],
        "removed_promo_lines": [],
    }
    chunks: list[str] = []
    for index, text in enumerate(page_texts, start=1):
        cleaned_lines: list[str] = []
        for line in text.splitlines():
            if _contains_promo_text(line):
                manifest["removed_promo_lines"].append({"page": index, "text": line.strip()})
                continue
            cleaned_lines.append(line)
        cleaned = "\n".join(cleaned_lines)
        cleaned = IMAGE_TAG_PATTERN.sub(
            lambda match: _rewrite_or_remove_image(match, final_stem, image_paths, manifest, asset_prefix),
            cleaned,
        )
        cleaned = normalize_latex_math(cleaned)
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
        chunks.append(f"<!-- page: {index} -->\n\n{cleaned}" if cleaned else f"<!-- page: {index} -->")

    return PostprocessResult(markdown="\n\n".join(chunks).rstrip() + "\n", manifest=manifest)


def collect_markdown_image_refs(markdown: str) -> set[str]:
    return set(IMAGE_TAG_PATTERN.findall(markdown))


def load_lecture_pages(lecture_dir: Path) -> tuple[list[Path], list[str]]:
    doc_paths = sort_doc_pages(lecture_dir.glob("doc_*.md"))
    return doc_paths, [path.read_text(encoding="utf-8") for path in doc_paths]


def migrate_lecture(lecture_dir: Path, final_root: Path, dry_run: bool = False, delete_old: bool = False) -> dict:
    doc_paths, page_texts = load_lecture_pages(lecture_dir)
    final_stem = lecture_dir.name
    image_dir = lecture_dir / "imgs"
    image_paths: dict[str, Path] = {}
    if image_dir.exists():
        for image_path in image_dir.glob("*"):
            if image_path.is_file():
                image_paths[f"imgs/{image_path.name}"] = image_path

    final_doc = final_root / f"{final_stem}.md"
    final_assets = final_root / f"{final_stem}-assets"
    manifest_path = final_root / f"{final_stem}.manifest.json"
    asset_prefix = _vault_relative_path(final_assets)
    result = postprocess_pages(page_texts, final_stem=final_stem, image_paths=image_paths, asset_prefix=asset_prefix)

    referenced_assets = {item["source"] for item in result.manifest["kept_images"]}
    result.manifest.update(
        {
            "source_dir": str(lecture_dir),
            "final_document_path": str(final_doc),
            "final_assets_dir": str(final_assets),
            "source_doc_count": len(doc_paths),
            "source_image_count": len(image_paths),
        }
    )

    if dry_run:
        return result.manifest

    final_root.mkdir(parents=True, exist_ok=True)
    final_assets.mkdir(parents=True, exist_ok=True)
    final_doc.write_text(result.markdown, encoding="utf-8")
    manifest_path.write_text(json.dumps(result.manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    for source_ref in referenced_assets:
        source_path = image_paths.get(source_ref)
        if source_path and source_path.exists():
            shutil.copy2(source_path, final_assets / source_path.name)

    if delete_old:
        for doc_path in doc_paths:
            doc_path.unlink()
        for image_path in lecture_dir.glob("layout_det_res_*.jpg"):
            image_path.unlink()
        if image_dir.exists():
            shutil.rmtree(image_dir)

    return result.manifest


def _vault_relative_path(path: Path) -> str:
    try:
        relative = path.resolve().relative_to(Path.cwd().resolve())
    except ValueError:
        relative = path
    return relative.as_posix()


def migrate_root(root: Path, final_root: Path | None = None, dry_run: bool = False, delete_old: bool = False) -> list[dict]:
    final_root = final_root or root / "_final"
    manifests: list[dict] = []
    for lecture_dir in sorted(path for path in root.iterdir() if path.is_dir() and path.name != "_final"):
        if list(lecture_dir.glob("doc_*.md")):
            manifests.append(migrate_lecture(lecture_dir, final_root, dry_run=dry_run, delete_old=delete_old))
    if not dry_run:
        summary_path = final_root / "migration_manifest.json"
        summary_path.write_text(json.dumps(manifests, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifests


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge PaddleOCR per-page markdown into final lecture OCR files.")
    parser.add_argument("root", help="PaddleOCR root containing lecture directories.")
    parser.add_argument("--final-root", help="Output directory. Default: <root>/_final.")
    parser.add_argument("--dry-run", action="store_true", help="Print summary without writing files.")
    parser.add_argument("--delete-old", action="store_true", help="Delete source doc_*.md, layout images and source imgs after migration.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root)
    final_root = Path(args.final_root) if args.final_root else root / "_final"
    manifests = migrate_root(root, final_root=final_root, dry_run=args.dry_run, delete_old=args.delete_old)
    print(json.dumps(manifests, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
