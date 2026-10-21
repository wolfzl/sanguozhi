## Context
The existing 65 portraits use generated JSON and a shared Astro component. The approved standalone Cao Cao draft must remain reproducible.

## Goals / Non-Goals
Publish seven expanded profiles while preserving other portraits and all event data. Do not invent missing dates, offices, deeds or a Sima Yi biography absent from this book.

## Decisions
Keep existing dossier fields and add optional expanded fields for titled introduction paragraphs, grouped achievement rows, scholarship, assessment, reading notes, relationship groups and source scope. Reuse approved Cao Cao records exactly. Add full source excerpts from primary biographies as appendix references, retaining traditional source text in data. Render searchable source excerpts with existing citation numbering. Existing pages retain their presentation. All narrative and table links remain reciprocal.

## Risks / Trade-offs
Longer pages require grouped headings, responsive tables and collapsed source excerpts. Note citations identify the quoted work separately from Chen Shou. Sima Yi uses scattered references rather than an invented dedicated biography. Source coverage is described rather than claiming an exhaustive search of every mention in the entire book.

## Migration Plan
Implement in a new worktree, run generation/reference/unit/build/browser checks, fast-forward the clean website checkout and restart preview 4324. Publish Cao Cao first and close 8767, then publish six expanded profiles. Git revert and rebuilding provide rollback.
