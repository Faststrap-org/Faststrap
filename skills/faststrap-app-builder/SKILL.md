---
name: faststrap-app-builder
description: Use when building or redesigning real FastHTML applications with Faststrap, such as company websites, SaaS landing pages, dashboards, portals, auth flows, admin systems, or multi-page product sites. This skill guides Faststrap work toward production-grade results by using Faststrap components first, Bootstrap for structure, HTMX for interactivity, and custom CSS for polish rather than generic Bootstrap presentation.
---

# Faststrap App Builder

Use this skill when the task is to build or significantly improve a real application with Faststrap + FastHTML.

## First moves

Before writing code:

1. **Look up the component API** in `references/component-api.md` to find exact signatures and defaults. This prevents hallucinating parameter names.
2. Inspect the current app's entrypoint, theme/defaults module, route layout, asset mount, and custom CSS.
3. If the user provides a Faststrap repo path, inspect:
   - `AGENTS.md`
   - `README.md`
   - the relevant component modules under `src/faststrap/components/`
   - the relevant docs pages under `docs/components/`
   - the most relevant files in `examples/` and `showcase/`
   - real-world apps: `neoportfolio/`, `neo-admin/`, `datascience_admin/`, `data_science/` for production patterns
4. If the user provides a reference app, inspect it before designing.
5. Match the page type to the closest reference:
   - start with `references/reference-index.md`
   - marketing/landing: use the reference index, then open `references/reference-apps.md` only if needed
   - dashboard/admin: use the reference index, then open `references/reference-apps.md` only if needed
   - auth/onboarding: see `references/nis-patterns.md`
6. If building a fresh app from scratch, start from `references/faststrap-quickstart.md` and adapt the template.
7. Inventory the existing Faststrap component surface before inventing new UI structure. Faststrap has 152+ components, so check `references/component-api.md` before building custom HTML.
8. Follow the implementation order of precedence below before inventing custom structure.

## Implementation order of precedence

Use this order unless the task clearly requires otherwise:

1. Faststrap components and Bootstrap-native layout/responsive utilities
2. HTMX for dynamic behavior and partial updates
3. Custom CSS for branding, atmosphere, and modern visual polish
4. JavaScript only when HTMX/Bootstrap cannot solve the problem cleanly or when browser/PWA APIs are required

This means:

- prefer Bootstrap spacing, grid, display, flex, container, offcanvas, modal, collapse, and utility classes before writing custom layout CSS
- prefer existing Faststrap components and patterns before creating bespoke wrappers or raw HTML structures
- prefer HTMX before custom JavaScript for interactivity, filtering, partial refresh, form flows, and inline actions
- use custom CSS to elevate visuals, not to reimplement Bootstrap responsiveness or hide/show behavior unnecessarily
- allow JavaScript for legitimate cases such as PWA flows, geolocation, service workers, media capture, complex charts/maps, or browser APIs HTMX cannot replace
- when two cards or columns sit side by side, define the mobile stack explicitly first with `Row(..., cols=1, cols_md=2)` or `Row(..., cols=1, cols_lg=2)` rather than assuming desktop structure will collapse well on its own
- if a supporting/highlight card is too content-heavy for mobile or tablet, hide it intentionally with Bootstrap display classes such as `d-none d-lg-block` instead of squeezing it into a weak small-screen composition

## Non-negotiable standards

- Do not ship generic Bootstrap-looking pages.
- Do not default to plain white sections, weak typography, or boilerplate hero-card-grid-footer layouts unless the references support that exact direction.
- Choose one explicit primary reference before writing the page.
- Prefer composing existing Faststrap components and patterns first, then layer custom CSS for polish.
- Assume there is probably already a relevant Faststrap component or pattern somewhere in the 100+ component surface; check the framework before inventing a new one.
- Build shared theme tokens and layout structure before polishing individual pages.
- Keep the UI responsive, accessible, and visually intentional.
- Do not rely on external CSS CDNs for project styling. Keep styling in local project assets and Faststrap/Bootstrap.
- Treat JavaScript as the last interaction tool, not the first one.
- Before finishing, run a dedicated Bootstrap-smell pass and remove untouched default pills, soft default shadows, over-rounded surfaces, and generic section treatment.
- **UX feedback is non-negotiable:** every user action that mutates state must show loading, success, or error feedback. Use `LoadingButton`, `hx-indicator`, `Toast`, `Alert`, and `FormErrorSummary`. A page where the user clicks and nothing visibly happens is incomplete.
- **Use `set_component_defaults()` in every app:** set global defaults for `Button`, `Card`, `Input`, and `Alert` at app startup so the whole app feels consistent without repeating kwargs on every call. Do not leave every component at its bare Bootstrap default.

