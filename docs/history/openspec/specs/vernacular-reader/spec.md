# vernacular-reader Specification

## Purpose
TBD - created by archiving change wudi-baihua-reader. Update Purpose after archive.
## Requirements
### Requirement: Complete vernacular reading
The reader SHALL offer a 白话 option only for volumes with a translation, rendering all main text and annotations separately while retaining source IDs.

#### Scenario: Read Wudi translation
- **WHEN** a reader selects 白话 on volume001
- **THEN** 123 main text translations and 122 annotation translations appear, marked as a draft, without duplicate IDs.

#### Scenario: Visit an untranslated volume
- **WHEN** the reader visits volume002
- **THEN** only simplified and traditional options appear, and the original text remains readable.

### Requirement: Preserve reading interactions
Switching reading versions SHALL preserve source content, source anchor URLs, note visibility and the current passage. Preferences SHALL survive reload and shall fail safely when storage is unavailable.

#### Scenario: Compare a cited annotation
- **WHEN** a cited annotation is visible and the reader switches between all three versions
- **THEN** the corresponding passage remains visible at the same anchor URL, and switching back restores original text exactly.

#### Scenario: Return after an untranslated volume
- **WHEN** a reader selects 白话, visits an untranslated volume and returns
- **THEN** the translated volume restores 白话 without breaking the fallback volume.

#### Scenario: Storage unavailable
- **WHEN** browser storage is blocked
- **THEN** all available versions can still be selected.
