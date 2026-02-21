# Changelog

All notable changes to Faststrap will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.6.post2] - 2026-02-21

### Changed

- Untracked generated coverage artifact (`coverage.xml`) from the repository root.
- Added CI guardrails to fail builds when generated/debug artifact files are tracked in commits.
- Bumped package version marker to `0.5.6.post2` for this maintenance patch.
- Added release-process tracking sections:
  - contributor release checklist
  - roadmap implementation-tracking notes for agreed follow-ups
- Refreshed docs/roadmap status metadata to reduce version/metrics drift.

### Quality

- Re-ran formatting, linting, type checks, and full test suite before tagging.

## [0.5.6.post1] - 2026-02-20

### Changed

- Harmonized release documentation between `README.md` and `ROADMAP.md` to reflect what is already shipped vs deferred after v0.6.
- Added explicit suggested release-cut sequence:
  - `v0.5.6`: accessibility + toggle group + text clamp + notification presets
  - `v0.5.7`: PageMeta + form error mapper
  - `v0.5.8`: doctor CLI + docs/version/changelog consistency cleanup
  - `v0.6.0`: broader milestone after markdown/location decisions
- Updated roadmap status labels to align with the current pre-v0.6 planning view.

### Quality

- Re-ran formatting, linting, type checks, and full test suite before finalizing this patch release.

## [0.5.6] - 2026-02-20

### Added

- **Accessibility module (`faststrap.accessibility`)**:
  - `SkipLink`
  - `VisuallyHidden`
  - `LiveRegion`
  - `FocusTrap`
- **Single-active group component**:
  - `ToggleGroup` for sort/tab/filter style button groups
- **Long text utility component**:
  - `TextClamp` with optional expandable/collapsible button
- **Notification presets** on top of existing feedback components:
  - `NoticeToast`, `NoticeAlert`
  - `SuccessToast`, `ErrorToast`, `WarningToast`, `InfoToast`
- **Head/meta composer**:
  - `PageMeta` for SEO + canonical + optional PWA/favicon composition with dedupe
- **Form validation bridge**:
  - `extract_field_error`, `map_formgroup_validation`, `FormGroupFromErrors`
- **CLI support**:
  - `faststrap` entrypoint
  - `faststrap doctor` diagnostics command

### Documentation

- Added docs for accessibility helpers, doctor CLI, ToggleGroup, TextClamp, notification presets, and PageMeta.
- Added feature demo app: `examples/05_new_components/pre_v060_features.py`.

### Quality

- Added focused tests for all new modules and integrations.

## [0.5.4] - 2026-02-11

### Added

**New Module: `faststrap.presets`** - HTMX interaction patterns and server-side response helpers

- **Interaction Presets** (5 components):
  - `ActiveSearch` - Live search with debounced server requests
  - `InfiniteScroll` - Infinite feed loading on scroll
  - `AutoRefresh` - Auto-polling for live updates
  - `LazyLoad` - Lazy-loaded content blocks
  - `LoadingButton` - Button with automatic loading state
- **Response Helpers** (6 functions):
  - `hx_redirect()` - Client-side redirect via HX-Redirect header
  - `hx_refresh()` - Full page refresh
  - `hx_trigger()` - Trigger client-side events
  - `hx_reswap()` - Change swap strategy dynamically
  - `hx_retarget()` - Change target element dynamically
  - `toast_response()` - Return content + out-of-band toast
- **Auth Decorator**:
  - `@require_auth` - Session-based route protection

**Error Handling Components** (2 components):

- `ErrorPage` - Full-page error displays for 404, 500, 403, and custom errors
  - Returns `(Title, Div)` tuple for FastHTML routes
  - Supports backend error messages
  - Customizable titles, icons, and action buttons
- `ErrorDialog` - Modal error displays with retry actions
  - HTMX out-of-band swap support
  - Backend error message integration
  - Variant support (danger, warning, info)

**Form Enhancements** (3 components):

- `FormGroup` - Wraps inputs with labels, help text, and validation feedback
  - Automatic validation state handling
  - Required field indicators
  - Error and success message display
- `ThemeToggle` - Dark/light mode toggle with HTMX server-side persistence
  - Bootstrap switch styling with icon indicators
  - Session/cookie/database persistence support
  - Optional label display