## Reference discipline

- Always open `references/reference-index.md` first when selecting a showcase reference.
- Pick one primary reference and at most one secondary reference.
- Prefer flagship references over legacy/simple ones unless the user explicitly asks for a simpler build.
- Reuse structure, responsiveness, and quality bar from the reference; do not copy text or brand voice.
- If the chosen reference is a legacy/simple example, compensate with stronger CSS and hierarchy decisions.

## Bootstrap-smell audit

Run this pass before finishing any polished page:

- palette feels branded, not stock Bootstrap blue
- cards and sections have intentional surface treatment, not untouched default Bootstrap panels
- typography hierarchy is obvious across hero, section, body, and label text
- border radii feel deliberate rather than default Bootstrap rounding
- spacing rhythm is consistent across sections, cards, controls, and stacks
- primary buttons feel intentional, not flat defaults
- mobile layout is designed explicitly, not just desktop collapsed downward
- light and dark variants both remain legible and intentional when both are supported
- empty, loading, success, and error states exist for key flows
- HTMX is used where interaction is needed instead of defaulting to custom JavaScript
- no generic hero-card-grid-footer boilerplate survived untouched

## Responsive layout rules

Faststrap uses Bootstrap's grid and utility classes. Do not write custom media queries for layout when Bootstrap already solves it.

### Row / Col responsive breakpoints

Use `Row` + `Col` with responsive `cols_*` parameters:

```python
Row(
    Col(Card("A"), cols=12, cols_md=6, cols_lg=4),
    Col(Card("B"), cols=12, cols_md=6, cols_lg=4),
    Col(Card("C"), cols=12, cols_md=6, cols_lg=4),
    Col(Card("D"), cols=12, cols_md=6, cols_lg=4),
    g=3,
)
```

This produces:
- mobile (`<768px`): 1 column (full width)
- tablet (`≥768px`): 2 columns
- desktop (`≥992px`): 4 columns

### Card grid templates

**4 cards:**
```python
Row(
    Col(Card("A"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("B"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("C"), cols=12, cols_md=6, cols_lg=3),
    Col(Card("D"), cols=12, cols_md=6, cols_lg=3),
    g=3,
)
```

**3 cards:**
```python
Row(
    Col(Card("A"), cols=12, cols_md=4, cols_lg=4),
    Col(Card("B"), cols=12, cols_md=4, cols_lg=4),
    Col(Card("C"), cols=12, cols_md=4, cols_lg=4),
    g=3,
)
```

**2 cards side by side on tablet, stacked on mobile:**
```python
Row(
    Col(Card("A"), cols=12, cols_md=6),
    Col(Card("B"), cols=12, cols_md=6),
    g=3,
)
```

**Dashboard stats (4-up on desktop, 2-up on tablet, 1-up on mobile):**
```python
Row(
    Col(StatCard("Revenue", "$12K", "+5%"), cols=12, cols_md=6, cols_lg=3),
    Col(StatCard("Users", "1.2K", "+12%"), cols=12, cols_md=6, cols_lg=3),
    Col(StatCard("Orders", "456", "+3%"), cols=12, cols_md=6, cols_lg=3),
    Col(StatCard("Growth", "8%", "+2%"), cols=12, cols_md=6, cols_lg=3),
    g=3,
)
```

### Responsive display utilities

Use Bootstrap display utilities to show/hide content at breakpoints. Never write custom `@media` rules for show/hide:

```python
# Hide on mobile, show on desktop
Div("Desktop only", cls="d-none d-lg-block")

# Show on mobile, hide on desktop
Div("Mobile only", cls="d-block d-lg-none")

# Show on tablet and up
Div("Tablet+", cls="d-none d-md-block")
```

### Responsive spacing

Use responsive spacing utilities instead of custom CSS:

