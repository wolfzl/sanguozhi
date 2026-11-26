## ADDED Requirements

### Requirement: Optional sourced person dossier
A person dossier SHALL display approved profile facts, a unified life and office timeline, civil and military achievements, and separately identified setbacks. It SHALL preserve uncertainty and SHALL cite source passages for recorded facts. Portraits without dossiers SHALL retain their existing presentation.

#### Scenario: Read Zhang Fei
- **WHEN** a reader opens Zhang Fei's portrait
- **THEN** the approved overview and contextual biography appear with a single career timeline, military achievements, civil empty state and setbacks.

#### Scenario: Check a disputed event
- **WHEN** the reader checks the Xiapi loss
- **THEN** its citation identifies the annotation work Yingxiong Ji and opens the corresponding source passage.

### Requirement: Navigable responsive dossier
Dossier event links SHALL target existing reciprocal events, reference links SHALL resolve, and tables SHALL remain readable at desktop and 320-pixel mobile widths without page overflow. Plain-name related figures SHALL NOT link to nonexistent person pages.

#### Scenario: Read on a narrow screen
- **WHEN** the dossier is viewed at 320 pixels
- **THEN** its timeline and achievement rows remain readable within the viewport.

### Requirement: Reproducible dossier generation
The card generator SHALL reproduce dossier content and all other portraits without unrelated changes.

#### Scenario: Regenerate cards
- **WHEN** the generator runs twice
- **THEN** both results are identical and all source quotations and event associations validate.
