# Faststrap Repo Guide

These instructions apply to the `Faststrap/` repository and are intended to make future Faststrap + FastHTML work consistent, fast, and production-safe.

## First Read

When working in this repo, build context in this order:

1. `README.md`
2. `BUILDING_COMPONENTS.md`
3. The relevant docs page under `docs/`
4. The closest test file under `tests/`
5. The closest example under `examples/` or `showcase/`

Do not invent Faststrap APIs from memory when local source, examples, and tests already define the contract.

## Mental Model

Faststrap is a Python component layer on top of FastHTML and Bootstrap 5.

- FastHTML provides the element primitives and app/runtime integration.
- Faststrap provides higher-level components, presets, theme helpers, and asset wiring.
- HTMX is a first-class integration path and should be preserved when extending components.
- Bootstrap is the visual/runtime foundation, so generated markup should remain idiomatic Bootstrap markup unless the component intentionally abstracts it.

## Preferred Build Workflow

When asked to build a feature with Faststrap:

1. Find the nearest existing component, preset, or example and copy its pattern.
2. Prefer composing existing Faststrap components before creating new primitives.
3. Keep public APIs explicit, typed, and Pythonic.
4. Preserve backward compatibility unless the user explicitly approves a breaking change.
5. Add or update tests in the same pass as the code change.
6. Align docs/examples when public behavior changes.

## Faststrap Conventions

### App setup

- Use `add_bootstrap(app, ...)` for runtime assets and theme wiring.
- If a feature depends on Faststrap runtime helpers, assume `add_bootstrap()` is part of the app contract and document that clearly.

### Component implementation

- Prefer FastHTML primitives from `fasthtml.common`.
- Merge user classes with `merge_classes(...)`.
- Normalize attrs with `convert_attrs(...)`.
- Use descriptive IDs like `modal_id`, `drawer_id`, `tab_id` instead of plain `id` parameters when the ID is a required API input.
- Favor safe defaults and explicit escaping/sanitization boundaries.

### Stability markers

- `@stable` means the public API is considered safe to build on.
- `@beta` means the surface is usable but may still evolve.
- Do not promote a component to `@stable` unless its API shape, docs, and tests are mature enough for downstream reliance.

### Tests

- Use `to_xml()` for render assertions.
- Add focused regression tests for public contracts, accessibility attrs, and edge cases.
- If behavior depends on JS/runtime wiring, validate the rendered hooks and keep docs honest about what is client-driven.

## Where To Look First

Use these local references before improvising:

- Getting started:
  - `examples/01_getting_started/hello_world.py`
  - `examples/01_getting_started/simple_form.py`
- Broad component usage:
  - `examples/demo_all.py`
  - `examples/phase5_demo.py`
  - `examples/05_new_components/README.md`
- Data/realtime features:
  - `examples/05_new_components/v060_data_foundations.py`
  - `examples/05_new_components/v060_sse_stream.py`
- Themes:
  - `examples/06_examples/01_builtin_themes.py`
  - `examples/06_examples/02_custom_themes.py`
- Real app/page composition:
  - `examples/showcase/admin_dashboard.py`
  - `examples/showcase/saas_landing.py`
  - `showcase/admin_dashboard.py`
  - `showcase/hotel_booking_showcase.py`

## FastHTML + Faststrap Rules Of Thumb

- Prefer server-rendered HTML and HTMX over custom JavaScript when either can solve the problem cleanly.
- If JavaScript is required, integrate it through Faststrap's asset pipeline rather than ad hoc page snippets when the behavior is reusable.
- Keep Bootstrap semantics intact so classes, ARIA, and built-in JS plugins continue to work as expected.
- Treat docs and examples as part of the product surface. Broken examples are release bugs.

## Before Finishing Work

1. Run the narrowest relevant tests while iterating.
2. Run `pytest -q` before finalizing substantive changes.
3. Call out any remaining beta surfaces or known risks explicitly.

