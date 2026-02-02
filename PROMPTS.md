# PROMPTS

Purpose: Curated prompts and usage notes for generating Cog annotations and example outputs.

## Conventions & Relations
- Track indices: use inline track notation to attach qualifiers to objects: `⟨Cog1#1: oak tree⟩` then `⟨Cog2p#1: tall⟩` (property QUALIFIES object #1).
- Part dot-paths: `⟨Cog3Int#1.1: leaves⟩` means `#1.1` PART_OF `#1`; `#1.1.1` is a subpart.
- Core relations (mechanical):
  - `Cog2p/Cog2t` → QUALIFIES → `Cog1/Cog3Int`
  - `Cog2v` → PROCESS_OF → `Cog1/Cog3Int`
  - `Cog3Int` → PART_OF → `Cog1/Cog3Int`
  - `Cog3Der` → DERIVED_FROM → `Cog1`
  - `Cog4` → PROVENANCE_OF/LOCATION_OF → `Cog1`
- Layering rule: annotate objects (Cog1/Cog1gen/Cog5) first, then add properties/parts/processes and link them.
- Clusters: allow multiple annotations on the same span when it encodes multiple roles (e.g., `fast-growing` = Cog2p + Cog2v). Ensure both tags link to an object.
- Validation tips: all Cog2/3/4 must be linked (no dangling tags). Support overlapping spans for clusters.

## Example prompts
1. Identify categories and return inline track annotations:

Prompt:
```
Annotate the following sentence with Cog inline tags using track indices: "The tall oak tree bears acorns in the marsh." Use the minimal tags and dot-paths for parts.
```
Desired output (example):
```
⟨Cog1#1: The oak tree⟩ ⟨Cog2p#1: tall⟩ ⟨Cog3Der#1.1: acorns⟩ ⟨Cog4#1: marsh⟩
```

2. Produce a JSON graph of nodes and edges from text (useful for downstream tools):

Prompt:
```
Parse the sentence and output an array of nodes (id, span, label) and edges (source, target, relation) according to Cog conventions.
```
Expected output shape (example):
```json
{
  "nodes": [{"id":"n1","label":"Cog1","span":"oak tree"},{"id":"n2","label":"Cog2p","span":"tall"}],
  "edges": [{"source":"n2","target":"n1","relation":"QUALIFIES"}]
}
```

> See `CHEATSHEET.md` for a printable quick reference.
