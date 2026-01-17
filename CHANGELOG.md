# Changelog

All notable changes to Faststrap will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

## [0.4.0] - 2026-01-01

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

### Phase 3 Complete: 8 New Components Added!
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