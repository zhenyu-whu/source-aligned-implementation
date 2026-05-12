## Source Manifest

<!--
Classify the source documents for this change before extracting Source Truth items.
Use exact paths. Required documents must be read. Conditionally relevant documents must be read when they are referenced by required docs for the current change's routes, scenes, fixtures, mutations, assets, object states, verification checks, or later-change boundaries.
-->

| Classification | Source Document | Reason / Change Link |
| --- | --- | --- |
| required | <!-- exact path --> | <!-- change row / capability / route / scene / fixture / mutation / asset / verification link --> |
| conditionally relevant and read | <!-- exact path --> | <!-- why this document affects the current change --> |
| reference-only | <!-- exact path --> | <!-- e.g. existing capability names only; must not narrow source truth --> |
| intentionally not read | <!-- exact path --> | <!-- concrete no-overlap reason; convenience or file size is not valid --> |

## Source Documents Read

<!-- List every original PRD, architecture, prototype, design, interaction, API, data, system, and verification document read for this change. Include exact paths and relevant headings/sections. -->

## Source Coverage Ledger

<!--
Maintain one row per source document read. Each document must either contribute to Source Truth, deferred/non-goal Source Truth, unresolved conflict, or an explicit no-current-change-impact note.
-->

| Source Document | Sections / Anchors Read | Extraction Buckets | Coverage Outcome |
| --- | --- | --- | --- |
| <!-- exact path --> | <!-- headings / rows / scene IDs / fixture keys / mutation names / asset IDs / object states --> | <!-- runtime / scene-loader; scene fixtures; shared slices; mock mutations; object-state fixtures; visual assets; mark / selection / token payloads; export preview / record; state vocabulary / forbidden drift; component / responsive constraints; verification obligations; later-change / non-goal boundaries; change-specific bucket --> | <!-- ST-001, ST-002 / deferred ST-... / unresolved conflict ST-... / no-current-change-impact: reason --> |

## Extraction Buckets

<!--
Use buckets to avoid losing source detail before consolidating Source Truth items.
Buckets are not a substitute for Source Truth items; every implementation-relevant obligation in buckets must be represented below.
Add change-specific buckets if needed.
-->

### Runtime / Scene-Loader

<!-- Route, scene config, fixture loading, shell/page/object consumption chain, and runtime boundary obligations. -->

### Scene Fixtures

<!-- Scene IDs, fixture keys, required slice presence, representative state combinations, and fixture acceptance obligations. -->

### Shared Slices

<!-- Data slice ownership, required fields, deterministic values, and state/data boundaries. -->

### Mock Mutations

<!-- Mutation names, affected slices, allowed writes, forbidden side effects, success/failure/running semantics. -->

### Object-State Fixtures

<!-- Object state variants hosted inside scenes, open/close context, local object fields, and non-scene boundaries. -->

### Visual Assets

<!-- Canvas, thumbnails, placeholders, empty states, export previews, dimensions, visual semantics, and no-real-asset boundaries. -->

### Mark / Selection / Token Payloads

<!-- Mark targets, selection geometry, token candidates, custom labels, stale/read-only behavior, and payload immutability. -->

### Export Preview / Record

<!-- Export preview asset, mock records, current-version-only export, and no real file generation. -->

### State Vocabulary / Forbidden Drift

<!-- Canonical keys, stage/overlay whitelist, no new routes/scenes/states/assets/mutations/services, and semantic separation. -->

### Component / Responsive Constraints

<!-- Token, component specimen, density, responsive, object degradation, and visual fidelity obligations. -->

### Verification Obligations

<!-- Smoke, screenshot, object, key-flow, and source-equivalent verification obligations relevant to this change. -->

### Later-Change / Non-Goal Boundaries

<!-- Source-backed deferrals and explicit non-goals that downstream artifacts must preserve. -->

## Source Truth Items

<!--
Use stable IDs. Extract every source-backed item relevant to the selected change.
Do not use this section to decide implementation shortcuts. Capture source truth first.
Only create Source Truth items for implementation-relevant obligations: behavior to implement, behavior to preserve, verification to perform, boundaries to enforce, or conflicts to resolve.
Do not create Source Truth items for workflow metadata, artifact readiness, dependency status, absence of blockers, "no questions", or "can proceed"; put those in Conflicts / Ambiguities or the Alignment Gate.
-->

### ST-001 <!-- short source-backed obligation name -->

- Source: <!-- exact file path plus heading / stable anchor / row / scene / route / object / API / asset / fixture / interaction name -->
- Extract: <!-- copied or tightly paraphrased source truth with all implementation-relevant details preserved -->
- Relevance: <!-- why this belongs to the current change -->
- Implementation Implication: <!-- what proposal/spec/design/tasks/apply must preserve -->
- Boundary: <!-- current-change scope / preserve-existing / later-change / non-goal / unresolved conflict -->

## Deferred / Non-Goal Source Truth

<!-- List source-backed later-change and non-goal items by Source Truth ID. Do not invent deferrals that are not backed by original sources. -->

## Conflicts / Ambiguities

<!-- Record conflicts, ambiguous ownership, or source gaps. Use "无" only when none remain. -->

## Source Truth Alignment Gate

- Source documents read: <!-- exact paths -->
- Source documents intentionally not read: <!-- exact paths and reasons, or "无" -->
- Required manifest coverage: <!-- confirm every required document is covered by Source Truth / deferred Source Truth / unresolved conflict / no-current-change-impact note -->
- Conditional manifest coverage: <!-- confirm every conditionally relevant document was read and covered, or list blockers -->
- Extraction bucket coverage: <!-- list each applicable bucket and the Source Truth IDs or deferred/non-goal IDs covering it -->
- Named identifier coverage: <!-- enumerate covered scenes / routes / object states / fixture keys / slices / mutations / asset IDs / component specimens / viewports / verification checks when relevant -->
- Current-change Source Truth IDs: <!-- ST-001, ST-002, ... -->
- Preserve-existing Source Truth IDs: <!-- ST-... or "无" -->
- Deferred / non-goal Source Truth IDs: <!-- ST-... or "无" -->
- Unresolved conflicts: <!-- ST-... or "无" -->
- Completeness confirmation: <!-- confirm no relevant source-backed obligation was intentionally omitted, or list blockers -->

<!-- Source Truth ID lists must enumerate exact IDs; do not use ranges such as ST-001-ST-010. -->
