## ADDED Requirements

### Requirement: <!-- requirement name -->
<!-- Normative behavior. Use SHALL/MUST/MUST NOT and keep wording testable. -->

Source Truth:
- `ST-001`: <!-- exact Source Truth ID and short obligation summary. Enumerate IDs individually; do not use ranges such as ST-001-ST-010. -->

Source Trace:
- `docs/...`: <!-- exact source, section, product workflow, architecture rule, route, command, API, DTO, table, migration, event, job, queue, storage path, auth/security rule, entitlement, prototype scene/object state, fixture slice, viewport rule, deployment environment, or verification row -->

#### Scenario: <!-- scenario name -->
- **WHEN** <!-- condition, user action, route, command, API call, worker event, state, data mutation, auth context, or failure path -->
- **THEN** <!-- expected observable production outcome aligned to source docs -->

## Production Alignment Gate

- Source Truth IDs covered: <!-- ST-001, ST-002, ...; enumerate exact IDs, no ranges -->
- Source docs read: <!-- exact docs files used -->
- Product workflow coverage: <!-- workflows covered or "无" -->
- Prototype route / object / responsive coverage: <!-- routes, scenes, objects, viewports covered or "无" -->
- Architecture / module coverage: <!-- apps/packages/runtime boundaries covered or "无" -->
- Data / API / backend coverage: <!-- tables, migrations, commands, DTOs, endpoints, transactions covered or "无" -->
- Auth / security / privacy coverage: <!-- auth, authorization, sensitive data, asset access, audit covered or "无" -->
- Async / realtime / worker coverage: <!-- jobs, queues, locks, SSE/outbox, reconciler covered or "无" -->
- AI / provider / sandbox coverage: <!-- task schemas, provider adapter, fixture replay, real-provider boundary covered or "无" -->
- Storage / asset coverage: <!-- asset layers, presigned URL, retention, export cache covered or "无" -->
- Observability / ops / deployment coverage: <!-- logs, metrics, audit, env/config, rollout, maintenance loops covered or "无" -->
- Verification coverage: <!-- unit/integration/e2e/contract/visual/security/ops checks covered or "无" -->
- Forbidden drift checked: <!-- explicit MUST NOT boundaries checked -->
