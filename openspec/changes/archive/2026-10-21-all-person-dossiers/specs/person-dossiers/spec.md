## MODIFIED Requirements
### Requirement: Optional sourced person dossier
Every published person SHALL use the approved Zhang Fei dossier presentation: sourced profile facts, a unified life and office timeline, civil and military achievements, and separate setbacks. Empty sections SHALL explain the limits of the available records. Uncertain and absent offices or titles SHALL remain explicit. Existing Zhang Fei content and all biographies, relations and reciprocal events SHALL be preserved.

#### Scenario: Read any existing person
- **WHEN** a reader opens any of the 65 existing people
- **THEN** their own profile facts and combined timeline appear, and each of the three achievement/setback sections contains cited records or a visible explanation.

#### Scenario: Check a disputed event
- **WHEN** the reader checks the Xiapi loss
- **THEN** its citation identifies the annotation work Yingxiong Ji and opens the corresponding source passage.

### Requirement: Navigable responsive dossier
Dossier event links SHALL target existing reciprocal events, reference links SHALL resolve, and tables SHALL remain readable at desktop and 320-pixel mobile widths without page overflow. Plain-name related figures SHALL NOT link to nonexistent person pages. Captions, courtesy names, glossary summaries and navigation SHALL reflect each person's own data, and every existing milestone event entry SHALL remain accessible.

#### Scenario: Read on a narrow screen
- **WHEN** the dossier is viewed at 320 pixels
- **THEN** its timeline and achievement rows remain readable within the viewport.

#### Scenario: Missing courtesy or glossary
- **WHEN** a person has no known courtesy name or no glossary
- **THEN** the page indicates the unknown name and does not display a glossary copied from another person.
