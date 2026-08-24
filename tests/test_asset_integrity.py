import json
import unittest
from pathlib import Path

from scripts.verify_assets import verify_repository


ROOT = Path(__file__).resolve().parents[1]


class AssetIntegrityTests(unittest.TestCase):
    def test_required_assets_and_hashes_match_manifest(self):
        self.assertEqual(verify_repository(ROOT), [])

    def test_manifest_declares_flattened_source_and_two_user_authorized_marks(self):
        manifest = json.loads((ROOT / "assets" / "provenance.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["source"]["slide_count"], 33)
        self.assertEqual(manifest["source"]["text_shape_count"], 0)
        self.assertEqual(
            {item["role"] for item in manifest["identity_assets"]},
            {"combined-lockup", "standalone-emblem"},
        )
        self.assertTrue(all(item["source_type"] == "user-provided" for item in manifest["identity_assets"]))
        self.assertTrue(all(item["public_use_authorized"] for item in manifest["identity_assets"]))

    def test_skill_does_not_reference_generated_identity_assets(self):
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        self.assertNotIn("generated_images", skill_text)
        self.assertIn("hohai-lockup-authorized.jpg", skill_text)
        self.assertIn("hohai-emblem-authorized.png", skill_text)


if __name__ == "__main__":
    unittest.main()
