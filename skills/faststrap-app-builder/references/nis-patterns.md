# Production app patterns

Use these real user projects as the primary reference set for how FastHTML and Faststrap are combined in production-style apps:

- `C:\Users\Meshell\Desktop\FastHTML\NIS`
- `C:\Users\Meshell\Desktop\FastHTML\Final-Year`
- `C:\Users\Meshell\Desktop\FastHTML\siwes-logbook-automation`

## Read first

- `NIS/main.py`
- `NIS/app/presentation/components/shared/theme.py`
- `NIS/app/presentation/components/ui/layout.py`
- `NIS/app/presentation/routes/landing.py`
- `NIS/app/presentation/routes/auth.py`
- `NIS/app/presentation/assets/css/custom.css`
- `Final-Year/main.py`
- `Final-Year/app/presentation/components/shared/theme.py`
- `siwes-logbook-automation/main.py`
- `siwes-logbook-automation/app/presentation/components/shared/theme.py`
- `siwes-logbook-automation/app/presentation/assets/custom.css`

## Patterns to copy

### App bootstrap

From `NIS/main.py`, `Final-Year/main.py`, and `siwes-logbook-automation/main.py`:

- create `FastHTML(...)` with real app settings
- call `add_bootstrap(app, theme=..., mode=...)`
- call a shared function that sets component defaults
- mount project assets with `mount_assets(...)`
- append project CSS after Faststrap so app-specific polish is easy to control
- wire PWA support only when the product actually needs it
- keep external dependencies minimal and deliberate

### Theme structure

From the shared `theme.py` modules:

- keep brand colors in one shared module
- use `create_theme(...)` for the brand system
- use `set_component_defaults(...)` for consistent app-wide component behavior
- expose color constants for custom layout pieces

### Layout structure

From `layout.py`:

- create dedicated layout helpers for recurring shells such as dashboard, auth, or landing
- keep navigation/layout composition outside page business logic
- use responsive structural wrappers and shared CSS classes for polish

### Presentation architecture

From `routes/`:

- organize routes by area or role
- keep reusable fragments in components modules
- use route setup functions like `setup_*_routes(app)` for modular composition

### Design language

From `landing.py` and `custom.css`:

- combine Faststrap sections/components with custom CSS classes
- layer imagery, overlays, gradients, glassmorphism, and floating cards deliberately
- use typography, spacing, and visual contrast to create hierarchy
- make CTAs obvious and section transitions intentional

## Priority rules extracted from the user's apps

- Bootstrap responsiveness should do most of the structural work.
- HTMX should be the first choice for interactivity.
- Custom CSS should mostly handle polish, brand feel, and the extra visual layer Bootstrap does not provide by itself.
- JavaScript is acceptable when the app genuinely needs it, especially for:
  - PWA/service worker flows
  - browser APIs
  - geolocation/maps
  - richer notifications or background sync
  - other cases HTMX cannot handle cleanly
- Do not treat the presence of JavaScript in SIWES as permission to default to JavaScript in ordinary app work.
- Do not bring in external CSS CDNs as a styling crutch.

## What this means for future builds

When the user asks for a company site, portal, or dashboard with Faststrap:

- do not stop at default component composition
- create a shared theme module
- create shared layouts
- add custom CSS that pushes the design beyond stock Bootstrap
- use the page structure and separation of concerns seen in NIS
- keep layout and responsiveness Bootstrap-first
- keep interactivity HTMX-first
- escalate to JavaScript only when justified by the feature