```python
# p-2 on mobile, p-4 on desktop
Card("Content", cls="p-2 p-lg-4")

# mb-3 on mobile, mb-4 on tablet+
Stack("A", "B", "C", gap=2, cls="mb-3 mb-md-4")
```

### Responsive text alignment

```python
# Center on mobile, left on desktop
Div("Text", cls="text-center text-lg-start")
```

### Sidebar layout pattern

```python
Row(
    Col(
        SidebarNavbar(...),
        cols=12, cols_md=3,
        cls="d-none d-md-block",
    ),
    Col(
        # Main content
        ...
    ),
)
```

For mobile, use a `Drawer` or `BottomNav` instead of the sidebar.

### Never do this

```python
# BAD: custom CSS for responsiveness
Div("Content", style="@media (min-width: 768px) { width: 50%; }")

# GOOD: Bootstrap utility
Div("Content", cls="col-12 col-md-6")
```

### Mobile-first rule

Always design mobile first. Start with the single-column layout (`cols=12` or `cols=1`), then add `cols_md`, `cols_lg`, `cols_xl` as the content gains space. Never design desktop-first and hope it collapses.

See `references/responsive-layout.md` for complete card grid patterns and responsive templates.

## Visual system rules

- Define a typography hierarchy before polishing components:
  - hero headline: large, tight line-height, deliberate tracking
  - section headline: clearly smaller than hero but still high-contrast
  - body copy: readable, quieter, and visibly distinct from headings
  - eyebrow/kicker text: compact and intentional, not decorative noise
- Establish spacing rhythm at the section level first:
  - major sections should feel intentionally separated
  - cards should have consistent internal padding
  - stacked controls should keep consistent gaps across breakpoints
- Use Bootstrap for structure, but do not leave Bootstrap's default radii, shadows, and surface treatment untouched on flagship pages.
- Give every polished page a clear surface strategy:
  - dark shell with lighter cards
  - soft light shell with elevated white cards
  - editorial split backgrounds
  - glass or layered atmosphere where it genuinely helps

## States and UX coverage

- Do not finish a page without checking empty, loading, success, and error states for the main interactive surfaces.
- Empty states should explain what to do next, not just say "No data".
- Loading states should use Faststrap or Bootstrap primitives visibly rather than leaving dead-looking blank areas.
- Error states should be readable, specific, and visually integrated with the page.
- Forms should show validation feedback, helper text where needed, and clear submit affordances.

## Accessibility rules

- Preserve semantic headings in descending order.
- Ensure interactive controls have discernible labels or `aria-label`s.
- Keep contrast strong enough in both light and dark themes.
- Do not hide important meaning in color alone.
- Preserve keyboard focus visibility; do not style it away.
- When using icon-only controls, provide accessible labels.
- Prefer buttons for actions and links for navigation; do not blur the two casually.

## CSS organization rules

- For single-file showcases or isolated demos, inline `Style(...)` blocks are acceptable.
- For multi-route or production-style apps, move custom CSS into local asset files and mount them properly.
- Prefer a small production CSS shape such as:
  - `_brand.css`
  - `_typography.css`
  - `_layout.css`
  - `_surfaces.css`
  - `_interactions.css`
- Keep Bootstrap utilities for layout/responsiveness and custom CSS for brand identity, surface treatment, and advanced polish.
- Avoid scattering one-off inline `style=` strings across a codebase when the app is larger than a simple showcase.

See `references/css-architecture.md` for a recommended production CSS structure.

## HTMX-first recipes

Prefer these patterns before reaching for custom JavaScript:

- `ActiveSearch` for live search/filtering
- `AutoRefresh` for polling dashboards or activity surfaces
- `LazyLoad` for deferred sections or below-the-fold content
- `LoadingButton` for async actions with visible feedback
- `ConfirmDialog` for destructive actions
- `FormGroup` + HTMX validation endpoints for live field feedback
- `DataTable` with built-in sort/search/pagination before inventing raw table wiring

When not to use HTMX as the primary tool:

- complex client-side charting behavior
- real-time collaboration
- browser/device APIs such as camera, geolocation, or push/service-worker flows

See `references/htmx-recipes.md` for concrete build patterns.

## Component selection

Before inventing a wrapper or custom HTML structure, check `references/component-selection.md`.

Use it to answer:

