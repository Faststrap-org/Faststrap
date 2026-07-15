# FastStrap Roadmap - Updated May 2026

**Vision:** The most complete, Pythonic, zero-JS Bootstrap 5 component library for FastHTML - a production-grade UI layer for web apps, data apps, ML tools, and AI-native interfaces.

---

## Current Status (v0.8.0 - May 2026)

**152 registered UI components live**
**170+ total components, helpers, presets, integrations, and utilities**
**790+ tests collected in CI**
**Full HTMX + Bootstrap 5.3.3 support**
**Core remains FastHTML/Bootstrap/HTMX-first**
**Zero custom JavaScript required**
**Optional integrations available** for ChartJS, GSAP, Markdown, maps, and richer motion/chart use cases
**Docs structure hardened** with component index, architecture guide, upgrade guide, performance guide, and docs standards
**v0.8 core primitives added**: `Stack`, `Cluster`, `Center`, `PageHeader`, `KeyValueList`, `RecordDetail`, `CodeBlock`, `JsonViewer`, `FormSection`, and `PollUntil`
**Visual primitives absorbed into core**: `FlipCard`, `TiltCard`, `RevealCard`, `GlowCard`, CSS loaders, `ProgressRing`, `GradientButton`, `FloatingActionButton`, and `ParallaxSection`

### Pre-v0.6 Delivered by v0.5.9

- Accessibility mini-module: `SkipLink`, `LiveRegion`, `VisuallyHidden`, `FocusTrap`
- `PageMeta` composer for SEO/social/canonical/favicon head tags
- Form validation bridge for backend errors -> `FormGroup`
- `faststrap doctor` CLI diagnostics
- `ToggleGroup` and `TextClamp` UI helpers
- `OptimisticAction` and `LocationAction` interaction presets
- `Markdown` and `MapView` display components (experimental)
- `Form.from_pydantic()` and `Table.from_df()` beta data bridges
- PWA advanced foundations (background sync, push scaffolding, route-aware cache controls)

### Deferred Post-v0.6

- Advanced DataTable query contract and optional ORM bridges
- Production map provider integrations and geospatial presets
- Extended PWA reliability presets (queue persistence, richer retry/telemetry)
- Workflow/UI helpers where audits keep showing repetition: `ResultCard`, `InlineEditor`, `Avatar`, and richer `Pagination` ergonomics
- Documentation-first polish for validation workflows, filter/search recipes, and non-table pagination guidance

### Suggested release cut

- `v0.5.6`: accessibility + toggle group + text clamp + notification presets
- `v0.5.7`: PageMeta + form error mapper
- `v0.5.8`: doctor CLI + docs/version/changelog consistency cleanup
- `v0.5.9`: markdown/map/data bridges + PWA foundations
- `v0.6.0`: advanced data APIs + realtime/preset hardening

### Implementation tracking (agreed follow-ups)

These items are intentionally tracked here so they are not lost between releases.

- `v0.5.8`:
  - Integrate `requires_js` metadata into `add_bootstrap(...)` via explicit component list input.
  - Add explicit duplicate `add_bootstrap(...)` guard using app state and clear error messaging.
  - Add CDN SRI (`integrity` + `crossorigin`) support for `use_cdn=True`.
- `v0.5.9`:
  - Ship `Form.from_pydantic()` beta data/form bridge.
  - Ship `Table.from_df()` beta dataframe bridge.
  - Ship `OptimisticAction` + `LocationAction` preset foundations.
  - Ship `Markdown` + `MapView` experimental display components.
  - Ship advanced PWA baseline controls.
- `v0.6.1+`:
  - Rich DataTable query contract and optional ORM bridges.
  - Advanced PWA opt-in implementations (Background Sync, Push, route-aware caching).

##  Overall Progress to v1.0

```text
Components:    152+ registered UI (170+ total with presets, integrations, helpers)
Tests:         790+ (target 800)
Coverage:      90%+ (target 95%)
Contributors:  15+/100 (15%)

```

### Completed Phases