- `SearchableSelect` - Server-side searchable dropdown using HTMX
  - Replaces Select2/Choices.js with pure HTMX
  - Debounced search
  - Initial options support

**Pattern Components** (3 components):

- `FooterModern` - Multi-column footer with branding, links, social icons
  - Responsive grid layout
  - Customizable background and text variants
  - Dynamic link generation support
- `Testimonial` - Customer testimonial card with avatar and rating
  - Star rating display
  - Avatar image support
  - Role/title display
- `TestimonialSection` - Testimonial grid section with title
  - Configurable column count
  - Section title and subtitle
  - Responsive layout

**Layout Components** (1 component):

- `AuthLayout` - Centered authentication page layout
  - Branding and logo support
  - Form field integration
  - Footer links for navigation
  - HTMX compatible

### Changed

- **Restructured `components/patterns/`** - Converted from single file to package directory
  - Extracted `FooterModern` to `patterns/footer.py`
  - Extracted `Testimonial` and `TestimonialSection` to `patterns/testimonial.py`
  - Extracted `NavbarModern` to `patterns/navbar.py`
  - Extracted `Feature` and `FeatureGrid` to `patterns/feature.py`
  - Extracted `PricingTier` and `PricingGroup` to `patterns/pricing.py`
  - Fixed Korean docstring issue in patterns module

### Documentation

- **Added comprehensive component documentation** (8 new docs):
  - `docs/components/feedback/error-page.md` - ErrorPage usage guide
  - `docs/components/feedback/error-dialog.md` - ErrorDialog usage guide
  - `docs/components/forms/formgroup.md` - FormGroup usage guide
  - `docs/components/forms/theme-toggle.md` - ThemeToggle usage guide
  - `docs/components/forms/searchable-select.md` - SearchableSelect usage guide
  - `docs/components/patterns/footer-modern.md` - FooterModern usage guide
  - `docs/components/patterns/testimonial-section.md` - TestimonialSection usage guide
  - `docs/layouts/auth.md` - AuthLayout usage guide
  - `docs/api/presets.md` - Presets module API reference
  - `docs/api/seo.md` - SEO module API reference
  - `docs/components/seo/meta.md` - SEO Meta usage guide
  - `docs/components/seo/structured-data.md` - SEO StructuredData usage guide
- All documentation includes live previews, use cases, integration patterns, and best practices

### Testing

- **Added 107 new tests** for v0.5.4 components
  - 23 tests for SEO Meta component
  - 15 tests for SEO StructuredData helper
  - 15 tests for ErrorPage
  - 11 tests for ErrorDialog
  - 10 tests for FormGroup
  - 10 tests for ThemeToggle
  - 9 tests for SearchableSelect
  - 14 tests for pattern components
- All 426 existing tests continue to pass

### Summary

**Component Count:** 51 → 67 (+16 components)  
**Module Count:** 5 → 7 (+2 modules: `presets`, `seo`)  
**Release Theme:** "SEO, Interaction Presets & Error Handling"

This release dramatically improves the developer experience with ready-to-use SEO tools, HTMX patterns, comprehensive error handling, and essential form enhancements. The new `faststrap.seo` and `faststrap.presets` modules are killer features that eliminate boilerplate for common web tasks.

---

## [0.5.3] - 2026-01-18

### Fixed

- **Bug #1**: Eliminated duplicate component defaults code in `core/theme.py`
  - Extracted defaults to `_DEFAULT_COMPONENT_DEFAULTS` constant
  - Reduced code duplication by 30 lines
  - Improved maintainability and consistency
- **Bug #2**: Fixed non-deterministic navbar IDs in `components/navigation/navbar.py`
  - Replaced `random.randint()` with deterministic counter
  - Enables consistent HTML output for snapshot testing
  - Better debugging experience
- **Bug #3**: Fixed Google Fonts URL encoding in `core/assets.py`
  - Now uses `urllib.parse.quote()` for proper URL encoding
  - Handles font names with spaces and special characters correctly
  - Standards-compliant font loading
- **Bug #4**: Improved registry autodiscovery error handling in `core/registry.py`
  - Safe attribute access using `getattr()` with fallback
  - Better error messages for malformed modules
  - More robust component discovery

### Documentation

