## Context
Astro static site, 34 people and 38 events, three timeline columns; local book preserves stable main-text and annotation anchors.
## Goals / Non-Goals
Expand the existing reading experience and canonical catalog; no new dependencies or unrelated redesign.
## Decisions
Use `lords` as fourth lane after the existing three to retain established lane coordinates. Common events span all four. The lords lane remains available after 208 for surviving independent forces; its label describes a reading grouping, not a unified polity. Separate editorial extension script runs after existing expansions. Map named participants to existing/new IDs, regenerate reciprocal eventIds, preserve old URLs. All means default, while explicit key URLs continue to work.
## Risks / Trade-offs
Four columns are narrower: compact gutters on desktop and retain single-column mobile. Some figures have attached biographies: mark scope, especially Ma Teng. Dates with differing records use ranges and explanatory notes.
## Migration Plan
Validate in independent worktree, build and browser-check, fast-forward existing local site only if clean, rebuild and restart its existing controller. Revert the change commit to roll back.
