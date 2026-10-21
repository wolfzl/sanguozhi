## ADDED Requirements

### Requirement: Comprehensive sourced portraits
The system SHALL publish the approved Cao Cao material and six expanded portraits using titled narrative, dated career records, civil achievements, military achievements, setbacks, relationships, assessment and source analysis. Every historical entry SHALL include exact source evidence with body and annotation layers distinguished.

#### Scenario: Read Cao Cao
- **WHEN** the reader visits Cao Cao
- **THEN** all approved records appear with grouped achievements and the complete primary biography appendix.

#### Scenario: Read Sima Yi
- **WHEN** the reader visits Sima Yi
- **THEN** the page explains the scattered source scope and does not claim a dedicated biography in this book.

### Requirement: Preserve existing navigation and portraits
The expansion SHALL preserve existing events and the other 58 portraits, including Zhang Fei, and SHALL retain valid reciprocal event navigation. Pages SHALL remain readable at 320-pixel mobile width. Source citations SHALL reveal and focus the correct excerpt, including when filtering sources.

#### Scenario: Follow a source citation
- **WHEN** a reader clicks an inline citation
- **THEN** its source opens and can be read even after a source search.

### Requirement: Reproducible validated publication
Generation SHALL be deterministic and validate exact quotations, source layers, required expanded sections and reciprocal links before publication. The approved review service SHALL be stopped after Cao Cao is published.

#### Scenario: Regenerate and publish
- **WHEN** cards are generated twice
- **THEN** both results match and the preview serves the verified portraits.