| Phase | Components | Status | Released |
|-------|------------|--------|----------|
| 1–2 | 12 (Button, Card, Alert, Modal, Navbar, Badge, Toast, Drawer, Container/Row/Col, Icon) | ✅ Complete | Dec 2025 |
| 3 | +8 (Tabs, Dropdown, Input, Select, Breadcrumb, Pagination, Spinner, Progress) | ✅ Complete | Dec 2025 |
| 4A | +10 (Table, Accordion, Checkbox, Radio, Switch, Range, ListGroup, Collapse, InputGroup, FloatingLabel) | ✅ Complete | Dec 2025 |
| 4B | +8 (FileInput, Tooltip, Popover, Figure, ConfirmDialog, EmptyState, StatCard, Hero) | ✅ Complete | Jan 2026 |
| 4C | Documentation (18 component docs, 95% coverage) | ✅ Complete | Jan 2026 |
| 5A | +6 (Image, Carousel, Placeholders, Scrollspy, SidebarNavbar, GlassNavbar) + Examples Reorganization | ✅ Complete | Jan 2026 |
| 5B | +16 (Presets Module [12 helpers], SEO Module [2 components], ErrorPage, ErrorDialog, FormGroup, ThemeToggle, SearchableSelect, FooterModern, Testimonial, TestimonialSection, AuthLayout) | ✅ Complete | Feb 2026 |
| 6 | +16 (DataTable, Chart, MetricCard, TrendCard, KPICard, DashboardGrid, FilterBar, DateRangePicker, MultiSelect, RangeSlider, ExportButton, SSEStream, SSETarget, NotificationCenter, Svg, Mermaid) | ✅ Complete | Mar 2026 |
| 7 | +14 (ResultCard, Avatar, AvatarGroup, StatusBadge, BadgeGroup, InlineEditor, Timeline, Stepper, CalendarDatePicker, FormWizard, CommandPalette) + optional integrations (ModernToast, ChartJS, GSAP) | ✅ Complete | May 2026 |
| 8 | +13 core primitives (Stack, Cluster, Center, PageHeader, KeyValueList, RecordDetail, CodeBlock, JsonViewer, FormSection, PollUntil) + visual primitives (FlipCard, TiltCard, RevealCard, GlowCard, 7 loaders, ProgressRing, GradientButton, FloatingActionButton, ParallaxSection) | ✅ Complete | May 2026 |

**Total: 152 registered UI components + 18 HTMX presets + SEO/PWA/accessibility helpers = 170+ total**

---

## Detailed Breakdown (for reference)

### Phase 4A  Core Bootstrap Completion (v0.4.0  Complete)

 **30 total components reached**

| Priority | Component | Status | Notes |
|----------|-----------|--------|-------|
| 1 | `Table` (+ THead, TBody, TRow, TCell) |  Complete | Responsive, striped, hover, bordered |
| 2 | `Accordion` (+ AccordionItem) |  Complete | Flush, always-open, icons |
| 3 | `Checkbox` |  Complete | Standard, inline, validation |
| 4 | `Radio` |  Complete | Standard, button style |
| 5 | `Switch` |  Complete | Toggle variant of checkbox |
| 6 | `Range` |  Complete | Slider with labels, steps |
| 7 | `ListGroup` (+ ListGroupItem) |  Complete | Actionable, badges, flush |
| 8 | `Collapse` |  Complete | Show/hide with data attributes |
| 9 | `InputGroup` |  Complete | Prepend/append addons |
| 10 | `FloatingLabel` |  Complete | Animated label inputs |

---

### Phase 4B  Enhanced Forms & Feedback (v0.4.5  Complete)

 **38 total components reached**

### Components to Build

| Priority | Component | Status | Notes |
|----------|-----------|--------|-------|
| 1 | `FileInput` |  Complete | Single/multiple, drag-drop preview |
| 2 | `Tooltip` |  Complete | Bootstrap JS init pattern |
| 3 | `Popover` |  Complete | Rich content overlays |
| 4 | `Figure` |  Complete | Image + caption wrapper |
| 5 | `ConfirmDialog` |  Complete | Modal preset for confirmations |
| 6 | `EmptyState` |  Complete | Card + Icon + placeholder text |
| 7 | `StatCard` |  Complete | Metric display card |
| 8 | `Hero` |  Complete | Landing page hero section |

---

##  Framework Guarantees (v1.0+)

Faststrap commits to the following architectural contracts:

* **Deterministic HTML**: Server-rendered output is predictable and testable (`assert_html`).
* **Zero-JS Core**: All components function without JavaScript; enhancements are progressive.
* **No Client State**: We avoid hidden client-side state stores; state lives on the server.
* **Accessibility First**: WCAG-aligned defaults for all components.
* **Stability Markers**: Explicit `@stable` and `@experimental` decorators for API confidence.

---

## Phase 4C  Documentation & Polish (v0.4.6  Completed)

 **Documentation Overhaul**

| Component | Status | Notes |
|-----------|--------|-------|
| Interactive Previews |  Complete | All 40+ components live-rendered |
| Theme Isolation |  Complete | Fixed CSS conflicts with MkDocs Material |
| `init.js` |  Complete | Bootstrap socialization for Tooltips/Popovers |

---

## Phase 5  Composed UI & Design System Layer (v0.5.x  Complete + pre-v0.6 extensions)

**Goal:** SaaS-ready patterns, layouts, and visual effects.
**Focus:** `faststrap.layouts`, `faststrap.patterns`, `faststrap.effects`.

### Components & Plans

**1. Design Components (Original Phase 5 Plan)**

| Priority | Component | Module | Status | Notes |
|----------|-----------|--------|--------|-------|
| 1 | `faststrap.effects` | New Module |  Complete | Zero-JS visual effects (fade, lift, highlight) |
| 2 | `DashboardLayout` | layouts | Complete | Admin panel layout with sidebar |
| 3 | `LandingLayout` | layouts | Complete | Marketing page layout |
| 4 | `NavbarModern` | patterns |  Complete | Implemented as `GlassNavbar` |
| 5 | `FeatureGrid` | patterns |  Complete | Icon + Title + Text grid |
| 6 | `PricingGroup` | patterns |  Complete | 3-column pricing cards |
| 7 | `TestimonialSection` | patterns | Complete | Customer testimonials |
| 8 | `FooterModern` | patterns | Complete | Modern multi-column footer |

