# FastStrap Roadmap – Updated January 2026

**Vision:** The most complete, Pythonic, zero-JS Bootstrap 5 component library for FastHTML — 100+ production-ready components built by the community, for the community.

---

## Current Status (v0.5.0 – January 2026)

**51 components live** – Phase 1 through 5 complete  
**320+ tests** – 85%+ coverage  
**Full HTMX + Bootstrap 5.3.3 support**  
**100% Bootstrap parity achieved** ✅  
**Zero custom JavaScript required**

## 📈 Overall Progress to v1.0

```text
Components:   █████████░ 51/100 (51%)
Tests:        ████████░░ 320/800 (40%)
Coverage:     █████████░ 90/95   (95%)
Contributors: ███░░░░░░░ 15+/100 (15%)

```

### Completed Phases

| Phase | Components | Status | Released |
|-------|------------|--------|----------|
| 1–2 | 12 | ✅ Complete | Dec 2025 |
| 3 | +8 (Tabs, Dropdown, Input, Select, Breadcrumb, Pagination, Spinner, Progress) | ✅ Complete | Dec 2025 |
| 4A | +10 (Table, Accordion, Checkbox, Radio, Switch, Range, ListGroup, Collapse, InputGroup, FloatingLabel) | ✅ Complete | Dec 2025 |
| 4B | +8 (FileInput, Tooltip, Popover, Figure, ConfirmDialog, EmptyState, StatCard, Hero) | ✅ Complete | Jan 2026 |
| 4C | Documentation (18 component docs, 95% coverage) | ✅ Complete | Jan 2026 |
| 5 | +6 (Image, Carousel, Placeholders, Scrollspy, SidebarNavbar, GlassNavbar) + Examples Reorganization | ✅ Complete | Jan 2026 |

**Total: 51 production-ready components** (100% Bootstrap parity + 2 premium navbars)

---
## Detailed Breakdown (for reference)
### Phase 4A – Core Bootstrap Completion (v0.4.0 – Complete)

✅ **30 total components reached**

| Priority | Component | Status | Notes |
|----------|-----------|--------|-------|
| 1 | `Table` (+ THead, TBody, TRow, TCell) | ✅ Complete | Responsive, striped, hover, bordered |
| 2 | `Accordion` (+ AccordionItem) | ✅ Complete | Flush, always-open, icons |
| 3 | `Checkbox` | ✅ Complete | Standard, inline, validation |
| 4 | `Radio` | ✅ Complete | Standard, button style |
| 5 | `Switch` | ✅ Complete | Toggle variant of checkbox |
| 6 | `Range` | ✅ Complete | Slider with labels, steps |
| 7 | `ListGroup` (+ ListGroupItem) | ✅ Complete | Actionable, badges, flush |
| 8 | `Collapse` | ✅ Complete | Show/hide with data attributes |
| 9 | `InputGroup` | ✅ Complete | Prepend/append addons |
| 10 | `FloatingLabel` | ✅ Complete | Animated label inputs |

---

### Phase 4B – Enhanced Forms & Feedback (v0.4.5 – Complete)

✅ **38 total components reached**

### Components to Build

| Priority | Component | Status | Notes |
|----------|-----------|--------|-------|
| 1 | `FileInput` | ✅ Complete | Single/multiple, drag-drop preview |
| 2 | `Tooltip` | ✅ Complete | Bootstrap JS init pattern |
| 3 | `Popover` | ✅ Complete | Rich content overlays |
| 4 | `Figure` | ✅ Complete | Image + caption wrapper |
| 5 | `ConfirmDialog` | ✅ Complete | Modal preset for confirmations |
| 6 | `EmptyState` | ✅ Complete | Card + Icon + placeholder text |
| 7 | `StatCard` | ✅ Complete | Metric display card |
| 8 | `Hero` | ✅ Complete | Landing page hero section |

---

## 🔒 Framework Guarantees (v1.0+)

Faststrap commits to the following architectural contracts:
* **Deterministic HTML**: Server-rendered output is predictable and testable (`assert_html`).
* **Zero-JS Core**: All components function without JavaScript; enhancements are progressive.
* **No Client State**: We avoid hidden client-side state stores; state lives on the server.
* **Accessibility First**: WCAG-aligned defaults for all components.
* **Stability Markers**: Explicit `@stable` and `@experimental` decorators for API confidence.

---

## Phase 4C – Documentation & Polish (v0.4.6 – Completed)

✅ **Documentation Overhaul**

| Component | Status | Notes |
|-----------|--------|-------|
| Interactive Previews | ✅ Complete | All 40+ components live-rendered |
| Theme Isolation | ✅ Complete | Fixed CSS conflicts with MkDocs Material |
| `init.js` | ✅ Complete | Bootstrap socialization for Tooltips/Popovers |


---

## Phase 5 – Composed UI & Design System Layer (v0.5.0 – Target Feb 2026)

