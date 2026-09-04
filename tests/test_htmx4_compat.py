"""Tests for HTMX cross-version bridge and HTMX 4 compatibility features."""

import json

from fasthtml.common import Div, FastHTML, Meta, Script, Span

from faststrap import DataTable, SSETarget, Toast, add_bootstrap
from faststrap.core.assets import (
    HTMX4_COMPAT_JS_URL,
    _detect_htmx4,
    _set_htmx_config,
    get_assets,
)
from faststrap.presets import LoadingButton, multi_response


def test_detect_htmx4():
    app_default = FastHTML()
    assert _detect_htmx4(app_default) is False

    app_v4 = FastHTML()
    app_v4.hdrs.append(Script(src="https://cdn.jsdelivr.net/npm/htmx.org@4.0.0/dist/htmx.min.js"))
    assert _detect_htmx4(app_v4) is True


def test_set_htmx_config_new_meta():
    app = FastHTML()
    _set_htmx_config(app, extensions=["hx-sse", "hx-pending"])
    metas = [h for h in app.hdrs if getattr(h, "attrs", {}).get("name") == "htmx-config"]
    assert len(metas) == 1
    content = json.loads(metas[0].attrs["content"])
    assert content["extensions"] == ["hx-sse", "hx-pending"]


def test_set_htmx_config_merge_existing():
    app = FastHTML()
    app.hdrs.append(Meta(name="htmx-config", content=json.dumps({"metaCharacter": "-"})))
    _set_htmx_config(app, extensions=["my-ext"])
    metas = [h for h in app.hdrs if getattr(h, "attrs", {}).get("name") == "htmx-config"]
    assert len(metas) == 1
    content = json.loads(metas[0].attrs["content"])
    assert content["metaCharacter"] == "-"
    assert content["extensions"] == ["my-ext"]


def test_add_bootstrap_htmx4_options():
    app = FastHTML()
    add_bootstrap(
        app,
        htmx4=True,
        htmx_compat=True,
        allow_extensions=["hx-sse", "hx-pending"],
    )
    scripts = [getattr(h, "attrs", {}).get("src", "") for h in app.hdrs]
    assert HTMX4_COMPAT_JS_URL in scripts

    metas = [h for h in app.hdrs if getattr(h, "attrs", {}).get("name") == "htmx-config"]
    assert len(metas) == 1
    cfg = json.loads(metas[0].attrs["content"])
    assert cfg["extensions"] == ["hx-sse", "hx-pending"]


def test_faststrap_htmx_bridge_in_assets():
    assets = get_assets(include_custom=True, use_cdn=False)
    bridge_scripts = [
        getattr(el, "attrs", {}).get("src", "")
        for el in assets
        if "faststrap-htmx.js" in getattr(el, "attrs", {}).get("src", "")
    ]
    assert len(bridge_scripts) == 1


def test_multi_response():
    # 1. Content + string toast
    res1 = multi_response(
        Div("Main content"),
        toast="Saved successfully!",
        toast_variant="success",
    )
    assert len(res1) == 2
    assert getattr(res1[1], "attrs", {}).get("hx-swap-oob") == "afterbegin:#toast-container"

    # 2. Content + OOB item + component toast
    custom_toast = Toast("Custom", variant="info", hx_swap_oob="afterbegin:#custom-toast")
    oob_counter = Span("10", id="counter", hx_swap_oob="true")
    res2 = multi_response(
        Div("Updated"),
        oob_counter,
        toast=custom_toast,
    )
    assert len(res2) == 3
    assert res2[1] is oob_counter
    assert res2[2] is custom_toast

    # 3. Empty content with OOB items
    res3 = multi_response(
        "",
        Span("5", id="badge", hx_swap_oob="true"),
    )
    assert len(res3) == 1
    assert getattr(res3[0], "attrs", {}).get("id") == "badge"


def test_datatable_morph_and_polling():
    dt = DataTable(
        data=[{"name": "Alice", "role": "Admin"}],
        endpoint="/users",
        poll_interval=10,
        poll_morph=True,
    )
    attrs = getattr(dt, "attrs", {})
    assert attrs.get("hx-get") == "/users"
    assert attrs.get("hx-trigger") == "every 10s"
    assert attrs.get("hx-swap") == "morph"


def test_sse_target_engines():
    # Native EventSource engine
    sse_native = SSETarget(
        Span("Connecting..."),
        endpoint="/stream",
        event="stats",
        engine="eventsource",
    )
    attrs_native = getattr(sse_native, "attrs", {})
    assert attrs_native.get("data-fs-sse") == "true"
    assert attrs_native.get("data-fs-sse-endpoint") == "/stream"
    assert attrs_native.get("data-fs-sse-event") == "stats"

    # HTMX SSE extension engine
    sse_htmx = SSETarget(
        Span("Connecting..."),
        endpoint="/stream",
        event="stats",
        engine="htmx",
        target="#stats-panel",
        swap="innerHTML",
    )
    attrs_htmx = getattr(sse_htmx, "attrs", {})
    assert attrs_htmx.get("hx-ext") == "sse"
    assert attrs_htmx.get("sse-connect") == "/stream"
    assert attrs_htmx.get("sse-swap") == "stats"
    assert attrs_htmx.get("hx-target") == "#stats-panel"
    assert attrs_htmx.get("hx-swap") == "innerHTML"


def test_loading_button_pending():
    btn = LoadingButton("Save", endpoint="/save", pending="#skeleton-form")
    attrs = getattr(btn, "attrs", {})
    assert attrs.get("hx-pending") == "#skeleton-form"
    assert attrs.get("hx-disabled-elt") == "this"
