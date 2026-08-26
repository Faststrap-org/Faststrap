# Faststrap Examples

A structured collection of production-ready, runnable examples for every Faststrap component and pattern.
Start from `01_quickstart/` and work your way down — each tier builds on the previous one.

## Running any example

```bash
cd examples/<folder>
python <file>.py
# Open http://localhost:5001
```

---

## Folder Map

```
examples/
├── 01_quickstart/          ← START HERE: minimum viable Faststrap apps
├── 02_layout/              ← Grid, Stack, Cluster, DashboardGrid, AspectRatio, Parallax
├── 03_forms/               ← All inputs, addons, radios, sliders, validation, wizards
├── 04_data_display/        ← Cards, tables, badges, timelines, SVG, code blocks
├── 05_navigation/          ← Navbars, GlassNavbar, SidebarNavbar, overlays, search
├── 06_feedback/            ← Alerts, toasts, spinners, loaders, skeletons, progress
├── 07_htmx_patterns/       ← HTMX-first interaction patterns, headers, and SSE
├── 08_themes_motion/       ← Themes, dark mode, animations, GSAP, a11y
├── 09_integrations/        ← Charts, maps, SEO, PWA
├── 10_page_templates/      ← Full-page layouts (auth, marketing, dashboard)
└── 11_real_world_apps/     ← Fully functional mini-apps
```

---

## What to run by goal

| I want to... | Start with |
|---|---|
| See Faststrap in 5 lines | `01_quickstart/hello_world.py` |
| Build forms with addons & validation | `03_forms/input_groups.py` or `03_forms/form_sections_validation.py` |
| Create a responsive metric dashboard | `02_layout/dashboard_grid.py` |
| Build a glassmorphism or sidebar app shell | `05_navigation/glass_sidebar_nav.py` |
| Add skeleton loading states | `06_feedback/skeletons_placeholders.py` |
| Add dark mode & color themes | `08_themes_motion/dark_mode.py` |
| Trigger HTMX server events | `07_htmx_patterns/header_triggers.py` |
| Add GSAP entrance motion | `08_themes_motion/motion.py` |
| Build an auth flow | `10_page_templates/auth_pages.py` |
| Explore a full production app | `11_real_world_apps/ecommerce/app.py` |

---

## Tier 1 — Quickstart (`01_quickstart/`)

| File | Demonstrates |
|---|---|
| `hello_world.py` | `FastHTML`, `add_bootstrap`, `Navbar`, `Container` |
| `first_card.py` | `Card`, `Button`, `Badge`, `Row`, `Col` |
| `first_form.py` | `Input`, `Select`, `FormGroup`, `Button` |
| `adding_htmx.py` | `hx_post`, `hx_target`, `hx_swap`, live updates |
| `first_app.py` | A complete starting point |

## Tier 2 — Component Galleries

### `02_layout/`
| File | Demonstrates |
|---|---|
| `containers.py` | `Stack`, `Cluster`, `Center`, `Separator` |
| `dashboard_grid.py` | `DashboardGrid` (auto-fill responsive metric grid) |
| `page_sections.py` | `PageHeader`, `SectionHeader`, `AspectRatio` |
| `parallax_hero.py` | `ParallaxSection` (CSS-only parallax background) |
| `split_switcher.py` | `SplitPane`, `Switcher` |

### `03_forms/`
| File | Demonstrates |
|---|---|
| `form_components.py` | `FormGroup`, `ThemeToggle`, `SearchableSelect` |
| `input_groups.py` | `InputGroup`, `InputGroupText`, `Radio`, `Range` |
| `form_sections_validation.py` | `FormSection`, `FormErrorSummary`, `FormBuilder`, `extract_field_error`, `map_formgroup_validation` |
| `otp.py` | `OTPInput`, `OTPInputGroup` |
| `date_pickers.py` | `CalendarDatePicker`, `DateRangePicker` |
| `advanced_buttons.py` | `GradientButton`, `FloatingActionButton`, `CloseButton`, `PlaceholderButton` |

### `04_data_display/`
| File | Demonstrates |
|---|---|
| `data_foundations.py` | `DataTable`, `StatCard`, `ResultCard` |
| `visual_cards.py` | `FlipCard`, `TiltCard`, `RevealCard`, `GlowCard` |
| `record_detail.py` | `KeyValueList`, `RecordDetail`, `JsonViewer` |
| `code_content.py` | `CodeBlock`, `Mermaid`, `Tag`, `Kbd` |
| `svg_display.py` | `Svg`, `render_svg`, `VisuallyHidden`, `datatable_page_url`, `datatable_export_params` |
| `display_extras.py` | `Stepper`, `Timeline`, `Carousel` |
| `component_wave.py` | `Tabs`, `Accordion`, `Modal`, `Drawer` |

