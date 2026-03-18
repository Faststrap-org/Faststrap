# App Repo AGENTS Template

Place a file like this in the root of any new FastHTML + Faststrap app repository.

```md
# App Build Guide

This repository is a real FastHTML application built with Faststrap.

## Required first reads

Before making UI changes, inspect:

1. `main.py` or the app entrypoint
2. the shared theme/defaults module
3. the main layout shell
4. the app CSS file
5. the closest route/page module for the task

## Framework reference

The Faststrap framework repo lives at:

- `C:/path/to/Faststrap`

Before building, inspect these framework references:

- `C:/path/to/Faststrap/AGENTS.md`
- `C:/path/to/Faststrap/examples/showcase/saas_landing.py`
- `C:/path/to/Faststrap/examples/showcase/admin_dashboard.py`
- `C:/path/to/Faststrap/showcase/hotel_booking_showcase.py`

## Local gold-standard reference apps

Use these projects as the visual and architectural bar:

- `C:/path/to/NIS`
- `C:/path/to/another/reference-app`

Inspect the closest matching files before writing code.

## UI quality bar

- The result must feel production-grade, branded, and intentional.
- Avoid generic Bootstrap-looking pages.
- Use Faststrap components plus custom CSS for polish.
- Respect responsive layout, spacing rhythm, typography hierarchy, and section contrast.
- Do not ship a plain hero-card-grid-footer layout unless the brief explicitly calls for it.

## Implementation priority

- Use Faststrap and Bootstrap capabilities first for layout, spacing, responsiveness, visibility control, and component behavior.
- Use HTMX first for interaction and partial updates.
- Use custom CSS mainly for brand feel, modern visuals, and refinements Bootstrap does not already solve well.
- Use JavaScript only when HTMX/Bootstrap cannot do the job cleanly or when browser/PWA APIs are required.
- Do not add external CSS CDNs for styling.

## Architecture rules

- Keep theme tokens and component defaults centralized.
- Keep layout shells separate from page business logic.
- Split routes/modules by area when the app is multi-page.
- Prefer existing Faststrap components and patterns before inventing raw HTML structures.

## Completion checklist

- Mobile and desktop both checked
- Shared theme/defaults applied consistently
- Custom CSS added where needed for polish
- Empty/loading/error states considered
- Relevant tests run
```
