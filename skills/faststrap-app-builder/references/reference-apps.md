# Reference apps

When building a Faststrap + FastHTML application, inspect the nearest matching local reference before coding.

## Marketing and company sites

- `Faststrap/examples/showcase/saas_landing.py`
  - use for SaaS/product marketing structure
- `Faststrap/showcase/hotel_booking_showcase.py`
  - use for richer landing-page styling, layered sections, and more intentional visual direction
- `Faststrap/showcase/agency_portfolio.py`
  - use for polished portfolio/agency presentation if that file is relevant to the brief

## Dashboards and internal tools

- `Faststrap/examples/showcase/admin_dashboard.py`
  - use for quick dashboard section composition
- `NIS/app/presentation/components/ui/layout.py`
  - use for real-world dashboard shell structure
- `NIS/app/presentation/routes/hq/dashboard.py`
  - use for an internal admin screen built with custom polish on top of Faststrap
- `Final-Year/main.py`
  - use for a real project bootstrapped with Faststrap theme defaults and route registration
- `Final-Year/app/presentation/components/shared/theme.py`
  - use for another shared theme/defaults pattern in a production-style app

## Auth and onboarding flows

- `NIS/app/presentation/routes/auth.py`
- `NIS/app/presentation/routes/register.py`

Use these when the app needs:

- branded login pages
- multi-step registration
- custom background treatment
- non-generic form presentation

## PWA and browser-API-heavy cases

- `siwes-logbook-automation/main.py`
- `siwes-logbook-automation/app/presentation/components/shared/theme.py`
- `siwes-logbook-automation/app/presentation/assets/custom.css`

Use these when the app needs:

- PWA installability
- offline-first flows
- service worker patterns
- browser capabilities that HTMX alone cannot provide

Even in these cases, do not let the presence of JavaScript pull the whole app away from HTMX-first interaction design.

## Theme and defaults

- `NIS/app/presentation/components/shared/theme.py`
- `Final-Year/app/presentation/components/shared/theme.py`
- `siwes-logbook-automation/app/presentation/components/shared/theme.py`
- `Faststrap/examples/06_examples/01_builtin_themes.py`
- `Faststrap/examples/06_examples/02_custom_themes.py`

## Selection rule

Choose one primary reference and one secondary reference. Do not mash together many unrelated styles unless the user explicitly asks for that.