**2. Core Enhancements (Added in v0.5.0)**

| Component | Status | Notes |
|-----------|--------|-------|
| `Image` |  Complete | Fluid, thumbnail, rounded, alignment utils |
| `Carousel` |  Complete | Auto-play, controls, indicators, fade |
| `Placeholder` |  Complete | Skeleton loading with glow/wave animations |
| `Scrollspy` |  Complete | Auto-updating navigation based on scroll |
| `SidebarNavbar` |  Complete | Premium vertical visual sidebar |
| `GlassNavbar` |  Complete | Premium glassmorphism navbar |

> **Note:** The `faststrap init` CLI tool has been cancelled in favor of a simpler `pip install` philosophy for community extensions.

---

### Phase 5B  HTMX Presets, Error Handling & SEO (v0.5.6  Complete)

 **67 total components reached**

**1. HTMX Presets Module (`faststrap.presets`)**

| Component | Type | Status | Notes |
|-----------|------|--------|-------|
| `ActiveSearch` | Interaction |  Complete | Live search with debouncing |
| `InfiniteScroll` | Interaction |  Complete | Load more on scroll |
| `AutoRefresh` | Interaction |  Complete | Auto-updating content |
| `LazyLoad` | Interaction |  Complete | Load content on visibility |
| `LoadingButton` | Interaction |  Complete | Button with loading state |
| `hx_redirect` | Response |  Complete | Server-side redirects |
| `hx_refresh` | Response |  Complete | Full page refresh |
| `hx_trigger` | Response |  Complete | Trigger client events |
| `hx_reswap` | Response |  Complete | Change swap strategy |
| `hx_retarget` | Response |  Complete | Change target element |
| `toast_response` | Response |  Complete | Toast notifications |
| `@require_auth` | Decorator |  Complete | Route protection |

**2. SEO Module (`faststrap.seo`)**

| Component | Type | Status | Notes |
|-----------|------|--------|-------|
| `SEO` | Component |  Complete | Meta tags, Open Graph, Twitter Cards, Article metadata |
| `StructuredData` | Helper |  Complete | JSON-LD for Article, Product, Breadcrumb, Organization, LocalBusiness |

**3. Error Handling Components**

| Component | Status | Notes |
|-----------|--------|-------|
| `ErrorPage` |  Complete | Full-page error displays (404, 500, 403) |
| `ErrorDialog` |  Complete | Modal error displays with retry |

**4. Form & Auth Enhancements**

| Component | Status | Notes |
|-----------|--------|-------|
| `FormGroup` |  Complete | Form field wrapper with validation |
| `ThemeToggle` |  Complete | Dark/light mode switch |
| `SearchableSelect` |  Complete | Server-side searchable dropdown |
| `AuthLayout` |  Complete | Centered auth page layout |

**5. Pattern Components**

| Component | Status | Notes |
|-----------|--------|-------|
| `FooterModern` |  Complete | Multi-column footer with branding |
| `Testimonial` |  Complete | Customer testimonial card |
| `TestimonialSection` |  Complete | Grid of testimonials |

**Documentation & Examples:**

* 8 comprehensive examples (error pages, error dialogs, presets interactions, presets responses, form components, auth pages, pattern components, SEO demo)
* Complete SEO documentation with best practices
* API reference for all presets
* 35+ new tests (530+ total)

---

## Phase 6  Data Science & Visualization (v0.6.x  Apr-Jul 2026)

**Goal:** Make Faststrap the #1 choice for Python data scientists building dashboards and data applications.

**Vision:** Zero-JavaScript data visualization with the power of pandas, Matplotlib, Plotly, and Altair - all in pure Python.

### v0.6.0  Data Foundations (Apr 2026)

**Focus:** Core data components for tables, charts, and DataFrame integration.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `DataTable` | Advanced table with sort/filter/pagination for DataFrames | Implemented |
| 2 | `Chart` | Wrapper for Matplotlib, Plotly, Altair with responsive sizing | Implemented |
| 3 | `Table.from_df()` | Convert pandas/polars DataFrame to Bootstrap table | Implemented |
| 4 | `MetricCard` | Enhanced StatCard with trends and deltas | Implemented |
| 5 | `TrendCard` | KPI card with sparkline visualization | Implemented |
| 6 | `KPICard` | Multi-metric dashboard card | Implemented |

**Features:**

* Pandas & Polars DataFrame support
* Client-side sorting/filtering for small datasets (<1000 rows)
* Server-side pagination for large datasets
* CSV/Excel export buttons
* Automatic type inference and formatting
* Theme-aware chart colors

### v0.6.1  Advanced Data Components (May 2026)

