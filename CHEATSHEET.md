# COG CHEAT SHEET — one page

Quick category list (label — meaning — one-line example):
- Cog1 — main object/entity — oak tree ("The oak tree grows").
- Cog1gen — generic class — fruit trees ("Fruit trees include apple").
- Cog1Ref — reference for comparison — dinner plate ("as large as a dinner plate").
- Cog2p — permanent property — wooden (wooden table).
- Cog2t — transient state — open (the door is open).
- Cog2v — process/action — blooms (the plant blooms).
- Cog3Int — intrinsic part — wheel (part of car).
- Cog3Der — derived product — timber (from tree).
- Cog4 — provenance/location — Toledo (blade from Toledo).
- Cog5 — independent related object — farmer, axe (affects the tree).

Core relations (use these):
- QUALIFIES: Cog2p/Cog2t -> Cog1/Cog3Int
- PROCESS_OF: Cog2v -> Cog1/Cog3Int
- PART_OF: Cog3Int -> Cog1/Cog3Int
- DERIVED_FROM: Cog3Der -> Cog1
- PROVENANCE_OF / LOCATION_OF: Cog4 -> Cog1

Inline track shorthand examples:
- `⟨Cog1#1: oak tree⟩ ⟨Cog2p#1: tall⟩`  (tall QUALIFIES oak tree)
- `⟨Cog3Int#1.1: leaf⟩` (leaf PART_OF oak tree)

Quick annotation checklist ✅
- Objects first (Cog1/Cog1gen/Cog5).
- Link every Cog2/3/4 to a parent object (no dangling tags).
- Use dot paths for parts and reuse indices for coreference.
- Cluster only when a span encodes multiple roles.
- Validate: no orphaned tags; overlapping spans allowed for clusters.

Keep this sheet open while annotating and refer to `PROMPTS.md` and `INSTRUCTIONS.md` for details.