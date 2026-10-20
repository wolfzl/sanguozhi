## ADDED Requirements
### Requirement: Four historical lanes
The event explorer SHALL support a lords lane alongside Wei, Shu and Wu, preserve canonical shared events, and default to all events.
#### Scenario: New visit and restored filters
- **WHEN** a reader visits events without parameters or selects the lords lane
- **THEN** all events are initially visible and lords selection survives reload and back navigation.
### Requirement: Unified Han grouping
The people explorer SHALL group Yuan figures and independent Han lords under 汉末 and provide related new Wei, Shu and Wu biographies.
#### Scenario: Find Han lords
- **WHEN** the reader selects 汉末
- **THEN** Yuan Shao, Yuan Shu, Gongsun Zan, Lü Bu and Ma Teng appear without a separate Yuan group.
### Requirement: Sourced connected content
Every new factual section SHALL cite bundled book passages; annotation sources SHALL be identified; event participants SHALL link reciprocally to people.
#### Scenario: Inspect a new event
- **WHEN** a reader opens a new event and follows its source or participant
- **THEN** the matching passage and linked person exist, and that person links back to the event.
