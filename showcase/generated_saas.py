"""Refactr — Developer automation SaaS landing page.

Full-featured reference showcase for the Faststrap framework:

- create_theme() brand palette (violet/cyan)
- Custom atmosphere CSS (shell gradients, glassmorphism)
- NavbarModern + ThemeToggle + cookie persistence
- Hero with live code console (architectural geometry)
- Logo trust rail
- FeatureGrid (6 cards)
- How-it-works 3-step visual
- PricingGroup (3 tiers) with featured tier
- TestimonialSection (3 cards)
- Newsletter CTA with LoadingButton
- FooterModern
- ActiveSearch with /api/search endpoint
- /api/subscribe endpoint with ToastContainer feedback
- Full dual-mode: dark default, ThemeToggle to light
- PageMeta for SEO
- Port 5010
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# ruff: noqa: E402
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from fasthtml.common import (
    H1,
    H2,
    A,
    Br,
    Code,
    Div,
    FastHTML,
    Form,
    P,
    Pre,
    Section,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Badge,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    Input,
    PageMeta,
    PricingGroup,
    PricingTier,
    Row,
    Testimonial,
    TestimonialSection,
    ThemeToggle,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import ActiveSearch, LoadingButton, hx_refresh, toast_response

# ── Theme ────────────────────────────────────────────────────────────────────
THEME_COOKIE = "refactr_theme"

REFACTR_THEME = create_theme(
    primary="#7000FF",
    secondary="#111827",
    success="#00C896",
    danger="#FF4560",
    warning="#FFB400",
    info="#00D4FF",
    radius="0.5rem",
    radius_lg="0.875rem",
    surface_bg_dark="#0b0b14",
    surface_muted_bg_dark="#111120",
)

app = FastHTML()
add_bootstrap(app, font_family="Outfit", theme=REFACTR_THEME, mode="dark")

# ── Custom CSS ───────────────────────────────────────────────────────────────
CUSTOM_CSS = Style("""
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Weight utilities ────────────────────────────────────────── */
.fw-500 { font-weight: 500 !important; }
.fw-600 { font-weight: 600 !important; }
.fw-700 { font-weight: 700 !important; }
.fw-800 { font-weight: 800 !important; }
.fw-900 { font-weight: 900 !important; }