### `05_navigation/`
| File | Demonstrates |
|---|---|
| `nav_showcase.py` | `Navbar`, `Breadcrumb`, `Pagination`, `Dropdown` |
| `glass_sidebar_nav.py` | `GlassNavbar`, `GlassNavItem`, `SidebarNavbar`, `SidebarNavItem`, `Scrollspy` |
| `full_nav_tour.py` | `SidebarNavbar`, `GlassNavbar`, `CommandPalette` |
| `search_profile.py` | `SearchBar`, `ProfileDropdown` |
| `tooltips_popovers.py` | `Tooltip`, `Popover` |

### `06_feedback/`
| File | Demonstrates |
|---|---|
| `loaders.py` | All 7 loaders (`DotsLoader`, `PulseLoader`, `RingLoader`, etc.) + `ProgressRing` |
| `skeletons_placeholders.py` | `Placeholder`, `PlaceholderCard`, `PlaceholderButton`, `SimpleToast` |
| `toasts_extended.py` | `ErrorToast`, `NoticeToast`, `NoticeAlert` |
| `error_pages.py` | `ErrorPage` (404, 500 templates) |
| `error_dialogs.py` | `ErrorDialog`, `ConfirmDialog` |
| `accessibility_presets.py` | `LiveRegion`, `FocusTrap`, `SkipLink`, `ToggleGroup`, `TextClamp` |

### `07_htmx_patterns/`
| File | Demonstrates |
|---|---|
| `interactions.py` | `ActiveSearch`, `InfiniteScroll`, `LazyLoad`, `AutoRefresh` |
| `search_filter.py` | `Debounce`, `SwapOnEvent`, `ConfirmPrompt`, `PollUntil` |
| `header_triggers.py` | `hx_trigger`, `hx_reswap`, `hx_retarget`, `sse_comment` |
| `responses.py` | `toast_response`, `hx_redirect`, `hx_refresh`, `require_auth` |
| `sse_streaming.py` | `SSETarget`, `SSEStream`, `sse_event` |
| `workflow_patterns.py` | `LoadingButton`, `OptimisticAction`, `LocationAction` |
| `pattern_components.py` | `InfiniteScroll`, `ScrollSpy` patterns |

### `08_themes_motion/`
| File | Demonstrates |
|---|---|
| `builtin_themes.py` | All 10 built-in themes |
| `custom_theme.py` | CSS custom property theme overrides |
| `dark_mode.py` | `mode="dark"`, `ThemeToggle` |
| `animations.py` | `Fx` animation utilities |
| `motion.py` | `Motion`, `MotionPreset`, `GsapPreset` |
| `gsap_motion.py` | `Gsap`, `GsapReveal` integrations |
| `math_demo.py` | `Math` (LaTeX rendering) |
| `theme_adapted.py` | Theme-adaptive components |

### `09_integrations/`
| File | Demonstrates |
|---|---|
| `seo.py` | `SEO`, `PageMeta`, `StructuredData` |
| `pwa.py` | `PwaMeta`, `InstallPrompt` |
| `pwa_demo.py` | Full PWA with offline support |

## Tier 3 — Page Templates (`10_page_templates/`)

| File | Use case |
|---|---|
| `auth_pages.py` | Login, Register, Reset Password |
| `marketing_landing.py` | Hero, Features, Pricing, Testimonials |
| `saas_landing.py` | SaaS landing page with CTA sections |
| `dashboard_template.py` | Admin dashboard layout |
| `patterns_demo.py` | Common UI patterns |

## Tier 4 — Real-World Apps (`11_real_world_apps/`)

| App | Description |
|---|---|
| `blog/` | Multi-page blog with create/read |
| `calculator/` | Interactive calculator with HTMX |
| `game/` | Simple browser game |
| `ecommerce/` | Product listing, cart, checkout |
| `saas_dashboard/` | Full SaaS admin dashboard |
| `admin_dashboard/` | Admin panel with data tables |
| `portfolio_standard/` | Developer portfolio (standard) |
| `portfolio_premium/` | Developer portfolio (premium) |
| `saas_landing/` | Full SaaS marketing site |
| `dashboard_template/` | Copy-paste dashboard starter |
| `landing_template/` | Copy-paste landing page starter |
