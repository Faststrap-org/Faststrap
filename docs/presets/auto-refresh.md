# AutoRefresh

Auto-refreshing content section. Polls the server at regular intervals and updates content. Replaces `setInterval` JavaScript patterns.

!!! success "Stability: Stable"
    This component is stable and ready for production use.

## Usage

```python
from faststrap.presets import AutoRefresh

AutoRefresh(
    endpoint="/api/metrics",
    target="this",
    interval=10000,  # 10 seconds
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `endpoint` | `str` | **required** | Server endpoint to poll |
| `target` | `str` | **required** | CSS selector or `"this"` for self |
| `interval` | `int` | `5000` | Milliseconds between requests |
| `content` | `Any` | Loading text | Initial content to display |
| `**kwargs` | | | Additional HTML/HTMX attrs |

## Example: Live Dashboard

```python
@app.get("/")
def dashboard():
    return Container(
        H1("Dashboard"),
        AutoRefresh(
            endpoint="/api/stats",
            target="#stats-panel",
            interval=5000,
        ),
        id="stats-panel",
    )

@app.get("/api/stats")
def stats():
    return Row(
        Col(StatCard("Users", get_user_count(), icon="people")),
        Col(StatCard("Revenue", f"${get_revenue()}", icon="currency-dollar")),
    )
```

!!! tip
    Use `target="this"` to replace the AutoRefresh element itself. This is useful when the refreshed content should include a new AutoRefresh trigger.
