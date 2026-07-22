# Component Selection Guide

Use this guide before inventing a custom wrapper or dropping into raw HTML.

The goal is to choose the closest existing Faststrap surface first, then add CSS and HTMX around it if needed.

---

## Quick Rule

- If Faststrap already has the structural component, use it.
- If Faststrap already has the interaction preset, use it.
- If the remaining need is purely visual polish, solve it with CSS.
- Invent a new component only when the same composition keeps repeating across real apps.

---

## Need a Card or Display Surface?

Use:

- `Card(*children, title=None, header=None, footer=None, **kwargs)` — general-purpose content card
- `StatCard(title, value, icon=None, trend=None, trend_type="neutral", **kwargs)` — one metric with optional trend
- `MetricCard(title, value, delta=None, delta_type="neutral", **kwargs)` — metric + compact delta
- `TrendCard(title, value, sparkline=None, delta=None, delta_type="neutral", **kwargs)` — metric + sparkline
- `KPICard(title, metrics, columns=2, **kwargs)` — grouped KPI surface
- `EmptyState(icon=None, title="No data available", description=None, action=None, **kwargs)` — empty/no-data screen
- `Table(*children, striped=False, hover=False, responsive=False, **kwargs)` — simple table markup
- `DataTable(data, sortable=False, searchable=False, pagination=False, **kwargs)` — sorting, search, pagination
- `Chart(figure, responsive=True, **kwargs)` — chart display wrapper (matplotlib/plotly/altair)
- `Markdown(text, sanitize=True, **kwargs)` — rendered markdown blocks
- `Figure(src, caption=None, fluid=True, **kwargs)` — image + caption
- `Image(src, alt=None, fluid=None, rounded=None, **kwargs)` — product/media image
- `Sheet(*children, sheet_id=None, title=None, **kwargs)` — mobile-first bottom sheet
- `Kbd(*children, size="md", variant="light", **kwargs)` — keyboard key display
- `Tag(children, variant="secondary", size="md", removable=False, **kwargs)` — chip/tag component
- `AspectRatio(children, ratio="16/9", **kwargs)` — ratio-constrained container
- `Separator(orientation="horizontal", thickness=None, spacing=None, **kwargs)` — semantic divider
- `CodeBlock(code, language=None, filename=None, copy=False, **kwargs)` — code display with copy
- `JsonViewer(data, title=None, expanded=True, **kwargs)` — collapsible JSON viewer
- `KeyValueList(items, striped=False, compact=False, **kwargs)` — key-value pair list
- `RecordDetail(items, title=None, actions=None, **kwargs)` — record detail view

Choose raw `Card()` when:

- the content is mostly custom layout
- you do not need a dedicated metric/table/chart abstraction

Choose `DataTable()` instead of a raw table when:

- users need search
- users need sort
- users need pagination
- the route already has server-backed filtering

---

## Need Form Controls?

Use:

- `Input()`
  - text, email, password, numeric, and general field input
- `Select()`
  - standard select menus
- `SearchableSelect()`
  - server-side searchable option picker
- `MultiSelect()`
  - multiple option selection
- `Checkbox()`
- `Radio()`
- `Switch()`
- `Range()`
- `RangeSlider()`
- `DateRangePicker()`
- `FileInput()`
- `FloatingLabel()`
- `InputGroup()` / `InputGroupText()`
- `ToggleGroup()`
- `ThemeToggle()`

Use `SearchableSelect()` when:

- the option list is large
- the options should be searched server-side
- you want HTMX-backed search instead of client-side select plugins

Use `DateRangePicker()` when:

- the user is filtering by time window
- the page needs dashboard/reporting controls

---

## Need Form Structure or Validation?

Use:

- `Form()`
  - structured form wrapper
- `FormBuilder()`
  - generated form surface when appropriate
- `FormGroup()`
  - label + help text + validation feedback around one control
- `FormErrorSummary()`
  - top-of-form error summary
- `FormGroupFromErrors()`
  - backend-error mapping helper
- `map_formgroup_validation()`
  - backend validation bridge

Recommended pattern:

- field UI: `FormGroup(...)`
- live validation: HTMX on the input inside `FormGroup(...)`
- submit-time validation: `FormGroupFromErrors(...)` or `map_formgroup_validation(...)`

---

## Need Feedback or Status UI?

Use:

- `Alert()`
  - inline status messages
- `Toast()` / `SimpleToast()` / `ToastContainer()`
  - transient notifications
- `Modal()`
  - blocking dialog content
- `ConfirmDialog()`
  - destructive action confirmation
- `Spinner()`
  - simple loading state
- `Placeholder()`
  - skeleton line/block
- `PlaceholderCard()`
  - card-like skeleton state
- `PlaceholderButton()`
  - loading button shape
- `Progress()` / `ProgressBar()`
  - completion/progression display
- `ErrorDialog()`
  - modal error handling
- `ErrorPage()`
  - full-page failure state
