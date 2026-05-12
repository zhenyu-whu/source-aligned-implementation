## Source Manifest

<!--
Classify the source documents for this change before extracting Source Truth items.
Use exact paths. Required documents must be read. Conditionally relevant documents must be read when they are referenced by required docs for the current change's workflows, routes, modules, commands, APIs, data entities, jobs/events, assets, security rules, environments, verification checks, or later-change boundaries.
-->

| Classification | Source Document | Reason / Change Link |
| --- | --- | --- |
| required | <!-- exact path --> | <!-- change row / capability / workflow / route / module / API / entity / job / environment / verification link --> |
| conditionally relevant and read | <!-- exact path --> | <!-- why this document affects the current change --> |
| reference-only | <!-- exact path --> | <!-- e.g. existing capability names only; must not narrow source truth --> |
| intentionally not read | <!-- exact path --> | <!-- concrete no-overlap reason; convenience or file size is not valid --> |

## Source Documents Read

<!-- List every original PRD, architecture, prototype, design, interaction, API, data, security, ops, deployment, and verification document read for this change. Include exact paths and relevant headings/sections. -->

## Source Coverage Ledger

<!--
Maintain one row per source document read. Each document must either contribute to Source Truth, deferred/non-goal Source Truth, unresolved conflict, or an explicit no-current-change-impact note.
-->

| Source Document | Sections / Anchors Read | Extraction Buckets | Coverage Outcome |
| --- | --- | --- | --- |
| <!-- exact path --> | <!-- headings / rows / workflow names / route names / command names / API names / entity names / job/event types / environment names / verification rows --> | <!-- product / workflow scope; architecture / module boundaries; domain / data / migrations; API / auth / security; async / realtime / AI / worker; storage / assets; frontend / UX / prototype fidelity; observability / ops / deployment; verification obligations; later-change / non-goal boundaries; change-specific bucket --> | <!-- ST-001, ST-002 / deferred ST-... / unresolved conflict ST-... / no-current-change-impact: reason --> |

## Extraction Buckets

<!--
Use buckets to avoid losing source detail before consolidating Source Truth items.
Buckets are not a substitute for Source Truth items; every implementation-relevant obligation in buckets must be represented below.
Add change-specific buckets if needed.
-->

### Product / Workflow Scope

<!-- User goals, workflows, product surfaces, acceptance criteria, and explicit product boundaries. -->

### Architecture / Module Boundaries

<!-- Package/app/module ownership, runtime boundaries, technology decisions, composition, and forbidden architectural drift. -->

### Domain / Data / Migrations

<!-- Entities, tables, DTOs, migrations, transactions, locks, idempotency, persistence ownership, and data invariants. -->

### API / Auth / Security

<!-- API endpoints/contracts, commands, authorization, permissions, privacy/security rules, entitlement checks, and audit requirements. -->

### Async / Realtime / AI / Worker

<!-- Jobs, queues, SSE/realtime events, outbox/reconciler behavior, AI provider boundaries, sandbox behavior, retries, and recovery. -->

### Storage / Assets

<!-- File/object storage, signing/access rules, generated assets, retained artifacts, export assets, and cleanup boundaries. -->

### Frontend / UX / Prototype Fidelity

<!-- Routes, pages, component states, interactions, responsive behavior, accessibility, and prototype fidelity obligations. -->

### Observability / Ops / Deployment

<!-- Logging, metrics, tracing, alerts, rollout, environment config, deployment, backfill, compatibility, and operational readiness. -->

### Verification Obligations

<!-- Unit, contract, integration, E2E, smoke, migration, security, observability, deployment, and source-equivalent verification obligations. -->

### Later-Change / Non-Goal Boundaries

<!-- Source-backed deferrals and explicit non-goals that downstream artifacts must preserve. -->

## Source Truth Items

<!--
Use stable IDs. Extract every source-backed item relevant to the selected production change.
Do not use this section to decide implementation shortcuts. Capture source truth first.
Only create Source Truth items for implementation-relevant obligations: behavior to implement, behavior to preserve, verification to perform, boundaries to enforce, or conflicts to resolve.
Do not create Source Truth items for workflow metadata, artifact readiness, dependency status, absence of blockers, "no questions", or "can proceed"; put those in Conflicts / Ambiguities or the Alignment Gate.
-->

### ST-001 <!-- short source-backed obligation name -->

- Source: <!-- exact file path plus heading / stable anchor / row / route / object / API / command / table / event / job / asset / fixture / interaction / ops / deployment / verification name -->
- Extract: <!-- copied or tightly paraphrased source truth with all implementation-relevant details preserved -->
- Relevance: <!-- why this belongs to the current change -->
- Implementation Implication: <!-- what proposal/spec/design/tasks/apply must preserve -->
- Boundary: <!-- current-change scope / preserve-existing / later-change / non-goal / unresolved conflict -->

## Deferred / Non-Goal Source Truth

<!-- List source-backed later-change and non-goal items by Source Truth ID. Do not invent deferrals that are not backed by original sources. -->

## Conflicts / Ambiguities

<!-- Record conflicts, ambiguous ownership, missing production decisions, or source gaps. Use "无" only when none remain. -->

## Source Truth Alignment Gate

- Source documents read: <!-- exact paths -->
- Source documents intentionally not read: <!-- exact paths and reasons, or "无" -->
- Required manifest coverage: <!-- confirm every required document is covered by Source Truth / deferred Source Truth / unresolved conflict / no-current-change-impact note -->
- Conditional manifest coverage: <!-- confirm every conditionally relevant document was read and covered, or list blockers -->
- Extraction bucket coverage: <!-- list each applicable bucket and the Source Truth IDs or deferred/non-goal IDs covering it -->
- Named identifier coverage: <!-- enumerate covered workflows / routes / modules / commands / APIs / DTOs / entities / tables / migrations / job or event types / provider boundaries / asset or storage IDs / auth rules / entitlements / environments / verification checks when relevant -->
- Current-change Source Truth IDs: <!-- ST-001, ST-002, ... -->
- Preserve-existing Source Truth IDs: <!-- ST-... or "无" -->
- Deferred / non-goal Source Truth IDs: <!-- ST-... or "无" -->
- Unresolved conflicts: <!-- ST-... or "无" -->
- Completeness confirmation: <!-- confirm no relevant source-backed obligation was intentionally omitted, or list blockers -->

<!-- Source Truth ID lists must enumerate exact IDs; do not use ranges such as ST-001-ST-010. -->
