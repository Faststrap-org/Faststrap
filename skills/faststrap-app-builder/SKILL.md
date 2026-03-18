---
name: faststrap-app-builder
description: Use when building or redesigning real FastHTML applications with Faststrap, such as company websites, SaaS landing pages, dashboards, portals, auth flows, admin systems, or multi-page product sites. This skill helps Codex inspect the right local framework repo, sample apps, and project files first so the result matches production-grade Faststrap + FastHTML patterns instead of generic Bootstrap output.
---

# Faststrap App Builder

Use this skill when the task is to build or significantly improve a real application with Faststrap + FastHTML.

## First moves

Before writing code:

1. Inspect the current app's entrypoint, theme/defaults module, route layout, asset mount, and custom CSS.
2. If the user provides a Faststrap repo path, inspect:
   - `AGENTS.md`
   - `README.md`
   - the most relevant files in `examples/` and `showcase/`
3. If the user provides a reference app, inspect it before designing.
4. Match the page type to the closest reference:
   - marketing/landing: see `references/reference-apps.md`
   - dashboard/admin: see `references/reference-apps.md`
   - auth/onboarding: see `references/nis-patterns.md`
5. Follow the implementation order of precedence below before inventing custom structure.

## Implementation order of precedence

Use this order unless the task clearly requires otherwise:

1. Faststrap components and Bootstrap-native layout/responsive utilities
2. HTMX for dynamic behavior and partial updates
3. Custom CSS for branding, atmosphere, and modern visual polish
4. JavaScript only when HTMX/Bootstrap cannot solve the problem cleanly or when browser/PWA APIs are required

This means:

- prefer Bootstrap spacing, grid, display, flex, container, offcanvas, modal, collapse, and utility classes before writing custom layout CSS
- prefer HTMX before custom JavaScript for interactivity, filtering, partial refresh, form flows, and inline actions
- use custom CSS to elevate visuals, not to reimplement Bootstrap responsiveness or hide/show behavior unnecessarily
- allow JavaScript for legitimate cases such as PWA flows, geolocation, service workers, media capture, complex charts/maps, or browser APIs HTMX cannot replace

## Non-negotiable standards

- Do not ship generic Bootstrap-looking pages.
- Do not default to plain white sections, weak typography, or boilerplate hero-card-grid-footer layouts unless the references support that exact direction.
- Prefer composing existing Faststrap components and patterns first, then layer custom CSS for polish.
- Build shared theme tokens and layout structure before polishing individual pages.
- Keep the UI responsive, accessible, and visually intentional.
- Do not rely on external CSS CDNs for project styling. Keep styling in local project assets and Faststrap/Bootstrap.
- Treat JavaScript as the last interaction tool, not the first one.

## Working pattern

1. Establish the app shell
- Create or inspect the FastHTML app entrypoint.
- Wire `add_bootstrap(app, ...)`.
- Mount project assets.
- Add shared custom CSS after Faststrap.

2. Establish shared design language
- Put brand colors and global component defaults in a single theme module.
- Define layout wrappers before page-level sections.
- Use custom CSS for depth: gradients, glass, section contrast, spacing rhythm, shadows, image treatment, and state styling.
- Keep structural responsiveness primarily in Bootstrap/Faststrap usage, not hand-written media-query-heavy layout rewrites unless clearly necessary.

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
- Run relevant tests; if the project has none, add at least focused smoke or route tests when practical.

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

## Read these references as needed

- `references/nis-patterns.md`: real production-style project wiring and theming patterns from the user's NIS, Final-Year, and SIWES apps
- `references/reference-apps.md`: which local Faststrap showcase files to inspect by page type
- `references/project-agents-template.md`: template instructions to place in fresh app repos so future sessions start with the right guardrails
