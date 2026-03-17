# Faststrap v0.6.0 Fix Plan (Pre-Release)

**Date:** 2026-03-16

## Purpose
This plan defines the concrete fixes required before cutting v0.6.0. It prioritizes functional correctness, documentation accuracy, and release integrity based on a full codebase audit and the Sonnet 4.6 findings (appended verbatim).

---

## Release Gate (Must Pass)
- All critical and partial issues resolved (see below).
- Examples and templates run without runtime errors.
- Docs and README reflect actual API surface, component counts, and built-in themes.
- Tests green: `ruff`, `black --check`, `mypy`, `pytest`.

---

## P0 Blockers (Fix Before Any v0.6.0 Tag)
1. **SearchableSelect click behavior is broken**
   - Default mode uses `hx-on-click` instead of `hx-on:click`, so clicks do nothing.
   - CSP-safe mode does not set `data-fs-value`, so selection becomes empty.
   - Files: `src/faststrap/components/forms/searchable_select.py`, `src/faststrap/core/assets.py`, `tests/test_components/test_searchable_select.py`.

2. **ErrorPage icon is rendered as raw text**
   - `ErrorPage` passes a string icon to `EmptyState`, which expects a component.
   - Fix by wrapping `icon` string in `Icon(...)` or teaching `EmptyState` to accept a string icon.
   - Files: `src/faststrap/components/feedback/error_page.py`, `src/faststrap/components/display/empty_state.py`.

3. **Examples fail with invalid theme values**
   - `add_bootstrap(theme="dark"/"light")` is invalid; theme expects a built-in theme name or `Theme`.
   - Files (representative): `examples/**/app.py`, `examples/05_examples/*`, `examples/landing_demo*.py`, `examples/portfolio_demo*.py`, `examples/01_hello_button/app.py`.

---

## P1 High Priority (User-Facing Breakage)
1. **Input does not support `input_type="textarea"`**
   - Many examples use it; currently renders `<input type="textarea">`.
   - Decide: add a Textarea component or handle `input_type="textarea"` in Input.
   - Files: `src/faststrap/components/forms/input.py`, `examples/01_getting_started/simple_form.py`, `examples/03_real_world_apps/blog/app.py`, `examples/05_examples/modern_dashboard.py`.

2. **Tabs can render multiple active tabs**
   - First tab auto-activated even if later item is explicitly active.
   - Fix by pre-scan for explicit active, then apply fallback only when none are set.
   - File: `src/faststrap/components/navigation/tabs.py`.

3. **Carousel/Modal ID collisions across multiple instances**
   - Stable IDs are based on limited signatures; duplicates likely for repeated structures.
   - Include item content hash or a deterministic counter in addition to signature fields.
   - Files: `src/faststrap/components/display/carousel.py`, `src/faststrap/components/feedback/modal.py`.

4. **Examples use invalid Card API**
   - `Card(body=...)` is not supported.
   - Update examples to pass children directly or add a `body` convenience parameter.
   - Files: `examples/demo_all.py`, `examples/phase4a_demo.py`.

5. **Button-as-link misuse in examples**
   - `Button(..., href=...)` without `as_="a"` creates invalid HTML.
   - Update examples to use `as_="a"` or `A(...)`.
   - Files: `examples/03_real_world_apps/blog/app.py`, `examples/ecommerce.py`, `examples/templates/dashboard/main.py`, `examples/showcase/portfolio_standard.py`.

---

## P2 Medium Priority (Quality & Consistency)
1. **Encoding corruption in docs/examples**
   - Replace garbled characters (e.g., `Â©`, `â€¢`, `ðŸ…`) with correct Unicode.
   - Files: widespread in `README.md`, `ROADMAP.md`, examples, showcases.

2. **Pagination glyphs corrupted**
   - Replace `Â«`, `â€¹` etc with proper characters.
   - File: `src/faststrap/components/navigation/pagination.py`.

3. **`Progress` divide-by-zero**
   - Guard `max_value=0` and define consistent behavior.
   - File: `src/faststrap/components/feedback/progress.py`.

4. **`Drawer.footer_cls` unused**
   - Either remove parameter or implement a footer slot.
   - File: `src/faststrap/components/navigation/drawer.py`.

5. **`convert_attrs` drops `aria_*` False values**
   - Current behavior contradicts changelog notes.
   - Reconcile behavior and update tests/docs.
   - File: `src/faststrap/utils/attrs.py`.

