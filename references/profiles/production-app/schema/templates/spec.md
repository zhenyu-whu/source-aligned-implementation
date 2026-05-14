## ADDED Requirements

### Requirement: <!-- requirement name，可保留英文技术标题 -->
<!-- 描述 normative behavior。保留 SHALL/MUST/MUST NOT 等规范关键字，并保持可测试。 -->

Source Truth:
- `ST-001`: <!-- exact Source Truth ID 和 obligation 摘要。逐个枚举 ID；不要使用 ST-001-ST-010 这类 ranges。 -->

Source Trace:
- `docs/...`: <!-- 来自相关 ST item 的 Source Pointers / Read Notes；填写 exact source、section、product workflow、architecture rule、route、command、API、DTO、table、migration、event、job、queue、storage path、auth/security rule、entitlement、prototype scene/object state、fixture slice、viewport rule、deployment environment 或 verification row；不要用整篇文档替代精准 section。 -->

#### Scenario: <!-- scenario name -->
- **WHEN** <!-- 描述 condition、user action、route、command、API call、worker event、state、data mutation、auth context 或 failure path -->
- **THEN** <!-- 描述与 source docs 对齐的 expected observable production outcome -->

## Production Alignment Gate

- Source Truth IDs covered: <!-- ST-001, ST-002, ...；逐个枚举 exact IDs，不使用 ranges -->
- Source docs read: <!-- 使用的 exact docs files 与 Source Pointers；说明文字，不要写宽泛整篇读取义务 -->
- Product workflow coverage: <!-- 覆盖的 workflows，或“无” -->
- Prototype route / object / responsive coverage: <!-- 覆盖的 routes、scenes、objects、viewports，或“无” -->
- Architecture / module coverage: <!-- 覆盖的 apps/packages/runtime boundaries，或“无” -->
- Data / API / backend coverage: <!-- 覆盖的 tables、migrations、commands、DTOs、endpoints、transactions，或“无” -->
- Auth / security / privacy coverage: <!-- 覆盖的 auth、authorization、sensitive data、asset access、audit，或“无” -->
- Async / realtime / worker coverage: <!-- 覆盖的 jobs、queues、locks、SSE/outbox、reconciler，或“无” -->
- AI / provider / sandbox coverage: <!-- 覆盖的 task schemas、provider adapter、fixture replay、real-provider boundary，或“无” -->
- Storage / asset coverage: <!-- 覆盖的 asset layers、presigned URL、retention、export cache，或“无” -->
- Observability / ops / deployment coverage: <!-- 覆盖的 logs、metrics、audit、env/config、rollout、maintenance loops，或“无” -->
- Verification coverage: <!-- 覆盖的 unit/integration/e2e/contract/visual/security/ops checks，或“无” -->
- Forbidden drift checked: <!-- 已检查的 explicit MUST NOT boundaries；说明文字 -->
