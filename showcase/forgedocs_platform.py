"""Flagship showcase — ForgeDocs Platform.

Production-grade developer tool / API documentation platform for Faststrap:

- Markdown for deep, multi-section reference docs (auth, errors, pagination, rate limits)
- Mermaid for live sequence/architecture diagrams
- Svg for custom technical icons
- PageMeta for comprehensive SEO (title, description, keywords, og, url)
- Scrollspy for sticky right-side table-of-contents highlighting
- SearchableSelect for live API endpoint explorer
- Tabs for multi-language code snippets (cURL, Python, Node.js, Go)
- ThemeToggle dark-mode-first with cookie persistence on every route
- Badge for HTTP method indicators (GET/POST/PUT/DELETE)
- NoticeAlert for status banners on API key management page
- InputGroup for masked API key reveal pattern
- Card for reference endpoint cards
- Icon for sidebar navigation
- Custom CSS: JetBrains Mono code blocks, copy-to-clipboard hover,
  focus-expand search bar, method badge pulse glows, Stripe-like sidebar.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H5,
    A,
    Button,
    Code,
    Div,
    FastHTML,
    Hr,
    Input,
    Li,
    Link,
    Nav,
    P,
    Pre,
    Script,
    Small,
    Span,
    Strong,
    Style,
    Ul,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Col,
    Container,
    Fx,
    Icon,
    InputGroup,
    InputGroupText,
    Markdown,
    Math,
    Mermaid,
    PageMeta,
    Row,
    Scrollspy,
    SearchableSelect,
    Svg,
    Tabs,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import hx_refresh

# ── Theme ──────────────────────────────────────────────────────────────────────
THEME_KEY = "forgedocs_theme"

FORGEDOCS_THEME = create_theme(
    primary="#6366F1",  # Indigo
    secondary="#334155",  # Slate
    success="#10B981",  # Emerald
    info="#38BDF8",  # Sky
    warning="#F59E0B",  # Amber
    danger="#F43F5E",  # Rose
    dark="#0F172A",  # Slate 900
    light="#F8FAFC",  # Slate 50
)

# ── Custom SVGs ────────────────────────────────────────────────────────────────
SVG_FORGE = """
<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/>
  <path d="m21 2-9.6 9.6"/>
  <circle cx="7.5" cy="15.5" r="5.5"/>
</svg>
"""

SVG_WEBHOOK = """
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>
</svg>
"""

# ── Content blocks ─────────────────────────────────────────────────────────────
MD_INTRO = """
The ForgeDocs API lets you programmatically manage workspaces, deployments, webhooks, tokens, and pipelines. The API is organized around **REST** — predictable resource-oriented URLs, standard HTTP response codes, and JSON throughout.

```bash
# Base URL
https://api.forgedocs.io/v1

# All requests require a Bearer token
curl -H "Authorization: Bearer fd_live_sk_abc123xyz" \\
     https://api.forgedocs.io/v1/workspaces
```

Our API is designed to be explored in any language. Select your preferred SDK from the code examples on the right.
"""

MD_AUTH = """
## Authentication

