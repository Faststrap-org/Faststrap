"""Generate docs/llms.txt and docs/llms-full.txt from the live Faststrap registry.

Run from the repository root:

    python scripts/generate_llms.py

The generated files are derived from ``faststrap.__all__``,
``faststrap.list_component_metadata()``, and live ``inspect.signature`` data, so
they can never drift from the public API.
"""

from __future__ import annotations

import inspect
import os
import re
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")

GITHUB_BASE = "https://github.com/Faststrap-org/Faststrap/blob/main/"
DOCS_BASE = "https://faststrap-org.github.io/Faststrap/"

TAGLINE = (
    "Python-native Bootstrap 5 UI components for FastHTML - web apps, dashboards, "
    "data tools, and AI-friendly interfaces."
)

CATEGORY_BLURBS = {
    "forms": "inputs, buttons, pickers, validation surfaces",
    "display": "cards, tables, badges, charts, data viewers",
    "feedback": "alerts, modals, toasts, loaders, progress",
    "navigation": "navbars, tabs, menus, drawers, pagination",
    "layout": "grid, containers, page scaffolding",
    "patterns": "composed marketing/product page sections",
}

HELPER_NAMES = {
    "add_bootstrap", "add_chartjs", "add_gsap", "add_pwa", "chartjs_assets",
    "gsap_assets", "convert_attrs", "merge_classes", "mount_assets", "get_assets",
    "cleanup_static_resources", "get_faststrap_static_url", "create_theme",
    "get_builtin_theme", "list_builtin_themes", "reset_component_defaults",
    "resolve_defaults", "set_component_defaults", "theme_variant_css",
    "find_components", "get_component", "get_components_by_pattern",
    "list_component_metadata", "list_components", "register", "render_svg",
    "datatable_export_params", "datatable_page_url", "datatable_query_params",
    "extract_field_error", "map_formgroup_validation", "stable", "beta",
    "experimental", "SEO", "UNSET",
}


def kebab(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


def module_to_repo_path(module):
    if not module or not module.startswith("faststrap"):
        return None
    return "src/" + module.replace(".", "/") + ".py"


def github_link(module):
    path = module_to_repo_path(module)
    return GITHUB_BASE + path if path else GITHUB_BASE


def first_doc_line(obj):
    doc = inspect.getdoc(obj)
    if not doc:
        return ""

def build_docs_page_map():
    pages = {}
    for root, _dirs, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), DOCS_DIR).replace(os.sep, "/")
                pages[rel[:-3]] = open(os.path.join(root, f), encoding="utf-8").read()
    return pages


def docs_url_for(name, pages):
    """Return a docs-site URL for a symbol, or None if no page documents it."""
    slug = kebab(name)
    candidates = [p for p in pages if p.lower().endswith("/" + slug) or p.lower() == slug]
    if not candidates:
        candidates = [p for p, text in pages.items() if name in text]
    if not candidates:
        return None
    page = min(candidates, key=lambda p: (p.count("/"), p))
    return DOCS_BASE + page + "/"


def collect():
    import faststrap
    from faststrap import __all__ as ALL

    pages = build_docs_page_map()
    meta_by_name = {m["name"]: m for m in faststrap.list_component_metadata()}

    components = defaultdict(list)
    helpers, type_aliases, constants = [], [], []

    for name in sorted(ALL):
        if name.startswith("__"):
            continue
        obj = getattr(faststrap, name, None)
        module = getattr(obj, "__module__", None)
        try:
            sig = str(inspect.signature(obj))
        except (ValueError, TypeError):
            sig = None
        entry = {
            "name": name,
            "module": module,
            "stability": getattr(obj, "__faststrap_stability__", None),
            "docs": docs_url_for(name, pages),
            "sig": sig,
            "doc": first_doc_line(obj),
        }
        if name in meta_by_name:
            entry["category"] = meta_by_name[name].get("category", "other")
            entry["requires_js"] = bool(meta_by_name[name].get("requires_js"))
            components[entry["category"]].append(entry)
        elif name in HELPER_NAMES:
            helpers.append(entry)
        elif sig == "(*args, **kwargs)" and module == "typing":
            type_aliases.append(entry)
        else:
            constants.append(entry)

    import faststrap.presets as presets_mod

    presets = []
    for name in sorted(getattr(presets_mod, "__all__", [])):
        obj = getattr(presets_mod, name, None)
        presets.append({
            "name": name,
            "module": getattr(obj, "__module__", "faststrap.presets"),
            "doc": first_doc_line(obj),
        })

    return {
        "exports": len(ALL),
        "registered": len(faststrap.list_components()),
        "themes": faststrap.list_builtin_themes(),
        "components": dict(components),
        "helpers": helpers,
        "aliases": type_aliases,
        "constants": constants,
        "presets": presets,
    }