6. **Version mismatch risk**
   - `__version__` is hardcoded but package uses VCS dynamic version.
   - Decide on single source of truth.
   - Files: `src/faststrap/__init__.py`, `pyproject.toml`.

---

## Documentation & Release Hygiene
1. **README/ROADMAP parity**
   - Fix built-in theme list (remove `dark-mode`/`light-mode` unless added).
   - Update component count and surface areas to match current code.
   - Files: `README.md`, `ROADMAP.md`, `ROADMAP_EXPANDED.md`.

2. **llms.txt freshness**
   - Update to v0.5.9+ or remove if not maintained.
   - File: `llms.txt`.

3. **Registry coverage**
   - Apply `@register(category=..., requires_js=...)` to missing components.
   - Ensures `add_bootstrap(components=[...])` works reliably.
   - Files: `src/faststrap/components/**`.

4. **Examples alignment**
   - Ensure examples match current API signatures and run without warnings.
   - Files: `examples/**` and `showcase/**`.

---

## v0.6.0 Scope Sanity Check
The roadmap lists DataTable/Chart/Metric cards for v0.6.0, but no implementation exists yet (`src/faststrap/components/advance/README.md` is placeholder). Decide one:
- **Option A:** Implement minimum viable DataTable + Chart wrappers.
- **Option B:** Re-scope v0.6.0 as stabilization + docs + refactor release.

---

## Execution Order (Recommended)
1. Fix SearchableSelect (P0)
2. Fix ErrorPage icon pipeline (P0)
3. Fix broken examples (theme, Input textarea, Card body, Button href)
4. Fix Tabs active logic + ID collisions
5. Repair encoding + pagination glyphs
6. Align docs/README/llms.txt
7. Complete registry coverage
8. Re-run tests, cut release notes

---

## Appendix A — Sonnet 4.6 Findings (verbatim)

"Let me gather the remaining deep details before writing my findings.Now I have everything I need for a thorough, deep analysis. Let me write it up.Now I have the full picture. Let me write the comprehensive findings.Here is my full deep-dive findings report:

---

## Faststrap: Deep Technical Analysis

### What the README Doesn't Tell You

The README describes Faststrap as "38 components." That's already two major versions out of date. The actual current state at v0.5.9 is **70 production components**, 646 passing tests, and a surface area that goes far beyond a component library. Here's what's actually under the hood.

---

### 1. The True Architecture (6 distinct layers)

Faststrap is not just a component library — it's a full Python web app toolkit built on FastHTML. By looking at the actual source structure, you can see it's organized into six coherent layers:

**Core runtime** (`core/`) — `assets.py` alone is a production-grade asset manager with thread-safe mounting, SRI hash support, CDN version-pinning to jsDelivr GitHub CDN (using your installed package version), a duplicate-call guard, and a `components` parameter that lets you selectively opt out of Bootstrap JS injection for lightweight pages. `effects.py` exposes an `Fx` class with 30 named CSS animation tokens (`Fx.hover_lift`, `Fx.shimmer`, `Fx.glass`, etc.) — all zero-JS, declared entirely in a custom `faststrap-fx.css` bundled with the package.

**Component registry** (`core/registry.py`) — Every component that calls `@register(category=..., requires_js=...)` is indexed at import time via lazy autodiscovery. You can call `list_components(category="feedback")` at runtime to get every JS-dependent component for conditional Bootstrap JS loading. This is genuinely novel for a component library.

**Stability contract** (`core/_stability.py`) — Three decorators `@stable`, `@beta`, `@experimental` mark every public function. `DashboardLayout` is `@beta`. `MapView` is `@experimental`. `Button` has no marker (implied stable). This is a real API versioning promise, not decoration.

**Presets module** (`presets/`) — This is almost entirely undocumented in the README. It has 14 helpers across three files: `interactions.py` has `ActiveSearch`, `InfiniteScroll`, `AutoRefresh`, `LazyLoad`, `LoadingButton`, `OptimisticAction`, and `LocationAction`. `responses.py` has `hx_redirect`, `hx_refresh`, `hx_trigger`, `hx_reswap`, `hx_retarget`, and `toast_response`. `auth.py` has `require_auth` — a full decorator that guards FastHTML routes with session-based auth, supporting async and sync handlers, with `next=` redirect param support. **None of these appear meaningfully in the README.**

