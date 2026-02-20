# InstallPrompt

PWA install prompt component for Progressive Web Apps.

## Basic Usage

```python
from faststrap import InstallPrompt

InstallPrompt(
    title="Install Our App",
    description="Get the best experience by installing our app!",
    ios_text="Tap Share and choose Add to Home Screen.",
    android_text="Tap Install to add this app to your home screen.",
    delay=3000
)
```

## API Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | str | "Install App" | Prompt title |
| `description` | str | "Add this app to your home screen for the best experience." | Prompt message |
| `ios_text` | str | iOS install instruction | iOS-specific helper text |
| `android_text` | str | Android install instruction | Android install button text |
| `delay` | int | `3000` | Milliseconds before prompt appears |
| `**kwargs` | Any | - | Additional HTML attributes |

## Example

```python
InstallPrompt(
    title="Install FastApp",
    description="Install our app for offline access and faster performance!",
    ios_text="Tap Share then Add to Home Screen.",
    android_text="Install Now",
    delay=2000
)
```

## See Also

- [Modal](modal.md) - Modal dialogs
- [Alert](alert.md) - Alert messages