/* ── Page shell ──────────────────────────────────────────────── */
.refactr-shell {
  background:
    radial-gradient(ellipse at 4% 0%, rgba(112, 0, 255, 0.22) 0%, transparent 38%),
    radial-gradient(ellipse at 92% 6%, rgba(0, 212, 255, 0.14) 0%, transparent 30%),
    linear-gradient(180deg, #05050e 0%, #090914 50%, #0e0e1c 100%);
  min-height: 100vh;
  color: #e2e8f0;
  overflow-x: hidden;
}

.refactr-shell[data-bs-theme="light"] {
  background:
    radial-gradient(ellipse at 4% 0%, rgba(112, 0, 255, 0.10) 0%, transparent 40%),
    radial-gradient(ellipse at 92% 6%, rgba(0, 212, 255, 0.07) 0%, transparent 30%),
    linear-gradient(180deg, #f8f7ff 0%, #f2f2fd 100%);
  color: #0f0f2a;
}

/* ── Navbar ──────────────────────────────────────────────────── */
.refactr-nav-wrap {
  position: sticky;
  top: 0;
  z-index: 30;
  background: rgba(5, 5, 14, 0.82);
  backdrop-filter: blur(20px) saturate(1.5);
  -webkit-backdrop-filter: blur(20px) saturate(1.5);
  border-bottom: 1px solid rgba(255, 255, 255, 0.055);
  padding: 0;
}

.refactr-shell[data-bs-theme="light"] .refactr-nav-wrap {
  background: rgba(250, 249, 255, 0.92);
  border-bottom-color: rgba(112, 0, 255, 0.09);
}

.refactr-navbar {
  background: transparent;
  border: none;
  border-radius: 0;
  box-shadow: none;
  padding: 0.7rem 0;
}

.refactr-navbar .nav-link {
  color: rgba(203, 213, 225, 0.75);
  font-size: 0.86rem;
  font-weight: 500;
  border-radius: 4px;
  padding: 0.38rem 0.8rem !important;
  transition: color 0.15s ease, background 0.15s ease;
}
.refactr-navbar .nav-link:hover { color: #fff; background: rgba(255,255,255,0.07); }
.refactr-shell[data-bs-theme="light"] .refactr-navbar .nav-link { color: rgba(15,15,42,0.68); }
.refactr-shell[data-bs-theme="light"] .refactr-navbar .nav-link:hover { color: #7000FF; background: rgba(112,0,255,0.06); }

/* Brand */
.refactr-brand {
  font-family: 'Outfit', sans-serif;
  font-weight: 900;
  font-size: 1.45rem;
  background: linear-gradient(135deg, #7000FF 30%, #00D4FF);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.03em;
}

/* ── Hero ────────────────────────────────────────────────────── */
.refactr-hero { padding: 5.5rem 0 4.5rem; position: relative; z-index: 1; }

.refactr-hero::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 -8rem;
  width: 26rem; height: 26rem;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(112,0,255,0.16), transparent 68%);
  filter: blur(48px);
  pointer-events: none;
  z-index: 0;
}

.refactr-kicker {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.3rem 0.75rem;
  border-radius: 4px;
  background: rgba(112, 0, 255, 0.12);
  border: 1px solid rgba(112, 0, 255, 0.22);
  color: #bf80ff;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}
.refactr-shell[data-bs-theme="light"] .refactr-kicker { color: #5500cc; background: rgba(112,0,255,0.06); border-color: rgba(112,0,255,0.16); }

.refactr-display {
  font-size: clamp(2.8rem, 6vw, 5.2rem);
  line-height: 1.02;
  letter-spacing: -0.045em;
  font-weight: 900;
  color: #f0f4ff;
}
.refactr-shell[data-bs-theme="light"] .refactr-display { color: #0a0a22; }

.refactr-gradient-text {
  background: linear-gradient(135deg, #00D4FF 0%, #7000FF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.refactr-subtitle {
  color: rgba(148, 163, 184, 0.88);
  font-size: 1.025rem;
  line-height: 1.72;
  max-width: 42rem;
}
.refactr-shell[data-bs-theme="light"] .refactr-subtitle { color: rgba(30,30,60,0.65); }

/* ── Code console ────────────────────────────────────────────── */
.refactr-console {
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(160deg, #0a0a1e, #060614);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.05),
    0 0 0 1px rgba(0,0,0,0.5),
    0 32px 80px rgba(0,0,0,0.55),
    0 0 60px rgba(112,0,255,0.08);
}

.refactr-console-bar {
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.025);
  padding: 0.65rem 1rem;
}

.refactr-dot {
  width: 0.58rem; height: 0.58rem;
  border-radius: 50%;
  display: inline-block;
}

.refactr-code {
  font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, monospace;
  font-size: 0.79rem;
  line-height: 1.9;
  color: #c4b5fd;
  white-space: pre-wrap;
}

.refactr-code .kw  { color: #7000FF; }
.refactr-code .fn  { color: #00D4FF; }
.refactr-code .str { color: #00C896; }
.refactr-code .cm  { color: rgba(148,163,184,0.45); }

/* ── Trust rail ──────────────────────────────────────────────── */
.refactr-trust-rail {
  border-top: 1px solid rgba(255,255,255,0.05);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  background: rgba(255, 255, 255, 0.018);
  padding: 1.5rem 0;
}
.refactr-shell[data-bs-theme="light"] .refactr-trust-rail {
  background: rgba(112,0,255,0.025);
  border-color: rgba(112,0,255,0.07);
}

.refactr-trust-pill {
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.025);
  color: rgba(203, 213, 225, 0.7);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.4rem 0.85rem;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  letter-spacing: 0.01em;
  transition: color 0.15s ease, border-color 0.15s ease;
}
.refactr-trust-pill:hover { color: #fff; border-color: rgba(112,0,255,0.3); }
.refactr-shell[data-bs-theme="light"] .refactr-trust-pill {
  border-color: rgba(112,0,255,0.1);
  background: rgba(255,255,255,0.8);
  color: rgba(15,15,42,0.6);
}
.refactr-shell[data-bs-theme="light"] .refactr-trust-pill:hover { color: #5500cc; }

/* ── Sections ────────────────────────────────────────────────── */
.refactr-section { padding: 5rem 0; }
.refactr-section-alt {
  background: rgba(255, 255, 255, 0.016);
  border-top: 1px solid rgba(255, 255, 255, 0.04);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}
.refactr-shell[data-bs-theme="light"] .refactr-section-alt {
  background: rgba(112, 0, 255, 0.03);
  border-color: rgba(112,0,255,0.07);
}

.refactr-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.28rem 0.65rem;
  border-radius: 4px;
  background: rgba(112, 0, 255, 0.09);
  border: 1px solid rgba(112, 0, 255, 0.16);
  color: #bf80ff;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}
.refactr-shell[data-bs-theme="light"] .refactr-eyebrow { color: #5500cc; }

.refactr-h2 {
  font-size: clamp(1.9rem, 3.8vw, 3rem);
  font-weight: 800;
  letter-spacing: -0.035em;
  line-height: 1.08;
  color: #f0f4ff;
}
.refactr-shell[data-bs-theme="light"] .refactr-h2 { color: #0a0a22; }

.refactr-body-muted {
  color: rgba(148, 163, 184, 0.8);
  font-size: 0.96rem;
  line-height: 1.68;
}
.refactr-shell[data-bs-theme="light"] .refactr-body-muted { color: rgba(30,30,60,0.58); }

/* ── Feature cards ───────────────────────────────────────────── */
.refactr-feature-card {
  position: relative;
  overflow: hidden;
  padding: 1.5rem 1.5rem 1.5rem 1.75rem;
  border-radius: 7px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.07);
  height: 100%;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  color: #e2e8f0;
}
.refactr-feature-card::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 3px;
  background: linear-gradient(180deg, #7000FF, #00D4FF);
  opacity: 0;
  transition: opacity 0.2s ease;
}
.refactr-feature-card:hover::before { opacity: 1; }
.refactr-feature-card:hover {
  transform: translateY(-4px);
  border-color: rgba(112, 0, 255, 0.2);
  box-shadow: 0 12px 40px rgba(112,0,255,0.08);
}
.refactr-shell[data-bs-theme="light"] .refactr-feature-card {
  background: #fff;
  border-color: rgba(15,23,42,0.08);
  color: #0f172a;
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
}
.refactr-shell[data-bs-theme="light"] .refactr-feature-card:hover {
  border-color: rgba(112,0,255,0.18);
  box-shadow: 0 12px 36px rgba(112,0,255,0.06);
}

.refactr-feat-icon {
  width: 2.6rem; height: 2.6rem;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
  margin-bottom: 1rem;
  background: rgba(112, 0, 255, 0.14);
  color: #bf80ff;
}
.refactr-shell[data-bs-theme="light"] .refactr-feat-icon {
  background: rgba(112,0,255,0.08);
  color: #7000FF;
}

/* ── Steps ───────────────────────────────────────────────────── */
.refactr-step-num {
  width: 2.4rem; height: 2.4rem;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 0.88rem;
  background: linear-gradient(135deg, #7000FF, #00D4FF);
  color: #fff;
  flex-shrink: 0;
  box-shadow: 0 4px 14px rgba(112,0,255,0.28);
  letter-spacing: 0.01em;
}

.refactr-step-card {
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.025);
  padding: 1.75rem;
  height: 100%;
  transition: border-color 0.2s ease, transform 0.2s ease;
}
.refactr-step-card:hover { border-color: rgba(112,0,255,0.25); transform: translateY(-3px); }
.refactr-shell[data-bs-theme="light"] .refactr-step-card {
  background: #fff;
  border-color: rgba(15,23,42,0.08);
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
}
.refactr-shell[data-bs-theme="light"] .refactr-step-card:hover { border-color: rgba(112,0,255,0.2); }

/* ── Pricing ─────────────────────────────────────────────────── */
.pricing-group .card {
  border: 1px solid rgba(255, 255, 255, 0.07) !important;
  border-radius: 8px !important;
  background: rgba(255, 255, 255, 0.03) !important;
  color: #e2e8f0;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.pricing-group .card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 2px;
  background: rgba(112,0,255,0.25);
  border-radius: 8px 8px 0 0;
}
.pricing-group .card.border-primary {
  border-color: rgba(112, 0, 255, 0.35) !important;
  box-shadow: 0 0 0 1px rgba(112,0,255,0.18), 0 20px 52px rgba(112,0,255,0.14);
}
.pricing-group .card.border-primary::before {
  height: 3px;
  background: linear-gradient(90deg, #7000FF, #00D4FF);
}
.pricing-group .card:hover { transform: translateY(-4px); }

.refactr-shell[data-bs-theme="light"] .pricing-group .card {
  background: #fff !important;
  border-color: rgba(15,23,42,0.08) !important;
  color: #0f172a;
  box-shadow: 0 2px 8px rgba(15,23,42,0.04);
}
.refactr-shell[data-bs-theme="light"] .pricing-group .card.border-primary {
  border-color: rgba(112,0,255,0.28) !important;
  box-shadow: 0 0 0 1px rgba(112,0,255,0.15), 0 20px 48px rgba(112,0,255,0.08);
}
.pricing-group .text-muted { color: rgba(148,163,184,0.78) !important; }
.refactr-shell[data-bs-theme="light"] .pricing-group .text-muted { color: #64748b !important; }
.pricing-group .btn { min-height: 2.7rem; font-weight: 700; border-radius: 5px; }

/* ── Testimonials ────────────────────────────────────────────── */
.refactr-testi .card {
  position: relative;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 8px;
  background: rgba(255,255,255,0.03);
  color: #e2e8f0;
  box-shadow: 0 12px 40px rgba(0,0,0,0.18);
  transition: border-color 0.2s ease, transform 0.2s ease;
}
.refactr-testi .card:hover { border-color: rgba(112,0,255,0.2) !important; transform: translateY(-3px); }
.refactr-testi .card::after {
  content: "\201C";
  position: absolute;
  top: 0.75rem; right: 1.25rem;
  font-size: 3.5rem;
  line-height: 1;
  color: rgba(112,0,255,0.08);
  font-weight: 900;
}
.refactr-testi .text-muted { color: rgba(148,163,184,0.75) !important; }
.refactr-shell[data-bs-theme="light"] .refactr-testi .card {
  background: #fff;
  border-color: rgba(15,23,42,0.08) !important;
  color: #0f172a;
  box-shadow: 0 2px 10px rgba(15,23,42,0.05);
}
.refactr-shell[data-bs-theme="light"] .refactr-testi .text-muted { color: #64748b !important; }

/* ── CTA strip ───────────────────────────────────────────────── */
.refactr-cta {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(112,0,255,0.28), transparent 55%),
    radial-gradient(ellipse at 82% 55%, rgba(0,212,255,0.18), transparent 45%),
    linear-gradient(135deg, #08081a, #0f0020);
  border-radius: 12px;
  border: 1px solid rgba(112,0,255,0.2);
  padding: 4rem 2.5rem;
}
.refactr-shell[data-bs-theme="light"] .refactr-cta {
  background: linear-gradient(135deg, #f5f0ff, #eff8ff);
  border-color: rgba(112,0,255,0.18);
}

/* ── Search panel ────────────────────────────────────────────── */
.refactr-search-panel {
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 8px;
  background: rgba(255,255,255,0.025);
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.refactr-shell[data-bs-theme="light"] .refactr-search-panel {
  background: #fff;
  border-color: rgba(15,23,42,0.08);
  box-shadow: 0 4px 20px rgba(15,23,42,0.06);
}
.refactr-search-result.card {
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 5px;
  background: rgba(255,255,255,0.02);
  color: #e2e8f0;
  transition: border-color 0.15s ease, background 0.15s ease;
}
.refactr-search-result.card:hover { border-color: rgba(112,0,255,0.25) !important; background: rgba(112,0,255,0.04); }
.refactr-shell[data-bs-theme="light"] .refactr-search-result.card {
  background: #f8f9ff;
  border-color: rgba(15,23,42,0.07) !important;
  color: #0f172a;
}

/* ── Footer ──────────────────────────────────────────────────── */
.refactr-footer {
  border-top: 1px solid rgba(255,255,255,0.05) !important;
  background: rgba(255,255,255,0.01) !important;
}
.refactr-shell[data-bs-theme="light"] .refactr-footer {
  background: #f5f0ff !important;
  border-top-color: rgba(112,0,255,0.08) !important;
}

/* ── Mobile ──────────────────────────────────────────────────── */
@media (max-width: 991.98px) {
  .refactr-hero { padding: 4rem 0 3rem; }
  .refactr-section { padding: 3.5rem 0; }
}
@media (max-width: 575.98px) {
  .refactr-display { letter-spacing: -0.03em; }
}
""")

# ── Sample data ──────────────────────────────────────────────────────────────
FEATURES = [
    (
        "robot",
        "AI-Powered Refactoring",
        "Automatically detect dead code, anti-patterns and outdated dependencies, then apply fixes with one click.",
    ),
    (
        "git",
        "Git-Native Workflows",
        "Every change is a clean, reviewable PR. Integrate with GitHub, GitLab or Bitbucket in under 60 seconds.",
    ),
    (
        "shield-check",
        "Security Audits",
        "Continuous CVE scanning across your full dependency tree. Ship without surprise vulnerabilities.",
    ),
    (
        "speedometer2",
        "Performance Analysis",
        "Bundle size, runtime profiling, and N+1 detection baked into every commit pipeline.",
    ),
    (
        "diagram-3",
        "Dependency Graph",
        "Visualise your module graph, spot circular imports, and understand blast radius before merging.",
    ),
    (
        "cloud-upload",
        "One-Click Deploys",
        "Push to staging or production directly from Refactr's dashboard — zero additional CI config needed.",
    ),
]

STEPS = [
    (
        "01",
        "Connect Your Repository",
        "Authorise Refactr via OAuth. We scan your codebase and build a full dependency map in under 2 minutes.",
    ),
    (
        "02",
        "Review AI Suggestions",
        "Refactr surfaces prioritized fixes as draft PRs — each one explained in plain English with full diffs.",
    ),
    (
        "03",
        "Ship & Track",
        "Merge in one click. Refactr tracks regressions, measures impact, and learns your team's preferences over time.",
    ),
]

TESTIMONIALS_DATA = [
    (
        "Refactr cut our security backlog from 340 open CVEs to zero in a single afternoon. The auto-generated PRs were clean enough to merge without review on most.",
        "Yemi Adeyemi",
        "CTO, Paystack-backed fintech",
    ),
    (
        "We run a monorepo with 1.4 million lines of Python. Refactr's dependency graph surfaced 12 circular imports we'd been ignoring for three years.",
        "Sasha Kowalski",
        "Staff Engineer, Series B SaaS",
    ),
    (
        "The GitHub integration is flawless. Every suggestion arrives as a PR with a one-sentence rationale. Junior devs can follow the logic immediately.",
        "Priya Menon",
        "Engineering Lead, Logistics SaaS",
    ),
]

SEARCH_ITEMS = [
    ("Auto-refactor", "Automatically rewrite outdated patterns to modern equivalents.", "AI"),
    ("Dependency scanner", "Deep scan of all transitive dependencies for CVEs.", "Security"),
    ("PR generation", "Open reviewable PRs directly in your Git provider.", "Git"),
    ("Performance profiler", "Runtime and bundle analysis on every commit.", "Perf"),
    ("Deployment pipeline", "Push to staging or production with zero config.", "Deploy"),
    ("Code coverage", "Track test coverage drift and highlight uncovered paths.", "QA"),
]

TRUST_LOGOS = [
    ("bi-github", "GitHub"),
    ("bi-gitlab", "GitLab"),
    ("bi-slack", "Slack"),
    ("bi-circle", "CircleCI"),
    ("bi-cloud", "AWS"),
    ("bi-arrow-repeat", "Terraform"),
]


# ── Theme helpers ────────────────────────────────────────────────────────────
def theme_from_req(req) -> str:
    return req.session.get(THEME_COOKIE) or req.cookies.get(THEME_COOKIE, "dark")


def refactr_toggle(theme: str, cls: str = "") -> Any:
    return ThemeToggle(
        current_theme=theme,
        endpoint="/theme/toggle",
        toggle_id="refactr-theme-toggle",
        cls=cls,
    )


# ── Section builders ─────────────────────────────────────────────────────────
def refactr_navbar(theme: str) -> Div:
    return Div(
        Container(
            Div(
                # Brand
                A(
                    Span("refactr", cls="refactr-brand"),
                    href="/",
                    cls="text-decoration-none me-4",
                ),
                # Nav links — collapsed on mobile
                Div(
                    A("Features", href="#features", cls="nav-link"),
                    A("How it works", href="#how-it-works", cls="nav-link"),
                    A("Pricing", href="#pricing", cls="nav-link"),
                    A("Search", href="#search", cls="nav-link"),
                    cls="collapse navbar-collapse d-none d-lg-flex align-items-center gap-1 me-auto",
                ),
                # Actions
                Div(
                    refactr_toggle(theme, cls="me-2"),
                    A(
                        "Log in",
                        href="#",
                        cls="btn btn-sm btn-outline-secondary me-2",
                        style="border-color:rgba(255,255,255,0.14);color:rgba(226,232,240,0.84);width:100px;",
                    ),
                    A(
                        "Start free →",
                        href="#pricing",
                        cls="btn btn-sm btn-primary fw-700",
                        style="width:100px;",
                    ),
                    cls="d-flex align-items-center ms-auto",
                ),
                cls="d-flex align-items-center py-2 w-100",
            ),
            cls="px-3 px-lg-4",
        ),
        cls="refactr-nav-wrap refactr-navbar navbar",
    )


def refactr_hero(theme: str) -> Section:
    code_preview = Div(
        Div(
            Div(
                Span(cls="refactr-dot", style="background:#FF5F57;"),
                Span(cls="refactr-dot ms-1", style="background:#FFBD2E;"),
                Span(cls="refactr-dot ms-1", style="background:#28CA41;"),
                Span("refactr.toml", cls="ms-3 text-muted", style="font-size:0.72rem;"),
                cls="d-flex align-items-center",
            ),
            cls="refactr-console-bar",
        ),
        Pre(
            Code(
                Span("# Refactr configuration\n", cls="cm"),
                Span("[pipeline]\n", cls="kw"),
                Span("  auto_pr      ", cls="fn"),
                " = ",
                Span("true\n", cls="str"),
                Span("  fail_on_cve  ", cls="fn"),
                " = ",
                Span('"high"\n', cls="str"),
                Span("  fix_patterns ", cls="fn"),
                " = ",
                Span('["deprecated", "n+1", "security"]\n\n', cls="str"),
                Span("[integrations]\n", cls="kw"),
                Span("  git_provider ", cls="fn"),
                " = ",
                Span('"github"\n', cls="str"),
                Span("  slack_channel", cls="fn"),
                " = ",
                Span('"#eng-refactr"\n\n', cls="str"),
                Span("[ai]\n", cls="kw"),
                Span("  model  ", cls="fn"),
                " = ",
                Span('"refactr-3-turbo"\n', cls="str"),
                Span("  review ", cls="fn"),
                " = ",
                Span("true", cls="str"),
                cls="refactr-code",
            ),
            cls="p-4 mb-0",
            style="background:transparent;",
        ),
        cls="refactr-console",
    )

    return Section(
        Container(
            Row(
                Col(
                    Div(
                        Span(
                            Icon("robot", cls="me-1"), "Powered by Refactr AI", cls="refactr-kicker"
                        ),
                    ),
                    H1(
                        "Ship cleaner code,",
                        Br(),
                        Span("faster than ever.", cls="refactr-gradient-text"),
                        cls=f"refactr-display mb-4 {Fx.slide_up}",
                    ),
                    P(
                        "Refactr connects to your repository and continuously "
                        "refactors, audits, and optimises your codebase — "
                        "delivering clean, reviewable PRs on autopilot.",
                        cls=f"refactr-subtitle mb-4 {Fx.fade_in} {Fx.delay_sm}",
                    ),
                    Div(
                        A(
                            Icon("rocket-takeoff-fill", cls="me-2"),
                            "Start for free",
                            href="#pricing",
                            cls=f"btn btn-primary btn-lg fw-700 me-3 {Fx.fade_in}",
                            style="border-radius:5px;",
                        ),
                        A(
                            Icon("play-circle", cls="me-2"),
                            "See a demo",
                            href="#how-it-works",
                            cls=f"btn btn-link fw-600 {Fx.fade_in} {Fx.delay_sm}",
                            style="color:rgba(203,213,225,0.82);",
                        ),
                        cls="d-flex align-items-center flex-wrap gap-2 mb-4",
                    ),
                    Div(
                        Span(
                            Icon("shield-check-fill", cls="text-success me-1"),
                            "SOC 2 Type II",
                            cls="me-3 small fw-600",
                        ),
                        Span(
                            Icon("lock-fill", cls="text-info me-1"),
                            "End-to-end encrypted",
                            cls="small fw-600",
                        ),
                        cls=f"d-flex flex-wrap gap-2 {Fx.fade_in} {Fx.delay_md}",
                        style="color:rgba(148,163,184,0.7);",
                    ),
                    md=6,
                    lg=6,
                    cls="mb-5 mb-md-0 align-self-center",
                ),
                Col(
                    Div(code_preview, cls=f"{Fx.slide_left} {Fx.delay_md}"),
                    md=6,
                    lg=6,
                    cls="d-none d-md-block align-self-center",
                ),
                cls="align-items-center g-5",
            ),
            cls="px-3 px-lg-4",
        ),
        cls="refactr-hero",
    )


def trust_rail() -> Section:
    pills = [
        Div(
            Icon(icon, cls="me-1") if not icon.startswith("bi-") else Span(cls=f"bi {icon} me-1"),
            label,
            cls="refactr-trust-pill",
        )
        for icon, label in TRUST_LOGOS
    ]
    return Section(
        Container(
            Div(
                Span(
                    "Trusted by engineering teams at",
                    cls="small fw-600 me-4",
                    style="color:rgba(148,163,184,0.5);white-space:nowrap;",
                ),
                Div(*pills, cls="d-flex flex-wrap align-items-center gap-2"),
                cls="d-flex align-items-center flex-wrap gap-3",
            ),
        ),
        cls="refactr-trust-rail",
    )


def features_section() -> Section:
    cards = [
        Col(
            Div(
                Div(Icon(icon), cls="refactr-feat-icon"),
                Strong(title, cls="d-block mb-2 fw-700"),
                P(desc, cls="refactr-body-muted mb-0 small"),
                cls=f"refactr-feature-card {Fx.fade_in}",
                style=f"animation-delay:{i*60}ms;",
            ),
            cls="mb-4",
        )
        for i, (icon, title, desc) in enumerate(FEATURES)
    ]
    return Section(
        Container(
            Div(
                Span(Icon("lightning-charge", cls="me-1"), "Capabilities", cls="refactr-eyebrow"),
                H2("Everything your codebase needs", cls=f"refactr-h2 mt-2 mb-2 {Fx.slide_up}"),
                P(
                    "One platform to refactor, audit, profile and deploy.",
                    cls="refactr-body-muted mb-5",
                ),
                Row(*cards, cols=1, cols_md=2, cols_lg=3, cls="g-3"),
                id="features",
            ),
        ),
        cls="refactr-section refactr-section-alt",
    )


def how_it_works_section() -> Section:
    step_cols = [
        Col(
            Div(
                Div(
                    Div(num, cls="refactr-step-num me-3"),
                    Strong(title, cls="fw-700 fs-6"),
                    cls="d-flex align-items-center mb-3",
                ),
                P(desc, cls="refactr-body-muted mb-0 small"),
                cls=f"refactr-step-card {Fx.fade_in}",
                style=f"animation-delay:{i*80}ms;",
            ),
            cls="mb-4",
        )
        for i, (num, title, desc) in enumerate(STEPS)
    ]
    return Section(
        Container(
            Div(
                Span(Icon("map", cls="me-1"), "How it works", cls="refactr-eyebrow"),
                H2("From connect to clean in minutes", cls=f"refactr-h2 mt-2 mb-2 {Fx.slide_up}"),
                P(
                    "No YAML sprawl. No custom scripts. Just connect and go.",
                    cls="refactr-body-muted mb-5",
                ),
                Row(*step_cols, cols=1, cols_md=3, cls="g-4"),
                id="how-it-works",
            ),
        ),
        cls="refactr-section",
    )


def pricing_section() -> Section:
    return Section(
        Container(
            Div(
                Span(Icon("tag", cls="me-1"), "Pricing", cls="refactr-eyebrow"),
                H2("Fair, transparent pricing", cls=f"refactr-h2 mt-2 mb-2 {Fx.slide_up}"),
                P(
                    "Start free. Scale as your team grows. No credit card required.",
                    cls="refactr-body-muted mb-5",
                ),
                PricingGroup(
                    PricingTier(
                        name="Starter",
                        price="$0",
                        period="/ month",
                        description="For solo developers and open-source projects.",
                        features=[
                            "1 private repo",
                            "50 AI suggestions/month",
                            "Basic CVE scan",
                            "Community support",
                        ],
                        cta_text="Start free",
                        cta_href="#",
                        outline=True,
                    ),
                    PricingTier(
                        name="Pro",
                        price="$29",
                        period="/ month",
                        description="For growing teams that ship continuously.",
                        features=[
                            "Unlimited repos",
                            "Unlimited AI suggestions",
                            "Full CVE + perf audit",
                            "PR auto-merge rules",
                            "Slack notifications",
                            "Priority support",
                        ],
                        cta_text="Start Pro trial →",
                        cta_href="#",
                        featured=True,
                        badge_text="Most popular",
                    ),
                    PricingTier(
                        name="Enterprise",
                        price="$99",
                        period="/ month",
                        description="For large teams with compliance requirements.",
                        features=[
                            "Everything in Pro",
                            "SOC 2 audit logs",
                            "SAML / SSO",
                            "Custom AI models",
                            "SLA guarantee",
                            "Dedicated CSM",
                        ],
                        cta_text="Contact sales",
                        cta_href="#",
                        outline=True,
                    ),
                ),
                P(
                    Icon("shield-check", cls="me-1 text-success"),
                    "All plans include a 14-day free trial. Cancel anytime.",
                    cls="text-center mt-4 small fw-600",
                    style="color:rgba(148,163,184,0.65);",
                ),
                id="pricing",
            ),
        ),
        cls="refactr-section refactr-section-alt",
    )


def testimonials_section() -> Section:
    return Section(
        Container(
            Div(
                Span(Icon("chat-quote", cls="me-1"), "Social proof", cls="refactr-eyebrow"),
                H2(
                    "Trusted by engineering teams worldwide",
                    cls=f"refactr-h2 mt-2 mb-5 {Fx.slide_up}",
                ),
                Div(
                    TestimonialSection(
                        *[
                            Testimonial(quote=q, author=a, role=r, rating=5)
                            for q, a, r in TESTIMONIALS_DATA
                        ],
                        columns=3,
                    ),
                    cls="refactr-testi",
                ),
            ),
        ),
        cls="refactr-section",
    )


def search_section() -> Section:
    return Section(
        Container(
            Div(
                Span(Icon("search", cls="me-1"), "Live search", cls="refactr-eyebrow"),
                H2("Explore features", cls=f"refactr-h2 mt-2 mb-2 {Fx.slide_up}"),
                P("Search across every Refactr capability below.", cls="refactr-body-muted mb-4"),
                Div(
                    ActiveSearch(
                        placeholder="Search features, integrations…",
                        endpoint="/api/search",
                        target="#refactr-results",
                        min_chars=1,
                        debounce=300,
                        cls="mb-3",
                    ),
                    Div(id="refactr-results"),
                    cls="refactr-search-panel p-4",
                ),
                id="search",
            ),
        ),
        cls="refactr-section refactr-section-alt",
    )


def cta_section() -> Section:
    return Section(
        Container(
            Div(
                Span(
                    "get started",
                    cls="refactr-eyebrow text-center d-block mb-3",
                    style="color:rgba(191,128,255,0.75);",
                ),
                H2(
                    "Your codebase deserves better.",
                    Br(),
                    "Start refactoring today.",
                    cls=f"refactr-h2 text-center text-white mb-3 {Fx.slide_up}",
                    style="font-size:clamp(1.9rem,3.5vw,2.8rem);",
                ),
                P(
                    "Join 12,000+ developers shipping cleaner code with Refactr.",
                    cls="text-center mb-4 fw-500",
                    style="color:rgba(255,255,255,0.6);",
                ),
                Form(
                    Div(
                        Input(
                            "email",
                            input_type="email",
                            placeholder="your@email.com",
                            cls="form-control",
                            style="border-radius:5px 0 0 5px;min-height:2.8rem;",
                        ),
                        LoadingButton(
                            "Get early access",
                            endpoint="/api/subscribe",
                            target="#cta-feedback",
                            variant="primary",
                            cls="fw-700",
                            style="border-radius:0 5px 5px 0;min-height:2.8rem;",
                        ),
                        cls="input-group",
                        style="max-width:440px;",
                    ),
                    Div(id="cta-feedback", cls="mt-2"),
                    cls="d-flex flex-column align-items-center",
                ),
                cls="refactr-cta text-center",
            ),
        ),
        cls="refactr-section",
    )


# ── Routes ───────────────────────────────────────────────────────────────────


@app.get("/")
def home(req) -> Any:
    theme = theme_from_req(req)
    return Div(
        PageMeta(
            title="Refactr — AI-Powered Code Refactoring",
            description="Refactr continuously refactors, audits and optimises your codebase, delivering clean PRs on autopilot. Start free.",
            keywords="code refactoring, AI developer tools, automated PRs, dependency scanner",
        ),
        CUSTOM_CSS,
        ToastContainer(id="toast-container"),
        refactr_navbar(theme),
        refactr_hero(theme),
        trust_rail(),
        features_section(),
        how_it_works_section(),
        pricing_section(),
        testimonials_section(),
        search_section(),
        cta_section(),
        FooterModern(
            brand="Refactr",
            tagline="Cleaner code, on autopilot.",
            links=[
                ("Features", "#features"),
                ("How it works", "#how-it-works"),
                ("Pricing", "#pricing"),
                ("Changelog", "#"),
                ("Docs", "#"),
                ("Status", "#"),
            ],
            cls="refactr-footer",
        ),
        cls="refactr-shell",
        **{"data-bs-theme": theme},
    )


@app.get("/api/search")
def api_search(q: str = "") -> Any:
    q = q.strip().lower()
    results = [
        (title, desc, tag)
        for title, desc, tag in SEARCH_ITEMS
        if not q or q in title.lower() or q in desc.lower() or q in tag.lower()
    ]
    if not results:
        return Div(
            Icon("search", cls="me-2"),
            f'No results for "{q}"',
            cls="text-center py-4 text-muted small",
        )
    return Div(
        *[
            Div(
                Div(
                    Badge(tag, variant="outline-primary", cls="me-2 small"),
                    Strong(title, cls="fw-600"),
                    cls="d-flex align-items-center mb-1",
                ),
                P(desc, cls="mb-0 small", style="color:rgba(148,163,184,0.78);"),
                cls="card p-3 refactr-search-result",
            )
            for title, desc, tag in results
        ],
        cls="d-grid gap-2",
    )


@app.post("/api/subscribe")
def api_subscribe(email: str = "") -> Any:
    if not email or "@" not in email:
        return toast_response("", message="Please enter a valid email address.", variant="danger")
    return toast_response(
        "", message=f"🎉 You're on the list! We'll reach out to {email} soon.", variant="success"
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    current = theme_from_req(req)
    new_theme = "light" if current == "dark" else "dark"
    req.session[THEME_COOKIE] = new_theme
    response = hx_refresh()
    response.set_cookie(THEME_COOKIE, new_theme, max_age=60 * 60 * 24 * 365)
    return response


if __name__ == "__main__":
    serve(port=5003)