- `NotificationCenter()`
  - notification list/panel pattern

Use `ConfirmDialog()` instead of raw `Modal()` when:

- the interaction is a standard "are you sure?" flow
- the user needs a clear confirm/cancel action

Use `PlaceholderCard()` instead of a blank gap when:

- a card-shaped region is loading
- the user would benefit from visible structure before content arrives

---

## Need Navigation?

Use:

- `Navbar()`
  - standard top navigation
- `GlassNavbar()`
  - premium/styled top navigation
- `NavbarModern()`
  - pattern-level marketing navbar
- `SidebarNavbar()`
  - dashboard or app sidebar navigation
- `BottomNav()` / `BottomNavItem()`
  - mobile navigation
- `Breadcrumb()`
  - location path / page hierarchy
- `Tabs()` / `TabPane()`
  - section switching
- `Accordion()` / `AccordionItem()`
  - collapsible grouped sections
- `Dropdown()` / `DropdownItem()`
  - menu actions or grouped nav links
- `Drawer()`
  - off-canvas navigation or side panel
- `Collapse()`
  - show/hide structural content
- `Pagination()`
  - standalone basic pagination UI

Use `BottomNav()` when:

- the app is mobile-first
- the main navigation must stay reachable on small screens

Use `Drawer()` when:

- the nav or settings surface should slide in
- the content should feel panel-based instead of page-based

---

## Need Layout or App Shell Structure?

Use:

- `Container()`
- `Row()`
- `Col()`
- `Hero()`
- `DashboardGrid()`
- `DashboardLayout()`
- `AuthLayout()`
- `LandingLayout()`

Recommended responsive rule:

- start with mobile-first row definitions such as `Row(..., cols=1, cols_md=2, cols_lg=3)`
- do not rely on desktop structure "just collapsing nicely"

Use `DashboardLayout()` when:

- the page is a dashboard/admin/internal tool
- there is sidebar or app-shell behavior

Use `AuthLayout()` when:

- the page is login, register, reset-password, or onboarding-focused

---

## Need Marketing / Pattern Components?

Use:

- `Feature()`
- `FeatureGrid()`
- `PricingTier()`
- `PricingGroup()`
- `Testimonial()`
- `TestimonialSection()`
- `FooterModern()`

Use these instead of rebuilding:

- feature lists
- pricing tables
- social proof sections
- multi-column marketing footers

---

## Need Interaction Without Custom JavaScript?

Use presets:

- `ActiveSearch`
  - live search/filtering
- `InfiniteScroll`
  - feed or list pagination on scroll
- `AutoRefresh`
  - polling updates
- `LazyLoad`
  - delayed region loading
- `LoadingButton`
  - loading-state actions
- `hx_redirect`
  - redirect after server action
- `hx_refresh`
  - full refresh after server action
- `hx_trigger`
  - trigger client events
- `hx_reswap`
  - adjust swap strategy
- `hx_retarget`
  - adjust swap target
- `toast_response`
  - response + toast

Use these before writing custom interaction wrappers.

---

## Need Theme / Defaults / Shared Design Language?

Use:

- `create_theme()`
- `set_component_defaults()`
- `resolve_defaults()`
- `ThemeToggle()`

Recommended shared setup:

- keep palette and theme creation in one module
- keep component defaults in one module
- add project CSS after Faststrap assets

---

## Need Accessibility / SEO / PWA Support?

Accessibility:

- `SkipLink`
- `LiveRegion`
- `FocusTrap`
- `VisuallyHidden`

SEO:

- `PageMeta`
- `SEO`
- `StructuredData`

PWA:

- `PwaMeta`
- `add_pwa()`

Do not reinvent these with custom snippets when Faststrap already provides the primitive.

---

## Practical Selection Cheatsheet

If you need:

- KPI dashboard cards
  - `StatCard`, `MetricCard`, `TrendCard`, `KPICard`
- searchable/sortable list
  - `DataTable`
- mobile transactional UI
  - `BottomNav`, `Sheet`, `Drawer`
- auth page
  - `AuthLayout`, `FormGroup`, `ThemeToggle`
- premium landing page
  - `Hero`, `FeatureGrid`, `PricingGroup`, `TestimonialSection`, `FooterModern`
- live search
  - `ActiveSearch`
- polling metrics
  - `AutoRefresh`
- confirm delete/archive
  - `ConfirmDialog`
- no-data state
  - `EmptyState`
- loading skeleton
  - `Placeholder`, `PlaceholderCard`

---

## When You Still Need Custom Composition

Custom composition is still correct when:

- the structure is domain-specific and not repeated across apps
- the content is mostly bespoke layout inside an existing `Card()` or `Row()`
- the interaction is a small HTMX endpoint swap rather than a reusable framework primitive

In those cases:

- keep Faststrap for the structural base
- keep HTMX for the interaction
- use CSS for polish
- avoid inventing a framework-level component too early