ForgeDocs uses **API keys** to authenticate all requests. You can create and revoke keys from the [API Keys](#keys) section.

```bash
# Provide the key as a Bearer token
Authorization: Bearer fd_live_sk_abc123xyz
```

Keys come in two flavours:

| Type | Prefix | Use |
|---|---|---|
| Live | `fd_live_sk_` | Production traffic only |
| Test | `fd_test_sk_` | Safe sandbox — no real data |
| Restricted | `fd_restr_sk_` | Scoped to specific resources |

> **Never** expose live keys in client-side code, public repos, or build logs.
Keys can be rotated at any time from your dashboard without downtime.

### Key Scopes

Restricted keys support fine-grained permission scopes. Specify a comma-separated list of allowed operations when creating the key:

```
workspaces:read deployments:write webhooks:admin
```
"""

MD_PAGINATION = """
## Pagination

All list endpoints return **cursor-based** pagination. Responses include a `next_cursor` token that you pass as a query parameter on the next request.

```python
import requests

def list_all(resource, token):
    items, cursor = [], None
    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(
            f"https://api.forgedocs.io/v1/{resource}",
            headers={"Authorization": f"Bearer {token}"},
            params=params,
        ).json()
        items.extend(r["data"])
        cursor = r.get("next_cursor")
        if not cursor:
            break
    return items
```

### Response envelope

```json
{
  "data": [...],
  "next_cursor": "cur_1Abc2DEfG3hij",
  "has_more": true,
  "total_count": 347
}
```
"""

MD_ERRORS = """
## Error Handling

ForgeDocs uses standard HTTP status codes. All errors return a JSON body with a machine-readable `code` field.

| Status | Code | Meaning |
|---|---|---|
| `400` | `invalid_request` | Malformed payload or missing parameter |
| `401` | `unauthorized` | Missing or expired API key |
| `403` | `forbidden` | Key lacks permission for this resource |
| `404` | `not_found` | Resource does not exist |
| `409` | `conflict` | Duplicate resource or state mismatch |
| `422` | `validation_error` | Field-level validation failed |
| `429` | `rate_limited` | Exceeded request quota |
| `500` | `server_error` | Internal error — report via support |

```json
{
  "error": {
    "code": "validation_error",
    "message": "name is required",
    "fields": { "name": ["This field may not be blank."] }
  }
}
```

Implement exponential backoff for `429` and `500` errors. Use the `Retry-After` header when present.
"""

MD_ENDPOINTS = """
## REST Endpoints

Our resource-oriented API follows standard CRUD conventions. All endpoints accept and return `application/json`.

| Method | Endpoint | Description |
|---|---|---|
| <span class="fd-method get">GET</span> | `/v1/workspaces` | List all workspaces |
| <span class="fd-method post">POST</span> | `/v1/workspaces` | Create a new workspace |
| <span class="fd-method get">GET</span> | `/v1/workspaces/{id}` | Retrieve a workspace |
| <span class="fd-method put">PUT</span> | `/v1/workspaces/{id}` | Update workspace settings |
| <span class="fd-method del">DELETE</span> | `/v1/workspaces/{id}` | Archive a workspace |
| <span class="fd-method post">POST</span> | `/v1/deployments` | Trigger a deployment |
| <span class="fd-method get">GET</span> | `/v1/deployments/{id}` | Get deployment status |
| <span class="fd-method post">POST</span> | `/v1/webhooks` | Register a webhook endpoint |
| <span class="fd-method get">GET</span> | `/v1/tokens` | List active auth tokens |
| <span class="fd-method post">POST</span> | `/v1/tokens` | Mint a new token |
| <span class="fd-method del">DELETE</span> | `/v1/tokens/{id}` | Revoke a token |
| <span class="fd-method get">GET</span> | `/v1/pipelines` | List CI/CD pipelines |
"""

MD_WEBHOOKS = """
## Webhooks

Webhooks allow ForgeDocs to push real-time events to your infrastructure. All webhook payloads are signed — verify the `X-ForgeDocs-Signature` header.

### Registering an endpoint

```bash
curl -X POST https://api.forgedocs.io/v1/webhooks \\
  -H "Authorization: Bearer fd_live_sk_abc123" \\
  -H "Content-Type: application/json" \\
  -d '{
    "url": "https://yourapp.com/hooks/forgedocs",
    "events": ["deployment.completed", "deployment.failed", "workspace.deleted"],
    "secret": "whsec_your_signing_secret"
  }'
```

### Available events

- `deployment.queued` — build added to queue
- `deployment.completed` — successful build and promotion
- `deployment.failed` — build or deploy failure
- `workspace.created` / `workspace.deleted`
- `token.revoked` — key revocation event
- `pipeline.triggered` / `pipeline.succeeded` / `pipeline.failed`

### Verifying signatures

```python
import hmac, hashlib

def verify(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```
"""

MERMAID_PIPELINE = """
sequenceDiagram
    participant Dev as Developer
    participant API as API Gateway
    participant Bus as Event Bus
    participant Worker as Deploy Worker
    participant CDN as Edge CDN

    Dev->>API: POST /v1/deployments
    activate API
    API->>Bus: Publish deployment.queued
    Bus-->>API: ACK (offset 2847)
    API-->>Dev: 202 Accepted { id, status }
    deactivate API

    Bus->>Worker: Consume deployment.queued
    activate Worker
    Worker->>Worker: Pull source & build
    Worker->>CDN: Push static assets
    CDN-->>Worker: Assets promoted
    Worker->>Bus: Publish deployment.completed
    Worker-->>Bus: Commit offset
    deactivate Worker
"""

MERMAID_AUTH = """
graph LR
    A[Client] -->|Bearer token| B{API Gateway}
    B -->|Valid| C[Resource Handler]
    B -->|Expired| D[401 Unauthorized]
    B -->|No scope| E[403 Forbidden]
    C --> F[Response 200]
"""

# ── Endpoints index for SearchableSelect ─────────────────────────────────────
ENDPOINTS_INDEX = [
    ("GET /v1/workspaces", "GET /v1/workspaces — List all workspaces"),
    ("POST /v1/workspaces", "POST /v1/workspaces — Create workspace"),
    ("GET /v1/workspaces/{id}", "GET /v1/workspaces/{id} — Retrieve workspace"),
    ("PUT /v1/workspaces/{id}", "PUT /v1/workspaces/{id} — Update workspace"),
    ("DELETE /v1/workspaces/{id}", "DELETE /v1/workspaces/{id} — Archive workspace"),
    ("POST /v1/deployments", "POST /v1/deployments — Trigger deployment"),
    ("GET /v1/deployments/{id}", "GET /v1/deployments/{id} — Get deploy status"),
    ("GET /v1/deployments", "GET /v1/deployments — List deployments"),
    ("POST /v1/webhooks", "POST /v1/webhooks — Register webhook"),
    ("GET /v1/webhooks", "GET /v1/webhooks — List webhooks"),
    ("DELETE /v1/webhooks/{id}", "DELETE /v1/webhooks/{id} — Delete webhook"),
    ("GET /v1/tokens", "GET /v1/tokens — List active tokens"),
    ("POST /v1/tokens", "POST /v1/tokens — Mint new token"),
    ("DELETE /v1/tokens/{id}", "DELETE /v1/tokens/{id} — Revoke token"),
    ("GET /v1/pipelines", "GET /v1/pipelines — List pipelines"),
    ("POST /v1/pipelines/{id}/trigger", "POST /v1/pipelines/{id}/trigger — Trigger pipeline"),
]

# ── Changelog data ─────────────────────────────────────────────────────────────
CHANGELOG = [
    {
        "version": "v2.4.0",
        "date": "2026-04-01",
        "type": "feature",
        "highlights": [
            "Added pipeline triggers endpoint",
            "Restricted key scopes GA",
            "Webhook retry with exponential backoff",
        ],
        "breaking": False,
    },
    {
        "version": "v2.3.1",
        "date": "2026-03-15",
        "type": "fix",
        "highlights": [
            "Fixed cursor pagination off-by-one on large datasets",
            "Corrected 403 vs 404 for deleted resources",
        ],
        "breaking": False,
    },
    {
        "version": "v2.3.0",
        "date": "2026-02-20",
        "type": "feature",
        "highlights": [
            "Webhook signature verification (SHA-256)",
            "Event filter patterns for partial webhook subscriptions",
        ],
        "breaking": False,
    },
    {
        "version": "v2.2.0",
        "date": "2026-01-10",
        "type": "feature",
        "highlights": [
            "CDN edge promotion API",
            "Deployment rollback endpoint",
            "Workspace SSO integration",
        ],
        "breaking": False,
    },
    {
        "version": "v2.0.0",
        "date": "2025-11-01",
        "type": "breaking",
        "highlights": [
            "Switched to cursor-based pagination (remove page/offset params)",
            "Auth token format changed to fd_live_sk_ prefix",
            "Deprecated /v0 endpoints removed",
        ],
        "breaking": True,
    },
]

# ── API Keys data ──────────────────────────────────────────────────────────────
API_KEYS = [
    {
        "name": "Production",
        "prefix": "fd_live_sk_",
        "masked": "••••••••••••••••4821",
        "scope": "Full access",
        "created": "2026-01-15",
        "type": "live",
    },
    {
        "name": "Staging",
        "prefix": "fd_test_sk_",
        "masked": "••••••••••••••••9302",
        "scope": "Full access",
        "created": "2026-02-20",
        "type": "test",
    },
    {
        "name": "Read-only Deploy Bot",
        "prefix": "fd_restr_sk_",
        "masked": "••••••••••••••••1107",
        "scope": "deployments:read",
        "created": "2026-03-05",
        "type": "restricted",
    },
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
/* ═══════════════════════════════════════════════════════════
   ForgeDocs · Premium DevTool CSS
   Philosophy: technical precision — Inter + JetBrains Mono,
   dark-mode-first, rigid spacing, Stripe-quality sidebar.
   Atmospheric CSS only — Bootstrap + Faststrap for layout.
   ═══════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── Base shell ─────────────────────────────────────────── */
.fd-app {
  min-height: 100vh;
  font-family: "Inter", system-ui, sans-serif;
  background: #F8FAFC;
  color: #1E293B;
}

.fd-app[data-bs-theme="dark"] {
  background: #020617;
  color: #E2E8F0;
}

/* ── Monospace surfaces ─────────────────────────────────── */
.fd-app code, .fd-app pre, .fd-app .fd-mono {
  font-family: "JetBrains Mono", "Fira Code", monospace;
}

/* ── Top header ─────────────────────────────────────────── */
.fd-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(248, 250, 252, 0.92);
  backdrop-filter: blur(14px) saturate(1.4);
  border-bottom: 1px solid rgba(15, 23, 42, 0.08);
  padding: 0.75rem 0;
}

.fd-app[data-bs-theme="dark"] .fd-header {
  background: rgba(2, 6, 23, 0.92);
  border-bottom-color: rgba(255, 255, 255, 0.06);
}

/* ── Brand ───────────────────────────────────────────────── */
.fd-brand {
  font-weight: 800;
  letter-spacing: -0.04em;
  font-size: 1.2rem;
  text-decoration: none;
  color: #0F172A;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  transition: opacity 0.15s ease;
}

.fd-app[data-bs-theme="dark"] .fd-brand { color: #F8FAFC; }
.fd-brand:hover { opacity: 0.8; }

/* ── Search bar (focus-expand animation) ─────────────────── */
.fd-search-wrap { position: relative; }

.fd-search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: #94A3B8;
  pointer-events: none;
  z-index: 2;
}

.fd-search-input {
  width: 200px;
  padding-left: 2.2rem !important;
  border-radius: 8px !important;
  font-size: 0.84rem !important;
  border-color: rgba(15, 23, 42, 0.1) !important;
  background: rgba(15, 23, 42, 0.04) !important;
  transition: width 0.25s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s ease, box-shadow 0.2s ease !important;
}

.fd-app[data-bs-theme="dark"] .fd-search-input {
  border-color: rgba(255, 255, 255, 0.08) !important;
  background: rgba(255, 255, 255, 0.04) !important;
  color: #E2E8F0 !important;
}

.fd-search-input:focus {
  width: 300px !important;
  border-color: rgba(99, 102, 241, 0.4) !important;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
  background: #fff !important;
}

.fd-app[data-bs-theme="dark"] .fd-search-input:focus {
  background: rgba(255, 255, 255, 0.06) !important;
}

/* ── Left sidebar ────────────────────────────────────────── */
.fd-sidebar {
  position: sticky;
  top: 4.5rem;
  height: calc(100vh - 4.5rem);
  overflow-y: auto;
  scrollbar-width: thin;
  padding: 1.5rem 1rem 1.5rem 0;
  border-right: 1px solid rgba(15, 23, 42, 0.07);
}

.fd-app[data-bs-theme="dark"] .fd-sidebar { border-right-color: rgba(255, 255, 255, 0.06); }

.fd-sidebar::-webkit-scrollbar { width: 3px; }
.fd-sidebar::-webkit-scrollbar-track { background: transparent; }
.fd-sidebar::-webkit-scrollbar-thumb { background: rgba(99, 102, 241, 0.2); border-radius: 2px; }

/* Sidebar section headers */
.fd-sidebar-section {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #94A3B8;
  margin: 1.25rem 0 0.5rem 0.6rem;
}

/* Sidebar nav links */
.fd-nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.38rem 0.6rem;
  color: #475569;
  text-decoration: none;
  font-size: 0.875rem;
  border-radius: 6px;
  transition: color 0.12s ease, background 0.12s ease;
  position: relative;
}

.fd-app[data-bs-theme="dark"] .fd-nav-link { color: #94A3B8; }

.fd-nav-link:hover, .fd-nav-link.active {
  background: rgba(99, 102, 241, 0.08);
  color: #4F46E5;
}

.fd-app[data-bs-theme="dark"] .fd-nav-link:hover,
.fd-app[data-bs-theme="dark"] .fd-nav-link.active {
  background: rgba(99, 102, 241, 0.14);
  color: #818CF8;
}

.fd-nav-link.active {
  font-weight: 600;
}

/* Slide-in left bar on active */
.fd-nav-link.active::before {
  content: "";
  position: absolute;
  left: -1rem;
  top: 20%;
  bottom: 20%;
  width: 2px;
  background: #4F46E5;
  border-radius: 1px;
}

.fd-app[data-bs-theme="dark"] .fd-nav-link.active::before { background: #818CF8; }

/* ── Prose / content area ────────────────────────────────── */
.fd-prose {
  line-height: 1.75;
  font-size: 0.95rem;
}

.fd-prose h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.035em; margin-bottom: 0.5rem; }
.fd-prose h2 { font-size: 1.35rem; font-weight: 700; letter-spacing: -0.025em; margin-top: 2.5rem; margin-bottom: 0.75rem; padding-top: 1rem; border-top: 1px solid rgba(15, 23, 42, 0.07); }
.fd-prose h3 { font-size: 1.1rem; font-weight: 600; margin-top: 1.75rem; margin-bottom: 0.5rem; }

.fd-app[data-bs-theme="dark"] .fd-prose h2 { border-top-color: rgba(255, 255, 255, 0.06); }

/* Code blocks */
.fd-prose pre {
  background: #1E293B !important;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  color: #E2E8F0;
  margin: 1.25rem 0;
  overflow-x: auto;
  font-size: 0.83rem;
  line-height: 1.65;
  position: relative;
}

.fd-app[data-bs-theme="dark"] .fd-prose pre {
  background: #0F172A !important;
  border-color: rgba(255, 255, 255, 0.06);
}

/* Copy-to-clipboard: appears on hover */
.fd-prose pre:hover::after {
  content: "Copy";
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  background: rgba(99, 102, 241, 0.18);
  color: #818CF8;
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 5px;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  cursor: pointer;
  font-family: "Inter", system-ui, sans-serif;
}

/* Inline code */
.fd-prose code:not(pre code) {
  background: rgba(99, 102, 241, 0.1);
  color: #4F46E5;
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.85em;
}

.fd-app[data-bs-theme="dark"] .fd-prose code:not(pre code) {
  background: rgba(129, 140, 248, 0.15);
  color: #A5B4FC;
}

/* Tables */
.fd-prose table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin: 1.25rem 0; }
.fd-prose th { text-align: left; padding: 0.65rem 0.75rem; font-weight: 600; font-size: 0.78rem; border-bottom: 2px solid rgba(15, 23, 42, 0.1); color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; }
.fd-prose td { padding: 0.65rem 0.75rem; border-bottom: 1px solid rgba(15, 23, 42, 0.06); vertical-align: top; }
.fd-prose tr:last-child td { border-bottom: none; }

.fd-app[data-bs-theme="dark"] .fd-prose th { border-bottom-color: rgba(255, 255, 255, 0.08); color: #94A3B8; }
.fd-app[data-bs-theme="dark"] .fd-prose td { border-bottom-color: rgba(255, 255, 255, 0.04); }

/* Blockquotes */
.fd-prose blockquote {
  border-left: 3px solid #6366F1;
  padding: 0.75rem 1rem;
  background: rgba(99, 102, 241, 0.06);
  border-radius: 0 8px 8px 0;
  margin: 1.25rem 0;
  font-size: 0.9rem;
}

.fd-app[data-bs-theme="dark"] .fd-prose blockquote { background: rgba(99, 102, 241, 0.1); }

/* ── HTTP Method Badges ──────────────────────────────────── */
.fd-method {
  font-family: "JetBrains Mono", monospace;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  letter-spacing: 0.03em;
  display: inline-block;
}

.fd-method.get {
  background: rgba(16, 185, 129, 0.12);
  color: #059669;
  animation: fd-pulse-get 3s ease-in-out infinite;
}

.fd-method.post {
  background: rgba(56, 189, 248, 0.12);
  color: #0284C7;
  animation: fd-pulse-post 3s ease-in-out infinite;
}

.fd-method.put {
  background: rgba(245, 158, 11, 0.12);
  color: #D97706;
}

.fd-method.del {
  background: rgba(244, 63, 94, 0.12);
  color: #E11D48;
}

.fd-app[data-bs-theme="dark"] .fd-method.get { color: #34D399; }
.fd-app[data-bs-theme="dark"] .fd-method.post { color: #38BDF8; }
.fd-app[data-bs-theme="dark"] .fd-method.put { color: #FCD34D; }
.fd-app[data-bs-theme="dark"] .fd-method.del { color: #FB7185; }

@keyframes fd-pulse-get {
  0%, 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
  50% { box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1); }
}

@keyframes fd-pulse-post {
  0%, 100% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }
  50% { box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.1); }
}

/* ── Scrollspy TOC ───────────────────────────────────────── */
.fd-scrollspy-nav {
  position: sticky;
  top: 5rem;
  font-size: 0.8rem;
  border-left: 2px solid rgba(15, 23, 42, 0.08);
  padding-left: 1rem;
}

.fd-app[data-bs-theme="dark"] .fd-scrollspy-nav { border-left-color: rgba(255, 255, 255, 0.06); }

.fd-scrollspy-nav a {
  color: #64748B;
  text-decoration: none;
  display: block;
  padding: 0.25rem 0;
  transition: color 0.1s;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fd-app[data-bs-theme="dark"] .fd-scrollspy-nav a { color: #94A3B8; }

.fd-scrollspy-nav a.active {
  color: #4F46E5;
  font-weight: 600;
}

.fd-app[data-bs-theme="dark"] .fd-scrollspy-nav a.active { color: #818CF8; }

/* ── Mermaid frame ───────────────────────────────────────── */
.fd-diagram-frame {
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid rgba(99, 102, 241, 0.18);
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.04), rgba(56, 189, 248, 0.03));
  box-shadow: 0 0 0 1px rgba(99, 102, 241, 0.08);
}

.fd-app[data-bs-theme="dark"] .fd-diagram-frame {
  background: rgba(15, 23, 42, 0.5);
  border-color: rgba(99, 102, 241, 0.2);
}

/* ── Version badge pill ──────────────────────────────────── */
.fd-version-card {
  border-radius: 12px;
  border: 1px solid rgba(15, 23, 42, 0.07);
  background: #fff;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.fd-version-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
}

.fd-app[data-bs-theme="dark"] .fd-version-card {
  background: #0F172A;
  border-color: rgba(255, 255, 255, 0.06);
}

/* ── API Key row ─────────────────────────────────────────── */
.fd-key-row {
  border-radius: 10px;
  border: 1px solid rgba(15, 23, 42, 0.07);
  background: #fff;
  padding: 1rem 1.25rem;
  margin-bottom: 0.75rem;
  transition: border-color 0.15s ease;
}

.fd-key-row:hover { border-color: rgba(99, 102, 241, 0.25); }

.fd-app[data-bs-theme="dark"] .fd-key-row {
  background: #0F172A;
  border-color: rgba(255, 255, 255, 0.07);
}

/* ── Type color chips ────────────────────────────────────── */
.fd-key-live { color: #059669; background: rgba(16, 185, 129, 0.1); }
.fd-key-test { color: #0284C7; background: rgba(56, 189, 248, 0.1); }
.fd-key-restricted { color: #D97706; background: rgba(245, 158, 11, 0.1); }

/* ── Explorer panel ─────────────────────────────────────── */
.fd-explorer-panel {
  background: #0F172A;
  border-radius: 12px;
  padding: 1.25rem;
  color: #E2E8F0;
  font-family: "JetBrains Mono", monospace;
  font-size: 0.84rem;
  line-height: 1.65;
  border: 1px solid rgba(255, 255, 255, 0.06);
  min-height: 120px;
}

.fd-explorer-panel .fd-resp-200 { color: #4ade80; }
.fd-explorer-panel .fd-resp-key { color: #93C5FD; }
.fd-explorer-panel .fd-resp-str { color: #FCA5A5; }
"""

# ── App factory ────────────────────────────────────────────────────────────────
app = FastHTML(
    hdrs=[
        Script("""
document.addEventListener("DOMContentLoaded", function() {
    const isDark = document.cookie.includes("forgedocs_theme=dark");
    if (window.mermaid) {
        mermaid.initialize({
            startOnLoad: true,
            theme: isDark ? 'dark' : 'default',
            fontFamily: 'Inter, system-ui, sans-serif',
            fontSize: 14,
        });
    }
});
"""),
        *PageMeta(
            title="ForgeDocs API Reference",
            description="Official developer documentation for the ForgeDocs API. Authentication, pagination, endpoints, webhooks, and architecture guides.",
            keywords=["api", "docs", "developer", "forgedocs", "webhooks", "rest", "faststrap"],
            url="https://docs.forgedocs.io",
            type="website",
        ),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
        ),
        Script(
            defer=True,
            src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
        ),
    ]
)
add_bootstrap(app, theme=FORGEDOCS_THEME, font_family="Inter")


