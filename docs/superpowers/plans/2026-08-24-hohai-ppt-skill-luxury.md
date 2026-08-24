# Hohai PPT Skill Luxury Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, commit, and publicly publish an installable Codex skill that recreates the approved Hohai University PPT visual system while using only exact identity crops from the supplied source deck.

**Architecture:** The repository root is the skill. A retained source PPTX and three source renders provide provenance and visual evidence; two unmodified rectangular crops provide the only permitted Hohai identity assets. Concise skill instructions route to detailed visual and provenance references, while a deterministic Python verifier and tests protect asset integrity.

**Tech Stack:** Markdown, YAML, JSON, Python 3 standard library plus Pillow for crop generation/tests, Codex skill-creator validator, Git, GitHub.

## Global Constraints

- GitHub repository name is `hohai_ppt_skill_luxury`.
- Codex frontmatter name is `hohai-ppt-skill-luxury` because underscores are invalid.
- The public source asset is the user-supplied `C:\Users\33165\Desktop\河海大学.pptx`.
- Hohai identity must come only from exact source-render crops; never generate, redraw, retype, vectorize, recolor, or download it.
- Exclude source subject matter and all `110` or anniversary elements from reusable output behavior.
- Do not use a complete source slide as an output-slide background.

---

### Task 1: Asset integrity contract

**Files:**
- Create: `tests/test_asset_integrity.py`
- Create: `scripts/verify_assets.py`
- Create later in Task 2: `assets/provenance.json`

**Interfaces:**
- Consumes: repository root and `assets/provenance.json`.
- Produces: `verify_repository(root: Path) -> list[str]`, where an empty list means every invariant passes.

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path
from scripts.verify_assets import verify_repository


def test_required_assets_and_hashes_match_manifest():
    assert verify_repository(Path(__file__).parents[1]) == []