`OptimisticAction` is particularly sophisticated — it fires three custom events (`faststrap:optimistic:apply`, `faststrap:optimistic:commit`, `faststrap:optimistic:rollback`) with a full detail payload including `actionId`, `endpoint`, `method`, `target`, and reason, hooking into HTMX's `before-request`, `after-request`, `response-error`, and `send-error` event lifecycle. It's a complete optimistic UI pattern without a single line of custom JavaScript from the user.

**SEO module** (`seo/`) — `SEO()` generates a full tuple of meta tags: basic, Open Graph (with article/product modes), Twitter Cards with all four card types, `robots`, `canonical`, `hreflang` alternates, and article-specific `published_time`/`modified_time`/`tags`. `StructuredData` generates JSON-LD for Article, Product (with AggregateRating), BreadcrumbList, Organization, and LocalBusiness Schema.org types. This is genuinely production-ready SEO tooling, not decorative.

**PWA module** (`pwa/`) — `add_pwa()` wires a full service worker with network-first navigation, stale-while-revalidate for static assets, `Promise.allSettled`-based pre-cache, old cache cleanup, configurable `route_cache_policies` per URL pattern, background sync scaffolding, and push notification scaffolding. The service worker is rendered from a Python template — you pass `pre_cache_urls`, `cache_version`, `enable_background_sync`, even `route_cache_policies: dict[str, str]` to tune which URLs get which caching strategy.

---

### 2. Undocumented Components You Won't Find in the README

Beyond the phase tables in the README, the `__init__.py` exports reveal these that aren't surfaced:

`Sheet` — a mobile-native bottom sheet (wraps `Drawer` with `placement="bottom"`, `rounded-top-4`, `max-height: 90vh`). `BottomNav` + `BottomNavItem` — mobile bottom navigation bars. `GlassNavbar` + `GlassNavItem` — glassmorphism navbar with configurable `blur_strength` ("low"/"medium"/"high") and `transparency` (0.0–1.0). `SidebarNavbar` + `SidebarNavItem` — a collapsible sidebar nav. `Scrollspy` — auto-updates nav links based on scroll position. `Carousel` + `CarouselItem`. `Placeholder`, `PlaceholderButton`, `PlaceholderCard` — Bootstrap loading skeleton components. `InstallPrompt` — A2HS (Add to Home Screen) prompt for PWA installs. `ErrorPage`, `ErrorDialog`, `ErrorToast` — full error state components. `TextClamp` — truncates long text with a JavaScript-free show-more toggle, driven entirely by `data-fs-*` attributes handled in the init script. `ToggleGroup` — single-active button group with a hidden input for form submission, zero JS. `SearchableSelect` — server-side HTMX-powered dropdown with `min_chars`, `debounce`, `csp_safe` mode (avoids inline click handlers for strict CSP environments), and stable ID generation via SHA-1 hash of props. `ThemeToggle` — light/dark switcher wired to an HTMX endpoint.

**Data bridges** (beta, v0.5.9): `Form.from_pydantic(model_class, *, action, include, exclude, submit_label...)` — introspects Pydantic model fields at runtime, maps `bool` → checkbox, `Literal[...]` → select, `Enum` → select with enum values, `Optional[X]` → non-required. Maps field `description` to `FormGroup` help text. `Table.from_df(data, *, columns, max_rows, include_index, header_map, ...)` — works with pandas or polars DataFrames, validates column existence and `max_rows` eagerly.

`MapView` — embeds a Leaflet.js map (CDN-first, experimental). Validates lat/lon/zoom ranges with clear `ValueError`s. Returns a tuple of `(Link CSS, Script JS, Div container, Script init)`. `Markdown` — renders Markdown to HTML with optional `bleach` sanitization, configurable `allowed_tags`, `allowed_attributes`, `allowed_protocols`, and optional Python-Markdown extensions.

---

### 3. Three-Layout System (Almost Entirely Hidden)

`DashboardLayout`, `AuthLayout`, and `LandingLayout` are full-page layout presets. `DashboardLayout` builds a complete admin panel: responsive sidebar, sticky top navbar, breadcrumbs slot, user dropdown slot, fluid main content, optional footer, `sidebar_width` control, and `theme` (light/dark). `AuthLayout` builds a centered card login/register page with logo, brand name, subtitle, form, and footer link. These are the kind of scaffolding a developer would spend an hour writing — they're in the box, marked `@beta`.

---

### 4. Developer Experience Tooling

