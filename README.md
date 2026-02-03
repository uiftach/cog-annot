# Cog-Annot: Object-Centered Semantic Annotation System

A comprehensive annotation system for marking object-centered semantics in descriptive and technical texts, with support for temporal designators (TD), movement anchors (MOV), and human operations (PLACTAC).

## Overview

Cog-Annot is designed to annotate:
- **Objects** and their relationships (Cog1, Cog1Ref, Cog5)
- **Properties** and states (Cog2p, Cog2t)
- **Spontaneous actions** (Cog2v)
- **Parts** and products (Cog3Int, Cog3Der)
- **Environments** and provenance (Cog4)
- **Temporal designators** (TD_ABS, TD_REL, TD_DUR)
- **Movement anchors** (MOV_SRC, MOV_DST, MOV_PATH)
- **Human operations** (PLACTAC_STEP)

## Core Principles

1. **Surface fidelity** - Annotate only what is explicitly present
2. **Minimal sufficiency** - Use fewest annotations needed
3. **One label per token/phrase** - No double tagging
4. **Object primacy** - System organized around objects, not events

## Quick Start

### Annotation Format
```
⟨CogType#track: text⟩
```

### Example
```
The ⟨Cog1#1: oak⟩ has ⟨Cog2p#1: hard⟩ ⟨Cog3Der#1: wood⟩ and grows in ⟨Cog4: mountains⟩.
```

## Key Distinctions

### Cog2v vs PLACTAC
- **Cog2v**: Spontaneous action BY the object (swims, flies, hunts)
- **PLACTAC**: Intended operation ON the object by external force (cutting, harvesting)

### Cog4 vs MOV
- **Cog4**: Habitat/environment (lives in water)
- **MOV**: Movement endpoint (swims to/from water)

## Documentation

- **[INSTRUCTIONS.md](INSTRUCTIONS.md)** - Complete annotation rules and guidelines
- **[Aristoteles/HA/](Aristoteles/HA/)** - Example: Aristotle's Historia Animalium (Greek text)

## Project Structure

```
cog-annot/
├── INSTRUCTIONS.md              # Complete annotation rules
├── README.md                    # This file
├── Aristoteles/
│   └── HA/
│       └── HA raw text to 491.14.txt  # Annotated Greek text
└── [Your texts here]/
```

## Contributing Your Own Texts

1. Create a folder for your author/corpus
2. Add your annotated text files
3. Follow the annotation guidelines in INSTRUCTIONS.md
4. Use the format: `⟨CogType#track: text⟩`

## Track Numbering System

- Track indices (e.g., `#1`, `#42`) identify unique objects throughout the text
- Use dot notation for parts: `#track.subtrack` (e.g., `#10.1` for a part of object #10)
- Generic objects can share tracks (e.g., all generic animals as `#1`)

## Getting Started with Git

To use this repository:

1. **Install Git**: Download from [git-scm.com](https://git-scm.com/)
2. **Clone the repository**: 
   ```bash
   git clone https://github.com/[username]/cog-annot.git
   ```
3. **Add your texts**: Create folders and annotate
4. **Commit changes**:
   ```bash
   git add .
   git commit -m "Add [your corpus name]"
   git push
   ```

## System Version

- Version: 2.0 (with Cog2v, PLACTAC, TD, MOV support)
- Last updated: February 2026
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