**Focus:** Dashboard layouts, filters, and data visualization patterns.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `DashboardGrid` | Responsive grid system for dashboards | Implemented |
| 2 | `FilterBar` | Composable filter components | Implemented |
| 3 | `DateRangePicker` | Date range selection with presets | Implemented |
| 4 | `MultiSelect` | Multi-select dropdown for filtering | Implemented |
| 5 | `RangeSlider` | Numeric range slider | Implemented |
| 6 | `ExportButton` | Export data to CSV/Excel/PDF | Implemented |
| 7 | `DistributionPlot` | Histogram with KDE overlay | Planned |
| 8 | `CorrelationMatrix` | Heatmap for correlation analysis | Planned |

**Features:**

* HTMX-powered filtering (zero-JS)
* Auto-refresh dashboards
* Print-friendly layouts
* Responsive dashboard grids

### v0.6.2  Real-time & ML Integration (Jun 2026)

**Focus:** Live data updates and machine learning model visualization.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `LiveChart` | Auto-updating chart with SSE | Planned |
| 2 | `LiveMetric` | Real-time metric display | Planned |
| 3 | `ConfusionMatrix` | ML model confusion matrix | Planned |
| 4 | `ROCCurve` | ROC curve visualization | Planned |
| 5 | `FeatureImportance` | Feature importance chart | Planned |
| 6 | `ModelMetrics` | Comprehensive model evaluation dashboard | Planned |

**Features:**

* Server-Sent Events (SSE) for real-time updates
* Streaming data tables
* ML model performance tracking
* Interactive cross-filtering

### v0.6.3  Productivity & Polish (Jul 2026)

**Focus:** Developer experience, form builders, and advanced visualizations.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `Form.from_pydantic()` | Auto-generate forms from Pydantic models | Planned |
| 2 | `TimeSeriesPlot` | Time series with moving averages | Planned |
| 3 | `GeoMap` | Geographic visualization (optional) | Planned |
| 4 | `NotificationCenter` | Centralized notification management | Implemented |

**Features:**

* Type-safe form generation
* Automatic validation from Pydantic
* Complete documentation with 20+ examples

### Proposed Frontend Primitives & Experience Layer (post-v0.6)

These are the next frontend-focused additions that would most improve day-to-day product building for Faststrap users.

| Component | Purpose | Notes |
|-----------|---------|-------|
| `Stack` | Vertical spacing primitive | Reduce repeated flex-column/gap scaffolding |
| `Cluster` | Inline wrapping action/chip layout | Great for toolbars, chips, and metadata rows |
| `Center` | Centered constrained content wrapper | Useful for auth, empty states, and hero content |
| `Switcher` | Responsive switch layout primitive | Better abstraction for summary cards and adaptive panels |
| `Sidebar` | Composable app-shell sidebar | Distinct from navbar-only composition |
| `SearchBar` | Polished global search surface | Optional HTMX suggestions |
| `ProfileDropdown` | Authenticated user menu | Strong fit for dashboards and portals |
| `Timeline` | Chronological event feed | Audits, bookings, releases, activities |
| `Stepper` | Multi-step progress indicator | Form flows and onboarding |
| `FormWizard` | Server-driven multi-step form helper | Built around HTMX + existing form primitives |
| `SplitPane` | Two-pane productivity layout | Docs, editors, inspectors, master/detail screens |
| `MegaMenu` | Premium expanded navigation | SaaS, docs, ecommerce |
| `CommandPalette` | Keyboard-driven command/search launcher | Progressive enhancement; minimal JS |
| `ModernToast` | Premium toast surface | Should remain server-rendered first, JS-enhanced only where valuable |
| `ChartJS` | Optional modern chart integration | Proposed extra: `faststrap[chartjs]` |

**Implementation stance:**

* Prefer zero-JS or HTMX-first where practical.
* Allow minimal progressive JavaScript when the UX benefit is high and the server-rendered baseline remains complete.
* Keep optional integrations, such as `ChartJS`, outside the default install footprint.

> **Note:** `ActiveSearch` and `InfiniteScroll` are already available in v0.5.6 as part of the `faststrap.presets` module.

### Canonical Next Build Roadmap

This section is the main source of truth for the next Faststrap buildout after the v0.6 data foundations. It merges the component suggestions from audits, implementation planning, and the Kilo/Gemini-style review into one roadmap so we stop tracking overlapping lists in different places.

#### Scope Summary

- **11 core component additions**
- **3 optional integration systems**
- **7 supporting framework and pattern improvements**
- **4 delivery waves** so we can ship meaningful value without bundling every idea into one release

#### Component Roadmap