- **Added**: Comprehensive docstring for `BaseComponent` class
  - Explains purpose for advanced users and third-party libraries
  - Includes usage examples for stateful components
  - Clarifies when to use class-based vs function-based components
- **Added**: README for `components/advance/` directory
  - Documents planned advanced components (DataTable, Chart, etc.)
  - Explains future roadmap for data science features
- **Added**: Component documentation for:
  - `Carousel` and `CarouselItem` - Image slideshow component
  - `Image` - Responsive image utilities
  - `Scrollspy` - Auto-updating navigation
  - `InstallPrompt` - PWA installation prompt

### Roadmap

- **Updated**: Phase 6 roadmap with comprehensive data science vision
  - v0.6.0: Data Foundations (DataTable, Chart, DataFrame integration)
  - v0.6.1: Advanced Data Components (Dashboards, Filters, Visualizations)
  - v0.6.2: Real-time & ML Integration (Live updates, Model metrics)
  - v0.6.3: Productivity & Polish (Pydantic forms, HTMX presets)
- **Added**: Competitive positioning vs Streamlit, Dash, and Panel
- **Added**: Target audience definition for data scientists and analysts

### Quality

- ✅ All 426 tests passing
- ✅ Ruff linting passed (0 errors)
- ✅ Mypy type checking passed (64 files)
- ✅ Black formatting applied
- ✅ 100% backward compatible (no breaking changes)

## [0.5.2] - 2026-01-18

### Added

- **PWA Support (`faststrap.pwa`)**: New module to make Faststrap apps installable.
  - `add_pwa()` helper for one-line PWA setup.
  - `PwaMeta` component for iOS/Android meta tags.
  - Automatic `manifest.json` generation.
  - Generic "Network-First" Service Worker (`sw.js`).
- **Mobile Components**:
  - `BottomNav` and `BottomNavItem` for mobile app navigation.
  - `Sheet` (Bottom Drawer) for modern mobile menus.
  - `InstallPrompt` for guiding users to install the app.
- **Documentation**: New `docs/PWA_GUIDE.md`.

## [0.5.1] - 2026-01-17

### Added

- **`mount_assets()` Helper Function**: Simplified static file mounting for user assets
  - Smart path resolution (handles relative and absolute paths automatically)
  - Auto-detects caller's directory using stack inspection
  - Validates directory exists before mounting
  - Auto-generates mount names from URL paths
  - Support for multiple directories with custom URL paths
  - Priority control for route ordering
  - Example: `mount_assets(app, "assets")` - one line instead of five!

### Fixed

- **CSS Bug**: Removed duplicate `animation` property in `.toast-fade-out` class (lines 90-91 in `core/assets.py`)
  - This duplicate could cause CSS parsing issues in some browsers
  - No functional impact, but improves code quality

### Documentation

- Added comprehensive examples for `mount_assets()` in function docstring
- Improved code quality: All tests passing (423 tests), ruff ✅, black ✅, mypy ✅

## [0.5.0] - 2026-01-16

### Added

- **Phase 5: Composed UI & Design System Layer**
  - **Image**: Responsive images with fluid, thumbnail, rounded, rounded circle, and alignment utilities
    - Lazy loading support with `loading="lazy"`
    - Dimension control with `width` and `height`
    - Accessibility with `alt` text
  - **Carousel**: Auto-play image sliders with controls, indicators, and fade transitions
    - `CarouselItem` component for individual slides with captions
    - Configurable interval, keyboard navigation, pause on hover
    - Dark variant for controls and indicators
  - **Placeholder**: Skeleton loading screens with glow/wave animations
    - `PlaceholderCard` - Pre-built card skeleton
    - `PlaceholderButton` - Button-shaped placeholder
    - Configurable size, color variants, and animations
  - **Scrollspy**: Auto-updating navigation based on scroll position
    - Offset configuration for fixed navbars
    - Smooth scroll support
    - Method configuration (auto, offset, position)
  - **SidebarNavbar**: Premium vertical sidebar for dashboards
    - `SidebarNavItem` component for individual items
    - Icon support with Bootstrap Icons
    - Light/dark themes, sticky positioning
    - Configurable width and collapsible mobile support
  - **GlassNavbar**: Premium glassmorphism navbar with blur and transparency
    - `GlassNavItem` component for individual items
    - Configurable blur strength (low, medium, high)
    - Transparency control (0.0-1.0)
    - Safari support with -webkit-backdrop-filter
  - **FeatureGrid**: Grid layout for feature sections (Pattern component)
  - **PricingGroup**: Horizontal pricing tier layout (Pattern component)

