import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ID = "native-single-pdf-export"
PLUGIN_DIR = ROOT / ".obsidian" / "plugins" / PLUGIN_ID


class NativeSinglePdfExportPluginTests(unittest.TestCase):
    def test_manifest_declares_desktop_plugin(self):
        manifest = json.loads((PLUGIN_DIR / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["id"], PLUGIN_ID)
        self.assertEqual(manifest["name"], "Native Single PDF Export")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["minAppVersion"], "1.7.2")
        self.assertTrue(manifest["isDesktopOnly"])

    def test_plugin_is_enabled_in_community_plugins(self):
        enabled = json.loads((ROOT / ".obsidian" / "community-plugins.json").read_text(encoding="utf-8"))

        self.assertIn(PLUGIN_ID, enabled)

    def test_main_js_exposes_required_native_export_surface(self):
        source = (PLUGIN_DIR / "main.js").read_text(encoding="utf-8")

        self.assertIn("registerObsidianProtocolHandler", source)
        self.assertIn("addCommand", source)
        self.assertIn("Export active Markdown to absolute path", source)
        self.assertIn("MarkdownRenderer.render", source)
        self.assertIn("MarkdownRenderer.renderMarkdown", source)
        self.assertIn("print-to-pdf", source)
        self.assertIn("new Component()", source)
        self.assertNotIn("new App(", source)
        self.assertIn("isAbsolutePath", source)
        self.assertIn("ensurePdfPath", source)
        self.assertIn("getAbstractFileByPath", source)
        self.assertIn("shell.openPath", source)


if __name__ == "__main__":
    unittest.main()