| Item | Type | Priority | Complexity | Wave | Notes |
|------|------|----------|------------|------|-------|
| `ResultCard` | Component | High | Low | 1 | Common success/error/result surface for settings, forms, and post-action feedback |
| `Avatar` | Component | High | Low | 1 | Foundational identity primitive for dashboards, nav, comments, and teams |
| `AvatarGroup` | Component | High | Low | 1 | Natural pair with `Avatar`; overlap stacks and count indicators |
| `StatusBadge` | Component | High | Low | 1 | Stronger semantic status surface than generic `Badge` for ops/admin UIs |
| `BadgeGroup` | Component | High | Low | 1 | Grouped badges/chips for status collections, tags, and compact metadata rows |
| `InlineEditor` | Component | High | Medium | 1 | Useful for editable tables, profile settings, and compact admin workflows |
| `Timeline` | Component | Medium | Medium | 2 | Good fit for activity, audit, booking, and release views |
| `Stepper` | Component | Medium | Medium | 2 | Progress indicator for onboarding, checkout, and setup flows |
| `CalendarDatePicker` | Component | Medium | Medium | 2 | Calendar-oriented date input distinct from range-first filtering controls |
| `FormWizard` | Component | Medium | High | 3 | Server-driven multi-step form flow; should build on `Stepper` + form helpers |
| `CommandPalette` | Component | Medium | High | 3 | Progressive enhancement feature with careful minimal-JS design |

#### Optional Integration Roadmap

These integrations are intentionally opt-in. They should not change Faststrap's zero-JS default path or add dependencies to the base install.

| Item | Type | Priority | Complexity | Wave | Notes |
|------|------|----------|------------|------|-------|
| `ModernToast` | Optional integration | Medium | Medium | 3 | Alternative modern toast system with configurable position, timing, style, and queue behavior |
| `ChartJS` | Optional integration | Medium | High | 3 | Optional Chart.js integration via an extra such as `faststrap[chartjs]` |
| `GSAP Motion` | Optional integration | Medium | High | 3 | Optional animation system via `faststrap[gsap]`; richer motion without changing core `Fx` defaults |

#### Supporting Framework and Pattern Improvements

| Item | Type | Priority | Complexity | Wave | Notes |
|------|------|----------|------------|------|-------|
| `StatCard` refinement | Existing component improvement | Medium | Low | 4 | Shipped: `delta` alias, default resolution, and `faststrap-stat-card` theme hook |
| `Pagination` improvements | Existing component improvement | High | Medium | 4 | Shipped: query preservation, custom page param, HTMX links, and URL control |
| Form validation helpers | Pattern/helper | High | Medium | 4 | Shipped: `LiveValidationField` and `ValidationMessage` for HTMX field validation |
| Data table pagination/sorting helpers | Pattern/helper | High | Medium | 4 | Shipped: `DataTable.query_params()` and `DataTable.page_url()` helpers |
| Confirmation/destructive-action helpers | Pattern/helper | Medium | Medium | 4 | Shipped: `ConfirmAction` HTMX confirmation button |
| Theme-variant utility support | Framework utility | Medium | Medium | 4 | Shipped: `theme_variant_css()` helper |
| Component discovery/registry improvements | Framework utility | Medium | Medium | 4 | Shipped: metadata, search, and pattern lookup helpers |

#### Delivery Logic

**Wave 1: Fast wins and reusable foundations**

- `ResultCard` - shipped
- `Avatar` - shipped
- `AvatarGroup` - shipped
- `StatusBadge` - shipped
- `BadgeGroup` - shipped
- `InlineEditor` - shipped

**Wave 2: Workflow and UI polish**

- `Timeline` - shipped
- `Stepper` - shipped
- `CalendarDatePicker` - shipped

**Wave 3: Bigger interactive surfaces and optional integrations**

- `FormWizard` - shipped
- `CommandPalette` - shipped
- `ModernToast` - shipped
- `ChartJS` - shipped
- `GSAP Motion` - shipped

**Wave 4: Framework ergonomics and pattern codification**

- `StatCard` refinement - shipped
- `Pagination` improvements - shipped
- Form validation helpers - shipped
- Data table pagination/sorting helpers - shipped
- Confirmation/destructive-action helpers - shipped
- Theme-variant utility support - shipped
- Component discovery/registry improvements - shipped

#### Planning Notes

- `Avatar` and `AvatarGroup` are tracked separately even though they will likely ship close together.
- `SkeletonLoader` is not tracked as a new component because `Placeholder`, `PlaceholderCard`, and `PlaceholderButton` already cover skeleton loading states.
- `PaginationControls` is folded into `Pagination` improvements because the core `Pagination` component already exists.
- `ChartJS` remains optional and should not change the zero-JS baseline for the rest of the framework.
- `GSAP Motion` follows the same optional integration stance as `ChartJS`: useful when requested, never part of the default runtime contract.
- `FormWizard` should not be built before `Stepper`; the step model needs to settle first.
- `CommandPalette` should keep a usable server-rendered baseline even if keyboard enhancements use small progressive JavaScript.
- This roadmap intentionally separates **new components** from **framework ergonomics** so release planning stays honest.

---

## Forward Roadmap: Documents, Data Science, and Agent Surfaces

This section tracks the next strategic roadmap after the v0.7.0 component wave.
It is intentionally split between lightweight core additions and optional
integration packs so Faststrap can keep its zero-JS core while becoming more
useful for data science teams, ML engineers, frontend builders, and AI agents.