```

- [ ] **Step 2: Run the test to verify RED**

Run: `python -m unittest discover -s tests -v`

Expected: FAIL because `scripts.verify_assets` or the asset manifest does not exist.

- [ ] **Step 3: Implement the verifier**

Implement SHA-256 verification, source/crop existence checks, image-dimension checks, crop-box bounds checks, and a scan that rejects generated-preview files as identity assets. Provide `python scripts/verify_assets.py` as a CLI returning nonzero with one line per error.

- [ ] **Step 4: Keep RED until Task 2 assets exist**

Run: `python -m unittest discover -s tests -v`

Expected: FAIL with missing asset or manifest messages, proving the test exercises the required artifacts.

- [ ] **Step 5: Commit the test contract**

```powershell
git add tests/test_asset_integrity.py scripts/verify_assets.py
git commit -m "test: define Hohai asset integrity contract"
```

### Task 2: Skill scaffold and authentic assets

**Files:**
- Create: `SKILL.md`
- Create: `agents/openai.yaml`
- Create: `assets/reference.pptx`
- Create: `assets/preview.png`
- Create: `assets/reference-middle.png`
- Create: `assets/reference-image-page.png`
- Create: `assets/hohai-lockup-on-dark.png`
- Create: `assets/hohai-lockup-on-light.png`
- Create: `assets/provenance.json`

**Interfaces:**
- Consumes: source PPTX and source renders already produced by the Presentations inspection workflow.
- Produces: an installable skill root and immutable brand assets named in `provenance.json`.

- [ ] **Step 1: Initialize the skill skeleton**

Run the official `init_skill.py` with skill name `hohai-ppt-skill-luxury`, output parent equal to the repository parent, and resources `references,assets,scripts`. Move only the generated required metadata into this already initialized repository without retaining example placeholders.

- [ ] **Step 2: Copy public source evidence**

Copy the user-authorized source PPTX to `assets/reference.pptx` and copy source slides 1, 17, and 30 to the three reference PNG paths.

- [ ] **Step 3: Crop authentic lockups**

Crop the source renders without scaling or alpha conversion. Use explicit pixel boxes recorded in `provenance.json`; visually inspect both crops and adjust only the box if lettering is clipped.

- [ ] **Step 4: Write provenance manifest**

Record original filename, slide count, flattened-deck finding, source SHA-256, each source render, crop box, crop dimensions, and crop SHA-256.

- [ ] **Step 5: Verify GREEN**

Run: `python -m unittest discover -s tests -v`

Expected: PASS with all required hashes and dimensions matching.

- [ ] **Step 6: Commit assets and scaffold**

```powershell
git add SKILL.md agents assets
git commit -m "feat: add authentic Hohai presentation assets"
```

### Task 3: Skill instructions and references

**Files:**
- Modify: `SKILL.md`
- Create: `references/visual-system.md`
- Create: `references/asset-provenance.md`
- Create: `README.md`
- Create: `NOTICE.md`

**Interfaces:**
- Consumes: exact asset names and hashes from Task 2.
- Produces: clear trigger, decision rules, page-family recipes, installation guidance, and trademark/source notice.

- [ ] **Step 1: Write concise frontmatter and overview**

Use only supported frontmatter keys. The description starts with `Use when` and names Hohai University, PowerPoint/PPTX, exact identity assets, and the luxury blue-white report style without summarizing the workflow.

- [ ] **Step 2: Encode the flattened-source exception**

State positively that the skill establishes a custom visual direction. The retained PPTX is provenance and visual evidence; output slides are rebuilt as editable objects and never cloned as full-slide raster backgrounds.

- [ ] **Step 3: Encode the identity contract**

Require selection of `hohai-lockup-on-dark.png` or `hohai-lockup-on-light.png` based on background, proportional scaling, and hash verification. Prohibit every substitute or transformation identified in the baseline evaluation.

- [ ] **Step 4: Document page families and visual tokens**

Define opening, divider, standard content, image-led, and closing compositions; blue-white palette; top rail; pale takeaway strip; restrained imagery; and editable-element requirements.

- [ ] **Step 5: Add packaging documentation**

Document clone/copy installation, invocation as `$hohai-ppt-skill-luxury`, retained source authorization, and rights limitations. Do not attach a license to the university presentation or marks.

- [ ] **Step 6: Commit instructions**

```powershell
git add SKILL.md references README.md NOTICE.md
git commit -m "docs: define Hohai luxury PPT workflow"
```

### Task 4: Validation and forward application test

**Files:**
- Modify only when evidence requires: `SKILL.md`, `references/*.md`, `scripts/verify_assets.py`
- Record locally outside the repository: forward-test report.

**Interfaces:**
- Consumes: completed skill directory.
- Produces: official validator output, asset-test output, and an independent behavioral report.

- [ ] **Step 1: Run official skill validation**

Run with UTF-8 mode: `python C:\Users\33165\.codex\skills\.system\skill-creator\scripts\quick_validate.py .`

Expected: validator reports a valid skill.

- [ ] **Step 2: Run deterministic repository verification**

Run: `python scripts/verify_assets.py`

Expected: `asset verification passed` and exit code 0.

- [ ] **Step 3: Run an independent application scenario**

Give a fresh evaluator the completed skill and a request for a new Hohai-styled digital-twin water presentation. Verify that it selects exact crop paths, rejects whole-slide copying and 110 content, and plans editable elements.

- [ ] **Step 4: Refine only observed gaps**

Patch narrow wording or validation gaps, then repeat Steps 1-3 until all pass.

- [ ] **Step 5: Commit verified refinements**

```powershell
git add -A
git commit -m "test: verify Hohai skill behavior"
```

### Task 5: Public GitHub publication

**Files:**
- No new repository files unless final verification identifies a gap.

**Interfaces:**
- Consumes: clean local `main` commit.
- Produces: public GitHub repository `hohai_ppt_skill_luxury` with the same commit contents.

- [ ] **Step 1: Check remote nonexistence and authenticated owner**

Verify no repository with the exact name exists and record the authenticated GitHub login.

- [ ] **Step 2: Create the public repository**

Create `hohai_ppt_skill_luxury` without auto-generated README, license, or `.gitignore`, so the local history remains canonical.

- [ ] **Step 3: Push local main**

Add the HTTPS remote and push `main`. Stop after one authentication failure and report the exact blocker instead of retrying with embedded credentials.

- [ ] **Step 4: Verify the remote**

Read repository metadata, `SKILL.md`, `assets/provenance.json`, and source PPTX size from GitHub. Confirm remote branch/commit matches the local HEAD.

- [ ] **Step 5: Record final state**

Update `.codex/memory/STATE.md` and `.codex/memory/DECISIONS.md`, then save the Engram session summary.

