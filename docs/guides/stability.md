# Stability Policy

Faststrap uses three stability markers to communicate API guarantees. Every public component, helper, and preset carries one of these markers, visible in its docstring and in the generated API reference.

---

## Stability Levels

| Marker | Guarantee | When Breaking Changes May Occur | Typical Use |
|---|---|---|---|
| `@stable` | API is locked. No breaking changes in minor or patch releases. Deprecations require one full minor version cycle before removal. | Major version only (e.g., 0.x → 1.0) | Core components used in production |
| `@beta` | API is functional but may still evolve. Breaking changes possible in minor releases with a deprecation warning when feasible. | Minor releases (e.g., 0.9 → 0.10) | Recently shipped components still gathering feedback |
| `@experimental` | API is provisional. May change without warning, including removal. Intended for early adopters and internal testing. | Any release | New patterns, exploratory features |

---

## What Each Marker Guarantees

### `@stable`

A stable component commits to:

- **No breaking parameter changes** — existing parameters will not be removed or have their behavior changed in incompatible ways.
- **No signature reordering** — positional argument order is preserved.
- **Backward-compatible additions only** — new optional parameters may be added with defaults.
- **Deprecation policy** — if a stable API must be removed, it is first deprecated (with a `DeprecationWarning`) for at least one minor version before removal in the next major version.
- **Documentation fidelity** — the documented behavior matches the implementation; regressions are treated as bugs.

### `@beta`

A beta component provides:

- **Functional API** — the component works and is tested.
- **Likely but not guaranteed stability** — the API is expected to stabilize, but breaking changes are possible based on user feedback.
- **Best-effort deprecation warnings** — when a beta API changes, a `DeprecationWarning` is emitted where feasible, but this is not guaranteed.
- **Docstring accuracy** — documented behavior should match implementation, but edge cases may still be discovered.

### `@experimental`

An experimental component:

- **May change at any time** — including removal, renaming, or signature overhaul.
- **May lack complete documentation** — the API is still being shaped.
- **Is opt-in** — you should only use experimental components if you accept the risk of churn.
- **Provides feedback value** — using and reporting issues on experimental components directly shapes the stable API.

---

## How Markers Are Applied

```python
from faststrap.core._stability import stable, beta, experimental

@stable
def Button(...):
    """A stable button component."""
    ...

@beta
def DataTable(...):
    """A beta data table with sorting and pagination."""
    ...

@experimental
def ExperimentalWidget(...):
    """An experimental widget."""
    ...
```

Markers are attached as attributes on the function object:

```python
>>> from faststrap import Button
>>> getattr(Button, "__faststrap_stability__", None)
'stable'

>>> from faststrap import DataTable
>>> getattr(DataTable, "__faststrap_stability__", None)
'beta'
```

---

## Discovering Stability Programmatically

The registry exposes stability metadata for every registered component:

```python
from faststrap import list_components, get_component

# List all stable components
stable = [
    name for name in list_components()
    if get_component(name).get("stability") == "stable"
]

# Check a specific component
info = get_component("Button")
print(info["stability"])  # 'stable'
print(info["stability_doc"])  # full docstring
```

---

## What Is *Not* Guaranteed

Regardless of marker, the following are **not** part of the stability contract:

- **Rendered HTML structure** — the exact HTML output (class names, nesting, wrapper elements) may change between minor versions as Bootstrap or accessibility requirements evolve. Your code should not depend on inspecting the rendered HTML.
- **CSS class names** — internal class names (e.g., `faststrap-btn`, `faststrap-card`) are not part of the public API and may change. Use the documented `cls`, `*_cls`, and `css_vars` hooks for customization.
- **Default visual appearance** — theme defaults may shift between minor versions. Pin your theme if you need visual stability.
- **Error message text** — exception messages may be reworded. Catch exception types, not message strings.
- **Performance characteristics** — while we strive not to regress, algorithmic complexity and render times are not part of the API contract.

---

## Versioning Schedule

Faststrap follows [Semantic Versioning](https://semver.org/) with the following conventions:

| Version | Meaning |
|---|---|
| `0.x` | Initial development. Breaking changes may occur in minor releases for `@beta` and `@experimental` components. `@stable` components are protected. |
| `1.0` | Public API stabilization milestone. All non-experimental components become `@stable`. |
| `1.x` | Stable release. Breaking changes only in major versions, only for deprecated APIs. |

---

## Reporting Stability Violations

If you believe a `@stable` component has introduced a breaking change in a minor or patch release, file an issue with:

1. The component name and version where the break occurred.
2. The previously working code (copy-paste example).
3. The error or unexpected behavior.
4. The expected behavior based on prior documentation.

Stability violations are treated as release blockers for future `@stable` components.