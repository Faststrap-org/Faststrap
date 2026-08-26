# Faststrap Showcase

This directory is the flagship reference layer for Faststrap.

Unlike the smaller examples in `examples/`, the files here are intended to show what Faststrap looks like when used for polished, production-style work.

## Purpose

Showcase apps should:

- attract new users to the framework
- prove Faststrap can build premium interfaces
- serve as the primary design references for docs, skills, and future sample work

## Current Reference Status

### Full Showcase Directory (20 Flagship Applications)

| Application | Port | Domain / Aesthetic | Key Components Demonstrated |
|---|---|---|---|
| [`novaflow_ai_saas.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/novaflow_ai_saas.py) | `5001` | AI SaaS Platform (Cyber-dark / Emerald) | `ActiveSearch`, `LoadingButton`, `Tabs`, `Accordion`, `PricingGroup`, `FooterModern` |
| [`northstar_ops_dashboard.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/northstar_ops_dashboard.py) | `5002` | Enterprise Operations Dashboard | `DashboardLayout`, `DataTable`, `KPICard`, `TrendCard`, `RangeSlider`, `MultiSelect` |
| [`generated_saas.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/generated_saas.py) | `5003` | AI Code Refactoring SaaS | `ActiveSearch`, `LoadingButton`, `toast_response`, `TestimonialSection` |
| [`saas_landing.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/saas_landing.py) | `5004` | Multi-tier SaaS Landing Page | `Hero`, `PricingGroup`, `FeatureGrid`, `ListGroup`, `ThemeToggle` |
| [`agency_portfolio.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/agency_portfolio.py) | `5005` | Creative Design Agency | `InfiniteScroll`, `TestimonialSection`, `LoadingButton`, `Navbar`, `FooterModern` |
| [`fastcloud_generated_saas.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/fastcloud_generated_saas.py) | `5006` | Cloud Infrastructure Platform | `NavbarModern`, `FeatureGrid`, `PricingTier`, `TestimonialSection`, `toast_response` |
| [`admin_dashboard.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/admin_dashboard.py) | `5010` | Nexus Analytics & User Admin | `StatCard`, `AutoRefresh`, `ActiveSearch`, `ChartJS`, `ErrorPage` |
| [`hotel_booking_showcase.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/hotel_booking_showcase.py) | `5011` | Luxury Hotel & Room Booking | `ActiveSearch`, `LazyLoad`, `AutoRefresh`, `LoadingButton`, `Badge` |
| [`carenest_clinic.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/carenest_clinic.py) | `5012` | Healthcare Clinic & Patient Portal | `FormGroup`, `InputGroup`, `Select`, `CalendarDatePicker`, `Modal` |
| [`ledgerleaf_finance.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/ledgerleaf_finance.py) | `5013` | Fintech & Digital Banking | `Sheet`, `SearchableSelect`, `StatCard`, `InputGroup`, `Tabs` |
| [`forgedocs_platform.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/forgedocs_platform.py) | `5014` | Interactive API Documentation | `SearchableSelect`, `CodeBlock`, `InputGroup`, `Badge`, `Alert` |
| [`furniture_store_showcase.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/furniture_store_showcase.py) | `5015` | Modern E-commerce Storefront | `Card`, `Badge`, `Button`, `Container`, `ThemeToggle` |
| [`lexbridge_corporate.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/lexbridge_corporate.py) | `5016` | Corporate Legal Practice | `Hero`, `Card`, `Accordion`, `Navbar`, `FooterModern` |
| [`learnloop_academy.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/learnloop_academy.py) | `5018` | EdTech & STEM Course Platform | `Math` (KaTeX), `ProgressBar`, `Tabs`, `Accordion`, `AutoRefresh` |
| [`education_exam_suite.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/education_exam_suite.py) | `5020` | Exam & Question Bank Suite | `Math`, `SplitPane`, `Switcher`, `DataCard`, `ProfileDropdown` |
| [`ai_research_hub.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/ai_research_hub.py) | `5021` | ML Model Registry & Experiments | `Math`, `FilePreview`, `DataCard`, `SearchBar`, `ProfileDropdown` |
| [`saas_admin_portal.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/saas_admin_portal.py) | `5022` | SaaS Subscription & Metrics Portal | `FilterBar`, `DateRangePicker`, `ExportButton`, `DataTable`, `MetricCard` |
| [`atlas_command_center.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/atlas_command_center.py) | `5028` | Incident Command Center (v0.7.0) | `CommandPalette`, `ChartJS`, `Timeline`, `ModernToastStack`, `StatusBadge` |
| [`onboardflow_workspace.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/onboardflow_workspace.py) | `5029` | Workspace Onboarding (v0.7.0) | `FormWizard`, `LiveValidationField`, `InlineEditor`, `Gsap`, `Stepper` |
| [`analytics_dashboard.py`](file:///C:/Users/Meshell/Desktop/FastHTML/Faststrap/showcase/analytics_dashboard.py) | `5099` | Telemetry & Events Analytics | `StatCard`, `Tabs`, `TabPane`, `ErrorPage`, `ThemeToggle` |

## Showcase Standards

Every flagship showcase should:

- use a strong visual direction
- use custom typography
- use a real Faststrap theme or `create_theme(...)`
- include a polished custom CSS layer
- feel mobile-first and production-ready
- demonstrate meaningful Faststrap component usage
- avoid placeholder content and stale version strings
- use readable, copyable reference-grade code

## Screenshot Convention

When adding showcase screenshots for docs/README, place them in:

- `docs/assets/showcase/`

Recommended filenames:

- `novaflow-ai-saas-light.png`
- `novaflow-ai-saas-dark.png`
- `northstar-ops-dashboard-light.png`
- `northstar-ops-dashboard-dark.png`

Use lowercase kebab-case so docs pages and README references stay predictable.

## Separation Of Concerns

Use:

- `examples/` for learning and focused component demos
- `showcase/` for aspirational, polished, flagship references

If an app is useful for teaching but not visually exceptional, it belongs in `examples/`, not here.