**Goal:** SaaS-ready patterns, layouts, and visual effects.  
**Focus:** `faststrap.layouts`, `faststrap.patterns`, `faststrap.effects`.

### Components & Plans

**1. Design Components (Original Phase 5 Plan)**

| Priority | Component | Module | Status | Notes |
|----------|-----------|--------|--------|-------|
| 1 | `faststrap.effects` | New Module | ✅ Complete | Zero-JS visual effects (fade, lift, highlight) |
| 2 | `DashboardLayout` | layouts | Planned | Admin panel layout with sidebar |
| 3 | `LandingLayout` | layouts | Planned | Marketing page layout |
| 4 | `NavbarModern` | patterns | ✅ Complete | Implemented as `GlassNavbar` |
| 5 | `FeatureGrid` | patterns | ✅ Complete | Icon + Title + Text grid |
| 6 | `PricingGroup` | patterns | ✅ Complete | 3-column pricing cards |
| 7 | `TestimonialSection` | patterns | Planned | Customer testimonials |
| 8 | `FooterModern` | patterns | Planned | Modern multi-column footer |

**2. Core Enhancements (Added in v0.5.0)**

| Component | Status | Notes |
|-----------|--------|-------|
| `Image` | ✅ Complete | Fluid, thumbnail, rounded, alignment utils |
| `Carousel` | ✅ Complete | Auto-play, controls, indicators, fade |
| `Placeholder` | ✅ Complete | Skeleton loading with glow/wave animations |
| `Scrollspy` | ✅ Complete | Auto-updating navigation based on scroll |
| `SidebarNavbar` | ✅ Complete | Premium vertical visual sidebar |
| `GlassNavbar` | ✅ Complete | Premium glassmorphism navbar |

> **Note:** The `faststrap init` CLI tool has been cancelled in favor of a simpler `pip install` philosophy for community extensions.





---

## Phase 6 – Data Science & Visualization (v0.6.x – Apr-Jul 2026)

**Goal:** Make Faststrap the #1 choice for Python data scientists building dashboards and data applications.

**Vision:** Zero-JavaScript data visualization with the power of pandas, Matplotlib, Plotly, and Altair - all in pure Python.

### v0.6.0 – Data Foundations (Apr 2026)

**Focus:** Core data components for tables, charts, and DataFrame integration.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `DataTable` | Advanced table with sort/filter/pagination for DataFrames | Planned |
| 2 | `Chart` | Wrapper for Matplotlib, Plotly, Altair with responsive sizing | Planned |
| 3 | `Table.from_df()` | Convert pandas/polars DataFrame to Bootstrap table | Planned |
| 4 | `MetricCard` | Enhanced StatCard with trends and deltas | Planned |
| 5 | `TrendCard` | KPI card with sparkline visualization | Planned |
| 6 | `KPICard` | Multi-metric dashboard card | Planned |

**Features:**
- Pandas & Polars DataFrame support
- Client-side sorting/filtering for small datasets (<1000 rows)
- Server-side pagination for large datasets
- CSV/Excel export buttons
- Automatic type inference and formatting
- Theme-aware chart colors

### v0.6.1 – Advanced Data Components (May 2026)

**Focus:** Dashboard layouts, filters, and data visualization patterns.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `DashboardGrid` | Responsive grid system for dashboards | Planned |
| 2 | `FilterBar` | Composable filter components | Planned |
| 3 | `DateRangePicker` | Date range selection with presets | Planned |
| 4 | `MultiSelect` | Multi-select dropdown for filtering | Planned |
| 5 | `RangeSlider` | Numeric range slider | Planned |
| 6 | `ExportButton` | Export data to CSV/Excel/PDF | Planned |
| 7 | `DistributionPlot` | Histogram with KDE overlay | Planned |
| 8 | `CorrelationMatrix` | Heatmap for correlation analysis | Planned |

**Features:**
- HTMX-powered filtering (zero-JS)
- Auto-refresh dashboards
- Print-friendly layouts
- Responsive dashboard grids

### v0.6.2 – Real-time & ML Integration (Jun 2026)

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
- Server-Sent Events (SSE) for real-time updates
- Streaming data tables
- ML model performance tracking
- Interactive cross-filtering

### v0.6.3 – Productivity & Polish (Jul 2026)

**Focus:** Developer experience, form builders, and HTMX presets.

| Priority | Component | Description | Status |
|----------|-----------|-------------|--------|
| 1 | `Form.from_pydantic()` | Auto-generate forms from Pydantic models | Planned |
| 2 | `ActiveSearch` | HTMX preset for live search | Planned |
| 3 | `InfiniteScroll` | HTMX preset for infinite scrolling | Planned |
| 4 | `TimeSeriesPlot` | Time series with moving averages | Planned |
| 5 | `GeoMap` | Geographic visualization (optional) | Planned |

**Features:**
- Type-safe form generation
- Automatic validation from Pydantic
- HTMX patterns library
- Complete documentation with 20+ examples

---

## 🎯 Data Science Positioning