`faststrap doctor` is a CLI diagnostic tool (`faststrap doctor --path .`) that scans your project files and reports: missing `add_bootstrap()` calls, `use_cdn=True` missing in detected serverless environments (Vercel, AWS Lambda, Cloud Run), `serve()` usage in serverless (which breaks), `mount_assets()` path conflicts, `toast_response()` without a `ToastContainer`, `ActiveSearch` missing `target=`, and FastHTML version mismatches against your `pyproject.toml`. This is the kind of tooling that differentiates a mature library from a set of helpers.

`set_component_defaults("Button", variant="outline-primary")` lets you globally change defaults for any component — with a `RuntimeWarning` if you call it after requests have started, and a `reset_component_defaults()` to undo it.

`llms.txt` is present at the repo root — a structured summary for LLM context injection (though it's slightly stale at v0.5.4 data).

---

### 5. What's Actually Tested

The test suite at 642+ tests is real and substantive. There are dedicated test files for `test_seo_structured_data.py`, `test_pwa.py`, `test_cli.py`, `test_accessibility.py`, `test_presets.py`, `test_map_view.py`, `test_form_builder.py`, `test_table_from_df.py`, `test_searchable_select.py`. The conftest fixtures inject `to_xml` rendering so tests assert actual HTML output. The coverage gap (~25% per the XML) is mostly in the static files and some edge paths — the core component logic is well-covered.

---

### Recommendations

**Documentation is the biggest gap.** The actual public API as exported by `__init__.py` is roughly 3× larger than what the README describes. The presets module (`require_auth`, `OptimisticAction`, `toast_response`, `hx_trigger`, etc.) is one of the most practically useful parts of the library and nearly invisible. A dedicated "Presets & HTMX patterns" doc page would unlock significant value.

**`llms.txt` is stale.** It references v0.5.4 and 67 components. Keeping this accurate matters because it's what LLM code assistants use when someone asks "how do I use Faststrap" — incorrect context leads to hallucinated APIs.

**Registry coverage is incomplete.** Only 16 of 70 components are decorated with `@register(...)`. The registry exists to enable features like conditional JS injection via `add_bootstrap(app, components=[...])`, but it can only work reliably if components are actually registered. The `@register` decorator should be applied consistently.

**`DashboardLayout` has a UX gap.** The sidebar uses Bootstrap collapse via `data-bs-toggle` but the toggle button targets the sidebar `id` directly — it won't work correctly with Bootstrap's offcanvas on mobile without explicit JS init. Given that it's `@beta`, a note about this in the docstring would prevent confusion.

**`Form.from_pydantic()` and `Table.from_df()` are beta gems.** These have the potential to be significant value drivers for the FastHTML + Pydantic crowd. The implementation is solid but they need dedicated example apps and docs. `Form.from_pydantic()` already handles `Optional`, `Enum`, `Literal`, `bool`, `EmailStr`, `float`, and defaults — that's a lot of coverage for a beta.

---

### What I Would Contribute

If I were contributing to Faststrap, here's where I'd focus:

**1. `DataTable` component with server-side contract.** The roadmap mentions this but it doesn't exist yet. A `DataTable` that accepts an `endpoint`, renders headers, and handles sort/filter/pagination via HTMX query params — with a standardized server response format — would be the most impactful single addition. The plumbing (HTMX, presets, `Table.from_df`) already exists.

**2. A `Notification` / `NotificationCenter` preset.** Using the existing `toast_response` + `ToastContainer` + `hx_trigger` primitives, a higher-level notification system with persistence (session or DB-backed) and a bell-icon dropdown would be a natural composition.

**3. Complete `@register` coverage.** Audit all 70 components and add `@register(category=..., requires_js=...)` to every one. This makes the registry the authoritative source of truth and enables `add_bootstrap(app, components=[...])` to actually conditionally skip JS for pages that don't need it.

**4. `SSEStream` preset.** The roadmap flags this as a v0.6.1 target. An `SSEStream` helper that wraps Starlette's `EventSourceResponse` with a Faststrap-compatible response format — and an `SSETarget` component on the client side that connects to it — would be a natural fit given how well the HTMX/Python model already works here.

**5. Fix `llms.txt` and document the presets module properly.** Not glamorous, but these two changes would probably have the highest ratio of developer-hours saved per line written.

---

Overall, Faststrap is significantly more capable than its README suggests. The architecture is clean, the stability contract is real, and the presets/SEO/PWA modules are production-quality additions that most comparable libraries don't have. The main work ahead is documentation parity with the actual codebase."
