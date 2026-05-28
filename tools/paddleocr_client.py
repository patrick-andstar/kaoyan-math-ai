import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


ASYNC_JOB_URL = "https://paddleocr.aistudio-app.com/api/v2/ocr/jobs"
SYNC_API_URL = "https://n9m00f8dgby1b4a4.aistudio-app.com/layout-parsing"
DEFAULT_MODEL = "PaddleOCR-VL-1.5"
TOKEN_ENV_VAR = "PADDLEOCR_TOKEN"

PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".bmp", ".gif", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}


def resolve_token(cli_token: str | None) -> str:
    token = cli_token or os.environ.get(TOKEN_ENV_VAR, "")
    token = token.strip()
    if not token:
        raise ValueError(
            f"Missing PaddleOCR token. Set {TOKEN_ENV_VAR} or pass --token for one run."
        )
    return token


def infer_file_type(path: Path) -> int:
    suffix = path.suffix.lower()
    if suffix in PDF_EXTENSIONS:
        return 0
    if suffix in IMAGE_EXTENSIONS:
        return 1
    raise ValueError(
        f"Cannot infer file type from {path.name!r}. Use --file-type pdf or --file-type image."
    )


def parse_file_type(value: str | None, file_path: str) -> int:
    if value is None:
        if is_url(file_path):
            parsed_path = Path(urlparse(file_path).path)
            return infer_file_type(parsed_path)
        return infer_file_type(Path(file_path))
    lowered = value.lower()
    if lowered == "pdf":
        return 0
    if lowered == "image":
        return 1
    raise ValueError("--file-type must be pdf or image")


def is_url(file_path: str) -> bool:
    return file_path.startswith("http://") or file_path.startswith("https://")


def safe_output_path(output_dir: Path, relative_path: str) -> Path:
    candidate = (output_dir / relative_path).resolve()
    root = output_dir.resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError(f"Refusing to write outside output directory: {relative_path}")
    return candidate


def default_optional_payload(args: argparse.Namespace) -> dict[str, bool]:
    return {
        "useDocOrientationClassify": args.orientation,
        "useDocUnwarping": args.unwarping,
        "useChartRecognition": args.chart,
    }


def post_async_job(
    file_path: str,
    token: str,
    model: str,
    optional_payload: dict[str, bool],
    timeout: int,
) -> str:
    headers = {"Authorization": f"bearer {token}"}
    if is_url(file_path):
        headers["Content-Type"] = "application/json"
        payload = {
            "fileUrl": file_path,
            "model": model,
            "optionalPayload": optional_payload,
        }
        response = requests.post(ASYNC_JOB_URL, json=payload, headers=headers, timeout=timeout)
    else:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        data = {
            "model": model,
            "optionalPayload": json.dumps(optional_payload),
        }
        with path.open("rb") as handle:
            response = requests.post(
                ASYNC_JOB_URL,
                headers=headers,
                data=data,
                files={"file": handle},
                timeout=timeout,
            )

    response.raise_for_status()
    body = response.json()
    return body["data"]["jobId"]


def wait_for_async_result(
    job_id: str,
    token: str,
    poll_interval: int,
    timeout: int,
    request_timeout: int,
) -> str:
    headers = {"Authorization": f"bearer {token}"}
    deadline = time.monotonic() + timeout
    while True:
        if time.monotonic() > deadline:
            raise TimeoutError(f"Timed out waiting for PaddleOCR job {job_id}")

        response = requests.get(f"{ASYNC_JOB_URL}/{job_id}", headers=headers, timeout=request_timeout)
        response.raise_for_status()
        data = response.json()["data"]
        state = data["state"]

        if state == "done":
            progress = data.get("extractProgress", {})
            print(
                "Job completed, extracted pages: "
                f"{progress.get('extractedPages', 'unknown')}"
            )
            return data["resultUrl"]["jsonUrl"]
        if state == "failed":
            raise RuntimeError(data.get("errorMsg", "PaddleOCR job failed"))

        progress = data.get("extractProgress", {})
        if progress:
            print(
                f"Job {state}, total pages: {progress.get('totalPages', '?')}, "
                f"extracted pages: {progress.get('extractedPages', '?')}"
            )
        else:
            print(f"Job {state}...")
        time.sleep(poll_interval)