Faststrap is uniquely positioned for data scientists:

**vs. Streamlit:**
- ✅ More customizable (full Bootstrap control)
- ✅ Production-ready (integrates into any FastHTML app)
- ✅ Better performance (server-side rendering)

**vs. Dash (Plotly):**
- ✅ Simpler API (no React, no callbacks)
- ✅ Zero JavaScript required
- ✅ Lighter weight

**vs. Panel (HoloViz):**
- ✅ Cleaner, more Pythonic API
- ✅ Better documentation
- ✅ Professional Bootstrap aesthetics

**Target Users:**
- Data scientists building internal dashboards
- Data analysts creating stakeholder reports
- ML engineers monitoring model performance
- Business intelligence developers

---

## 🌍 Community Ecosystem (Safe Path)

**Goal:** Enable a community-driven ecosystem without bloating core.

These phases are documentation and process-driven, not runtime dependencies.

### 1. Extension Contracts (v0.5.x)
- [ ] Document contracts for Theme Packs and Component Packs.
- [ ] Define "explicit import" usage pattern (no auto-discovery).

### 2. The Registry (v0.6.x)
- [ ] Create `Faststrap-org/faststrap-extensions` repo (Metadata only).
- [ ] List approved themes and components.

### 3. Tooling (v0.7+)
- [ ] `faststrap init --template=community/xyz` (Scaffold only).

### Extension Design Rules

All Faststrap extensions must:
- Use explicit imports (no auto-registration)
- Avoid monkey-patching core APIs
- Declare compatibility with Faststrap versions
- Remain optional and replaceable
- Never affect core runtime behavior

---

## 🔒 Stability & Versioning Policy

### Component Maturity Levels

🟢 **Stable** (`@stable`)
- API won't break in minor versions.
- Comprehensive tests (>90% coverage).
- Example: `Button`, `Card`, `Input`.

🟡 **Beta** (`@beta`)
- API may change in minor versions.
- Basic tests (>70% coverage).
- Example: New Phase 6 components.

🔴 **Experimental** (`@experimental`)
- API will likely change.
- Minimal tests.
- Use at own risk.

---

## 🚫 Non-Goals

What Faststrap intentionally *won't* do:

- ❌ **Client-side reactivity** (use Alpine.js if needed)
- ❌ **Custom CSS framework** (we're Bootstrap-native)
- ❌ **Database ORM** (use SQLModel/SQLAlchemy)
- ❌ **Full auth backend** (we provide UI, you provide logic)

**Why?** Faststrap excels at Bootstrap + HTMX + Python. We integrate with best-in-class tools rather than replacing them.

---

## Phase 6E – Accessibility & Compliance (Post-v0.6)

**Goal**: Enterprise-grade compliance tools.
- [ ] ARIA validation helpers
- [ ] Focus management utilities
- [ ] Contrast-safe defaults checking


    Accessibility defaults are already applied throughout earlier phases; Phase 6E adds validation & compliance tooling.
---

---

## v1.0.0 – Production Release (Target Aug 2026)

**Goal:** Full Bootstrap parity + SaaS patterns + Documentation  
**Target:** 100+ components

### Milestones

- [ ] 100+ components
- [ ] 95%+ test coverage
- [ ] Full documentation website (MkDocs Material)
- [ ] Component playground / live demos
- [ ] 3-5 starter templates (Dashboard, Admin, E-commerce)
- [ ] Video tutorials
- [ ] Community contributions from 50+ developers

---

## Success Metrics

| Metric | v0.3.1 | v0.4.5 (Now) | v0.5.0 | v1.0.0 |
|--------|--------------|--------------|--------|--------|
| Components | 20 | 38 | 50 | 100+ |
| Tests | 219 | 230+ | 500+ | 800+ |
| Coverage | 80% | 85%+ | 90% | 95%+ |
| Contributors | 5+ | 15+ | 25+ | 50+ |

---

## How to Contribute

1. **Pick a component** from any Phase table above
2. **Comment on GitHub Issues** → "I'll build [Component]" → get assigned
3. **Use templates**: `src/faststrap/templates/component_template.py`
4. **Follow guides**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
5. **Write tests**: 10-15 tests per component using `to_xml()`
6. **Submit PR** → merged in ≤48 hours

---

## Documentation Website (In Progress)

**Stack:** MkDocs Material + GitHub Pages

**Structure:**
- Getting Started (Installation, Quick Start)
- Component Reference (Forms, Display, Feedback, Navigation, Layout)
- Theming Guide (Built-in themes, Custom themes, Dark mode)
- HTMX Integration Guide
- API Reference

---

## Community Feedback

Tell us what you need most:
- [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)
- Vote on issues with 👍
- [FastHTML Discord](https://discord.gg/qcXvcxMhdP) → #faststrap channel

Your votes directly influence what gets built next.

---

**Last Updated: January 2026**  
**Current Version: 0.4.5 (38 components live)**

**Let's build the definitive UI library for FastHTML — together.**