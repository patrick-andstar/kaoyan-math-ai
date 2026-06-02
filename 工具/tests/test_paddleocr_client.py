import json
import os
import tempfile
import unittest
from pathlib import Path

from tools import paddleocr_client as client
from tools import ocr_postprocess


class PaddleOcrClientTests(unittest.TestCase):
    def test_default_async_model_uses_latest_vl_release(self):
        parser = client.build_parser()
        args = parser.parse_args(["chapter.pdf"])

        self.assertEqual(client.DEFAULT_MODEL, "PaddleOCR-VL-1.6")
        self.assertEqual(args.model, "PaddleOCR-VL-1.6")

    def test_infers_file_type_from_extension(self):
        self.assertEqual(client.infer_file_type(Path("chapter.pdf")), 0)
        self.assertEqual(client.infer_file_type(Path("page.PNG")), 1)

    def test_rejects_unknown_file_type(self):
        with self.assertRaises(ValueError):
            client.infer_file_type(Path("notes.txt"))

    def test_reads_token_from_environment(self):
        old_value = os.environ.get("PADDLEOCR_TOKEN")
        try:
            os.environ["PADDLEOCR_TOKEN"] = "secret-token"
            self.assertEqual(client.resolve_token(None), "secret-token")
        finally:
            if old_value is None:
                os.environ.pop("PADDLEOCR_TOKEN", None)
            else:
                os.environ["PADDLEOCR_TOKEN"] = old_value

    def test_safe_output_path_blocks_traversal(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(ValueError):
                client.safe_output_path(Path(temp_dir), "../outside.png")

    def test_extracts_layout_results_from_jsonl(self):
        payload = {
            "result": {
                "layoutParsingResults": [
                    {"markdown": {"text": "page 1", "images": {}}, "outputImages": {}},
                    {"markdown": {"text": "page 2", "images": {}}, "outputImages": {}},
                ]
            }
        }
        rows = client.extract_layout_results_from_jsonl(json.dumps(payload))
        self.assertEqual([row["markdown"]["text"] for row in rows], ["page 1", "page 2"])

    def test_save_layout_results_writes_single_final_ocr_document(self):
        rows = [
            {"markdown": {"text": "page 1", "images": {}}, "outputImages": {}},
            {"markdown": {"text": "page 2", "images": {}}, "outputImages": {}},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            client.save_layout_results(rows, Path(temp_dir), download_images=False, timeout=1)

            self.assertTrue((Path(temp_dir) / "final_ocr.md").exists())
            self.assertFalse((Path(temp_dir) / "doc_0.md").exists())
            text = (Path(temp_dir) / "final_ocr.md").read_text(encoding="utf-8")
            self.assertIn("<!-- page: 1 -->", text)
            self.assertIn("page 1", text)
            self.assertIn("<!-- page: 2 -->", text)
            self.assertIn("page 2", text)

    def test_save_layout_results_copies_kept_images_to_assets(self):
        original_download_url = client.download_url
        client.download_url = lambda url, timeout: b"fake-image-bytes"
        try:
            rows = [
                {
                    "markdown": {
                        "text": '<div><img src="imgs/img_in_chart_box_110_139_882_1212.jpg" /></div>',
                        "images": {"imgs/img_in_chart_box_110_139_882_1212.jpg": "https://example.test/chart.jpg"},
                    },
                    "outputImages": {},
                }
            ]
            with tempfile.TemporaryDirectory() as temp_dir:
                output_dir = Path(temp_dir) / "lecture"
                client.save_layout_results(rows, output_dir, download_images=True, timeout=1)

                self.assertTrue((output_dir / "lecture-assets" / "img_in_chart_box_110_139_882_1212.jpg").exists())
                self.assertFalse((output_dir / "imgs").exists())
                text = (output_dir / "final_ocr.md").read_text(encoding="utf-8")
                self.assertIn("![[lecture-assets/img_in_chart_box_110_139_882_1212.jpg|550]]", text)
        finally:
            client.download_url = original_download_url

    def test_save_layout_results_removes_output_image_staging_files(self):
        original_download_url = client.download_url
        client.download_url = lambda url, timeout: b"fake-image-bytes"
        try:
            rows = [
                {
                    "markdown": {"text": "page", "images": {}},
                    "outputImages": {"layout_det_res": "https://example.test/layout.jpg"},
                }
            ]
            with tempfile.TemporaryDirectory() as temp_dir:
                output_dir = Path(temp_dir) / "lecture"
                client.save_layout_results(rows, output_dir, download_images=True, timeout=1)

                self.assertFalse((output_dir / "_ocr_output_images").exists())
                self.assertFalse((output_dir / "layout_det_res_0.jpg").exists())
        finally:
            client.download_url = original_download_url

    def test_doc_pages_sort_naturally(self):
        names = ["doc_10.md", "doc_2.md", "doc_1.md"]
        self.assertEqual(
            [path.name for path in ocr_postprocess.sort_doc_pages(Path(name) for name in names)],
            ["doc_1.md", "doc_2.md", "doc_10.md"],
        )

    def test_filters_useless_images_and_removes_references(self):
        page = (
            '<div><img src="imgs/img_in_footer_image_box_39_1423_433_1499.jpg" /></div>\n'
            '<div>后续更新去公众号有机研，微信 45550060</div>\n'
            '<div><img src="imgs/img_in_image_box_90_838_169_897.jpg" /></div>\n'
            '<div><img src="imgs/img_in_chart_box_110_139_882_1212.jpg" /></div>'
        )
        result = ocr_postprocess.postprocess_pages(
            [page],
            final_stem="01-第1讲-函数极限与连续",
            image_paths={
                "imgs/img_in_footer_image_box_39_1423_433_1499.jpg": Path("footer.jpg"),
                "imgs/img_in_image_box_90_838_169_897.jpg": Path("small.jpg"),
                "imgs/img_in_chart_box_110_139_882_1212.jpg": Path("chart.jpg"),
            },
        )

        self.assertNotIn("footer_image", result.markdown)
        self.assertNotIn("img_in_image_box_90_838_169_897", result.markdown)
        self.assertIn("![[01-第1讲-函数极限与连续-assets/img_in_chart_box_110_139_882_1212.jpg|550]]", result.markdown)
        self.assertEqual(len(result.manifest["kept_images"]), 1)
        self.assertEqual(len(result.manifest["rejected_images"]), 2)


    def test_keeps_large_coordinate_image_even_when_file_is_small(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = Path(temp_dir) / "large-line-drawing.jpg"
            image_path.write_bytes(b"small-file")

            reject, reason = ocr_postprocess.is_rejected_image(
                "imgs/img_in_image_box_110_139_882_1212.jpg",
                image_path,
            )

        self.assertFalse(reject, reason)

    def test_normalizes_inline_math_delimiter_spacing(self):
        result = ocr_postprocess.postprocess_pages(
            ["sequence $ a_{n} $ and points $ \\{x_{n}\\} $"],
            final_stem="lecture",
        )

        self.assertIn("sequence $a_{n}$ and points $\\{x_{n}\\}$", result.markdown)
        self.assertNotIn("$ a_{n} $", result.markdown)
        self.assertNotIn("$ \\{x_{n}\\} $", result.markdown)

    def test_promotes_cases_formula_to_block_math(self):
        result = ocr_postprocess.postprocess_pages(
            ["sum $ S_n=\\begin{cases}na_1,&r=1,\\\\\\frac{a_1(1-r^n)}{1-r},&r\\ne1.\\end{cases} $"],
            final_stem="lecture",
        )

        self.assertIn(
            "$$\nS_n=\\begin{cases}na_1,&r=1,\\\\\\frac{a_1(1-r^n)}{1-r},&r\\ne1.\\end{cases}\n$$",
            result.markdown,
        )
        self.assertNotIn("$ S_n=\\begin{cases}", result.markdown)

    def test_inline_math_normalization_does_not_cross_block_math(self):
        result = ocr_postprocess.postprocess_pages(
            ["泰勒展开式$ \\rightarrow \n\n$$\ny=f(x)\n$$\n\n后文"],
            final_stem="lecture",
        )

        self.assertIn("泰勒展开式$\\rightarrow$\n\n$$\ny=f(x)\n$$\n\n后文", result.markdown)
        self.assertNotIn("$\\rightarrow\n\n$$", result.markdown)

    def test_promotes_multiline_cases_formula_to_one_block(self):
        result = ocr_postprocess.postprocess_pages(
            ["A $ \\begin{cases}\na,&x<0,\\\\\nb,&x>0\\end{cases} $ end"],
            final_stem="lecture",
        )

        self.assertIn(
            "A\n\n$$\n\\begin{cases}\na,&x<0,\\\\\nb,&x>0\\end{cases}\n$$\n\nend",
            result.markdown,
        )
        self.assertNotIn("\\begin{cases}$", result.markdown)
        self.assertNotIn("\\end{cases} $", result.markdown)

    def test_promotes_split_aligned_environment_to_one_block(self):
        result = ocr_postprocess.postprocess_pages(
            ["$ \\begin{aligned}$\na&=b\\\\\nc&=d\n\\end{aligned} $"],
            final_stem="lecture",
        )

        self.assertIn(
            "$$\n\\begin{aligned}\na&=b\\\\\nc&=d\n\\end{aligned}\n$$",
            result.markdown,
        )
        self.assertNotIn("$\\begin{aligned}$", result.markdown)

    def test_repairs_block_environment_with_prose_after_closing_dollar(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$\n\\begin{vmatrix}x&y\\\\z&w\\end{vmatrix}=0 $（说明 $P_i$）."],
            final_stem="lecture",
        )

        self.assertIn("$$\n\\begin{vmatrix}x&y\\\\z&w\\end{vmatrix}=0\n$$\n\n（说明 $P_i$）.", result.markdown)

    def test_merges_split_block_environment(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$\nF(x)=\\begin{cases}a,&x\\leq0,\\\\\n$$\n\nb,&x>0\\end{cases} $"],
            final_stem="lecture",
        )

        self.assertIn(
            "$$\nF(x)=\\begin{cases}a,&x\\leq0,\\\\\nb,&x>0\\end{cases}\n$$",
            result.markdown,
        )
        self.assertNotIn("\\end{cases} $", result.markdown)

    def test_marks_unclosed_inline_formula_as_pending_confirmation(self):
        result = ocr_postprocess.postprocess_pages(
            ["例题答案为 $ y_t = \\_\\"],
            final_stem="lecture",
        )

        self.assertIn("$y_t = \\_$", result.markdown)
        self.assertIn("待确认：OCR 公式可能截断", result.markdown)

    def test_balances_remaining_odd_dollar_line_as_pending_confirmation(self):
        result = ocr_postprocess.postprocess_pages(
            ["text $a$ then broken $b$ and $c"],
            final_stem="lecture",
        )

        self.assertIn("$c$ %% 待确认：OCR 公式边界异常 %%", result.markdown)

    def test_does_not_balance_dollars_inside_block_math(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$\n\\begin{cases}a,\\\\ $b\\end{cases}\n$$"],
            final_stem="lecture",
        )

        self.assertIn("\\begin{cases}a,\\\\ b\\end{cases}", result.markdown)
        self.assertNotIn("OCR 公式边界异常", result.markdown)


    def test_unwraps_single_argument_fraction_around_equation_chain(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$ \\frac{y_{-}^{\\prime}(0)=\\lim_{x\\to0^{-}}\\frac{y(x)-y(0)}{x}=-1} $$"],
            final_stem="lecture",
        )

        self.assertIn(
            "$$ y_{-}^{\\prime}(0)=\\lim_{x\\to0^{-}}\\frac{y(x)-y(0)}{x}=-1 $$",
            result.markdown,
        )
        self.assertNotIn("\\frac{y_{-}^{\\prime}(0)=", result.markdown)

    def test_keeps_valid_two_argument_fraction(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$ \\frac{a+b}{c+d}=1 $$"],
            final_stem="lecture",
        )

        self.assertIn("$$ \\frac{a+b}{c+d}=1 $$", result.markdown)

    def test_normalizes_malformed_underlined_side_derivative(self):
        result = ocr_postprocess.postprocess_pages(
            ["$$ \\underline{y^{\\prime}}_{+}(0)=\\lim_{x\\to0^{+}}\\frac{y(x)-y(0)}{x}=1 $$"],
            final_stem="lecture",
        )

        self.assertIn(
            "$$ y_{+}^{\\prime}(0)=\\lim_{x\\to0^{+}}\\frac{y(x)-y(0)}{x}=1 $$",
            result.markdown,
        )
        self.assertNotIn("\\underline{y^{\\prime}}_{+}(0)", result.markdown)

    def test_migrate_lecture_uses_vault_relative_asset_links(self):
        with tempfile.TemporaryDirectory(dir=".") as temp_dir:
            workspace = Path(temp_dir)
            lecture_dir = workspace / "paddleocr" / "01-lecture"
            image_dir = lecture_dir / "imgs"
            final_root = workspace / "paddleocr" / "_final"
            image_dir.mkdir(parents=True)
            (lecture_dir / "doc_0.md").write_text(
                '<div><img src="imgs/img_in_chart_box_110_139_882_1212.jpg" /></div>',
                encoding="utf-8",
            )
            (image_dir / "img_in_chart_box_110_139_882_1212.jpg").write_bytes(b"fake-image")

            ocr_postprocess.migrate_lecture(lecture_dir, final_root)

            final_text = (final_root / "01-lecture.md").read_text(encoding="utf-8")
            expected_ref = (
                final_root / "01-lecture-assets" / "img_in_chart_box_110_139_882_1212.jpg"
            ).relative_to(Path.cwd()).as_posix()
            self.assertIn(
                f"![[{expected_ref}|550]]",
                final_text,
            )
            self.assertNotIn("![[01-lecture-assets/", final_text)


if __name__ == "__main__":
    unittest.main()