### Fixed

- **Critical Bug**: Fixed static file mounting issue with `fast_app()` where Bootstrap CSS and JS files returned 404 errors
  - Removed faulty `is_mounted()` check that prevented static files from mounting
  - Static files now mount correctly with both `FastHTML()` and `fast_app()` initialization patterns
  - Added error handling for duplicate mount attempts
  - **Impact**: Developers can now use `fast_app()` without workarounds

### Changed

- Component count: 45 → 51 components
- Updated examples with `phase5_demo.py` showcasing all new components
- Documentation updated to reflect Phase 5 completion

## [0.4.6] - 2026-01-03

### Added

- **Documentation Completion (95% Coverage)**:
  - Created 18 new component documentations (Select, Dropdown, Spinner, Progress, Breadcrumb, Pagination, Accordion, InputGroup, FloatingLabel, ButtonGroup, ListGroup, Drawer, Icon, Collapse, Effects, DashboardLayout, LandingLayout)
  - All docs include Bootstrap CSS class guides, HTMX integration examples, `set_component_defaults` usage, responsive design patterns, and accessibility best practices
  - Total: 43/45 components documented (NavbarModern and ConfirmDialog pending)
  
- **Examples Reorganization**:
  - Created new organized structure: `01_getting_started/`, `02_components/`, `03_real_world_apps/`, `04_advanced/`, `05_integrations/`
  - Comprehensive `examples/README.md` guide with learning paths
  - 4 beginner tutorials: hello_world.py, first_card.py, simple_form.py, adding_htmx.py
  - 3 complete real-world apps: blog (posts, comments, admin), calculator (HTMX-powered), tic-tac-toe game
  - Advanced examples: effects_showcase.py demonstrating all Fx animations

- **Project Files Updated**:
  - README.md: Updated component counts (45 total), documentation coverage stats, examples section
  - CHANGELOG.md: Added v0.4.6 entry
  - All project documentation reflects current state

### Changed

- Component count: 38 → 45 components
- Documentation coverage: 53% → 95%
- Examples: Scattered 28 files → Organized learning path

## [0.4.0] - 2026-01-01

### Added

- **Table** component with `THead`, `TBody`, `TRow`, `TCell`
- **Accordion** and `AccordionItem` components
- **ListGroup** and `ListGroupItem` components
- **Collapse** component
- **InputGroup** with prepend/append addons and `InputGroupText`
- **FloatingLabel** animated form inputs
- **Checkbox**, **Radio**, **Switch** form controls
- **Range** slider input

## [0.4.5] - 2026-02-01

### Added

- **Phase 4B: Enhanced Forms & Feedback**
  - **FileInput**: Enhanced file upload with preview, `multiple`, `accept` support
  - **Tooltip**: Contextual hints with auto-initialization (hover/focus)
  - **Popover**: Rich content overlays with title and content
  - **Figure**: Correctly styled images with captions
  - **ConfirmDialog**: Specialized Modal wrapper for destructive actions
  - **EmptyState**: Visual placeholder for empty data states
  - **StatCard**: Dashboard metric component with trends and icons
  - **Hero**: Jumbotron-style landing page section
- **New Documentation Site**:
  - Full **MkDocs** implementation with searchable API reference
  - Comprehensive "Getting Started" guides and component docs
  - Automated `mkdocstrings` integration for all components
- **Rebranding & Organization Migration**:
  - Migrated to `Faststrap-org` GitHub Organization
  - New **Navy Blue** professional theme with **Lightning Bolt** logo
  - Updated all internal links and asset CDN references

### Planned for Phase 5 (Dashboard & Layouts)

- Sidebar, Footer, DashboardLayout
- FormWizard, Stepper
- DataTable
- Timeline, Carousel, MegaMenu

---

## [0.3.1] - 2025-12-31

### Added

- **Enhanced attribute handling** in `convert_attrs()`:
  - Filter `None` and `False` values
  - Support `style` dict and `css_vars` dict
  - Structured `data={...}` and `aria={...}` dictionaries