### Existing Surface Check

The following proposed component/API names were checked against the current
Faststrap source, tests, docs, examples, README, and roadmap and are not
currently shipped:

- `PdfEmbed`
- `PdfViewer`
- `CodeBlock`
- `JsonViewer`
- `KeyValueList`
- `Stack`
- `Cluster`
- `Center`
- `Sidebar`
- `SplitPane`
- `LogViewer`
- `PageHeader`
- `FormSection`
- `FilePreview`
- `DataCard`
- `RecordDetail`
- `SectionHeader`
- `ResourceList`
- `PollUntil`
- `Debounce`
- `ConfirmPrompt`
- `SwapOnEvent`
- `DataFramePreview`
- `ModelCard`
- `DatasetCard`
- `ExperimentRunCard`
- `ArtifactList`
- `TrainingProgress`
- `PredictionResult`
- `AgentManifest`
- `agent_action`
- `ToolCallCard`
- `AgentTrace`
- `MessageThread`
- `ReasoningTimeline`
- `EvalResultCard`

Adjacent existing capabilities that should not be duplicated:

- `Chart` already covers the core chart wrapper.
- `ChartJS` is the optional Chart.js integration.
- `DataTable` already covers table search, sort, pagination, and query helpers.
- `Markdown`, `Mermaid`, and `MapView` already cover existing renderer/integration surfaces.
- `Placeholder`, `PlaceholderCard`, and `PlaceholderButton` already cover skeleton loading.
- `ModernToast` already covers the polished toast alternative to core Bootstrap toasts.

### Core Track: Document and App UI Utilities

These should remain lightweight, HTML-first, and dependency-free where possible.

| Candidate | Status | Rationale |
|-----------|--------|-----------|
| `Stack` | Complete | Vertical layout primitive for repeated `d-flex flex-column gap-*` patterns. |
| `Cluster` | Complete | Horizontal wrapping layout primitive for toolbar/action/filter rows. |
| `Center` | Complete | Centering primitive for empty states, auth shells, and focused panels. |
| `Sidebar` | Planned | App-shell primitive distinct from `SidebarNavbar`; pairs a fixed/sidebar region with scrollable main content. |
| `SplitPane` | Planned | Two-pane editor/inspector/master-detail layout; start non-resizable in core, richer behavior later if needed. |
| `PdfEmbed` / `PdfViewer` | Planned | Basic iframe/object PDF display with download fallback; no PDF.js in core. |
| `CodeBlock` | Complete | Developer/docs/AI app primitive for displaying code snippets. |
| `JsonViewer` | Complete | Useful for APIs, ML outputs, agent traces, and config dashboards. |
| `KeyValueList` | Complete | Common metadata/detail display pattern. |
| `LogViewer` | Planned | Useful for jobs, deployment logs, agent runs, and ML training logs. |
| `FormSection` | Complete | Groups related fields with title, description, and optional divider. |
| `FilePreview` | Planned | Generic file preview shell with safe fallback/download behavior. |
| `DataCard` / `RecordDetail` | Partial | `RecordDetail` is complete; `DataCard` remains planned. |
| `PageHeader` / `SectionHeader` | Partial | `PageHeader` is complete; `SectionHeader` remains planned. |
| `ResourceList` | Planned | Entity list pattern with icon/avatar/status/action support. |

### Core Track: Interaction Presets

These should stay HTMX-first and dependency-free.

| Candidate | Status | Rationale |
|-----------|--------|-----------|
| `Debounce` | Planned | Small helper for consistent `delay:Xms changed` HTMX triggers. |
| `ConfirmPrompt` | Planned | Cleanly applies `hx-confirm` to actions without custom JavaScript. |
| `SwapOnEvent` | Planned | Trigger HTMX swaps from custom client events. |
| `PollUntil` | Complete | Poll job/status endpoints until final replacement markup appears; high value for queues and ML jobs. |

### Data Science and ML Track

These should make Faststrap a strong option for internal analytics and ML
operations apps without requiring React.

The near-term competitive gap is interactive plotting. The existing `Chart`
component handles core Python chart output, while `faststrap[plots]` should
focus on richer Plotly/Altair/Vega-style interaction.

| Candidate | Status | Rationale |
|-----------|--------|-----------|
| `DataFramePreview` | Planned | Friendly dataframe/table preview for pandas/polars-like workflows. |
| `ModelCard` | Planned | Model metadata, version, task, metrics, and deployment status. |
| `DatasetCard` | Planned | Dataset metadata, splits, license, rows, and source links. |
| `ExperimentRunCard` | Planned | Run status, params, metrics, artifacts, and timestamps. |
| `ArtifactList` | Planned | Files/checkpoints/reports produced by jobs or model runs. |
| `TrainingProgress` | Planned | Epoch/progress/metric trend summary for ML jobs. |
| `PredictionResult` | Planned | Human-readable model output with confidence and explanation slots. |
| `ConfusionMatrix` | Planned optional/core-adjacent | Useful ML diagnostic display that can start as a table/heatmap without new dependencies. |

