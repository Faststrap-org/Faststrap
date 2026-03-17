# Stat Card

Stat cards are used on dashboards and reports to highlight key metrics. They typically include a title, a value, an optional icon, and a trend indicator (up/down).

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="card w-100">
      <div class="card-body">
        <div class="d-flex align-items-center justify-content-between">
          <div class="flex-grow-1">
            <p class="text-muted small text-uppercase fw-semibold mb-1">Total Revenue</p>
            <h3 class="mb-0 fw-bold">$45,231.89 <span class="text-success small fw-bold ms-2">+20.1%</span></h3>
          </div>
          <div class="d-flex align-items-center justify-content-center rounded p-3 bg-body-tertiary">
            <i class="bi bi-currency-dollar fs-4"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
StatCard(
    title="Total Revenue",
    value="$45,231.89",
    icon=BI("currency-dollar"),
    trend="+20.1%",
    trend_type="up"
)
```
  </div>
</div>

---

## v0.6.0 Metric Cards

FastStrap also ships specialized dashboard cards:

```python
MetricCard("Revenue", "$128k", delta="+12%", delta_type="up")
TrendCard("Active Users", "9,842", sparkline="<svg></svg>", sparkline_safe=True)
KPICard(
    "KPIs",
    metrics=[("Retention", "84%", "+2%", "up"), ("Churn", "3.1%", "-0.4%", "down")],
)
```

---

## MetricCard

`MetricCard` extends `StatCard` with a compact delta indicator.

```python
MetricCard(
    "Revenue",
    "$128k",
    delta="+12%",
    delta_type="up",
)
```

---

## TrendCard

`TrendCard` adds a sparkline slot. Use `sparkline_safe=True` only with trusted SVG or HTML.

```python
TrendCard(
    "Active Users",
    "9,842",
    sparkline="<svg></svg>",
    sparkline_safe=True,
)
```

---

## KPICard

`KPICard` renders multiple metrics inside one card.

```python
KPICard(
    "KPIs",
    metrics=[
        ("Retention", "84%", "+2%", "up"),
        ("Churn", "3.1%", "-0.4%", "down"),
    ],
)
```

---

## Visual Examples & Use Cases

### 1. Negative Trends
Use `trend_variant="danger"` for decreases in metrics.

<div class="component-preview">
  <div class="preview-header">Live Preview (Negative Trend)</div>
  <div class="preview-render">
    <div class="card w-100">
      <div class="card-body">
        <div class="d-flex align-items-center justify-content-between">
          <div class="flex-grow-1">
            <p class="text-muted small text-uppercase fw-semibold mb-1">Active Users</p>
            <h3 class="mb-0 fw-bold">1,234 <span class="text-danger small fw-bold ms-2">-5%</span></h3>
            <p class="text-muted small mb-0">from last month</p>
          </div>
          <div class="d-flex align-items-center justify-content-center rounded p-3 bg-body-tertiary">
            <i class="bi bi-people fs-4"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
StatCard(
    title="Active Users",
    value="1,234",
    trend="-5%",
    trend_type="down",
    icon=BI("people"),
    footer=P("from last month", cls="text-muted small mb-0")
)
```
  </div>
</div>

### 2. Branding (Variants)
Apply color to the icon or card borders using the `variant` argument.

!!! note "Code & Output"
    ```python
    StatCard(..., variant="primary", bg_variant="soft-primary")
    ```

---

## Parameter Reference

| FastStrap Param | Type | Description |
| :--- | :--- | :--- |
| `label` | `str` | Title of the metric (e.g. "Total Sales"). |
| `value` | `str | int` | The main display number or value. |
| `icon` | `str` | Bootstrap icon name. |
| `trend` | `str` | Percentage or text indicating change (e.g. "+12%"). |
| `trend_label` | `str` | Context for the trend (e.g. "since yesterday"). |
| `trend_variant` | `str` | Color of trend text: `success`, `danger`, `warning`. |
| `variant` | `str` | Color theme for the icon/label. |

::: faststrap.components.display.stat_card.StatCard
    options:
        show_source: true
        heading_level: 4
