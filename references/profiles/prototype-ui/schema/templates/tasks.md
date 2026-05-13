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
| <!-- ST-001；每行只能有一个 ID，不使用 ST-001-ST-010 这类 ranges。包含每个 current-change Source Truth item 与此 tasks 文件任意位置引用的每个 ST ID。 --> | <!-- 概述 source-backed obligation；当该行是 preserve 或 forbidden-drift item 时，也写清 deferred/non-goal boundary 摘要。 --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 source-equivalent proof：user interaction、API test、data assertion、edge path、rendered layout check、forbidden-drift/static check 等。 --> |

### Requirement / Scenario Coverage

| Capability | Requirement | Scenario | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- | --- |
| <!-- capability name --> | <!-- exact requirement name --> | <!-- exact scenario name --> | <!-- ST-001, ST-002；逐个枚举 exact IDs，不使用 ranges --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 scenario-level observable proof。 --> |

### Design Obligation Coverage

| Design Section | Design Obligation | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- |
| <!-- exact design section / decision / gate item --> | <!-- 说明 material implementation、preservation 或 verification obligation。 --> | <!-- ST-001, ST-002, 或 Not applicable；逐个枚举 exact IDs，不使用 ranges --> | <!-- 例如 2.1, 4.2 --> | <!-- 例如 6.1, 6.3 --> | <!-- 说明 design-obligation proof。 --> |

## 1. Runtime / Data / Asset

- [ ] 1.1 <!-- 描述要实现或更新的 route、scene、fixture、mock 或 asset foundations。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Runtime / data / fixture / mutation / asset design obligations。 -->
  Source: <!-- Scene registry、fixture contracts、interaction map、mock asset plan 或 state vocabulary anchors。 -->
  Preserve: <!-- 说明必须保留的 canonical keys、fixture slices、mock write boundaries、collection cardinality、asset IDs 与 forbidden drift。 -->
  Proof: <!-- 说明 deterministic scene/object state renders 与 linked mutation/fixture checks 如何证明 canonical source 对齐。 -->

## 2. Page Body

- [ ] 2.1 <!-- 描述要实现的 page surface behavior。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Page / object / responsive design section、region、component specimen 或 decision。 -->
  Source: <!-- Page spec、component specimen、fixture contract、interaction map、design-system 或 verification matrix anchors。 -->
  Preserve: <!-- 说明必须保留的 UI regions、fixture collections、item counts、action placement/cardinality、component slots、responsive behavior 与 forbidden simplifications。 -->
  Proof: <!-- 说明 source-backed scene/route 的 observable UI 如何匹配 spec/design，包括 relevant 时的 structure/count/region checks。 -->

## 3. Object State

- [ ] 3.1 <!-- 描述要实现的 object open/close、local state 或 recovery behavior。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Object host、object-local state、retention 与 responsive degradation obligations。 -->
  Source: <!-- Object spec、interaction map、fixture variant、component specimen 与 design-system anchors。 -->
  Preserve: <!-- 说明必须保留的 host route/state retention、object status names、close semantics、recovery context、method/cardinality 与 forbidden generic page drift。 -->
  Proof: <!-- 说明 source-backed object state 可观察、actions 保留 host context 且 linked object checks 通过。 -->

## 4. Interaction / Mutation

- [ ] 4.1 <!-- 描述要串接的 interaction-map action 或 local mutation。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Mutation / data flow / object transition design obligations。 -->
  Source: <!-- Interaction-map action、fixture-contract mutation、route/scene/object anchors。 -->
  Preserve: <!-- 说明必须保留的 allowed slice writes、route/object state outcomes、no real service calls、no unplanned state 与 current context retention。 -->
  Proof: <!-- 说明 user-visible trigger 只产生 documented route/scene/object/local state outcome，且 mutation verification 通过。 -->

## 5. Responsive / Visual Fidelity

- [ ] 5.1 <!-- 描述要应用的 viewport、component 或 asset rules。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- Requirement / scenario names。 -->
  Design: <!-- Responsive / visual fidelity / component specimen obligations。 -->
  Source: <!-- Design-system viewport rules、component specimens、mock asset plan、verification matrix、page/object responsive rules。 -->
  Preserve: <!-- 说明必须保留的 layout regions、action reachability、count/placement、mobile degradation、token usage、asset IDs 与 no text overlap。 -->
  Proof: <!-- 说明 desktop/notebook/mobile 或 applicable viewport check 与 design-system/component-specimens/mock-asset-plan 无漂移。 -->

## 6. Verification

- [ ] 6.1 <!-- 描述要新增或更新的 scene smoke、object、key flow、asset 或 responsive checks。 -->
  Source Truth: <!-- 此任务实现或验证的 exact ST-... IDs。逐个枚举 IDs，不使用 ranges。 -->
  Spec: <!-- 此 verification 覆盖的 Requirement / scenario names。 -->
  Design: <!-- 此 verification 覆盖的 design obligations。 -->
  Source: <!-- Verification matrix rows、interaction-map key flows、component/asset/viewport anchors。 -->
  Preserve: <!-- 说明 verification 必须证明 relevant 时的 structure、count、region、state、interaction 或 responsive constraints；仅 text-existence checks 不足以覆盖 collection/action-placement behavior。 -->
  Proof: <!-- 说明 targeted verification command 通过，并覆盖相关 spec scenarios、design obligations 与 preserve constraints。 -->
