import json
import unittest
from pathlib import Path

from scripts.verify_assets import verify_repository


ROOT = Path(__file__).resolve().parents[1]


class AssetIntegrityTests(unittest.TestCase):
    def test_required_assets_and_hashes_match_manifest(self):
        self.assertEqual(verify_repository(ROOT), [])

    def test_manifest_declares_flattened_source_and_two_lockups(self):
        manifest = json.loads((ROOT / "assets" / "provenance.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["source"]["slide_count"], 33)
        self.assertEqual(manifest["source"]["text_shape_count"], 0)
        self.assertEqual(
            {item["role"] for item in manifest["identity_assets"]},
            {"light-on-dark", "dark-on-light"},
        )

    def test_skill_does_not_reference_generated_identity_assets(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        self.assertNotIn("generated_images", skill_text)
        self.assertIn("hohai-lockup-on-dark.png", skill_text)
        self.assertIn("hohai-lockup-on-light.png", skill_text)


if __name__ == "__main__":
    unittest.main()