def theme_from_req(req) -> str:
    return req.session.get(THEME_KEY) or req.cookies.get(THEME_KEY, "dark")


def fd_theme_toggle(theme: str, cls: str = "") -> Any:
    return ThemeToggle(
        current_theme=theme,
        endpoint="/theme/toggle",
        toggle_id="forgedocs-theme-toggle",
        cls=cls,
    )


def fd_method_badge(method: str) -> Span:
    cls_map = {"GET": "get", "POST": "post", "PUT": "put", "DELETE": "del"}
    return Span(method, cls=f"fd-method {cls_map.get(method, '')}")


def fd_header(theme: str, active_page: str = "/") -> Div:
    pages = [
        ("/", "Reference"),
        ("/api-explorer", "API Explorer"),
        ("/changelog", "Changelog"),
        ("/keys", "API Keys"),
    ]
    return Div(
        Container(
            Div(
                A(
                    Svg(SVG_FORGE, sanitize=False, cls="text-primary"),
                    " ForgeDocs",
                    href="/",
                    cls="fd-brand",
                ),
                Nav(
                    *[
                        A(
                            label,
                            href=href,
                            cls=f"fd-nav-link {'active fw-600' if active_page == href else ''}",
                        )
                        for href, label in pages
                    ],
                    cls="d-none d-md-flex align-items-center gap-1",
                ),
                Div(
                    Div(
                        Icon("search", cls="fd-search-icon"),
                        Input(
                            "search_docs",
                            input_type="text",
                            placeholder="Search docs… ⌘K",
                            cls="form-control form-control-sm fd-search-input",
                        ),
                        cls="fd-search-wrap d-none d-md-block",
                    ),
                    fd_theme_toggle(theme, cls="ms-3"),
                    A(
                        "Dashboard",
                        href="#",
                        cls="btn btn-sm btn-outline-secondary ms-2 border-0 fw-500 d-none d-md-inline-flex",
                    ),
                    cls="d-flex align-items-center",
                ),
                cls="d-flex justify-content-between align-items-center",
            )
        ),
        cls="fd-header",
    )


