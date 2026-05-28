import json
import os
import tempfile
import unittest
from pathlib import Path

from tools import paddleocr_client as client


class PaddleOcrClientTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