def fmt_entry(e, full):
    label = "`" + e["name"] + "`"
    if e.get("stability"):
        label += " (" + e["stability"] + ")"
    bits = []
    if e.get("doc"):
        bits.append(e["doc"])
    if e.get("requires_js"):
        bits.append("requires Bootstrap JS")
    src = "[source](" + github_link(e["module"]) + ")"
    page = "[docs](" + e["docs"] + ")" if e.get("docs") else None
    links = " - ".join(x for x in (page, src) if x)
    line = "- " + label
    if bits:
        line += " - " + " | ".join(bits)
    if links:
        line += " (" + links + ")"
    if full and e.get("sig"):
        line += "\n  - Signature: `" + e["name"] + e["sig"] + "`"
    return line


def render(data, full):
    L = []
    L.append("# FastStrap")
    L.append("")
    L.append("> " + TAGLINE)
    L.append("")
    L.append("**%d registered UI components** - **%d public exports** - MIT - Python 3.10+ - FastHTML 0.6+" % (data["registered"], data["exports"]))
    L.append("")
    L.append("## Quick Start")
    L.append("")
    L.append("```python")
    L.append("from fasthtml.common import FastHTML, serve")
    L.append("from faststrap import add_bootstrap, Card, Button")
    L.append("")
    L.append("app = FastHTML()")
    L.append("add_bootstrap(app)")
    L.append("")
    L.append('@app.get("/")')
    L.append("def home():")
    L.append("    return Card(")
    L.append('        "Hello FastStrap!",')
    L.append('        Button("Get started", variant="primary"),')
    L.append('        title="Welcome",')
    L.append("    )")
    L.append("")
    L.append("serve()  # http://localhost:5001")
    L.append("```")
    L.append("")
    L.append("Install: `pip install faststrap` (optional: `pip install faststrap[markdown]`).")
    L.append("")
    L.append("## Key Links")
    L.append("")
    L.append("- [Documentation](" + DOCS_BASE + ")")
    L.append("- [README](https://github.com/Faststrap-org/Faststrap/blob/main/README.md)")
    L.append("- [Changelog](https://github.com/Faststrap-org/Faststrap/blob/main/CHANGELOG.md)")
    L.append("- [Component Registry API](" + DOCS_BASE + "api/registry/): programmatic component discovery for agents/tools")
    L.append("- [Component Defaults API](" + DOCS_BASE + "api/defaults/): `UNSET` semantics and `set_component_defaults`")
    L.append("")
    L.append("## Component Catalog")
    L.append("")
    L.append("%d components registered via `@register`:" % data["registered"])
    L.append("")
    for category in sorted(data["components"]):
        entries = data["components"][category]
        blurb = CATEGORY_BLURBS.get(category, "")
        L.append("### " + category.title() + " (%d)" % len(entries) + ((" - " + blurb) if blurb else ""))
        L.append("")
        L.extend(fmt_entry(e, full) for e in entries)
        L.append("")
    return L

def build_output(data, full):
    L = render(data, full)
    L.append("## HTMX Presets")
    L.append("")
    L.extend(fmt_entry(e, False) for e in data["presets"])
    L.append("")
    L.append("## Layouts, Integrations, Helpers")
    L.append("")
    L.extend(fmt_entry(e, full) for e in data["helpers"])
    L.append("")
    if data["aliases"] or data["constants"]:
        L.append("## Type Aliases & Constants")
        L.append("")
        for e in data["aliases"] + data["constants"]:
            L.append("- `%s` (%s)" % (e["name"], e["module"] or "faststrap"))
        L.append("")
    L.append("## Theming")
    L.append("")
    L.append("Built-in themes: " + ", ".join(data["themes"]))
    L.append("")
    L.append("Modes: `light`, `dark`, `auto`. Create custom themes with `create_theme()`.")
    L.append("")
    L.append("## AI/Agent Discovery")
    L.append("")
    L.append("```python")
    L.append("from faststrap import find_components, get_component, list_component_metadata")
    L.append("")
    L.append('find_components("toast")            # name/docstring search')
    L.append('get_component("Modal")              # fetch a component callable by name')
    L.append('list_component_metadata(category="display")  # structured metadata')
    L.append("```")
    L.append("")
    L.append("## Verification")
    L.append("")
    L.append("- Generated by `scripts/generate_llms.py` from the live registry - do not edit by hand.")
    L.append("- Every signature above comes from `inspect.signature` of the installed package.")
    L.append("- Re-run `python scripts/generate_llms.py` after any API change.")
    L.append("")
    return "\n".join(L)


def main():
    data = collect()
    for fname, content in (("llms.txt", build_output(data, full=False)),
                           ("llms-full.txt", build_output(data, full=True))):
        path = os.path.join(DOCS_DIR, fname)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(content)
        print("wrote %s (%d lines)" % (path, len(content.splitlines())))


if __name__ == "__main__":
    main()