def run_async(
    file_path: str,
    token: str,
    model: str,
    optional_payload: dict[str, bool],
    poll_interval: int,
    timeout: int,
    request_timeout: int,
) -> list[dict[str, Any]]:
    job_id = post_async_job(file_path, token, model, optional_payload, request_timeout)
    print(f"Job submitted successfully. job id: {job_id}")
    jsonl_url = wait_for_async_result(job_id, token, poll_interval, timeout, request_timeout)
    response = requests.get(jsonl_url, timeout=request_timeout)
    response.raise_for_status()
    return extract_layout_results_from_jsonl(response.text)


def run_sync(
    file_path: str,
    token: str,
    file_type: int,
    optional_payload: dict[str, bool],
    timeout: int,
) -> list[dict[str, Any]]:
    if is_url(file_path):
        raise ValueError("Synchronous API only supports local files. Use --mode async for URLs.")

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    file_data = base64.b64encode(path.read_bytes()).decode("ascii")
    payload = {
        "file": file_data,
        "fileType": file_type,
        **optional_payload,
    }
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    }
    response = requests.post(SYNC_API_URL, json=payload, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()["result"]["layoutParsingResults"]


def extract_layout_results_from_jsonl(text: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            result = json.loads(line)["result"]
            results.extend(result["layoutParsingResults"])
        except (KeyError, json.JSONDecodeError) as exc:
            raise ValueError(f"Invalid JSONL response at line {line_number}") from exc
    return results


def download_url(url: str, timeout: int) -> bytes:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.content


def save_layout_results(
    layout_results: list[dict[str, Any]],
    output_dir: Path,
    download_images: bool,
    timeout: int,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for page_num, result in enumerate(layout_results):
        markdown = result.get("markdown", {})
        md_path = output_dir / f"doc_{page_num}.md"
        md_path.write_text(markdown.get("text", ""), encoding="utf-8")
        print(f"Markdown document saved at {md_path}")

        if not download_images:
            continue

        for image_path, image_url in markdown.get("images", {}).items():
            full_image_path = safe_output_path(output_dir, image_path)
            full_image_path.parent.mkdir(parents=True, exist_ok=True)
            full_image_path.write_bytes(download_url(image_url, timeout))
            print(f"Image saved to: {full_image_path}")

        for image_name, image_url in result.get("outputImages", {}).items():
            image_path = safe_output_path(output_dir, f"{image_name}_{page_num}.jpg")
            image_path.write_bytes(download_url(image_url, timeout))
            print(f"Image saved to: {image_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Submit a PDF or image to PaddleOCR VL and save markdown results."
    )
    parser.add_argument("file", help="Local file path or HTTPS URL. URLs require --mode async.")
    parser.add_argument(
        "--mode",
        choices=("async", "sync"),
        default="async",
        help="Use async job API or sync layout-parsing API. Default: async.",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for doc_N.md and downloaded images. Default: output.",
    )
    parser.add_argument(
        "--token",
        help=f"One-run token override. Prefer setting {TOKEN_ENV_VAR} instead.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Async model. Default: {DEFAULT_MODEL}.")
    parser.add_argument("--file-type", choices=("pdf", "image"), help="Required only if extension is ambiguous.")
    parser.add_argument("--orientation", action="store_true", help="Enable document orientation classification.")
    parser.add_argument("--unwarping", action="store_true", help="Enable document unwarping.")
    parser.add_argument("--chart", action="store_true", help="Enable chart recognition.")
    parser.add_argument("--no-images", action="store_true", help="Save markdown only, without downloading images.")
    parser.add_argument("--poll-interval", type=int, default=5, help="Async polling interval in seconds.")
    parser.add_argument("--timeout", type=int, default=1800, help="Overall async wait timeout in seconds.")
    parser.add_argument("--request-timeout", type=int, default=120, help="HTTP request timeout in seconds.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        token = resolve_token(args.token)
        optional_payload = default_optional_payload(args)
        file_type = parse_file_type(args.file_type, args.file)

        print(f"Processing file: {args.file}")
        if args.mode == "async":
            layout_results = run_async(
                args.file,
                token,
                args.model,
                optional_payload,
                args.poll_interval,
                args.timeout,
                args.request_timeout,
            )
        else:
            layout_results = run_sync(
                args.file,
                token,
                file_type,
                optional_payload,
                args.request_timeout,
            )

        save_layout_results(
            layout_results,
            Path(args.output_dir),
            download_images=not args.no_images,
            timeout=args.request_timeout,
        )
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