def fd_sidebar(active: str = "#intro") -> Div:
    nav_items = [
        ("Getting Started", None, None),
        ("#intro", "Introduction", None),
        ("#auth", "Authentication", None),
        ("#pagination", "Pagination", None),
        ("#errors", "Errors", None),
        ("Core Resources", None, None),
        ("#endpoints", "Endpoints", None),
        ("#webhooks", "Webhooks", SVG_WEBHOOK),
        ("Reference", None, None),
        ("#architecture", "Architecture", None),
        ("#rate-limits", "Rate Limits", None),
    ]
    items = []
    for href, label, svg in nav_items:
        if href is None:
            items.append(Div(label, cls="fd-sidebar-section"))
        else:
            inner = [
                Svg(svg, sanitize=False, style="width:14px;height:14px") if svg else None,
                label,
            ]
            items.append(
                A(
                    *[x for x in inner if x],
                    href=href,
                    cls=f"fd-nav-link d-flex align-items-center gap-2 {'active' if active == href else ''}",
                )
            )
    return Div(*items, cls="fd-sidebar")


def fd_scrollspy_panel() -> Div:
    return Scrollspy(
        target="doc-content",
        items=[
            ("intro", "Introduction"),
            ("auth", "Authentication"),
            ("pagination", "Pagination"),
            ("errors", "Errors"),
            ("endpoints", "Endpoints"),
            ("webhooks", "Webhooks"),
            ("architecture", "Architecture"),
            ("rate-limits", "Rate Limits"),
        ],
        nav_cls="fd-scrollspy-nav",
        offset=100,
    )


