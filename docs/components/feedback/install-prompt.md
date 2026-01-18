# InstallPrompt

PWA install prompt component for Progressive Web Apps.

## Basic Usage

```python
from faststrap import InstallPrompt

InstallPrompt(
    title="Install Our App",
    message="Get the best experience by installing our app!",
    install_text="Install",
    dismiss_text="Not now"
)
```

## API Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | str | "Install App" | Prompt title |
| `message` | str | - | Prompt message |
| `install_text` | str | "Install" | Install button text |
| `dismiss_text` | str | "Dismiss" | Dismiss button text |
| `variant` | str | "primary" | Button variant |
| `**kwargs` | Any | - | Additional HTML attributes |

## Example

```python
InstallPrompt(
    title="Install FastApp",
    message="Install our app for offline access and faster performance!",
    install_text="Install Now",
    dismiss_text="Maybe Later",
    variant="success"
)
```

## See Also

- [Modal](modal.md) - Modal dialogs
- [Alert](alert.md) - Alert messages
