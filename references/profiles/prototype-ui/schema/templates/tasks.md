## Requirement Coverage

<!--
Map every current-change Source Truth item, Requirement scenario, and material design obligation to implementation task IDs, verification task IDs, and verification proof.
Also map every deferred/non-goal, preserve-existing, or unresolved-conflict Source Truth ID that is referenced anywhere in this tasks file as a preserve constraint, forbidden-drift boundary, negative requirement, implementation constraint, verification obligation, or coverage-table reference.
This section is a generation-quality gate, not executable work. Do not put checkbox tasks here.
Use one row per source-truth item, requirement scenario, or material design obligation. Do not use aggregate rows as a substitute for covering the underlying scenarios or obligations.
-->

### Source Truth Coverage

| Source Truth ID | Source Truth Summary | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- |
| <!-- ST-001; exactly one ID per row, no ranges such as ST-001-ST-010. Include every current-change Source Truth item and every ST ID referenced anywhere in this tasks file. --> | <!-- Short source-backed obligation summary, including deferred/non-goal boundary summaries when the row is a preserve or forbidden-drift item. --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Source-equivalent proof: user interaction, API test, data assertion, edge path, rendered layout check, forbidden-drift/static check, etc. --> |

### Requirement / Scenario Coverage

| Capability | Requirement | Scenario | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- | --- |
| <!-- capability name --> | <!-- exact requirement name --> | <!-- exact scenario name --> | <!-- ST-001, ST-002; enumerate exact IDs, no ranges --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Scenario-level observable proof. --> |

### Design Obligation Coverage

| Design Section | Design Obligation | Source Truth IDs | Implementation Task IDs | Verification Task IDs | Verification Proof |
| --- | --- | --- | --- | --- | --- |
| <!-- exact design section / decision / gate item --> | <!-- material implementation, preservation, or verification obligation --> | <!-- ST-001, ST-002, or Not applicable; enumerate exact IDs, no ranges --> | <!-- e.g. 2.1, 4.2 --> | <!-- e.g. 6.1, 6.3 --> | <!-- Design-obligation proof. --> |

## 1. Runtime / Data / Asset

- [ ] 1.1 <!-- Implement or update route/scene/fixture/mock/asset foundations. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Runtime / data / fixture / mutation / asset design obligations. -->
  Source: <!-- Scene registry, fixture contracts, interaction map, mock asset plan, or state vocabulary anchors. -->
  Preserve: <!-- Canonical keys, fixture slices, mock write boundaries, collection cardinality, asset IDs, and forbidden drift. -->
  Proof: <!-- Deterministic scene/object state renders from canonical source and linked mutation/fixture checks pass. -->

## 2. Page Body

- [ ] 2.1 <!-- Implement page surface behavior. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Page / object / responsive design section, region, component specimen, or decision. -->
  Source: <!-- Page spec, component specimen, fixture contract, interaction map, design-system, or verification matrix anchors. -->
  Preserve: <!-- UI regions, fixture collections, item counts, action placement/cardinality, component slots, responsive behavior, and forbidden simplifications. -->
  Proof: <!-- Source-backed scene/route has observable UI matching spec/design, including structure/count/region checks where relevant. -->

## 3. Object State

- [ ] 3.1 <!-- Implement object open/close/local state/recovery. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Object host, object-local state, retention, and responsive degradation obligations. -->
  Source: <!-- Object spec, interaction map, fixture variant, component specimen, and design-system anchors. -->
  Preserve: <!-- Host route/state retention, object status names, close semantics, recovery context, method/cardinality, and forbidden generic page drift. -->
  Proof: <!-- Source-backed object state is observable, actions preserve host context, and linked object checks pass. -->

## 4. Interaction / Mutation

- [ ] 4.1 <!-- Wire interaction-map action or local mutation. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Mutation / data flow / object transition design obligations. -->
  Source: <!-- Interaction-map action, fixture-contract mutation, route/scene/object anchors. -->
  Preserve: <!-- Allowed slice writes, route/object state outcomes, no real service calls, no unplanned state, and current context retention. -->
  Proof: <!-- User-visible trigger produces only the documented route/scene/object/local state outcome and mutation verification passes. -->

## 5. Responsive / Visual Fidelity

- [ ] 5.1 <!-- Apply viewport/component/asset rules. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names. -->
  Design: <!-- Responsive / visual fidelity / component specimen obligations. -->
  Source: <!-- Design-system viewport rules, component specimens, mock asset plan, verification matrix, page/object responsive rules. -->
  Preserve: <!-- Layout regions, action reachability, count/placement, mobile degradation, token usage, asset IDs, and no text overlap. -->
  Proof: <!-- Desktop/notebook/mobile or applicable viewport check has no drift from design-system/component-specimens/mock-asset-plan. -->

## 6. Verification

- [ ] 6.1 <!-- Add or update scene smoke, object, key flow, asset, or responsive checks. -->
  Source Truth: <!-- Exact ST-... IDs implemented or verified by this task. Enumerate IDs individually; do not use ranges. -->
  Spec: <!-- Requirement / scenario names covered by this verification. -->
  Design: <!-- Design obligations covered by this verification. -->
  Source: <!-- Verification matrix rows, interaction-map key flows, component/asset/viewport anchors. -->
  Preserve: <!-- Verification must prove structure, count, region, state, interaction, or responsive constraints where relevant; text-existence-only checks are insufficient for collection/action-placement behavior. -->
  Proof: <!-- Targeted verification command passes and covers the relevant spec scenarios, design obligations, and preserve constraints. -->
