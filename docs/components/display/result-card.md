# Result Card

`ResultCard` presents the outcome of an action: saved settings, failed submissions, empty flows, or follow-up next steps.

It is intentionally small, semantic, and HTMX-friendly. Success and info states use `role="status"`; warning and error states use `role="alert"`.

## Import

```python
from faststrap import ResultCard, Button
```

## Basic Usage

```python
ResultCard(
    title="Settings saved",
    message="Your preferences have been updated.",
    status="success",
)
```

## Error State

```python
ResultCard(
    title="Could not save",
    message="Please review the highlighted fields and try again.",
    status="error",
)
```

## With Action

```python
ResultCard(
    title="Invite sent",
    message="We emailed the new team member.",
    status="success",
    action=Button("View team", href="/team", variant="primary"),
)
```

## Usage Scenarios

### After Form Submission

```python
@app.post("/settings")
def save_settings(...):
    if success:
        return ResultCard(
            title="Settings saved",
            message="Your preferences have been updated.",
            status="success",
            action=Button("Back to dashboard", href="/dashboard"),
        )
    return ResultCard(
        title="Could not save",
        message="Please review the highlighted fields and try again.",
        status="error",
    )
```

### Empty State

```python
ResultCard(
    title="No matching records",
    message="Try adjusting your search or filter criteria.",
    status="info",
    action=Button("Clear filters", variant="secondary"),
)
```

## Customizing With Slot Classes

Slot classes let you restyle parts of the card without wrapping it:

```python
ResultCard(
    title="Experiment finished",
    message="42 runs completed. 3 failed. Full logs attached.",
    status="warning",
    icon="bi-hourglass-split",
    icon_cls="fs-4 text-warning",
    title_cls="fw-semibold",
    message_cls="text-body-secondary",
)
```

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main result title. |
| `message` | `str | None` | Optional supporting message. |
| `status` | `success | error | warning | info` | Semantic result state. |
| `icon` | `str | None` | Bootstrap icon name override. |
| `action` | `Any | None` | Optional action component. |
| `compact` | `bool` | Use tighter spacing. |
| `icon_cls` | `str | None` | Extra classes for the icon slot. |
| `title_cls` | `str | None` | Extra classes for the title slot. |
| `message_cls` | `str | None` | Extra classes for the message slot. |

## Accessibility

- `ResultCard` uses `role="status"` for success/info and `role="alert"` for warning/error.
- Ensure `action` buttons have accessible names.
- Use `compact` sparingly when space is constrained and content is minimal.

::: faststrap.components.display.result_card.ResultCard
    options:
        show_source: true
        heading_level: 3