def fd_code_tabs() -> tuple:
    tabs = Tabs(
        ("tab-curl", "cURL", True),
        ("tab-python", "Python", False),
        ("tab-node", "Node.js", False),
        ("tab-go", "Go", False),
    )
    content = Div(
        Div(
            Pre(
                Code(
                    'curl -X GET https://api.forgedocs.io/v1/workspaces \\\n  -H "Authorization: Bearer fd_live_sk_abc123xyz" \\\n  -H "Accept: application/json"'
                )
            ),
            id="tab-curl",
            cls="tab-pane fade show active",
        ),
        Div(
            Pre(
                Code(
                    'import requests\n\nheaders = {"Authorization": "Bearer fd_live_sk_abc123xyz"}\nr = requests.get(\n    "https://api.forgedocs.io/v1/workspaces",\n    headers=headers,\n)\nworkspaces = r.json()["data"]\nprint(f"Found {len(workspaces)} workspaces")'
                )
            ),
            id="tab-python",
            cls="tab-pane fade",
        ),
        Div(
            Pre(
                Code(
                    'const res = await fetch("https://api.forgedocs.io/v1/workspaces", {\n  headers: {\n    "Authorization": "Bearer fd_live_sk_abc123xyz",\n    "Accept": "application/json",\n  },\n});\nconst { data } = await res.json();\nconsole.log(`Found ${data.length} workspaces`);'
                )
            ),
            id="tab-node",
            cls="tab-pane fade",
        ),
        Div(
            Pre(
                Code(
                    'package main\n\nimport (\n    "fmt"\n    "net/http"\n)\n\nfunc main() {\n    req, _ := http.NewRequest("GET", "https://api.forgedocs.io/v1/workspaces", nil)\n    req.Header.Set("Authorization", "Bearer fd_live_sk_abc123xyz")\n    resp, _ := http.DefaultClient.Do(req)\n    defer resp.Body.Close()\n    fmt.Println("Status:", resp.StatusCode)\n}'
                )
            ),
            id="tab-go",
            cls="tab-pane fade",
        ),
        cls="tab-content mt-3 fd-prose",
    )
    return tabs, content