- which card/data surface fits this need?
- is there already a form or validation helper?
- should this be a navigation component, a layout primitive, or a preset?
- is this actually a CSS problem rather than a missing component?

## Working pattern

1. Establish the app shell
- Create or inspect the FastHTML app entrypoint.
- Wire `add_bootstrap(app, ...)`.
- Mount project assets.
- Add shared custom CSS after Faststrap.

2. Establish shared design language
- Put brand colors and global component defaults in a single theme module.
- Use `set_component_defaults()` to configure global defaults for `Button`, `Card`, `Input`, and `Alert` at app startup. This ensures consistency without repeating kwargs on every call.
- Define layout wrappers before page-level sections.
- Use custom CSS for depth: gradients, glass, section contrast, spacing rhythm, shadows, image treatment, and state styling.
- Keep structural responsiveness primarily in Bootstrap/Faststrap usage, not hand-written media-query-heavy layout rewrites unless clearly necessary.
- Treat mobile as the base layout. Build the one-column version first, then opt into multi-column layouts at `md`/`lg` breakpoints where the content can breathe.

3. Build pages from references, not from scratch
- Pick the nearest reference app.
- Reuse its structural ideas, not its text.
- Preserve the user's domain and content hierarchy.

4. Favor production composition
- Split layouts, shared UI, and routes cleanly.
- Use route modules rather than oversized single-file pages when the app has multiple screens.
- Keep business logic out of presentation modules when possible.

5. Verify before finishing
- Check mobile and desktop structure.
- Check that Faststrap theme/defaults are actually applied.
- Check empty states, CTA clarity, spacing consistency, and contrast.
- Run the Bootstrap-smell audit explicitly.
- Run relevant tests; if the project has none, add at least focused smoke or route tests when practical.

## Finish checklist

Before you consider the UI done, verify:

- typography hierarchy is deliberate
- spacing rhythm is consistent
- mobile layout is intentional, not just collapsed desktop
- responsive breakpoints use `cols_md`, `cols_lg`, etc., not custom CSS media queries
- Bootstrap display utilities (`d-none`, `d-md-block`, etc.) are used for show/hide instead of custom CSS
- empty/loading/error states exist for key flows
- accessibility labels and focus states remain intact
- at least one final pass was made specifically to remove Bootstrap-default visual leakage
- `set_component_defaults()` is configured for `Button`, `Card`, `Input`, and `Alert` so the app feels cohesive

See also:

- `references/visual-design-rules.md`
- `references/troubleshooting.md`
- `references/form-workflow.md`

## Design bar

Good Faststrap app work should feel:

- branded rather than template-like
- structured rather than improvised
- spacious rather than cramped
- editorial and intentional rather than default Bootstrap
- polished enough to resemble the provided showcase apps

## Anti-patterns

- dumping everything into one route file
- using only stock Faststrap examples without adapting the visual language
- relying on raw inline styles everywhere instead of shared CSS
- ignoring the user's reference projects
- making every page look like the same SaaS starter
- reaching for JavaScript before HTMX
- replacing Bootstrap layout/responsive utilities with avoidable custom CSS
- importing third-party styling CDNs for things Faststrap/Bootstrap and local CSS should handle
- forcing dense secondary cards, stat panels, or highlight boxes to remain visible on mobile when Bootstrap display utilities can preserve a cleaner small-screen hierarchy

## Dark Mode

Faststrap supports dark mode via `add_bootstrap(app, mode="dark")` or `ThemeToggle()`.

- Every component supports `[data-bs-theme="dark"]` and `[data-bs-theme="light"]` variants
- For custom CSS, always provide both light and dark counterparts (see `references/css-architecture.md`)
- Use `ThemeToggle(current_theme="auto")` to let users switch themes
- Dark mode shell: `#0b1120` or `#0f172a` backgrounds with `#e2e8f0` text
- Light mode shell: `#f8fafc` or `#ffffff` backgrounds with `#0f172a` text
- Glassmorphism surfaces work best in dark mode: `background: rgba(255,255,255,0.04); backdrop-filter: blur(14px)`

## Fx Animations

Zero-JS CSS animations via the `Fx` helper class. Always include `Fx.base` when using any animation.

