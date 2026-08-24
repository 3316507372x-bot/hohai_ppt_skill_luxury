# hohai_ppt_skill_luxury

A portable Codex skill for editable PowerPoint decks in the approved Hohai University blue-white academic report style.

## Install

Clone the repository so its root is a Codex skill directory. The repository name retains the user-requested underscores; the validated Codex invocation name uses hyphens.

```powershell
git clone https://github.com/3316507372x-bot/hohai_ppt_skill_luxury.git "$env:USERPROFILE\.codex\skills\hohai-ppt-skill-luxury"
```

Invoke it as `$hohai-ppt-skill-luxury` and describe the presentation you want.

## What is retained

- The user-authorized source PPTX.
- Three source-render references for opening, content, and image-led composition.
- Two exact combined emblem/wordmark crops from the source deck.
- Hash-based provenance and an asset verifier.

Run the verifier after cloning:

```powershell
python scripts\verify_assets.py
```

The source deck controls style and identity only. Its subject matter and every `110` anniversary element are excluded from reusable output behavior.

