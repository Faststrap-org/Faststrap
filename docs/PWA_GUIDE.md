# Building PWAs with Faststrap

Faststrap v0.5.2 introduces "PWA Mode" – a set of tools to make your FastHTML application installable on mobile devices with zero hassle.

## Quick Start

Transform any Faststrap app into a PWA in 1 line of code:

```python
from faststrap import add_pwa

app = FastHTML()
add_bootstrap(app)

# 🚀 Enable PWA Mode
add_pwa(app, 
    name="My Native App",
    theme_color="#6F42C1",
    icon_path="/static/icon.png"
)
```

## What `add_pwa` Does

This single function handles the complex "glue" required for PWA installation:

1.  **Injects Meta Tags**: Automatically adds `viewport`, `theme-color`, and iOS-specific tags (`apple-mobile-web-app-capable`).
2.  **Serves Manifest**: Generates and serves a valid `/manifest.json` based on your arguments.
3.  **Service Worker**: Mounts a background worker (`sw.js`) that caches core assets for offline usage.
4.  **Offline Page**: Serves a default `/offline` route when the user has no network.

## Mobile Components

To make your app *feel* native, use these new components:

### 1. Bottom Navigation (`BottomNav`)

The standard tab bar for mobile apps.

```python
BottomNav(
    BottomNavItem("Home", icon="house-fill", active=True),
    BottomNavItem("Profile", icon="person-circle"),
    fixed=True,
    variant="light"
)
```

### 2. Sheet (`Sheet`)

A bottom-up modal implementation of the Drawer, perfect for menus and options.

```python
Sheet(
    Div(
        H5("Options"),
        Button("Save", cls="btn btn-primary w-100 mb-2"),
        Button("Cancel", cls="btn btn-outline-secondary w-100", data_bs_dismiss="offcanvas")
    ),
    sheet_id="mySheet",
    title="Edit Item"
)
```

### 3. Install Prompt (`InstallPrompt`)

A smart component that helps users install your app.
- **On Android/Desktop**: Shows a button that triggers the native install dialog.
- **On iOS**: Shows a toast usage instruction ("Tap Share -> Add to Home Screen") because iOS doesn't support automatic prompts.

```python
InstallPrompt(
    title="Get the App",
    description="Install for a better experience!"
)
```

## Customizing the Service Worker

`add_pwa()` uses a default "Network First, Cache Fallback" strategy. If you need custom caching logic:

1.  Set `service_worker=False` in `add_pwa`.
2.  Write your own `sw.js`.
3.  Mount it manually:
    ```python
    @app.get("/sw.js")
    def sw():
        return FileResponse("path/to/my/sw.js")
    ```
