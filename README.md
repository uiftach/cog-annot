# cog-annot

**Annotate cognitive task datasets with labels for model training.**

## Overview
cog-annot is a compact project of natural-language instructions, prompts, and procedures for labeling cognitive task datasets and producing reproducible model-training inputs.

## Quickstart
1. Add step-by-step procedures to `INSTRUCTIONS.md` (how to prepare data, label formats, quality checks).
2. Add and curate prompts in `PROMPTS.md` and include example inputs/outputs.
3. Run prompts against your model and store outputs in the `results/` folder with short notes.
4. Track next tasks and priorities in `ROADMAP.md`.

## Suggested file list
- `README.md` (this file)
- `INSTRUCTIONS.md` — detailed procedures and acceptance criteria
- `PROMPTS.md` — prompts, examples, tags
- `ROADMAP.md` — next steps and priorities
- `CONTRIBUTING.md` — contribution guidelines
- `LICENSE` — license text (TBD)
- `.gitignore`
- `results/` — capture example outputs and experiment notes

## Contributing
Open issues for new prompts, label schemas, or experiments. PRs should include rationale and example outputs.

## License
TBD — add a license file or choose a suitable open license (e.g., MIT).

---

> Notes: This project is intentionally a natural-language instruction corpus; no code is required to start.