def fd_rate_limits_section() -> Div:
    return Div(
        H2("Rate Limits", id="rate-limits"),
        P("All endpoints are rate limited per API key. Limits vary by plan:"),
        Div(
            Div(
                Div(
                    Badge("Starter", variant="secondary"),
                    P("100 req/min", cls="fw-700 fs-5 my-1"),
                    P("Burst: 20 req/sec", cls="text-muted small mb-0"),
                    cls="p-4",
                ),
                cls="col-md-4 mb-3",
            ),
            Div(
                Div(
                    Badge("Growth", variant="primary"),
                    P("1,000 req/min", cls="fw-700 fs-5 my-1"),
                    P("Burst: 100 req/sec", cls="text-muted small mb-0"),
                    cls="p-4",
                ),
                cls="col-md-4 mb-3",
            ),
            Div(
                Div(
                    Badge("Scale", variant="success"),
                    P("10,000 req/min", cls="fw-700 fs-5 my-1"),
                    P("Burst: 500 req/sec", cls="text-muted small mb-0"),
                    cls="p-4",
                ),
                cls="col-md-4 mb-3",
            ),
            cls="row g-3 mb-3",
        ),
        P("Rate limit metadata is returned in every response header:"),
        Pre(
            Code(
                "X-RateLimit-Limit: 1000\nX-RateLimit-Remaining: 987\nX-RateLimit-Reset: 1712934600"
            ),
            cls="fd-prose",
        ),
        cls="mt-3",
    )


# ── ROUTES ────────────────────────────────────────────────────────────────────