```python
from faststrap import Fx

# Entrance + hover + delay
Card("Hello", cls=[Fx.base, Fx.fade_in, Fx.hover_lift, Fx.delay_sm])
```

Quick reference:
- **Entrance:** `Fx.fade_in`, `Fx.slide_up`, `Fx.slide_down`, `Fx.zoom_in`, `Fx.bounce_in`
- **Hover:** `Fx.hover_lift`, `Fx.hover_scale`, `Fx.hover_glow`, `Fx.hover_tilt`
- **Loading:** `Fx.spin`, `Fx.pulse`, `Fx.shimmer`
- **Visual:** `Fx.glass`, `Fx.shadow_soft`, `Fx.shadow_sharp`, `Fx.gradient_shift`
- **Speed:** `Fx.fast` (150ms), `Fx.slow` (500ms), `Fx.slower` (1000ms)
- **Delay:** `Fx.delay_xs` (100ms) through `Fx.delay_xl` (1000ms)

See `references/fx-animations.md` for the complete reference.

## Testing

Faststrap apps should be tested at two levels:

### Component Tests

Use `to_xml()` to verify component rendering:

```python
from fasthtml.common import to_xml
from faststrap import Button, Card

def test_button_renders():
    html = to_xml(Button("Click", variant="primary"))
    assert 'class="btn btn-primary"' in html
    assert "Click" in html
```

### App-Level Tests

Use FastHTML's test client for route-level testing:

```python
from fasthtml.test import TestClient

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text

def test_form_submission(client):
    response = client.post("/login", data={
        "email": "test@example.com",
        "password": "password123",
    })
    assert response.status_code == 200
```

### HTMX Tests

```python
def test_htmx_search(client):
    response = client.get(
        "/search",
        headers={"HX-Request": "true"},
        params={"q": "test"},
    )
    assert response.status_code == 200
```

Run tests:
```bash
pytest tests/ -q
```

## Deployment

### Static Export

For marketing sites, docs, and blogs, use Faststrap's static export:

```bash
python -m faststrap export main:app ./dist
```

See `docs/deployment/static-export.md` for full documentation.

### Dynamic Deployment

For apps with HTMX, sessions, or server-side logic:

- **Vercel:** Use `add_bootstrap(app, use_cdn=True)` and expose the ASGI app
- **Railway:** Standard FastHTML deployment with `python main.py`
- **Render:** Use `web: python main.py` in `Procfile`
- **Fly.io:** Use the Dockerfile or `fly launch`
- **VPS:** Use `gunicorn` or `uvicorn` with `main:app`

Always run `faststrap doctor` before deploying:

```bash
python -m faststrap doctor
```

## Read these references as needed

- `references/ux-feedback.md`: **required reading for every interactive page** — loading states, success/error feedback, button states, form feedback, and UX checklist
- `references/responsive-layout.md`: **required reading for every page with cards, grids, or sidebars** — Row/Col responsive patterns, Bootstrap utilities, mobile-first card grids
- `references/component-api.md`: **complete API signatures** for all 152+ components — look up exact params before calling any component
- `references/faststrap-quickstart.md`: copy-paste app templates for fresh projects
- `references/visual-patterns.md`: **22 concrete visual design patterns** extracted from production Faststrap apps — read this before designing any page
- `references/reference-index.md`: canonical first-stop guide for picking the right showcase or production reference by page type and quality bar
- `references/reference-apps.md`: which local Faststrap showcase files to inspect by page type
- `references/htmx-recipes.md`: concrete HTMX-first interaction patterns for search, refresh, validation, confirm, lazy loading, and inline editing
- `references/component-selection.md`: practical guide for choosing existing Faststrap components before inventing new ones
- `references/css-architecture.md`: production CSS file organization and token structure
- `references/form-workflow.md`: complete form, validation, submit, and success/error flow patterns
- `references/visual-design-rules.md`: baseline design quality bar for typography, surfaces, spacing, and responsiveness
- `references/troubleshooting.md`: common failure modes and how to correct them quickly
- `references/nis-patterns.md`: real production-style project wiring and theming patterns
- `references/mmercyj-patterns.md`: polished company-site composition and mobile-first responsive simplification patterns
- `references/fx-animations.md`: Fx class reference for all animations and effects
- `references/project-agents-template.md`: template instructions to place in fresh app repos so future sessions start with the right guardrails
