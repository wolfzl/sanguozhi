# person-portraits Specification

## Purpose
TBD - created by archiving change all-person-portraits. Update Purpose after archive.
## Requirements
### Requirement: Concise dated portraits
All existing person pages SHALL present concise biographies, sourced lifespan information and dated milestones; uncertain dates SHALL remain visibly uncertain.
#### Scenario: Read a portrait
- **WHEN** a reader opens any of the 65 person pages
- **THEN** the page shows a sourced lifespan, a natural biography and dated key experiences without labeling every birth as inferred.

### Requirement: People and events navigation
Important events in portraits SHALL link to existing event pages and SHALL have reciprocal person associations; missing major career events SHALL receive sourced pages.
#### Scenario: Follow an important experience
- **WHEN** a reader follows a narrative or milestone event link
- **THEN** a valid event page opens and its participant list includes the relevant person.

### Requirement: Grounded relationships and stories
Portrait facts and relationships SHALL cite the bundled Three Kingdoms text or its annotations, with annotation works identified; supplementary lifespan evidence MAY use clearly identified primary sources.
#### Scenario: Verify a family relationship or story
- **WHEN** a reader opens its citation
- **THEN** the matching primary passage is available and uncertain chronology is explained.