- **CloseButton helper** for reusable close buttons in alerts, modals, drawers
- **Expanded Button component**:
  - `as_` to render as `<a>` or `<button>`
  - `full_width`, `active`, `pill` flags
  - `icon_pos`, `icon_cls`, `spinner_pos`, `spinner_cls`, `loading_text`
  - `css_vars` and `style` support
  - Better accessibility for loading state
- **Slot class overrides** for multi-part components:
  - `Card`: `header_cls`, `body_cls`, `footer_cls`, `title_cls`, `subtitle_cls`, `text_cls`
  - `Modal`: `dialog_cls`, `content_cls`, `header_cls`, `body_cls`, `footer_cls`, `title_cls`, `close_cls`
  - `Drawer`: `header_cls`, `body_cls`, `title_cls`, `close_cls`
  - `Dropdown`: `toggle_cls`, `menu_cls`, `item_cls`
- **Registry metadata** enabled for JS-requiring components (`Modal`, `Drawer`, `Dropdown`)
- **Theme layer**:
  - `create_theme()` for custom themes
  - Built-in themes (e.g., `"green-nature"`, `"blue-ocean"`, `"dark-mode"`)
  - Theme integration in `add_bootstrap()` and `get_assets()`
- **Centralized type definitions** in `core/types.py`
- **Component defaults system** with `resolve_defaults()` function
- **Optional IDs** with deterministic UUID generation for `Modal` and `Drawer`
- **Demo app** showcasing all enhancements (`examples/demo_all.py`)

### Changed

- Fixed duplicate assembly bug in `Modal`
- Updated exports in `__init__.py` to include theme utilities
- Improved consistency in close button usage across components
- Bumped version to 0.3.1

### Fixed

- Modal assembly duplication
- Close button class handling in `Alert`, `Modal`, `Drawer`

---

## [0.3.0] - 2025-12-12

### Phase 3 Complete: 8 New Components Added

FastStrap now includes 20 total components.

#### Added - Navigation (4)

- **Tabs**: Navigation tabs and pills with content panes. Support for vertical layout and HTMX mode.
- **Dropdown**: Contextual menus with split button support and directional control ("---" dividers).
- **Breadcrumb**: Navigation trail with icon support and auto-active states.
- **Pagination**: Page navigation with range customization and size variants.

#### Added - Forms (2)

- **Input**: Full HTML5 type support, labels, help text, and ARIA accessibility.
- **Select**: Single/multiple selection modes with default selection support.

#### Added - Feedback (2)

- **Spinner**: Border and grow animation types with color variants.
- **Progress**: Percentage-based bars with striped/animated styles and stacked support.

#### Added - Core Features

- **Centralized `convert_attrs()`**: Consistent HTMX attribute handling (`hx_get` -> `hx-get`).
- **Default Favicon**: Built-in SVG favicon injected automatically via `add_bootstrap()`.

### [0.2.3] - 2025-12-09

#### Added

- **Developer Templates**: Boilerplate for rapid component and test development.
- **Organization**: Components grouped into `forms/`, `display/`, `feedback/`, `navigation/`, and `layout/`.

#### Fixed

- **Critical**: Local Bootstrap assets correctly included in PyPI wheel for offline usage.

### [0.2.2] - 2025-12-09

#### Added

- Interactive demo with HTMX theme toggle and toast triggers.
- Proven zero-JS interactive patterns.

### [0.2.0] - 2025-12-08

First production-ready release with 12 core components.

### [0.1.0] - 2025-12-05

Initial release establishing the foundation.

[0.4.5]: https://github.com/Faststrap-org/Faststrap/compare/v0.4.0...v0.4.5
[0.4.0]: https://github.com/Faststrap-org/Faststrap/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/Faststrap-org/Faststrap/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/Faststrap-org/Faststrap/compare/v0.2.3...v0.3.0
[0.2.3]: https://github.com/Faststrap-org/Faststrap/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/Faststrap-org/Faststrap/compare/v0.2.0...v0.2.2
[0.2.0]: https://github.com/Faststrap-org/Faststrap/compare/v0.1.0...v0.2.0

---

## Semantic Versioning

- **MAJOR**: Breaking changes that require user action
- **MINOR**: New features, enhancements, or non-breaking changes
- **PATCH**: Bug fixes and internal improvements

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.
