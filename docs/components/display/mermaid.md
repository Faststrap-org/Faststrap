# Mermaid

Render Mermaid diagrams using Mermaid.js on the client.

---

## Quick Start

Mermaid requires the Mermaid.js runtime. Include it once:

```python
from fasthtml.common import Script
from faststrap import Mermaid

Script(src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js")
Mermaid("""
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Ship]
    B -->|No| D[Revise]
""")
```

---

## Theme and Security

```python
Mermaid(
    """
sequenceDiagram
  client->>server: request
  server-->>client: response
""",
    theme="dark",
    security_level="strict",
)
```

Mermaid config is global. If you need custom config, initialize Mermaid manually before rendering.

---

## Layout Control

```python
Mermaid(diagram, min_width=280)
```

---

## HTMX Support

Faststrap re-initializes Mermaid diagrams after HTMX swaps when Mermaid.js is available.

---

## Security Notes

Only render trusted diagrams when using relaxed security settings. Keep `security_level="strict"` for untrusted input.

---

## API Reference

::: faststrap.components.display.mermaid.Mermaid
    options:
        show_source: true
        heading_level: 4