@app.get("/")
def index(req) -> Any:
    theme = theme_from_req(req)
    code_tabs, code_content = fd_code_tabs()

    content = Div(
        Div(
            Span(
                "ForgeDocs",
                cls="text-primary fw-bold small text-uppercase mb-2 d-block",
                style="letter-spacing:.08em",
            ),
            H1("API Reference", id="intro", style="font-weight:800; letter-spacing:-0.04em"),
            Div(
                Badge("v2.4.0", variant="success", cls="me-2"),
                Badge("REST", variant="secondary", cls="me-2"),
                Badge("JSON", variant="secondary"),
                cls="mb-3",
            ),
            P(
                "The ForgeDocs API is organized around REST. It has predictable, resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.",
                cls="lead mb-0 text-muted",
            ),
            cls="mb-5",
        ),
        Div(Markdown(MD_AUTH), id="auth", cls="fd-prose"),
        code_tabs,
        code_content,
        Div(Markdown(MD_PAGINATION), id="pagination", cls="fd-prose mt-5"),
        Div(Markdown(MD_ERRORS), id="errors", cls="fd-prose mt-5"),
        Div(Markdown(MD_ENDPOINTS), id="endpoints", cls="fd-prose mt-5"),
        Div(Markdown(MD_WEBHOOKS), id="webhooks", cls="fd-prose mt-5"),
        Div(
            H2("Architecture", id="architecture"),
            P(
                "The ForgeDocs event ingestion pipeline is designed for high throughput and at-least-once delivery semantics with idempotent workers."
            ),
            Div(
                Mermaid(MERMAID_PIPELINE),
                cls="fd-diagram-frame my-4",
            ),
            P("Authentication flow:", cls="fw-600 mt-4 mb-2"),
            Div(
                Mermaid(MERMAID_AUTH),
                cls="fd-diagram-frame",
            ),
            P("Rate limit formula:", cls="fw-600 mt-4 mb-2"),
            Math(
                r"R = \frac{T}{W} \times C",
                display_mode=True,
            ),
            cls="fd-prose mt-5",
        ),
        fd_rate_limits_section(),
        Div(style="height:40vh"),
        id="doc-content",
        style="position:relative;",
    )

    return Div(
        Style(CSS),
        fd_header(theme, "/"),
        Container(
            Row(
                Col(fd_sidebar("#intro"), md=3, lg=2, cls="d-none d-md-block"),
                Col(content, md=9, lg=8, cls="py-4 px-md-4 px-lg-5"),
                Col(fd_scrollspy_panel(), lg=2, cls="d-none d-lg-block pt-4"),
            )
        ),
        data_bs_theme=theme,
        cls="fd-app",
        **{"data-bs-spy": "scroll", "data-bs-target": ".fd-scrollspy-nav", "data-bs-offset": "100"},
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    req.session[THEME_KEY] = "light" if theme_from_req(req) == "dark" else "dark"
    return hx_refresh()


@app.get("/api/endpoints/search")
def endpoints_search(q: str = "") -> Any:
    """HTMX search handler for SearchableSelect on the API Explorer page."""
    from fasthtml.common import A

    q_lower = q.lower()
    hits = [
        (value, label)
        for value, label in ENDPOINTS_INDEX
        if not q or q_lower in value.lower() or q_lower in label.lower()
    ][:12]
    if not hits:
        return Div(P("No endpoints matched.", cls="text-muted small px-3 py-2"), cls="list-group")
    return Div(
        *[
            A(
                label,
                href="#",
                cls="list-group-item list-group-item-action small fd-mono",
                data_value=value,
                data_fs_searchable_option="true",
            )
            for value, label in hits
        ],
        cls="list-group",
    )


@app.get("/api-explorer")
def api_explorer(req) -> Any:
    theme = theme_from_req(req)

    example_responses = {
        "GET /v1/workspaces": '{\n  "data": [\n    {\n      "id": "ws_Abc123",\n      "name": "Production",\n      "status": "active",\n      "region": "us-east-1",\n      "created_at": "2026-01-15T09:30:00Z"\n    }\n  ],\n  "next_cursor": null,\n  "has_more": false,\n  "total_count": 1\n}',
        "POST /v1/deployments": '{\n  "id": "dep_XyZ789",\n  "workspace_id": "ws_Abc123",\n  "status": "queued",\n  "commit_sha": "a1b2c3d4",\n  "created_at": "2026-04-11T13:24:00Z"\n}',
        "POST /v1/webhooks": '{\n  "id": "wh_Def456",\n  "url": "https://yourapp.com/hooks/forgedocs",\n  "events": ["deployment.completed", "deployment.failed"],\n  "active": true,\n  "created_at": "2026-04-11T13:24:00Z"\n}',
    }

    default_resp = example_responses["GET /v1/workspaces"]

    return Div(
        Style(CSS),
        fd_header(theme, "/api-explorer"),
        Container(
            Div(
                Div(
                    Span(
                        "Interactive",
                        cls="text-primary fw-bold small text-uppercase mb-1 d-block",
                        style="letter-spacing:.08em",
                    ),
                    H1("API Explorer", style="font-weight:800;letter-spacing:-0.04em"),
                    P(
                        "Select an endpoint, inspect the request, and see a realistic mock response. In production, this would fire against a sandbox environment.",
                        cls="lead text-muted",
                    ),
                    cls=f"mb-5 {Fx.base} {Fx.fade_in}",
                ),
                Row(
                    Col(
                        Div(
                            H5("Select Endpoint", cls="fw-bold mb-3"),
                            SearchableSelect(
                                "/api/endpoints/search",
                                name="endpoint",
                                placeholder="Search endpoints… e.g. workspaces",
                                initial_options=ENDPOINTS_INDEX[:6],
                                csp_safe=True,
                                cls="mb-3",
                            ),
                            H5("Request Headers", cls="fw-bold mb-2"),
                            InputGroup(
                                InputGroupText("Authorization"),
                                Input(
                                    "auth_header",
                                    input_type="text",
                                    value="Bearer fd_live_sk_••••••••4821",
                                    cls="form-control fd-mono",
                                    readonly=True,
                                ),
                                cls="mb-3",
                            ),
                            InputGroup(
                                InputGroupText("Content-Type"),
                                Input(
                                    "content_type_header",
                                    input_type="text",
                                    value="application/json",
                                    cls="form-control fd-mono",
                                    readonly=True,
                                ),
                                cls="mb-4",
                            ),
                            H5("Request Body (POST only)", cls="fw-bold mb-2"),
                            Div(
                                Pre(
                                    '{\n  "name": "my-workspace",\n  "region": "us-east-1"\n}',
                                    style="margin:0;font-size:0.82rem;line-height:1.6;",
                                ),
                                cls="fd-explorer-panel mb-4",
                            ),
                            Button(
                                Icon("send-fill", cls="me-2"),
                                "Send Request",
                                cls="btn btn-primary w-100 fw-600",
                                style="border-radius:10px;min-height:2.75rem",
                            ),
                        ),
                        md=5,
                        cls="mb-4",
                    ),
                    Col(
                        Div(
                            H5("Response", cls="fw-bold mb-3"),
                            Div(
                                Div(
                                    Div(
                                        Span("●", cls="text-success me-1"),
                                        Span("200 OK", cls="fw-600"),
                                        cls="d-flex align-items-center",
                                    ),
                                    Div("application/json · 142ms", cls="text-muted small"),
                                    cls="d-flex justify-content-between align-items-center mb-3",
                                ),
                                Pre(
                                    default_resp,
                                    style="background:transparent;border:none;padding:0;color:#93C5FD;margin:0;font-size:0.81rem;line-height:1.65;",
                                ),
                                cls="fd-explorer-panel",
                            ),
                            H5("Available Endpoints", cls="fw-bold mt-4 mb-3"),
                            Div(
                                *[
                                    Div(
                                        fd_method_badge(method),
                                        Span(path, cls="ms-2 fd-mono small"),
                                        cls="mb-2 d-flex align-items-center",
                                    )
                                    for method, path in [
                                        ("GET", "/v1/workspaces"),
                                        ("POST", "/v1/workspaces"),
                                        ("POST", "/v1/deployments"),
                                        ("GET", "/v1/deployments/{id}"),
                                        ("POST", "/v1/webhooks"),
                                        ("GET", "/v1/tokens"),
                                        ("DELETE", "/v1/tokens/{id}"),
                                    ]
                                ],
                                cls="fd-key-row",
                            ),
                        ),
                        md=7,
                        cls="mb-4",
                    ),
                ),
            ),
            cls="py-5",
        ),
        data_bs_theme=theme,
        cls="fd-app",
    )


@app.get("/changelog")
def changelog(req) -> Any:
    theme = theme_from_req(req)

    type_map = {
        "feature": ("success", "stars"),
        "fix": ("info", "bug"),
        "breaking": ("danger", "exclamation-triangle-fill"),
    }

    version_cards = []
    for entry in CHANGELOG:
        badge_variant, badge_icon = type_map.get(entry["type"], ("secondary", "info-circle"))
        version_cards.append(
            Div(
                Div(
                    Div(
                        Badge(entry["version"], variant=badge_variant, cls="me-2 px-3 py-2 fs-6"),
                        Badge(
                            "Breaking change" if entry["breaking"] else entry["type"].title(),
                            variant="danger" if entry["breaking"] else "light",
                            cls="" if entry["breaking"] else "text-muted",
                        ),
                        cls="d-flex align-items-center flex-wrap gap-2 mb-1",
                    ),
                    Small(entry["date"], cls="text-muted fd-mono"),
                    cls="mb-3",
                ),
                Ul(
                    *[Li(h, cls="mb-1") for h in entry["highlights"]],
                    cls="mb-0",
                ),
                cls="fd-version-card p-4 mb-3",
            )
        )

    return Div(
        Style(CSS),
        fd_header(theme, "/changelog"),
        Container(
            Div(
                Div(
                    Span(
                        "History",
                        cls="text-primary fw-bold small text-uppercase mb-1 d-block",
                        style="letter-spacing:.08em",
                    ),
                    H1("Changelog", style="font-weight:800;letter-spacing:-0.04em"),
                    P(
                        "All notable changes to the ForgeDocs API. Breaking changes are marked clearly.",
                        cls="lead text-muted",
                    ),
                    cls="mb-5",
                ),
                Row(
                    Col(
                        *version_cards,
                        md=8,
                    ),
                    Col(
                        Div(
                            H5("Subscribe to updates", cls="fw-bold mb-2"),
                            P(
                                "Get notified about new versions and breaking changes.",
                                cls="text-muted small mb-3",
                            ),
                            InputGroup(
                                Input(
                                    "email",
                                    input_type="email",
                                    placeholder="your@email.com",
                                    cls="form-control",
                                ),
                                Button("Subscribe", cls="btn btn-primary"),
                            ),
                            Hr(),
                            H5("Version support", cls="fw-bold mb-2"),
                            Div(
                                *[
                                    Div(
                                        Div(v, cls="fw-600 small"),
                                        Badge(status, variant=bv),
                                        cls="d-flex justify-content-between align-items-center py-2 border-bottom",
                                    )
                                    for v, status, bv in [
                                        ("v2.x (current)", "Supported", "success"),
                                        ("v1.x", "Maintenance", "warning"),
                                        ("v0.x", "Deprecated", "danger"),
                                    ]
                                ],
                            ),
                        ),
                        md=4,
                        cls="ps-md-4",
                    ),
                ),
            ),
            cls="py-5",
        ),
        data_bs_theme=theme,
        cls="fd-app",
    )


@app.get("/keys")
def api_keys_page(req) -> Any:
    theme = theme_from_req(req)

    return Div(
        Style(CSS),
        fd_header(theme, "/keys"),
        Container(
            Div(
                Alert(
                    Strong("Security reminder: "),
                    " Never share your live keys. Revoke and rotate immediately if you suspect exposure. All key events are logged.",
                    variant="warning",
                    dismissible=True,
                    cls="mb-4",
                ),
                Div(
                    Div(
                        Span(
                            "Authentication",
                            cls="text-primary fw-bold small text-uppercase mb-1 d-block",
                            style="letter-spacing:.08em",
                        ),
                        H1("API Keys", style="font-weight:800;letter-spacing:-0.04em"),
                        P(
                            "Manage your authentication credentials. Keys are secret — treat them like passwords.",
                            cls="lead text-muted",
                        ),
                    ),
                    Button(
                        Icon("plus", cls="me-2"),
                        "Create Key",
                        cls="btn btn-primary fw-600 align-self-start",
                        style="border-radius:10px",
                    ),
                    cls="d-flex flex-column flex-md-row justify-content-between gap-3 mb-5",
                ),
                Row(
                    Col(
                        H5("Active Keys", cls="fw-bold mb-3"),
                        *[
                            Div(
                                Div(
                                    Div(
                                        Div(key["name"], cls="fw-700 mb-1"),
                                        Div(
                                            Span(
                                                key["type"].title(),
                                                cls=f"badge fd-key-{key['type']} me-2 px-2 py-1 rounded-2",
                                                style="font-size:0.7rem",
                                            ),
                                            Span(key["scope"], cls="text-muted small"),
                                        ),
                                        Small(f"Created {key['created']}", cls="text-muted"),
                                    ),
                                    Div(
                                        InputGroup(
                                            InputGroupText(key["prefix"]),
                                            Input(
                                                f"key_{i}",
                                                input_type="password",
                                                value="secret_value_here",
                                                cls="form-control fd-mono",
                                                style="max-width:180px;font-size:0.82rem;",
                                                id=f"key-{i}",
                                                **{"data-value": key["masked"]},
                                            ),
                                            Button(
                                                Icon("eye"),
                                                cls="btn btn-outline-secondary",
                                                onclick=f"var el=document.getElementById('key-{i}');el.type=el.type==='password'?'text':'password'",
                                            ),
                                            cls="mb-2",
                                        ),
                                        Div(
                                            Button(
                                                "Copy", cls="btn btn-sm btn-outline-secondary me-1"
                                            ),
                                            Button(
                                                "Rotate", cls="btn btn-sm btn-outline-warning me-1"
                                            ),
                                            Button("Revoke", cls="btn btn-sm btn-outline-danger"),
                                            cls="d-flex gap-1",
                                        ),
                                        cls="d-flex flex-column align-items-end",
                                    ),
                                    cls="d-flex justify-content-between align-items-start flex-wrap gap-3",
                                ),
                                cls="fd-key-row",
                            )
                            for i, key in enumerate(API_KEYS)
                        ],
                        lg=8,
                    ),
                    Col(
                        Div(
                            H5("Best Practices", cls="fw-bold mb-3"),
                            Div(
                                *[
                                    Div(
                                        Icon(icon, cls="text-primary me-2"),
                                        tip,
                                        cls="d-flex align-items-start mb-2 small",
                                    )
                                    for icon, tip in [
                                        (
                                            "shield-check",
                                            "Use restricted keys with minimal scopes in CI/CD",
                                        ),
                                        ("arrow-repeat", "Rotate live keys every 90 days"),
                                        (
                                            "eye-slash",
                                            "Store keys in environment variables, not source code",
                                        ),
                                        ("journal-check", "Monitor key usage in the audit log"),
                                        ("x-circle", "Revoke unused keys immediately"),
                                    ]
                                ],
                            ),
                            Hr(),
                            H5("Audit Log", cls="fw-bold mb-3"),
                            Div(
                                *[
                                    Div(
                                        Span(evt, cls="small fw-500"),
                                        Span(ts, cls="text-muted small fd-mono"),
                                        cls="d-flex justify-content-between py-2 border-bottom",
                                    )
                                    for evt, ts in [
                                        ("Key created (Staging)", "2026-04-11 09:14"),
                                        ("Key rotated (Production)", "2026-03-15 16:22"),
                                        ("Key revoked (Old Bot)", "2026-03-01 11:08"),
                                        ("Key created (Production)", "2026-01-15 09:30"),
                                    ]
                                ],
                            ),
                        ),
                        lg=4,
                    ),
                ),
            ),
            cls="py-5",
        ),
        data_bs_theme=theme,
        cls="fd-app",
    )


if __name__ == "__main__":
    serve(port=5013)
