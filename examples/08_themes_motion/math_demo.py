"""
Faststrap v0.9.0 Math Demo

Demonstrates KaTeX-based math/chemistry rendering:
- Math inline
- Math display mode
- Chemistry (mhchem)
- Physics formulas
"""

from fasthtml.common import (
    FastHTML,
    H1,
    H2,
    P,
    Link,
    Script,
    serve,
)

from faststrap import Container, Math, add_bootstrap

app = FastHTML(
    hdrs=(
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"),
        Script(src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/mhchem.min.js"),
    )
)
add_bootstrap(app, theme="indigo-night", mode="light")


@app.get("/")
def home():
    return Container(
        H1("Faststrap v0.9.0 — Math", cls="display-5 fw-bold mb-2"),
        P(
            "KaTeX-based LaTeX math and chemistry rendering.",
            cls="lead text-muted mb-4",
        ),
        H2("Inline Math", cls="h4 mb-3"),
        P(
            "The quadratic formula: ",
            Math(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
            " is fundamental to algebra.",
        ),
        H2("Display Mode", cls="h4 mb-3 mt-4"),
        Math(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}",
            display_mode=True,
        ),
        H2("Chemistry", cls="h4 mb-3 mt-4"),
        P(
            "Water formation: ",
            Math(r"\ce{2H2 + O2 -> 2H2O}"),
            " and combustion: ",
            Math(r"\ce{CH4 + 2O2 -> CO2 + 2H2O}"),
        ),
        Math(
            r"\ce{2H2 + O2 ->[ignite] 2H2O}",
            display_mode=True,
        ),
        H2("Physics", cls="h4 mb-3 mt-4"),
        P(
            "Newton's law of universal gravitation: ",
            Math(r"F = G \frac{m_1 m_2}{r^2}"),
        ),
        Math(
            r"E = mc^2",
            display_mode=True,
        ),
        H2("Maxwell's Equations", cls="h4 mb-3 mt-4"),
        Math(
            r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}",
            display_mode=True,
        ),
        cls="my-5",
    )


if __name__ == '__main__':
    serve()
