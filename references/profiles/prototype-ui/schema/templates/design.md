## Context

<!-- Background, current prototype state, source docs, constraints, and dependencies. -->

## Goals / Non-Goals

**Goals:**
<!-- What this design achieves for the prototype. -->

**Non-Goals:**
<!-- What this design explicitly excludes. -->

## Prototype Source Map

<!-- Map this change to Source Truth IDs and exact original sources: plan row, PRD/architecture/prototype docs, handoff, page/object specs, system readiness docs, API/data contracts, and verification matrix rows. -->

## Decisions

<!-- Source-backed technical/design decisions. Include rationale and alternatives when there is a real choice. -->

## Runtime / Data Flow Design

<!-- Explain route -> scene config -> fixture -> shell -> page body -> object state for this change, and equivalent frontend/backend/data flow where applicable. Cover every current-change Source Truth item. -->

## Fixture / Mutation / Asset Design

<!-- Describe deterministic fixture slices, local state, mock mutations, stable assets, and forbidden real services. -->

## Page / Object / Responsive Design

<!-- Describe page regions, object open/close and recovery behavior, component specimens, viewport behavior, and object degradation. -->

## Verification Design

<!-- Describe the source-equivalent checks required for this change: user-equivalent interactions, API/contract tests, mutation/persistence assertions, failure/edge paths, rendered layout checks, scene smoke, key flow, object, asset, and responsive checks. -->

## Prototype Alignment Gate

- Source Truth IDs implemented / preserved / deferred: <!-- ST-001 implemented, ST-002 preserved, ST-003 deferred, ...; enumerate exact IDs, no ranges such as ST-001-ST-010 -->
- Canonical keys used: <!-- state keys, stage keys, overlay keys, scene IDs, object keys -->
- Source trace complete: <!-- yes/no plus missing items -->
- No new scene/page/object/lifecycle/overlay introduced: <!-- yes/no -->
- Interactions trace to `interaction-map.md`: <!-- yes/no or not applicable -->
- Fixture writes stay inside allowed slices/local state: <!-- yes/no or not applicable -->
- Assets/components trace to readiness docs: <!-- yes/no or not applicable -->
- Responsive obligations captured: <!-- yes/no or not applicable -->
- Later-change boundaries preserved: <!-- yes/no -->

## Risks / Trade-offs

<!-- Known risks and mitigations. -->

## Open Questions

<!-- Outstanding questions. Use "无" only when none remain. -->