### Optional `faststrap[plots]` Scope

| Candidate | Status | Rationale |
|-----------|--------|-----------|
| `PlotlyChart` | Planned | Embed interactive Plotly figures without requiring Dash. |
| `AltairChart` | Planned | Embed Altair/Vega-Lite specs for data-science workflows. |
| `VegaChart` | Planned | Lower-level Vega/Vega-Lite bridge for teams already using specs. |
| `DistributionPlot` | Planned | Common statistical visualization helper. |
| `CorrelationMatrix` | Planned | Common analytics/ML exploratory view. |

### AI and Agent Track

This is an optional structured surface for agents. Faststrap should not become
a full app/state framework, but it can expose app structure and declared actions
so agents do not need to rely on brittle screenshot/click workflows.

| Candidate | Status | Rationale |
|-----------|--------|-----------|
| `faststrap[agents]` | Planned optional extra | Keeps agent tooling opt-in and out of the zero-JS/default core. |
| `AgentManifest` | Planned | Generates a structured JSON description of routes, actions, forms, tables, and resources. |
| `agent_action` | Planned | Python decorator for declaring structured actions callable by agents. |
| `/.well-known/faststrap-agent.json` | Planned | Conventional discovery endpoint for capable agents. |
| Form/table schema export | Planned | Allows agents to understand fields, filters, columns, and row actions. |
| `AgentTrace` | Planned | Visual trace of agent steps and tool calls. |
| `ToolCallCard` | Planned | Render one tool invocation/result pair. |
| `MessageThread` | Planned | AI/chat thread display primitive. |
| `ReasoningTimeline` | Planned | Timeline-style display for planning/evaluation steps. |
| `EvalResultCard` | Planned | Compact display for eval scores, pass/fail status, and notes. |

Initial display primitives for this track:

- `MessageThread`
- `ToolCallCard`
- `AgentTrace`
- `ReasoningTimeline`

Initial structured API primitives:

- `agent_action`
- `AgentManifest`
- `/.well-known/faststrap-agent.json`
- form/table schema export hooks

### Optional Integration Packs

These are useful, but should remain explicit opt-ins:

Priority order:

1. `faststrap[plots]` for Plotly, Altair, Vega-Lite, or ECharts bridges.
2. `faststrap[agents]` for structured agent manifests and action endpoints.
3. `faststrap[ml]` for ML/data-science cards and report patterns if the surface grows beyond core.
4. `faststrap[editor]` for rich text, Markdown, or code editing.
5. `faststrap[upload]` for advanced drag/drop uploads, queues, progress, and previews.
6. `faststrap[tables]` for heavier data-grid features such as pinning or virtualization.
7. `faststrap[maps]` for Leaflet/MapLibre/provider-backed map integrations.
8. `faststrap[pdfjs]` for rich PDF navigation, zoom, and search.
9. `faststrap[docs]` for documentation-site primitives and component preview/playground patterns.

### Guardrails

- Core stays Bootstrap + FastHTML + HTMX friendly.
- Core additions should work without custom JavaScript.
- Heavy browser libraries live behind optional extras.
- Optional integrations must degrade gracefully when assets are not loaded.
- Agent-facing APIs should be explicit, inspectable, and safe by default.
- New data/ML components should compose existing `Card`, `Badge`, `Table`, `DataTable`, `Progress`, and `Chart` primitives where possible.

### Adoption Track: Interactive Component Playground

The docs site should eventually include a lightweight playground where users can
adjust common component parameters and see rendered output without installing
Faststrap locally.

Preferred stance:

- Static-docs friendly.
- No production server required.
- Start with curated components (`Button`, `Alert`, `Card`, `Badge`, `Avatar`, `MetricCard`).
- Treat Pyodide/CodeSandbox-style execution as optional progressive enhancement.
- Prefer a safe parameter editor over arbitrary code execution for the first version.

### Recommended Next Build Sequence

**Wave A: Core primitives, no new dependencies**

1. `Stack`, `Cluster`, `Center`
2. `PageHeader`, `KeyValueList`, `RecordDetail`
3. `CodeBlock`, `JsonViewer`
4. `FormSection`
5. `PollUntil`

**Wave B: `faststrap[plots]`**

1. `PlotlyChart`
2. `AltairChart`
3. `VegaChart`
4. `DistributionPlot`
5. `CorrelationMatrix`

**Wave C: `faststrap[agents]`**

1. `agent_action`
2. `AgentManifest`
3. `MessageThread`
4. `ToolCallCard`
5. form/table schema export hooks

**Wave D: `faststrap[ml]`**

1. `ModelCard`
2. `DatasetCard`
3. `ExperimentRunCard`
4. `TrainingProgress`
5. `PredictionResult`
6. `ConfusionMatrix`

---

##  Data Science Positioning

Faststrap is uniquely positioned for data scientists:

**vs. Streamlit:**

*  More customizable (full Bootstrap control)
*  Production-ready (integrates into any FastHTML app)
*  Better performance (server-side rendering)

**vs. Dash (Plotly):**

