## Requirement Coverage

<!--
将每个 current-change Source Truth item、Requirement scenario 与 material design obligation 映射到 implementation task IDs、verification task IDs 与 verification proof。
同时映射此 tasks 文件中任何位置引用的 deferred/non-goal、preserve-existing 或 unresolved-conflict Source Truth ID，尤其是 preserve constraint、forbidden-drift boundary、negative requirement、implementation constraint、verification obligation 或 coverage-table reference。
本节是 generation-quality gate，不是 executable work。不要在这里放 checkbox tasks。
每个 source-truth item、requirement scenario 或 material design obligation 使用一行；不要用 aggregate rows 替代底层 scenarios 或 obligations 的覆盖。
-->

### Source Truth Coverage

| Source Truth ID | Source Truth Summary | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- |
| <!-- ST-001；每行只能有一个 ID，不使用 ST-001-ST-010 这类 ranges。包含每个 current-change Source Truth item 与此 tasks 文件任意位置引用的每个 ST ID。 --> | <!-- 概述 source-backed obligation；当该行是 preserve 或 forbidden-drift item 时，也写清 deferred/non-goal boundary 摘要。 --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 source-equivalent proof：user interaction、API test、data assertion、worker/realtime path、security check、rendered layout check、forbidden-drift/static check 等。 --> |

### Requirement / Scenario Coverage

| Capability | Requirement | Scenario | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- | --- |
| <!-- capability name --> | <!-- exact requirement name --> | <!-- exact scenario name --> | <!-- ST-001, ST-002；逐个枚举 exact IDs，不使用 ranges --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 scenario-level observable proof。 --> |

### Design Obligation Coverage

| Design Section | Design Obligation | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- |
| <!-- exact design section / decision / gate item --> | <!-- 说明 material implementation、preservation 或 verification obligation。 --> | <!-- ST-001, ST-002, 或 Not applicable；逐个枚举 exact IDs，不使用 ranges --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 design-obligation proof。 --> |

## 1. Repository / Runtime Foundation

- [ ] 1.1 <!-- 描述要实现或更新的 repository structure、workspace scripts、runtime process boundaries、config validation 或 local infrastructure foundations。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Architecture / module boundary 或 runtime foundation obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 Architecture sections、package boundary rules、engineering baseline、deployment/environment anchors。 -->
  Preserve: <!-- 说明必须保留的 monorepo boundaries、script conventions、config ownership、environment parity、forbidden parallel tooling 与 runtime process constraints。 -->
  Proof: <!-- 说明 workspace command、config validation、local infra、typecheck/lint/test 或 runtime startup evidence 如何证明 source-backed foundation。 -->

## 2. Domain / Data / Authorization

- [ ] 2.1 <!-- 描述要实现的 domain command、policy、database schema/migration、transaction、idempotency、lock、entitlement 或 authorization behavior。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Domain / data / migration / auth design obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 PRD object model、architecture data model、auth/security、billing/entitlement、idempotency、lock 或 migration anchors。 -->
  Preserve: <!-- 说明必须保留的 domain ownership、transaction boundaries、current-state/log split、table invariants、idempotency semantics、lock semantics、authorization rules、privacy boundaries 与 forbidden direct table writes。 -->
  Proof: <!-- 说明 domain unit test、db integration test、migration check、authorization negative test、idempotency assertion 或 data invariant evidence 如何通过。 -->

## 3. API / Async / Realtime

- [ ] 3.1 <!-- 描述要实现的 API route/handler、DTO validation、queue/job worker、provider boundary、SSE/outbox event、reconciler、export job 或 realtime projection behavior。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- API / async / realtime / AI / worker design obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 API protocol、SSE envelope、action/job chain、provider sandbox、worker transaction、outbox、reconciler、export/storage anchors。 -->
  Preserve: <!-- 说明必须保留的 DTO shape、command/use-case entry、minimal queue payload、DB-as-truth recovery、provider/sandbox separation、SSE replay semantics、status transitions 与 no optimistic business facts。 -->
  Proof: <!-- 说明 API/contract test、worker integration test、SSE/outbox replay test、provider sandbox fixture replay、failure/retry/reconciler test 或 export/cache assertion 如何通过。 -->

## 4. Frontend / UX

- [ ] 4.1 <!-- 描述要实现的 production frontend route、page surface、editor workflow、component/object behavior、client state、visual fidelity 或 responsive behavior。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Frontend / UX / prototype fidelity design obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 PRD flow/page/module anchors、prototype page/object/system docs、interaction map、state vocabulary、design-system、component specimen、verification matrix anchors。 -->
  Preserve: <!-- 说明必须保留的 route ownership、UI regions、action placement/cardinality、local-vs-server state split、fixture-derived states、object semantics、responsive behavior、accessibility 与 forbidden prototype drift。 -->
  Proof: <!-- 说明 user-equivalent E2E、component test、route smoke、visual/responsive screenshot、accessibility check 或 client-state interaction evidence 如何通过。 -->

## 5. Security / Ops / Deployment

- [ ] 5.1 <!-- 描述要实现或更新的 security/privacy controls、asset access、structured logging、audit、metrics、maintenance loop、environment/deployment readiness、migration ordering 或 runbook support。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Observability / ops / deployment / rollout obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 Security/privacy、storage、observability、audit、deployment、environment、maintenance loop 或 rollout anchors。 -->
  Preserve: <!-- 说明必须保留的 private-by-default data/assets、presigned URL authorization、sensitive-log redaction、trace/audit keys、local/staging/production separation、maintenance ownership、deployment compatibility 与 forbidden public exposure。 -->
  Proof: <!-- 说明 security/privacy test、audit/log assertion、env/config check、maintenance loop test、migration dry run、deployment smoke 或 operational readiness evidence 如何通过。 -->

## 6. Verification

- [ ] 6.1 <!-- 描述要新增或更新的 source-equivalent verification，覆盖 domain、db、API、worker、SSE、security、frontend、responsive、ops 或 deployment readiness。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- 此 verification 覆盖的 Requirement / scenario names。 -->
  Design: <!-- 此 verification 覆盖的 design obligations。 -->
  Source: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 Verification strategy、architecture testing section、prototype verification matrix、security/privacy rules、API/data contracts、worker/realtime anchors。 -->
  Preserve: <!-- 说明 verification 必须证明 source-level structure、count、region、state、interaction、data persistence、API contract、auth path、event/job behavior、failure/recovery、responsive behavior 或 ops/deployment constraints；仅 text-existence checks 不足。 -->
  Proof: <!-- 说明 targeted verification command 通过，并覆盖相关 spec scenarios、design obligations、source docs 与 preserve constraints。 -->
