"""
09_integrations/pwa.py
Demonstrates: PwaMeta, InstallPrompt

PwaMeta: injects PWA manifest link tags and meta tags into the <head>.
InstallPrompt: a dismissible banner that prompts users to install the app.

To make a full PWA you also need:
  1. A manifest.json at /manifest.json
  2. A service worker registered at /sw.js
  3. Icons at the paths specified in PwaMeta
"""

from fasthtml.common import FastHTML, H1, H2, P, Div, A, serve
from faststrap import (
    add_bootstrap,
    Container,
    PwaMeta,
    InstallPrompt,
    Card,
    Stack,
    CodeBlock,
    Alert,
    Button,
    Row,
    Col,
)

app = FastHTML()
add_bootstrap(app, theme="blue-ocean", mode="light")

MANIFEST_EXAMPLE = """{
  "name": "My Faststrap App",
  "short_name": "FSApp",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0066cc",
  "icons": [
    { "src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}"""

SW_EXAMPLE = """// public/sw.js
const CACHE = "my-app-v1";
const ASSETS = ["/", "/static/bootstrap.min.css"];

self.addEventListener("install", e => {
    e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});

self.addEventListener("fetch", e => {
    e.respondWith(
        caches.match(e.request).then(r => r || fetch(e.request))
    );
});"""


@app.get("/")
def home():
    pwa_meta = PwaMeta(
        name="My Faststrap App",
        short_name="FSApp",
        theme_color="#0066cc",
        background_color="#ffffff",
        description="A demo PWA built with Faststrap",
        icon_path="/assets/icon.png",
        icon_192="/assets/icon-192.png",
        icon_512="/assets/icon-512.png",
        manifest_path="/manifest.json",
    )
    return (
        # PwaMeta returns a tuple of <meta> and <link> tags for the <head>
        *pwa_meta,
        # InstallPrompt is the visible banner
        InstallPrompt(
            app_name="My Faststrap App",
            message="Install this app for the best experience",
            install_text="Install",
        ),
        Container(
            H1("Progressive Web App (PWA)", cls="display-5 fw-bold mb-2"),
            P(
                "PwaMeta injects the required manifest and meta tags. "
                "InstallPrompt shows a dismissible install banner.",
                cls="lead text-muted mb-5",
            ),

            Alert(
                "The purple install banner above was added by InstallPrompt. "
                "PwaMeta injected the manifest link into the page <head>.",
                variant="info",
                cls="mb-4",
            ),

            H2("PwaMeta — usage", cls="h4 fw-semibold mb-1"),
            P("PwaMeta() returns a tuple of tags that must be unpacked into the response:", cls="text-muted mb-3"),
            CodeBlock(
                '''pwa_meta = PwaMeta(
    name="My App",
    short_name="App",
    theme_color="#0066cc",
    manifest_path="/manifest.json",
    icon_192="/assets/icon-192.png",
    icon_512="/assets/icon-512.png",
)

@app.get("/")
def home():
    return (
        *pwa_meta,          # ← unpack meta tags into response tuple
        Container(...),     # ← your page content
    )''',
                language="python", copy=True,
            ),

            H2("manifest.json", cls="h4 fw-semibold mb-3 mt-5"),
            CodeBlock(MANIFEST_EXAMPLE, language="json", filename="manifest.json", copy=True),

            H2("Service Worker", cls="h4 fw-semibold mb-3 mt-5"),
            CodeBlock(SW_EXAMPLE, language="javascript", filename="sw.js", copy=True),

            cls="my-5",
        ),
    )


if __name__ == "__main__":
    serve()