*  Simpler API (no React, no callbacks)
*  Zero JavaScript required
*  Lighter weight

**vs. Panel (HoloViz):**

*  Cleaner, more Pythonic API
*  Better documentation
*  Professional Bootstrap aesthetics

**Target Users:**

* Data scientists building internal dashboards
* Data analysts creating stakeholder reports
* ML engineers monitoring model performance
* Business intelligence developers

---

##  Community Ecosystem (Safe Path)

**Goal:** Enable a community-driven ecosystem without bloating core.

These phases are documentation and process-driven, not runtime dependencies.

### 1. Extension Contracts (v0.5.x)

* [ ] Document contracts for Theme Packs and Component Packs.

* [ ] Define "explicit import" usage pattern (no auto-discovery).

### 2. The Registry (v0.6.x)

* [ ] Create `Faststrap-org/faststrap-extensions` repo (Metadata only).

* [ ] List approved themes and components.

### 3. Tooling (v0.7+)

* [ ] `faststrap init --template=community/xyz` (Scaffold only).

### Extension Design Rules

All Faststrap extensions must:

* Use explicit imports (no auto-registration)
* Avoid monkey-patching core APIs
* Declare compatibility with Faststrap versions
* Remain optional and replaceable
* Never affect core runtime behavior

---

##  Stability & Versioning Policy

### Component Maturity Levels

 **Stable** (`@stable`)

* API won't break in minor versions.
* Comprehensive tests (>90% coverage).
* Example: `Button`, `Card`, `Input`.

 **Beta** (`@beta`)

* API may change in minor versions.
* Basic tests (>70% coverage).
* Example: New Phase 6 components.

 **Experimental** (`@experimental`)

* API will likely change.
* Minimal tests.
* Use at own risk.

---

##  Non-Goals

What Faststrap intentionally *won't* do:

*  **Client-side reactivity** (use Alpine.js if needed)
*  **Custom CSS framework** (we're Bootstrap-native)
*  **Database ORM** (use SQLModel/SQLAlchemy)
*  **Full auth backend** (we provide UI, you provide logic)

**Why** Faststrap excels at Bootstrap + HTMX + Python. We integrate with best-in-class tools rather than replacing them.

---

## Phase 6E  Accessibility & Compliance (Post-v0.6)

**Goal**: Enterprise-grade compliance tools.

* [ ] ARIA validation helpers
* [ ] Focus management utilities
* [ ] Contrast-safe defaults checking

    Accessibility defaults are already applied throughout earlier phases; Phase 6E adds validation & compliance tooling.

---

---

## v1.0.0  Production Release (Milestone-Driven)

**Goal:** Complete ML/DS visualization layer + interactive docs + CLI scaffolding + community scale
**Release:** When quality gates pass — no fixed calendar date

### Quality Gates (v1.0 definition of done)

* [ ] ML/DS visualization wave shipped (DistributionPlot, CorrelationMatrix, LiveChart, LiveMetric, ConfusionMatrix, ROCCurve, FeatureImportance, ModelMetrics, TimeSeriesPlot)
* [ ] 95%+ test coverage (currently 90%+)
* [ ] Interactive component playground / live docs
* [ ] `faststrap init --template=` CLI scaffolding (5 templates)
* [ ] DataTable ↔ SQLAlchemy query bridge (server-side sort/filter/page)
* [ ] Full documentation website complete (MkDocs Material)
* [ ] Video tutorials
* [ ] Community contributions from 50+ developers

---

## Success Metrics

| Metric | v0.4.5 | v0.6.0 | v0.8.0 (Now) | v1.0.0 |
|--------|--------|--------|--------------|--------|
| Components | 38 | 109+ | 152 registered (170+ total) | 200+ |
| Tests | 230+ | 683 | 790+ | 800+ |
| Coverage | 85%+ | 90%+ | 90%+ | 95%+ |
| Contributors | 15+ | 15+ | 15+ | 50+ |

---

## How to Contribute

1. **Pick a component** from any Phase table above
2. **Comment on GitHub Issues**  "I'll build [Component]"  get assigned
3. **Use templates**: `src/faststrap/templates/component_template.py`
4. **Follow guides**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
5. **Write tests**: 10-15 tests per component using `to_xml()`
6. **Submit PR**  merged in 48 hours

---

## Documentation Website (In Progress)

**Stack:** MkDocs Material + GitHub Pages

**Structure:**

* Getting Started (Installation, Quick Start)
* Component Reference (Forms, Display, Feedback, Navigation, Layout)
* Theming Guide (Built-in themes, Custom themes, Dark mode)
* HTMX Integration Guide
* API Reference

---

## Community Feedback

Tell us what you need most:

* [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)
* Vote on issues with
* [FastHTML Discord](https://discord.gg/qcXvcxMhdP)  #faststrap channel

Your votes directly influence what gets built next.

---

**Last Updated: July 2026**
**Current Version: v0.8.0 (core primitive wave + visual primitives absorbed into core)**

**Let's build the definitive UI library for FastHTML  together.**
