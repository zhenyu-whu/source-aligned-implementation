## Requirement Coverage

<!--
Map every current-change Source Truth item, Requirement scenario, and material design obligation to implementation task IDs, verification task IDs, and verification proof.
This section is a generation-quality gate, not executable work. Do not put checkbox tasks here.
Use one row per source-truth item, requirement scenario, or material design obligation. Do not use aggregate rows as a substitute for covering the underlying scenarios or obligations.
-->

### Source Truth Coverage

| Source Truth ID | Source Truth Summary | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- |
| <!-- ST-001; exactly one ID per row, no ranges such as ST-001-ST-010 --> | <!-- Short source-backed obligation summary. --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Source-equivalent proof: user interaction, API test, data assertion, worker/realtime path, security check, rendered layout check, etc. --> |

### Requirement / Scenario Coverage

| Capability | Requirement | Scenario | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- | --- |
| <!-- capability name --> | <!-- exact requirement name --> | <!-- exact scenario name --> | <!-- ST-001, ST-002; enumerate exact IDs, no ranges --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Scenario-level observable proof. --> |

### Design Obligation Coverage

| Design Section | Design Obligation | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- |
| <!-- exact design section / decision / gate item --> | <!-- material implementation, preservation, or verification obligation --> | <!-- ST-001, ST-002, or Not applicable; enumerate exact IDs, no ranges --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Design-obligation proof. --> |

## 1. Repository / Runtime Foundation

- [ ] 1.1 <!-- Implement or update repository structure, workspace scripts, runtime process boundaries, config validation, or local infrastructure foundations. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Architecture / module boundary or runtime foundation obligations. -->
  Source: <!-- Architecture sections, package boundary rules, engineering baseline, deployment/environment anchors. -->
  Preserve: <!-- Monorepo boundaries, script conventions, config ownership, environment parity, forbidden parallel tooling, and runtime process constraints. -->
  Proof: <!-- Workspace command, config validation, local infra, typecheck/lint/test, or runtime startup evidence proves the source-backed foundation. -->

## 2. Domain / Data / Authorization

- [ ] 2.1 <!-- Implement domain command, policy, database schema/migration, transaction, idempotency, lock, entitlement, or authorization behavior. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Domain / data / migration / auth design obligations. -->
  Source: <!-- PRD object model, architecture data model, auth/security, billing/entitlement, idempotency, lock, or migration anchors. -->
  Preserve: <!-- Domain ownership, transaction boundaries, current-state/log split, table invariants, idempotency semantics, lock semantics, authorization rules, privacy boundaries, and forbidden direct table writes. -->
  Proof: <!-- Domain unit test, db integration test, migration check, authorization negative test, idempotency assertion, or data invariant evidence passes. -->

## 3. API / Async / Realtime

- [ ] 3.1 <!-- Implement API route/handler, DTO validation, queue/job worker, provider boundary, SSE/outbox event, reconciler, export job, or realtime projection behavior. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- API / async / realtime / AI / worker design obligations. -->
  Source: <!-- API protocol, SSE envelope, action/job chain, provider sandbox, worker transaction, outbox, reconciler, export/storage anchors. -->
  Preserve: <!-- DTO shape, command/use-case entry, minimal queue payload, DB-as-truth recovery, provider/sandbox separation, SSE replay semantics, status transitions, and no optimistic business facts. -->
  Proof: <!-- API/contract test, worker integration test, SSE/outbox replay test, provider sandbox fixture replay, failure/retry/reconciler test, or export/cache assertion passes. -->

## 4. Frontend / UX

- [ ] 4.1 <!-- Implement production frontend route, page surface, editor workflow, component/object behavior, client state, visual fidelity, or responsive behavior. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Frontend / UX / prototype fidelity design obligations. -->
  Source: <!-- PRD flow/page/module anchors, prototype page/object/system docs, interaction map, state vocabulary, design-system, component specimen, verification matrix anchors. -->
  Preserve: <!-- Route ownership, UI regions, action placement/cardinality, local-vs-server state split, fixture-derived states, object semantics, responsive behavior, accessibility, and forbidden prototype drift. -->
  Proof: <!-- User-equivalent E2E, component test, route smoke, visual/responsive screenshot, accessibility check, or client-state interaction evidence passes. -->

## 5. Security / Ops / Deployment

- [ ] 5.1 <!-- Implement or update security/privacy controls, asset access, structured logging, audit, metrics, maintenance loop, environment/deployment readiness, migration ordering, or runbook support. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Observability / ops / deployment / rollout obligations. -->
  Source: <!-- Security/privacy, storage, observability, audit, deployment, environment, maintenance loop, or rollout anchors. -->
  Preserve: <!-- Private-by-default data/assets, presigned URL authorization, sensitive-log redaction, trace/audit keys, local/staging/production separation, maintenance ownership, deployment compatibility, and forbidden public exposure. -->
  Proof: <!-- Security/privacy test, audit/log assertion, env/config check, maintenance loop test, migration dry run, deployment smoke, or operational readiness evidence passes. -->

## 6. Verification

- [ ] 6.1 <!-- Add or update source-equivalent verification across domain, db, API, worker, SSE, security, frontend, responsive, ops, or deployment readiness. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names covered by this verification. -->
  Design: <!-- Design obligations covered by this verification. -->
  Source: <!-- Verification strategy, architecture testing section, prototype verification matrix, security/privacy rules, API/data contracts, worker/realtime anchors. -->
  Preserve: <!-- Verification must prove source-level structure, count, region, state, interaction, data persistence, API contract, auth path, event/job behavior, failure/recovery, responsive behavior, or ops/deployment constraints where relevant. Text-existence-only checks are insufficient. -->
  Proof: <!-- Targeted verification command passes and covers the relevant spec scenarios, design obligations, source docs, and preserve constraints. -->
