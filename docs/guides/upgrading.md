# Upgrading

This guide highlights the main changes to watch when upgrading Faststrap applications.

## From v0.5.x To v0.8.x

Faststrap v0.8.x is a larger jump from the early v0.5 line. The core install path remains lightweight, but the component surface, defaults system, docs structure, and optional integrations have grown significantly.

### Application Setup

Most apps can keep the same `add_bootstrap(app)` call:

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()
add_bootstrap(app)
```

For serverless deployments, prefer CDN mode explicitly:

```python
add_bootstrap(app, use_cdn=True)
```

Faststrap now also supports `FASTSTRAP_USE_CDN=true`, `force_static_url`, custom favicon URLs, Google Fonts, and component-aware Bootstrap JS loading. See [Core API](../api/core.md) for the full reference.

### Components Added Since v0.5

The v0.6 to v0.8 line added the bulk of Faststrap's data, workflow, and application primitives:

- Data and dashboard: `DataTable`, `Chart`, `MetricCard`, `TrendCard`, `KPICard`, `DashboardGrid`, `FilterBar`, `DateRangePicker`, `MultiSelect`, `RangeSlider`, `ExportButton`
- Rich display: `Avatar`, `AvatarGroup`, `Timeline`, `Stepper`, `ResultCard`, `StatusBadge`, `BadgeGroup`, `Markdown`, `Mermaid`, `Svg`, `MapView`
- Workflow and forms: `InlineEditor`, `FormWizard`, `WizardStep`, `CalendarDatePicker`, `LiveValidationField`, `ValidationMessage`, `FormErrorSummary`
- Core primitives: `Stack`, `Cluster`, `Center`, `PageHeader`, `KeyValueList`, `RecordDetail`, `CodeBlock`, `JsonViewer`, `FormSection`
- Visual primitives: `FlipCard`, `TiltCard`, `RevealCard`, `GlowCard`, loaders, `ProgressRing`, `GradientButton`, `FloatingActionButton`, `ParallaxSection`
- Small v0.8.1 additions: `Separator`, `Kbd`, `OTPInput`, `OTPInputGroup`, `AspectRatio`, `Tag`

### Renames And Compatibility Aliases

Use `FormBuilder.from_pydantic()` for new Pydantic form generation:

```python
from faststrap import FormBuilder
```

`Form.from_pydantic()` remains as a deprecated compatibility path, but ordinary `Form(...)` rendering now delegates to FastHTML's native form element so wildcard imports do not break existing apps.

Bootstrap table aliases are available when your app also imports FastHTML table primitives:

```python
from faststrap import BsTable, BsTHead, BsTBody, BsTRow, BsTCell
```

### Optional Dependencies

Install core first:

```bash
pip install --upgrade faststrap
```

Install Markdown support only when using the `Markdown` display component:

```bash
pip install "faststrap[markdown]"
```

Chart.js and GSAP integrations use browser assets by default. The `chartjs` and `gsap` extras are compatibility markers and do not install additional Python packages.

### Behavior Changes To Review

- Component defaults use the `UNSET` sentinel internally, so passing `None` can intentionally clear a configured default.
- `Button(...)` defaults to `type="button"` to avoid accidental form submissions. Use `type="submit"` for submit buttons.
- Large `DataTable` pagination now renders a bounded page window with ellipses instead of every page number.
- `add_bootstrap()` duplicate calls warn and return instead of raising.
- `SimpleToast` no longer renders a duplicate close button; dismissal is handled by its fade-out timing.

### Recommended Migration Flow

1. Upgrade Faststrap and run your app locally.
2. Run `faststrap doctor` from the project root.
3. Search for `Form.from_pydantic`, `Button(` inside forms, and any custom component wrappers using `None` as a default passthrough.
4. Install `faststrap[markdown]` only if your app renders `Markdown(...)`.
5. Run your test suite and check browser console output for pages that use Bootstrap JS, HTMX swaps, OTP inputs, Mermaid, SSE, or searchable selects.

## From v0.6.x To v0.7.x

Faststrap v0.7.x adds a major component wave, optional integrations, and a safer defaults model.

### Component Defaults And `UNSET`

Faststrap now distinguishes omitted values from explicit `None`.

```python
from faststrap import Button, set_component_defaults

set_component_defaults("Button", size="lg")

Button("Large by default")
Button("Normal size here", size=None)
```

When writing wrapper components, default overridable options to `UNSET` instead of `None`.

```python
from faststrap import UNSET

def MyButton(*children, size=UNSET, **kwargs):
    ...
```

See [Component Defaults](../api/defaults.md).

### New Components

The v0.7.x wave includes:

- `ResultCard`
- `Avatar` and `AvatarGroup`
- `StatusBadge` and `BadgeGroup`
- `InlineEditor`
- `Timeline` and `TimelineItem`
- `Stepper` and `StepperStep`
- `CalendarDatePicker`
- `FormWizard` and `WizardStep`
- `CommandPalette` and `CommandItem`
- `LiveValidationField` and `ValidationMessage`

### Optional Integrations

Optional integrations remain outside the core dependency path:

```bash
pip install faststrap
pip install "faststrap[markdown]"
```

Chart.js and GSAP integrations load frontend assets from CDN by default and do not require extra Python packages. `faststrap[markdown]` installs the optional Python dependencies needed by the Markdown renderer. Core `Fx` animations remain the default lightweight motion system. GSAP is opt-in.

### Pydantic Forms

Use `FormBuilder.from_pydantic()` for new code.

```python
from faststrap import FormBuilder
```

`Form.from_pydantic()` remains as a compatibility alias but emits a deprecation warning when called. The builder requires Pydantic v2.

### Tables

`Table`, `THead`, `TBody`, `TRow`, and `TCell` remain the primary table API.

If your app also imports native FastHTML table primitives, optional aliases are available:

```python
from faststrap import BsTable, BsTHead, BsTBody, BsTRow, BsTCell
```

### DataTable Pagination

Large `DataTable` paginators now render a bounded page window with ellipses instead of every page link. If you relied on every page number being present in the DOM, update that behavior.

### Button Type Default

Rendered `<button>` elements now default to `type="button"` to avoid accidental form submission.

Use `type="submit"` explicitly for submit buttons:

```python
Button("Save", type="submit")
```

## Upgrade Checklist

- Run your app and inspect forms that depend on implicit submit behavior.
- Replace new code using `Form.from_pydantic()` with `FormBuilder.from_pydantic()`.
- Review custom wrapper components and use `UNSET` where defaults should flow through.
- Run `faststrap doctor` to catch common setup issues.
- Run your test suite and `mkdocs build` if you publish docs.
