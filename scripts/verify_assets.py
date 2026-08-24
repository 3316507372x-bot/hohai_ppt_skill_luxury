#!/usr/bin/env python3
"""Verify that retained Hohai presentation assets match their provenance manifest."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from PIL import Image


MANIFEST_PATH = Path("assets/provenance.json")
REQUIRED_TOP_LEVEL = {
    "schema_version",
    "source",
    "reference_renders",
    "source_reference_crops",
    "identity_assets",
}
ALLOWED_IDENTITY_FILES = {
    "assets/hohai-emblem-authorized.png",
    "assets/hohai-lockup-authorized.jpg",
}
SOURCE_REFERENCE_CROP_FILES = {
    "assets/hohai-lockup-on-dark.png",
    "assets/hohai-lockup-on-light.png",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _verify_file(root: Path, entry: dict, errors: list[str], *, require_dimensions: bool) -> None:
    relative = entry.get("path")
    expected_hash = entry.get("sha256")
    if not relative or not expected_hash:
        errors.append("manifest entry is missing path or sha256")
        return

    path = root / relative
    if not path.is_file():
        errors.append(f"missing required asset: {relative}")
        return

    actual_hash = sha256_file(path)
    if actual_hash.lower() != str(expected_hash).lower():
        errors.append(f"sha256 mismatch: {relative}")

    if require_dimensions:
        try:
            with Image.open(path) as image:
                actual_size = [image.width, image.height]
        except Exception as exc:  # pragma: no cover - message is exercised through CLI use
            errors.append(f"cannot inspect image {relative}: {exc}")
            return
        expected_size = entry.get("dimensions")
        if actual_size != expected_size:
            errors.append(f"dimension mismatch: {relative}; expected {expected_size}, got {actual_size}")


def verify_repository(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    manifest_file = root / MANIFEST_PATH
    if not manifest_file.is_file():
        return [f"missing manifest: {MANIFEST_PATH.as_posix()}"]

    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid manifest: {exc}"]

    missing_keys = REQUIRED_TOP_LEVEL - manifest.keys()
    if missing_keys:
        errors.append(f"manifest missing keys: {', '.join(sorted(missing_keys))}")

    source = manifest.get("source", {})
    _verify_file(root, source, errors, require_dimensions=False)
    if source.get("slide_count") != 33:
        errors.append("source slide_count must be 33")
    if source.get("text_shape_count") != 0:
        errors.append("source text_shape_count must be 0")

    render_by_slide: dict[int, dict] = {}
    for entry in manifest.get("reference_renders", []):
        _verify_file(root, entry, errors, require_dimensions=True)
        slide = entry.get("source_slide")
        if isinstance(slide, int):
            render_by_slide[slide] = entry

    seen_reference_crop_paths: set[str] = set()
    for entry in manifest.get("source_reference_crops", []):
        _verify_file(root, entry, errors, require_dimensions=True)
        relative = entry.get("path")
        if relative:
            normalized = str(relative).replace("\\", "/")
            seen_reference_crop_paths.add(normalized)
            if normalized not in SOURCE_REFERENCE_CROP_FILES:
                errors.append(f"unapproved source reference crop path: {normalized}")

        slide = entry.get("source_slide")
        crop = entry.get("crop_box")
        render = render_by_slide.get(slide)
        if not render:
            errors.append(f"identity asset has no declared source render for slide {slide}")
            continue
        if not isinstance(crop, list) or len(crop) != 4:
            errors.append(f"identity asset has invalid crop_box: {relative}")
            continue
        width, height = render.get("dimensions", [0, 0])
        left, top, right, bottom = crop
        if not (0 <= left < right <= width and 0 <= top < bottom <= height):
            errors.append(f"identity crop is outside source render: {relative}")
        if entry.get("dimensions") != [right - left, bottom - top]:
            errors.append(f"identity dimensions do not match crop_box: {relative}")

    if seen_reference_crop_paths != SOURCE_REFERENCE_CROP_FILES:
        errors.append("source reference crop paths must be exactly the two retained source crops")

    seen_roles: set[str] = set()
    seen_identity_paths: set[str] = set()
    for entry in manifest.get("identity_assets", []):
        _verify_file(root, entry, errors, require_dimensions=True)
        role = entry.get("role")
        relative = entry.get("path")
        if role:
            seen_roles.add(role)
        if entry.get("source_type") != "user-provided":
            errors.append(f"identity asset is not declared user-provided: {relative}")
        if entry.get("public_use_authorized") is not True:
            errors.append(f"identity asset lacks public-use authorization: {relative}")
        if relative:
            normalized = str(relative).replace("\\", "/")
            seen_identity_paths.add(normalized)
            if normalized not in ALLOWED_IDENTITY_FILES:
                errors.append(f"unapproved identity path: {normalized}")
            if "generated" in normalized.lower() or Path(normalized).name.lower().startswith("exec-"):
                errors.append(f"generated identity asset is forbidden: {normalized}")

    if seen_roles != {"combined-lockup", "standalone-emblem"}:
        errors.append("identity roles must be exactly combined-lockup and standalone-emblem")
    if seen_identity_paths != ALLOWED_IDENTITY_FILES:
        errors.append("identity paths must be exactly the two user-authorized identity assets")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = verify_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("asset verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
