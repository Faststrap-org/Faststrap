# Learning Paths

Faststrap serves several kinds of Python developer. The same component library can support a polished product interface, a data-heavy internal tool, or an ML workflow without forcing every project to adopt the same visual or JavaScript layer.

## Beginners: Build A First App

Follow this order when FastHTML and Faststrap are both new:

1. Read [Installation](../getting-started/installation.md) and [Quick Start](../getting-started/quick-start.md).
2. Learn the render model and asset lifecycle in the [Architecture Guide](architecture.md).
3. Start with [Button](../components/forms/button.md), [Card](../components/display/card.md), [Input](../components/forms/input.md), and [Grid](../components/layout/grid.md).
4. Add server-driven behavior with [HTMX Integration](htmx-integration.md) and the [preset overview](../presets/index.md).
5. Add validation, accessibility, and deployment only as the app needs them.

The recommended first application shape is intentionally small:

```python
from fasthtml.common import FastHTML
from faststrap import Button, Card, Container, add_bootstrap

app = FastHTML()
add_bootstrap(app)

@app.get("/")
def home():
    return Container(
        Card("Your first Faststrap page", footer=Button("Continue")),
    )
```

## Frontend And Product Developers

Use the [Component Index](../components/index.md) to choose a composable primitive before writing custom markup. A practical route is:

- `Navbar` or `SidebarNavbar` for application navigation.
- `PageHeader`, `Stack`, `Cluster`, and `Center` for page composition.
- `FormGroup`, `FormBuilder`, `DataTable`, and `FilterBar` for workflows.
- `Toast`, `ModernToast`, `Modal`, and `ErrorDialog` for feedback.
- `theme_variant_css()` and [Theming](theming.md) for brand identity.
- [Custom Components](custom-components.md) when a reusable surface is genuinely missing.

Use HTMX presets before adding custom JavaScript for search, polling, lazy loading, loading states, confirmation, and server responses. Use an integration when the browser or a third-party library is the actual source of complexity.

## Data Science Developers

Faststrap is useful when Python already owns the data and workflow logic, but the result still needs a real routed web interface:

- `DataTable` for searchable, sortable, paginated records; use server-side mode for large datasets.
- `MetricCard`, `TrendCard`, `KPICard`, `DataCard`, and `RecordDetail` for experiment and operational summaries.
- `Chart`, `Figure`, `MapView`, `Markdown`, `Math`, `Mermaid`, and `JsonViewer` for outputs and explanations.
- `FilterBar`, `DateRangePicker`, `MultiSelect`, `RangeSlider`, and `ExportButton` for exploration controls.
- `PollUntil`, `AutoRefresh`, `SSETarget`, and `SSEStream` for jobs, progress, and live feeds.

The core remains dependency-conscious. Optional renderers and browser libraries should be installed only when the project needs them; consult each component page for dependency and security boundaries.

## ML And AI Application Developers

Start with the data-tool path, then add explicit workflow surfaces:

- `TrainingProgress`, `LiveMetric`, and roadmap components are planned rather than current core APIs; do not import them until they appear in a release.
- Today, compose `Progress`, `MetricCard`, `DataTable`, `CodeBlock`, `JsonViewer`, `ResultCard`, `NotificationCenter`, and `SSETarget` for training or inference workflows.
- Use the [Component Registry](../api/registry.md) to let tooling discover available UI primitives instead of guessing component names.
- Keep agent-facing actions explicit in application routes. Faststrap's registry describes UI components; it is not an authorization system or a substitute for route validation.

## Senior Developers And Maintainers

Read these in order when you need predictable extension and release behavior:

1. [Architecture](architecture.md) for the FastHTML-to-HTML render and asset model.
2. [Component Defaults](../api/defaults.md) for `UNSET`, process-global configuration, and reset behavior.
3. [Custom Components](custom-components.md) for registration, attribute conversion, and class composition.
4. [Registry API](../api/registry.md) for metadata and AI/tooling discovery.
5. [Performance](performance.md), [Security](security.md), and [Testing](testing.md) before deployment.
6. [Upgrading](upgrading.md) and `CHANGELOG.md` when moving between releases.

## Coverage And Stability

The [Component Index](../components/index.md) is the complete registered UI inventory for the current source tree. Individual pages explain public behavior; generated API blocks expose exact signatures. Stability markers in source and the [Stability Policy](stability.md) indicate how much compatibility protection an API receives.

Documentation examples are copy-ready, but they are not authorization, database, or deployment policies. Test route behavior, permissions, responsive rendering, and browser interactions in the application that consumes Faststrap.
