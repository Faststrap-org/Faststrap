# Static Export

Faststrap can export a FastHTML application as a set of static HTML, CSS, and JavaScript files. This is useful for deploying to static hosting providers like Netlify, Vercel Static, GitHub Pages, or any CDN.

The export captures the **initial rendered state** of every GET route, copies all static assets, and rewrites URLs so the site works without a Python server.

!!! tip "When to use static export"
    - Marketing sites, documentation, blogs
    - Landing pages with no server-side logic
    - Dashboards with pre-rendered data
    - Any app that can be served from a CDN

    For dynamic apps with HTMX, WebSockets, or server-side sessions, use a regular FastHTML deployment instead.

---

## Quick Start

```bash
python -m faststrap export myapp:app ./dist
```

This creates a `dist/` directory with static files ready for hosting.

---

## How It Works

1. **Discovers GET routes** in your FastHTML app
2. **Renders each route** using FastHTML's ASGI test client
3. **Copies static assets** (Bootstrap CSS/JS, Faststrap CSS/JS, fonts, your mounted assets)
4. **Rewrites URLs** so pages work from nested paths (`/static/...` → `./static/...`)
5. **Writes HTML files** to the output directory

---

## Command Reference

```bash
python -m faststrap export APP OUTPUT [OPTIONS]
```

### Arguments

| Argument | Description |
| --- | --- |
| `APP` | App to export, in `module:app_variable` format (e.g. `main:app`) |
| `OUTPUT` | Output directory for static files |

### Options

| Option | Description |
| --- | --- |
| `--static-url PATH` | Static URL path (default: `/static`) |
| `--exclude PATH` | Path prefix to exclude (can be repeated) |
| `--no-js` | Exclude JavaScript assets |

---

## Examples

### Basic Export

```bash
python -m faststrap export main:app ./dist
```

### Exclude API Routes

```bash
python -m faststrap export main:app ./dist --exclude /api --exclude /admin
```

### JS-Free Export

```bash
python -m faststrap export main:app ./dist --no-js
```

### Custom Static URL

```bash
python -m faststrap export main:app ./dist --static-url /assets
```

---

## Python API

You can also export programmatically:

```python
from faststrap import add_bootstrap, export_static
from fasthtml.common import FastHTML

app = FastHTML()
add_bootstrap(app)

# ... define routes ...

output_dir = export_static(
    app,
    output_dir="dist",
    static_url="/static",
    exclude_paths=["/api", "/admin"],
    include_js=True,
)
```

---

## Output Structure

```
dist/
├── index.html              # Homepage
├── about/
│   └── index.html          # /about
├── contact/
│   └── index.html          # /contact
└── static/
    ├── css/
    │   ├── bootstrap.min.css
    │   ├── bootstrap-icons.min.css
    │   ├── faststrap-fx.css
    │   ├── faststrap-layouts.css
    │   ├── faststrap-toast.css
    │   ├── faststrap-visual.css
    │   └── fonts/
    └── js/
        ├── bootstrap.bundle.min.js
        ├── faststrap-init.js
        └── modern-toast.js
```

---

## Deploying Static Exports

### Netlify

Create `netlify.toml`:

```toml
[build]
  publish = "dist"
  command = "python -m faststrap export main:app dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

### Vercel

Create `vercel.json`:

```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

Build command:
```bash
python -m faststrap export main:app ./dist
```

### GitHub Pages

```bash
python -m faststrap export main:app ./dist
git checkout gh-pages
cp -r dist/* .
git add .
git commit -m "Deploy"
git push origin gh-pages
```

---

## Limitations

| Feature | Static Export | Dynamic App |
| --- | --- | --- |
| Initial page render | ✅ | ✅ |
| Bootstrap CSS/JS | ✅ | ✅ |
| Faststrap CSS/JS | ✅ | ✅ |
| HTMX interactions | ❌ Initial only | ✅ Full |
| Form submissions | ❌ No server | ✅ Full |
| Database queries | ❌ | ✅ |
| WebSockets / SSE | ❌ | ✅ |
| Dynamic routing | ❌ | ✅ |

**HTMX note:** Static export captures the initial HTML state. HTMX-powered interactions (search, live validation, infinite scroll) require a running FastHTML server.

---

## See Also

- [Vercel Deployment](../deployment/vercel.md)
- [Netlify Deployment](../deployment/railway.md)
- [Render Deployment](../deployment/render.md)
- [Fly.io Deployment](../deployment/flyio.md)
