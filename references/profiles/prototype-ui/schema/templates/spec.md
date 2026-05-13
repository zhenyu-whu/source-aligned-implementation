## ADDED Requirements

### Requirement: <!-- requirement name -->
<!-- 描述 normative behavior。保留 SHALL/MUST/MUST NOT 等规范关键字，并保持可测试。 -->

Source Truth:
- `ST-001`: <!-- exact Source Truth ID 和 obligation 摘要。逐个枚举 ID；不要使用 ST-001-ST-010 这类 ranges。 -->

Source Trace:
- `docs/prototype/...`: <!-- exact source、section、scene、route、object state、fixture slice、interaction、asset、viewport rule、API/data contract 或 key flow；解释性内容。 -->

#### Scenario: <!-- scenario name -->
- **WHEN** <!-- 描述 condition、user action、route、scene、object state 或 mock mutation -->
- **THEN** <!-- 描述与 prototype source 对齐的 expected observable outcome -->

## Prototype Alignment Gate

- Source Truth IDs covered: <!-- ST-001, ST-002, ...；逐个枚举 exact IDs，不使用 ranges -->
- Source docs read: <!-- 使用的 exact docs/prototype files；说明文字 -->
- Scene / route coverage: <!-- 覆盖的 scenes 与 routes，或“无” -->
- Object state coverage: <!-- 覆盖的 objects 与 states，或“无” -->
- Fixture / mutation / API / data coverage: <!-- 覆盖的 slices、mock mutations、API/data/backend contracts，或“无” -->
- Asset / component coverage: <!-- 覆盖的 asset IDs 与 component specimens，或“无” -->
- Responsive coverage: <!-- 覆盖的 desktop/notebook/mobile obligations，或“无” -->
- Forbidden drift checked: <!-- 已检查的 explicit MUST NOT boundaries；说明文字 -->
