## Context

<!-- Background, current production state, source docs, constraints, dependencies, and existing implementation context. -->

## Goals / Non-Goals

**Goals:**
<!-- What this design achieves for the production system. -->

**Non-Goals:**
<!-- What this design explicitly excludes. -->

## Production Source Map

<!-- Map this change to Source Truth IDs and exact original sources: PRD sections, architecture sections, prototype pages/objects/system docs, API/data/security/ops/deployment references, and verification rows. -->

## Decisions

<!-- Source-backed technical/product decisions. Include rationale and alternatives when there is a real choice. -->

## Architecture / Module Boundary Design

<!-- Explain app/package ownership, runtime/process boundaries, dependency direction, configuration ownership, and forbidden cross-layer shortcuts. -->

## Domain / Data / Migration Design

<!-- Explain domain commands/use-cases, policies/rules, data model, migrations, transaction boundaries, idempotency, locks, persistence, and backfill/compatibility when relevant. -->

## API / Auth / Security Design

<!-- Explain routes/handlers, DTO validation, session/user mapping, authorization, entitlement checks, privacy boundaries, sensitive data handling, asset access, and audit behavior. -->

## Async / Realtime / AI / Worker Design

<!-- Explain queues, job payloads, worker handlers, provider adapters, sandbox/fixture replay, SSE/outbox events, reconciler/maintenance loops, retries, failure recovery, and lock release. -->

## Frontend / UX / Prototype Fidelity Design

<!-- Explain page regions, route flow, client state, user interactions, object/component behavior, visual fidelity, responsive behavior, loading/empty/failure/disabled states, and where prototype UX is intentionally preserved. -->

## Observability / Ops / Deployment Design

<!-- Explain structured logs, trace keys, audit records, metrics/alerts, environment variables, local/staging/production differences, deployment/migration ordering, operational runbooks, and maintenance tasks. -->

## Verification Design

<!-- Describe source-equivalent checks: domain unit tests, db integration tests, API/contract tests, worker/reconciler tests, SSE/outbox tests, auth/security/privacy negative tests, provider sandbox tests, frontend E2E/visual/responsive checks, deployment/config checks, and staging smoke when relevant. -->

## Rollout / Compatibility

<!-- Describe expand/deploy/switch/contract ordering, backward compatibility, migration/backfill, queue/job compatibility, feature flags/config, and rollback constraints. Use "无" only when not applicable. -->

## Production Alignment Gate

- Source Truth IDs implemented / preserved / deferred: <!-- ST-001 implemented, ST-002 preserved, ST-003 deferred, ...; enumerate exact IDs, no ranges such as ST-001-ST-010 -->
- Canonical product and technical keys used: <!-- routes, commands, DTOs, tables, events, jobs, assets, entitlement names, env names, state keys -->
- Source trace complete: <!-- yes/no plus missing items -->
- No unplanned route/page/object/service/API/table/job/event/provider/environment introduced: <!-- yes/no -->
- Interactions trace to source-backed flows/contracts: <!-- yes/no or not applicable -->
- Data writes, migrations, locks, idempotency, and transactions stay inside source-defined ownership boundaries: <!-- yes/no or not applicable -->
- Auth, authorization, privacy, asset access, and audit rules trace to source-backed references: <!-- yes/no or not applicable -->
- Async jobs, SSE/outbox, provider calls, sandbox behavior, and reconciler behavior trace to source-backed references: <!-- yes/no or not applicable -->
- Assets/components/prototype UX/responsive obligations captured: <!-- yes/no or not applicable -->
- Observability/ops/deployment obligations captured: <!-- yes/no or not applicable -->
- Later-change boundaries preserved: <!-- yes/no -->

## Risks / Trade-offs

<!-- Known risks and mitigations. -->

## Open Questions

<!-- Outstanding questions. Use "无" only when none remain. -->
