"""Flagship showcase - NovaFlow AI SaaS landing page.

This showcase is intended to be a premium marketing reference for Faststrap:

- Bootstrap and Faststrap for layout, spacing, forms, and components
- HTMX presets for live interactions
- custom CSS only for atmosphere, polish, and brand direction
- zero custom JavaScript; theme persistence uses Faststrap's HTMX pattern
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    H2,
    H3,
    H4,
    A,
    Br,
    Code,
    Div,
    FastHTML,
    Form,
    P,
    Small,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Alert,
    Badge,
    Card,
    Col,
    Container,
    Feature,
    FeatureGrid,
    FooterModern,
    Fx,
    Hero,
    Icon,
    Input,
    LandingLayout,
    NavbarModern,
    PricingGroup,
    PricingTier,
    Row,
    Select,
    Testimonial,
    TestimonialSection,
    ThemeToggle,
    ToastContainer,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import ActiveSearch, LoadingButton, hx_refresh, toast_response

THEME_COOKIE = "novaflow_theme"

NOVAFLOW_THEME = create_theme(
    primary="#5B6CFF",
    secondary="#172033",
    success="#12B886",
    danger="#F06595",
    warning="#F59F00",
    info="#7C5CFC",
)

SHOWCASE_CSS = """
/* ═══════════════════════════════════════════════════════════
   NovaFlow · Premium CSS redesign
   Philosophy: architectural geometry (4-8px radii), sharp
   accent lines, intentional glassmorphism, strong type scale.
   "Premium" = restraint + precision, not rounded corners.
   ═══════════════════════════════════════════════════════════ */

/* ── Page shell ─────────────────────────────────────────── */
.nova-app {
  background:
    radial-gradient(ellipse at 2% 0%, rgba(91, 108, 255, 0.2), transparent 36%),
    radial-gradient(ellipse at 88% 8%, rgba(124, 92, 252, 0.14), transparent 28%),
    linear-gradient(180deg, #080e1c 0%, #0d1528 40%, #f2f4f8 40%, #f2f4f8 100%);
  color: var(--bs-body-color);
  min-height: 100vh;
  transition: background 0.3s ease, color 0.3s ease;
}

.nova-shell {
  position: relative;
  overflow-x: clip;
}

/* Subtle mesh — only spans the dark hero zone */
.nova-shell::before {
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 40%;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255,255,255,0.022) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.022) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: linear-gradient(180deg, rgba(0,0,0,0.55) 0%, transparent 100%);
  z-index: 0;
}

/* Left-side ambient glow */
.nova-shell::after {
  content: "";
  position: absolute;
  inset: 5rem auto auto -9rem;
  width: 26rem;
  height: 26rem;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(91,108,255,0.18), transparent 68%);
  filter: blur(52px);
  pointer-events: none;
  z-index: 0;
}

/* ── Navbar ───────────────────────────────────────────────── */
/* Flat bar — sharp, like Linear/Railway, not a floating pill */
.nova-nav-wrap {
  position: sticky;
  top: 0;
  z-index: 20;
  padding: 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  background: rgba(8,14,28,0.82);
  backdrop-filter: blur(22px) saturate(1.5);
  -webkit-backdrop-filter: blur(22px) saturate(1.5);
}

.nova-navbar {
  background: transparent;
  border: none;
  border-radius: 0;
  box-shadow: none;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.nova-navbar .nav-link {
  color: rgba(203,213,225,0.78);
  font-size: 0.86rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  border-radius: 4px;
  padding: 0.4rem 0.8rem !important;
  transition: color 0.15s ease, background 0.15s ease;
}

.nova-navbar .nav-link:hover,
.nova-navbar .nav-link:focus-visible {
  color: #fff;
  background: rgba(255,255,255,0.07);
}

.nova-navbar .btn {
  font-size: 0.84rem;
  font-weight: 600;
  letter-spacing: 0.015em;
  border-radius: 5px;
  padding: 0.4rem 1rem;
}

.nova-navbar .btn-primary {
  box-shadow: 0 1px 0 rgba(255,255,255,0.12) inset,
              0 0 0 1px rgba(91,108,255,0.45),
              0 6px 20px rgba(91,108,255,0.24);
}

.nova-navbar .btn-outline-secondary {
  border-color: rgba(255,255,255,0.13);
  color: rgba(226,232,240,0.84);
}

.nova-navbar .btn-outline-secondary:hover {
  background: rgba(255,255,255,0.07);
  border-color: rgba(255,255,255,0.2);
  color: #fff;
}

/* ── Brand mark ───────────────────────────────────────────── */
.nova-brand-mark {
  width: 1.9rem;
  height: 1.9rem;
  border-radius: 5px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #5B6CFF, #7C5CFC);
  color: #fff;
  font-size: 0.85rem;
  box-shadow: 0 2px 12px rgba(91,108,255,0.4);
  flex-shrink: 0;
}

/* ── Hero ─────────────────────────────────────────────────── */
.nova-hero {
  position: relative;
  padding-top: 5.5rem;
  padding-bottom: 5rem;
  z-index: 1;
}

/* Right-side accent glow behind the console */
.nova-hero::before {
  content: "";
  position: absolute;
  inset: 4rem 2% auto auto;
  width: 20rem;
  height: 20rem;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(124,92,252,0.18), transparent 68%);
  filter: blur(32px);
  pointer-events: none;
}

/* Badge / chip */
.nova-chip {
  border: 1px solid rgba(255,255,255,0.09);
  background: rgba(255,255,255,0.04);
  border-radius: 4px;
  color: rgba(203,213,225,0.86);
  font-size: 0.78rem;
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* Display headline — tight, editorial, high contrast */
.nova-display {
  font-size: clamp(2.8rem, 6vw, 5.2rem);
  line-height: 1.02;
  letter-spacing: -0.04em;
  font-weight: 800;
  color: #eef2ff;
}

.nova-subtitle {
  max-width: 40rem;
  color: rgba(148,163,184,0.88);
  font-size: 1.025rem;
  line-height: 1.72;
  font-weight: 400;
}

/* Stat pills — architectural boxes, not bubbles */
.nova-stat-pill {
  border: 1px solid rgba(255,255,255,0.07);
  background: rgba(255,255,255,0.025);
  color: #eef2ff;
  border-radius: 5px;
  transition: border-color 0.18s ease, background 0.18s ease;
}

.nova-stat-pill:hover {
  border-color: rgba(91,108,255,0.28);
  background: rgba(91,108,255,0.05);
}

.nova-stat-pill strong {
  font-size: 1.3rem;
  font-weight: 800;
  display: block;
  letter-spacing: -0.035em;
  line-height: 1.1;
  color: #fff;
}

.nova-stat-pill small {
  font-size: 0.73rem;
  color: rgba(148,163,184,0.78);
  font-weight: 400;
}

/* ── Code console ─────────────────────────────────────────── */
.nova-console {
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(160deg, rgba(10,16,30,0.99), rgba(7,11,21,1));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.05),
    0 0 0 1px rgba(0,0,0,0.6),
    0 32px 72px rgba(0,0,0,0.55);
}

.nova-console-bar {
  background: rgba(255,255,255,0.025);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  padding: 0.7rem 1.2rem;
}

.nova-dot {
  width: 0.62rem;
  height: 0.62rem;
  border-radius: 50%;
  display: inline-block;
}

.nova-code {
  color: #a5b4fc;
  font-size: 0.81rem;
  line-height: 1.82;
  white-space: pre-wrap;
  font-family: "JetBrains Mono", "Fira Code", ui-monospace, monospace;
  letter-spacing: 0.005em;
}

/* Surface tiles inside console */
.nova-surface {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.065);
  border-radius: 4px;
  transition: border-color 0.18s ease, background 0.18s ease;
}

.nova-surface:hover {
  border-color: rgba(91,108,255,0.22);
  background: rgba(91,108,255,0.04);
}

/* ── Logo rail ─────────────────────────────────────────────── */
.nova-logo-rail {
  border-top: 1px solid rgba(15,23,42,0.07);
  border-bottom: 1px solid rgba(15,23,42,0.07);
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(8px);
  color: #0f172a;
}

.nova-logo-pill {
  border: 1px solid rgba(15,23,42,0.09);
  background: #fff;
  color: #475569;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.8rem;
  letter-spacing: 0.01em;
  transition: color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
}

.nova-logo-pill:hover {
  color: #0f172a;
  border-color: rgba(91,108,255,0.22);
  box-shadow: 0 2px 8px rgba(91,108,255,0.08);
}

/* ── Momentum / info strip ─────────────────────────────────── */
.nova-momentum .card {
  border: 1px solid rgba(15,23,42,0.08);
  border-radius: 6px;
  background: #fff;
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
  color: #0f172a;
  transition: border-color 0.18s ease, box-shadow 0.18s ease;
}

.nova-momentum .card:hover {
  border-color: rgba(91,108,255,0.18);
  box-shadow: 0 8px 24px rgba(15,23,42,0.07);
}

/* ── Dark principle card ───────────────────────────────────── */
.nova-principle-card {
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 8px;
  background: rgba(255,255,255,0.035);
  box-shadow: 0 20px 56px rgba(0,0,0,0.24);
}

.nova-mini-stat {
  border: 1px solid rgba(255,255,255,0.065);
  border-radius: 5px;
  background: rgba(255,255,255,0.025);
  min-height: 100%;
  transition: border-color 0.18s ease, background 0.18s ease;
}

.nova-mini-stat:hover {
  border-color: rgba(91,108,255,0.22);
  background: rgba(91,108,255,0.03);
}

.nova-checklist {
  display: grid;
  gap: 0.65rem;
}

.nova-checklist-item {
  display: flex;
  gap: 0.85rem;
  align-items: flex-start;
  padding: 0.85rem 0.95rem;
  border-radius: 5px;
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,255,255,0.065);
  transition: border-color 0.18s ease, background 0.18s ease;
}

.nova-checklist-item:hover {
  border-color: rgba(91,108,255,0.2);
  background: rgba(91,108,255,0.04);
}

/* ── Section system ────────────────────────────────────────── */
.nova-section {
  position: relative;
  z-index: 1;
}

/* Light sections — clean white with subtle separator lines */
.nova-section-light {
  background: linear-gradient(180deg, #f2f4f8 0%, #ffffff 100%);
  color: #0f172a;
  border-top: 1px solid rgba(15,23,42,0.06);
  border-bottom: 1px solid rgba(15,23,42,0.06);
}

.nova-section-light h1,
.nova-section-light h2,
.nova-section-light h3,
.nova-section-light h4,
.nova-section-light h5,
.nova-section-light h6,
.nova-section-light strong,
.nova-momentum h1,
.nova-momentum h2,
.nova-momentum h3,
.nova-momentum h4,
.nova-momentum strong,
.nova-logo-rail strong {
  color: #0f172a;
}

.nova-section-light .text-muted,
.nova-logo-rail .text-muted,
.nova-momentum .text-muted,
.feature-item .text-muted,
.nova-proof-card .text-muted,
.nova-panel .text-muted,
.pricing-group .text-muted,
.nova-search-results .text-muted,
.nova-search-empty .text-muted {
  color: #64748b !important;
}

/* Dark sections — refined, not flat black */
.nova-section-dark {
  background:
    radial-gradient(ellipse at top right, rgba(91,108,255,0.1), transparent 36%),
    linear-gradient(180deg, #09111f, #0d1728);
  border-top: 1px solid rgba(255,255,255,0.05);
}

/* ── Feature cards (light section) ────────────────────────── */
.feature-item {
  position: relative;
  overflow: hidden;
  height: 100%;
  padding: 1.5rem 1.5rem 1.5rem 1.75rem;
  border-radius: 6px;
  background: #fff;
  border: 1px solid rgba(15,23,42,0.08);
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  color: #0f172a;
}

/* Vertical left-edge accent — revealed on hover only */
.feature-item::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 3px;
  background: linear-gradient(180deg, #5B6CFF, #7C5CFC);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.feature-item:hover::before { opacity: 1; }

.feature-item:hover {
  transform: translateY(-4px);
  border-color: rgba(91,108,255,0.15);
  box-shadow: 0 12px 40px rgba(15,23,42,0.09);
}

.feature-icon {
  width: 2.6rem;
  height: 2.6rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  margin-bottom: 0.875rem;
  font-size: 1.05rem;
}

/* ── Proof / use-case cards (light) ───────────────────────── */
.nova-proof-card {
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(15,23,42,0.08) !important;
  border-radius: 6px !important;
  background: linear-gradient(160deg, #ffffff, #f8faff);
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
  color: #0f172a;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.nova-proof-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 32px rgba(15,23,42,0.09);
  border-color: rgba(91,108,255,0.16) !important;
}

/* Thin top-line accent on proof cards */
.nova-proof-card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 2px;
  background: linear-gradient(90deg, rgba(91,108,255,0.7), transparent);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.nova-proof-card:hover::before { opacity: 1; }

.nova-proof-label {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.28rem 0.6rem;
  border-radius: 3px;
  background: rgba(91,108,255,0.06);
  color: #3b50e0;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  border: 1px solid rgba(91,108,255,0.12);
}

/* ── Search panels ─────────────────────────────────────────── */
.nova-panel {
  border: 1px solid rgba(15,23,42,0.08);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 4px 20px rgba(15,23,42,0.06);
}

.nova-panel-dark {
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 8px;
  background: rgba(255,255,255,0.03);
  backdrop-filter: blur(18px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.24);
}

.nova-search-input {
  min-height: 2.9rem;
  border-radius: 5px !important;
  font-size: 0.88rem;
  box-shadow: none;
}

.nova-search-input:focus {
  border-color: rgba(91,108,255,0.42);
  box-shadow: 0 0 0 3px rgba(91,108,255,0.1);
}

.nova-search-results .card {
  border: 1px solid rgba(15,23,42,0.08);
  border-radius: 6px;
  box-shadow: 0 1px 4px rgba(15,23,42,0.04);
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  color: #0f172a;
}

.nova-search-results .card:hover {
  transform: translateY(-2px);
  border-color: rgba(91,108,255,0.16);
  box-shadow: 0 8px 24px rgba(15,23,42,0.08);
}

.nova-search-tag {
  display: inline-flex;
  align-items: center;
  padding: 0.28rem 0.65rem;
  border-radius: 4px;
  background: rgba(15,23,42,0.04);
  border: 1px solid rgba(15,23,42,0.08);
  color: #475569;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  cursor: pointer;
  transition: color 0.15s ease, border-color 0.15s ease;
}

.nova-search-tag:hover {
  color: #0f172a;
  border-color: rgba(91,108,255,0.2);
}

.nova-search-empty {
  border: 1px dashed rgba(15,23,42,0.1);
  border-radius: 6px;
  background: rgba(255,255,255,0.6);
  color: #0f172a;
}

/* ── Pricing ────────────────────────────────────────────────── */
.pricing-group .card {
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(15,23,42,0.08);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(15,23,42,0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  color: #0f172a;
  background: #fff;
}

/* Thin top bar on all tiers */
.pricing-group .card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 2px;
  background: rgba(91,108,255,0.22);
}

.pricing-group .card:hover {
  transform: translateY(-4px);
  border-color: rgba(91,108,255,0.18);
  box-shadow: 0 16px 48px rgba(15,23,42,0.1);
}

/* Highlighted / featured plan */
.pricing-group .card.border-primary {
  border-color: rgba(91,108,255,0.3) !important;
  box-shadow:
    0 0 0 1px rgba(91,108,255,0.18),
    0 20px 52px rgba(91,108,255,0.12);
}

.pricing-group .card.border-primary::before {
  height: 3px;
  background: linear-gradient(90deg, #5B6CFF, #7C5CFC);
}

.pricing-group .btn {
  min-height: 2.7rem;
  font-weight: 600;
  border-radius: 5px;
  letter-spacing: 0.01em;
}

.nova-pricing-note {
  color: #64748b;
  font-size: 0.92rem;
}

/* ── Testimonials ─────────────────────────────────────────── */
.nova-testimonials .card {
  position: relative;
  border: 1px solid rgba(255,255,255,0.07) !important;
  border-radius: 8px;
  background: rgba(255,255,255,0.04);
  color: #e2e8f0;
  box-shadow: 0 12px 40px rgba(0,0,0,0.18);
  transition: border-color 0.2s ease, transform 0.2s ease;
}

.nova-testimonials .card:hover {
  border-color: rgba(255,255,255,0.12) !important;
  transform: translateY(-3px);
}

.nova-testimonials .card::after {
  content: "\201C";
  position: absolute;
  top: 0.875rem;
  right: 1.25rem;
  font-size: 3.5rem;
  line-height: 1;
  color: rgba(255,255,255,0.06);
  font-weight: 900;
}

.nova-testimonials .text-muted {
  color: rgba(148,163,184,0.8) !important;
}

/* ── CTA section ───────────────────────────────────────────── */
.nova-cta-card {
  max-width: 52rem;
  margin-inline: auto;
  border: 1px solid rgba(255,255,255,0.07);
  background: rgba(255,255,255,0.04);
  backdrop-filter: blur(20px);
  border-radius: 8px;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.06),
    0 24px 64px rgba(0,0,0,0.3);
}

.nova-cta-card .form-control,
.nova-cta-card .form-select {
  border-radius: 5px;
  min-height: 2.9rem;
  border-color: rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.96);
  font-size: 0.88rem;
}

.nova-cta-card .btn-primary {
  border-radius: 5px;
  box-shadow: 0 6px 20px rgba(91,108,255,0.28);
  font-weight: 600;
}

.nova-cta-note {
  display: inline-flex;
  align-items: center;
  gap: 0.42rem;
  padding: 0.42rem 0.82rem;
  border-radius: 4px;
  background: rgba(255,255,255,0.04);
  color: rgba(203,213,225,0.84);
  border: 1px solid rgba(255,255,255,0.07);
  font-size: 0.8rem;
  font-weight: 500;
}

/* ── Footer ─────────────────────────────────────────────────── */
.nova-footer {
  margin-top: 0 !important;
  color: #e2e8f0;
  border-top: 1px solid rgba(255,255,255,0.06) !important;
}

.nova-footer a {
  transition: color 0.15s ease;
}

.nova-footer a:hover {
  color: #fff !important;
  opacity: 1;
}

.nova-footer h4,
.nova-footer h5,
.nova-footer h6,
.nova-footer strong,
.nova-footer .fs-4 {
  color: #f8fafc !important;
}

.nova-footer .text-muted {
  color: rgba(148,163,184,0.68) !important;
}

.nova-footer a {
  color: rgba(203,213,225,0.68) !important;
}

/* ── Light-mode overrides ──────────────────────────────────── */
.nova-app[data-bs-theme="light"] {
  background:
    radial-gradient(ellipse at 2% 0%, rgba(91,108,255,0.08), transparent 36%),
    radial-gradient(ellipse at 88% 8%, rgba(124,92,252,0.05), transparent 28%),
    linear-gradient(180deg, #ecf0fc 0%, #f7f9ff 32%, #f2f4f8 32%, #f2f4f8 100%);
}

[data-bs-theme="light"] .nova-nav-wrap {
  background: rgba(255,255,255,0.92);
  border-bottom-color: rgba(15,23,42,0.08);
}

[data-bs-theme="light"] .nova-shell::before {
  background-image:
    linear-gradient(rgba(15,23,42,0.018) 1px, transparent 1px),
    linear-gradient(90deg, rgba(15,23,42,0.018) 1px, transparent 1px);
}

[data-bs-theme="light"] .nova-shell::after {
  background: radial-gradient(circle, rgba(91,108,255,0.12), transparent 68%);
}

[data-bs-theme="light"] .nova-navbar .nav-link { color: rgba(51,65,85,0.8); }
[data-bs-theme="light"] .nova-navbar .nav-link:hover { color: #0f172a; background: rgba(15,23,42,0.05); }

[data-bs-theme="light"] .nova-navbar .btn-outline-secondary {
  border-color: rgba(15,23,42,0.14);
  color: #334155;
}
[data-bs-theme="light"] .nova-navbar .btn-outline-secondary:hover {
  background: rgba(15,23,42,0.05);
  color: #0f172a;
}

[data-bs-theme="light"] .nova-chip {
  border-color: rgba(15,23,42,0.08);
  background: rgba(255,255,255,0.88);
  color: #334155;
}

[data-bs-theme="light"] .nova-display { color: #080e1c; }
[data-bs-theme="light"] .nova-subtitle { color: rgba(51,65,85,0.76); }

[data-bs-theme="light"] .nova-stat-pill {
  border-color: rgba(15,23,42,0.08);
  background: rgba(255,255,255,0.92);
  color: #0f172a;
}
[data-bs-theme="light"] .nova-stat-pill strong { color: #080e1c; }
[data-bs-theme="light"] .nova-stat-pill small { color: #64748b; }

[data-bs-theme="light"] .nova-console {
  border-color: rgba(15,23,42,0.08);
  background: linear-gradient(160deg, #f4f6ff, #edf0ff);
  box-shadow: 0 2px 8px rgba(15,23,42,0.06), 0 20px 56px rgba(15,23,42,0.1),
              inset 0 1px 0 rgba(255,255,255,0.9);
}
[data-bs-theme="light"] .nova-console-bar {
  background: rgba(15,23,42,0.03);
  border-bottom-color: rgba(15,23,42,0.07);
}
[data-bs-theme="light"] .nova-code { color: #3730a3; }
[data-bs-theme="light"] .nova-surface {
  background: rgba(255,255,255,0.9);
  border-color: rgba(15,23,42,0.08);
}

[data-bs-theme="light"] .nova-section-dark {
  background:
    radial-gradient(ellipse at top right, rgba(91,108,255,0.06), transparent 36%),
    linear-gradient(180deg, #eef2ff, #f5f8fc);
  border-top-color: rgba(15,23,42,0.06);
}

[data-bs-theme="light"] .nova-testimonials .card {
  border-color: rgba(15,23,42,0.08) !important;
  background: rgba(255,255,255,0.96);
  color: #0f172a;
  box-shadow: 0 2px 8px rgba(15,23,42,0.05);
}
[data-bs-theme="light"] .nova-testimonials .card::after { color: rgba(15,23,42,0.05); }
[data-bs-theme="light"] .nova-testimonials .text-muted { color: #64748b !important; }

[data-bs-theme="light"] .nova-principle-card {
  border-color: rgba(15,23,42,0.08) !important;
  background: rgba(255,255,255,0.92);
}
[data-bs-theme="light"] .nova-mini-stat,
[data-bs-theme="light"] .nova-checklist-item {
  border-color: rgba(15,23,42,0.08);
  background: rgba(255,255,255,0.88);
}

[data-bs-theme="light"] .nova-cta-card {
  border-color: rgba(15,23,42,0.08);
  background: rgba(255,255,255,0.94);
  box-shadow: 0 8px 32px rgba(15,23,42,0.08);
}
[data-bs-theme="light"] .nova-cta-note {
  color: #334155;
  background: rgba(255,255,255,0.88);
  border-color: rgba(15,23,42,0.08);
}

/* ── Footer light-mode overrides ───────────────────────────── */
/* Without these, near-white footer text is invisible on light bg */
[data-bs-theme="light"] .nova-footer {
  color: #334155 !important;
  border-top-color: rgba(15,23,42,0.07) !important;
  background: #f2f4f8 !important;
}
[data-bs-theme="light"] .nova-footer h4,
[data-bs-theme="light"] .nova-footer h5,
[data-bs-theme="light"] .nova-footer h6,
[data-bs-theme="light"] .nova-footer strong,
[data-bs-theme="light"] .nova-footer .fs-4 {
  color: #0f172a !important;
}
[data-bs-theme="light"] .nova-footer .text-muted {
  color: #64748b !important;
}
[data-bs-theme="light"] .nova-footer a {
  color: #475569 !important;
}
[data-bs-theme="light"] .nova-footer a:hover {
  color: #0f172a !important;
}

/* ── Section-dark inherits text in light mode ───────────────── */
/* nova-section-dark becomes light-bg (see rule above) — ensure */
/* child text stays dark and readable                           */
[data-bs-theme="light"] .nova-section-dark {
  color: #0f172a;
}
[data-bs-theme="light"] .nova-checklist-item {
  color: #1e293b;
}
[data-bs-theme="light"] .nova-mini-stat {
  color: #1e293b;
}

/* ── Responsive ────────────────────────────────────────────── */
@media (max-width: 991.98px) {
  .nova-display { font-size: clamp(2.2rem, 9vw, 3.5rem); letter-spacing: -0.03em; }
  .nova-hero { padding-top: 3.5rem; padding-bottom: 3.5rem; }
  .nova-shell::before { height: 36%; }

  .nova-navbar {
    padding-top: 0.6rem;
    padding-bottom: 0.6rem;
  }

  .nova-navbar .navbar-collapse {
    padding: 0.875rem 0;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin-top: 0.5rem;
  }

  [data-bs-theme="light"] .nova-navbar .navbar-collapse {
    border-top-color: rgba(15,23,42,0.07);
  }
}

@media (max-width: 575.98px) {
  .nova-display { font-size: clamp(1.9rem, 10vw, 2.8rem); }
  .nova-hero { padding-top: 2.75rem; }
}
"""
COMPONENT_INDEX = [
    {
        "name": "DataTable",
        "kind": "Data",
        "pitch": "Sortable and searchable tables with HTMX-friendly server contracts.",
    },
    {
        "name": "Chart",
        "kind": "Analytics",
        "pitch": "Embed Matplotlib, Plotly, Altair, SVG, or safe HTML charts without leaving Python.",
    },
    {
        "name": "DashboardGrid",
        "kind": "Layout",
        "pitch": "Responsive dashboard card grid tuned for analytics and operations screens.",
    },
    {
        "name": "NotificationCenter",
        "kind": "Feedback",
        "pitch": "A production-style bell menu built from Faststrap notifications and HTMX updates.",
    },
    {
        "name": "SearchableSelect",
        "kind": "Forms",
        "pitch": "HTMX-powered server search for large option sets with CSP-safe mode support.",
    },
    {
        "name": "ThemeToggle",
        "kind": "Forms",
        "pitch": "Dark/light preference toggle for polished apps with server persistence patterns.",
    },
    {
        "name": "FormBuilder",
        "kind": "Forms",
        "pitch": "Generate forms directly from Pydantic models to reduce repetitive UI wiring.",
    },
    {
        "name": "Markdown",
        "kind": "Content",
        "pitch": "Render Markdown safely with optional sanitization and extension support.",
    },
    {
        "name": "Mermaid",
        "kind": "Content",
        "pitch": "Render Mermaid diagrams for technical docs and product workflows.",
    },
    {
        "name": "ExportButton",
        "kind": "Data",
        "pitch": "Standardize CSV and Excel exports with a consistent server-side contract.",
    },
    {
        "name": "MetricCard",
        "kind": "Analytics",
        "pitch": "Elevated KPI card with trend deltas for premium product dashboards.",
    },
    {
        "name": "SSETarget",
        "kind": "Realtime",
        "pitch": "Progressively enhance live panels with SSE when your host supports streaming.",
    },
]

TESTIMONIALS = [
    {
        "quote": "Faststrap let us keep our team in Python and still ship a launch site that looked investor-ready in one sprint.",
        "author": "Nina Cole",
        "role": "Head of Product, Ribbon AI",
        "rating": 5,
    },
    {
        "quote": "We replaced a fragile pile of front-end glue with a cleaner HTMX flow and our design quality actually went up.",
        "author": "Tayo Mensah",
        "role": "Founder, StackPilot",
        "rating": 5,
    },
    {
        "quote": "The presets are the sleeper feature. Loading states, search, and partial updates felt cohesive instead of improvised.",
        "author": "Mira Shah",
        "role": "Engineering Lead, Northpath",
        "rating": 5,
    },
]

FOOTER_COLUMNS = [
    {
        "title": "Product",
        "links": [
            {"text": "Components", "href": "#features"},
            {"text": "Pricing", "href": "#pricing"},
            {"text": "Search Surface", "href": "#search"},
        ],
    },
    {
        "title": "Use Cases",
        "links": [
            {"text": "SaaS", "href": "#use-cases"},
            {"text": "Dashboards", "href": "#use-cases"},
            {"text": "Portfolios", "href": "#use-cases"},
        ],
    },
    {
        "title": "Resources",
        "links": [
            {"text": "Docs", "href": "https://faststrap-org.github.io/Faststrap/"},
            {"text": "GitHub", "href": "https://github.com/Faststrap-org/Faststrap"},
            {
                "text": "Showcase Plan",
                "href": "https://github.com/Faststrap-org/Faststrap/blob/main/SHOWCASE_PROGRAM_PLAN.md",
            },
        ],
    },
]

SOCIAL_LINKS = [
    {"icon": "github", "href": "https://github.com/Faststrap-org/Faststrap"},
    {"icon": "box-arrow-up-right", "href": "https://faststrap-org.github.io/Faststrap/"},
]


app = FastHTML()
add_bootstrap(
    app,
    theme=NOVAFLOW_THEME,
    mode="auto",
    font_family="Plus Jakarta Sans",
    include_favicon=False,
)


def current_theme(req: Any) -> str:
    theme = req.session.get(THEME_COOKIE) or req.cookies.get(THEME_COOKIE, "dark")
    return theme if theme in {"light", "dark"} else "dark"


def feature_items() -> list[Any]:
    items = [
        (
            "Zero context switching",
            "Build polished interfaces in Python without splitting your product thinking across two stacks.",
            "code-slash",
            "bg-primary-subtle text-primary",
        ),
        (
            "HTMX-first interactions",
            "Ship live search, lazy content, loading states, and response flows without a custom JS tangle.",
            "lightning-charge-fill",
            "bg-info-subtle text-info-emphasis",
        ),
        (
            "Bootstrap-native output",
            "Keep the reliability of Bootstrap markup while layering stronger motion, polish, and composition.",
            "grid-1x2-fill",
            "bg-warning-subtle text-warning-emphasis",
        ),
        (
            "Real data surfaces",
            "Use DataTable, Chart, MetricCard, and DashboardGrid for webapps that actually carry product weight.",
            "bar-chart-fill",
            "bg-success-subtle text-success-emphasis",
        ),
        (
            "Theme-aware by default",
            "Use built-in themes or custom palettes and keep components visually coherent across light and dark surfaces.",
            "palette-fill",
            "bg-danger-subtle text-danger-emphasis",
        ),
        (
            "Production-oriented helpers",
            "Toast responses, auth guards, SEO, PWA support, and deployment guidance are part of the framework surface.",
            "shield-check",
            "bg-secondary-subtle text-secondary-emphasis",
        ),
    ]
    cards: list[Any] = []
    for title, desc, icon, icon_cls in items:
        cards.append(
            Div(
                Feature(title, desc, icon=icon, icon_cls=icon_cls),
                cls=f"{Fx.base} {Fx.fade_in} {Fx.hover_lift} h-100",
            )
        )
    return cards


def use_case_cards() -> list[Any]:
    use_cases = [
        (
            "Launch Pages",
            "Editorial SaaS landing pages with stronger hierarchy, richer interactions, and real conversion surfaces.",
            "rocket-takeoff-fill",
            "Marketing",
        ),
        (
            "Internal Dashboards",
            "Analytics and ops interfaces with cards, filters, tables, notifications, and export-friendly data flows.",
            "window-sidebar",
            "Operations",
        ),
        (
            "Client Websites",
            "Corporate sites, portfolios, booking pages, and ecommerce fronts that do not look like stock Bootstrap.",
            "stars",
            "Brand",
        ),
    ]
    cards: list[Any] = []
    for idx, (title, text, icon, label) in enumerate(use_cases):
        cards.append(
            Col(
                Card(
                    Div(
                        Span(
                            Icon("stars", cls="small"),
                            label,
                            cls="nova-proof-label mb-3",
                        ),
                        Div(
                            Icon(icon, cls="fs-3 text-primary"),
                            cls="mb-3",
                        ),
                        H3(title, cls="h4 fw-bold"),
                        P(text, cls="text-muted mb-0"),
                    ),
                    cls=f"nova-proof-card h-100 border-0 {Fx.base} {Fx.fade_in} {Fx.hover_lift} {Fx.delay_sm if idx else ''}",
                ),
                md=4,
                cls="mb-4",
            )
        )
    return cards


def search_result_cards(query: str) -> list[Any]:
    normalized = query.strip().lower()
    if not normalized:
        return []
    kind_icons = {
        "Data": "table",
        "Analytics": "bar-chart-fill",
        "Layout": "grid-1x2-fill",
        "Feedback": "bell-fill",
        "Forms": "ui-checks-grid",
        "Content": "markdown-fill",
        "Realtime": "activity",
    }
    hits = [
        item
        for item in COMPONENT_INDEX
        if normalized in item["name"].lower()
        or normalized in item["kind"].lower()
        or normalized in item["pitch"].lower()
    ][:6]
    if not hits:
        return []
    cards: list[Any] = []
    for item in hits:
        cards.append(
            Col(
                Card(
                    Div(
                        Div(
                            Span(
                                Icon(kind_icons.get(item["kind"], "box"), cls="me-2 text-primary"),
                                item["kind"],
                                cls="nova-search-tag mb-3",
                            ),
                        ),
                        H4(item["name"], cls="h5 fw-bold"),
                        P(item["pitch"], cls="text-muted mb-0"),
                    ),
                    cls="h-100 border-0",
                ),
                md=6,
                cls="mb-3",
            )
        )
    return cards


@app.get("/")
def home(req) -> Any:
    theme = current_theme(req)

    nav = NavbarModern(
        brand=Div(
            Span(Icon("stars"), cls="nova-brand-mark"),
            Div(
                Strong("NovaFlow", cls="d-block lh-1"),
                Small("Faststrap flagship showcase", cls="text-body-secondary"),
                cls="d-flex flex-column",
            ),
            cls="d-flex align-items-center gap-3",
        ),
        items=[
            Div(
                A("Features", href="#features", cls="nav-link"),
                A("Search", href="#search", cls="nav-link"),
                A("Pricing", href="#pricing", cls="nav-link"),
                A("Stories", href="#stories", cls="nav-link"),
                cls="navbar-nav flex-lg-row gap-lg-2 me-auto",
            ),
            Div(
                ThemeToggle(
                    current_theme=theme,
                    endpoint="/theme/toggle",
                    show_label=False,
                    toggle_id="novaflow-theme-toggle",
                    cls="me-lg-2",
                ),
                A(
                    "View Docs",
                    href="https://faststrap-org.github.io/Faststrap/",
                    cls="btn btn-outline-secondary",
                ),
                A("Start Free", href="#cta", cls="btn btn-primary"),
                cls="d-flex flex-column flex-lg-row gap-2 align-items-lg-center mt-3 mt-lg-0",
            ),
        ],
        glass=True,
        cls="nova-navbar px-3",
    )

    hero = Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge(
                            "FastHTML + Faststrap + HTMX",
                            variant="light",
                            cls="text-dark fw-semibold px-3 py-2 mb-4",
                        ),
                        Div(
                            Span("Build polished Python web apps", cls="d-block"),
                            Span(
                                "without defaulting to front-end chaos.", cls="d-block text-primary"
                            ),
                            cls=f"nova-display fw-bold {Fx.base} {Fx.slide_up}",
                        ),
                        P(
                            "NovaFlow is the kind of SaaS front-end Faststrap should make obvious: strong hierarchy, real interaction patterns, Bootstrap-native foundations, and enough visual polish to feel launch-ready.",
                            cls=f"lead mt-4 mb-4 nova-subtitle {Fx.base} {Fx.fade_in} {Fx.delay_sm}",
                        ),
                        Div(
                            A(
                                Span(Icon("rocket-takeoff-fill", cls="me-2"), "Start building"),
                                href="#cta",
                                cls=f"btn btn-primary btn-lg px-4 {Fx.base} {Fx.fade_in} {Fx.delay_md}",
                            ),
                            A(
                                Span(Icon("search", cls="me-2"), "Explore components"),
                                href="#search",
                                cls=f"btn btn-outline-light btn-lg px-4 {Fx.base} {Fx.fade_in} {Fx.delay_lg}",
                            ),
                            cls="d-flex flex-column flex-sm-row gap-3",
                        ),
                        Div(
                            Div(
                                Strong("12 min"),
                                Br(),
                                Small("to first polished page"),
                                cls="nova-stat-pill px-4 py-3",
                            ),
                            Div(
                                Strong("110+"),
                                Br(),
                                Small("exports across UI, data, and presets"),
                                cls="nova-stat-pill px-4 py-3",
                            ),
                            Div(
                                Strong("Python"),
                                Br(),
                                Small("all the way from UI to backend"),
                                cls="nova-stat-pill px-4 py-3",
                            ),
                            cls="d-grid d-md-flex gap-3 mt-4",
                        ),
                        cls="pt-4 pt-lg-5",
                    ),
                    lg=7,
                    cls="mb-5 mb-lg-0",
                ),
                Col(
                    Div(
                        Div(
                            Span(cls="nova-dot bg-danger"),
                            Span(cls="nova-dot bg-warning mx-2"),
                            Span(cls="nova-dot bg-success"),
                            Span("NovaFlow launch console", cls="ms-3 small text-body-secondary"),
                            cls="nova-console-bar px-4 py-3 d-flex align-items-center",
                        ),
                        Div(
                            P(
                                "Launch sequence",
                                cls="text-uppercase small text-body-secondary mb-3",
                            ),
                            Div(
                                Code(
                                    "add_bootstrap(app, theme=novaflow, mode='auto', font_family='Plus Jakarta Sans')",
                                    cls="nova-code",
                                ),
                                Br(),
                                Code(
                                    "NavbarModern(...), FeatureGrid(...), PricingGroup(...)",
                                    cls="nova-code",
                                ),
                                Br(),
                                Code(
                                    "ActiveSearch(...), LoadingButton(...), toast_response(...)",
                                    cls="nova-code",
                                ),
                                cls="mb-4",
                            ),
                            Row(
                                Col(
                                    Div(
                                        Small(
                                            "Ship launch surfaces",
                                            cls="text-body-secondary d-block mb-2",
                                        ),
                                        Strong("Marketing pages with product weight"),
                                        cls="nova-surface p-3 d-block h-100",
                                    ),
                                    md=6,
                                    cls="mb-3",
                                ),
                                Col(
                                    Div(
                                        Small(
                                            "Keep interactions calm",
                                            cls="text-body-secondary d-block mb-2",
                                        ),
                                        Strong("HTMX flows instead of client-state bloat"),
                                        cls="nova-surface p-3 d-block h-100",
                                    ),
                                    md=6,
                                    cls="mb-3",
                                ),
                            ),
                            Div(
                                Span(
                                    Icon("check2-circle", cls="me-2 text-success"),
                                    "Bootstrap semantics preserved",
                                ),
                                Br(),
                                Span(
                                    Icon("check2-circle", cls="me-2 text-success"),
                                    "Minimal JS only where HTMX cannot help",
                                ),
                                Br(),
                                Span(
                                    Icon("check2-circle", cls="me-2 text-success"),
                                    "Custom CSS reserved for polish, not reinvention",
                                ),
                                cls="text-body-secondary small",
                            ),
                            cls="p-4 p-lg-5",
                        ),
                        cls=f"nova-console {Fx.base} {Fx.zoom_in}",
                    ),
                    lg=5,
                ),
                cls="align-items-center",
            )
        ),
        cls="nova-hero",
        id="top",
    )

    logo_rail = Div(
        Container(
            Div(
                *[
                    Span(label, cls="nova-logo-pill px-4 py-2")
                    for label in [
                        "Northpath",
                        "Ribbon AI",
                        "Cinder Ops",
                        "Atlas Cloud",
                        "StackPilot",
                        "FrameOS",
                    ]
                ],
                cls="d-flex flex-wrap gap-3 justify-content-center py-4",
            )
        ),
        cls="nova-logo-rail",
    )

    momentum_strip = Div(
        Container(
            Row(
                Col(
                    Card(
                        Div(
                            Small(
                                "Conversion-ready sections",
                                cls="text-uppercase text-muted fw-semibold",
                            ),
                            H3(
                                "Hero, pricing, proof, and CTA all wired into one surface.",
                                cls="h5 mt-2 mb-1",
                            ),
                            P(
                                "The page reads like a launch asset, not a component dump.",
                                cls="text-muted mb-0",
                            ),
                        ),
                        cls="border-0 h-100",
                    ),
                    md=4,
                    cls="mb-3 mb-md-0",
                ),
                Col(
                    Card(
                        Div(
                            Small(
                                "HTMX where it earns its keep",
                                cls="text-uppercase text-muted fw-semibold",
                            ),
                            H3(
                                "Search, theme persistence, and submission feedback stay server-driven.",
                                cls="h5 mt-2 mb-1",
                            ),
                            P(
                                "You keep the flow dynamic without turning the page into a JS project.",
                                cls="text-muted mb-0",
                            ),
                        ),
                        cls="border-0 h-100",
                    ),
                    md=4,
                    cls="mb-3 mb-md-0",
                ),
                Col(
                    Card(
                        Div(
                            Small(
                                "Polish without fragility",
                                cls="text-uppercase text-muted fw-semibold",
                            ),
                            H3(
                                "Bootstrap carries structure while CSS handles atmosphere and depth.",
                                cls="h5 mt-2 mb-1",
                            ),
                            P(
                                "That is the design contract we want showcase apps to demonstrate.",
                                cls="text-muted mb-0",
                            ),
                        ),
                        cls="border-0 h-100",
                    ),
                    md=4,
                ),
                cls="g-3",
            )
        ),
        cls="nova-section nova-momentum py-4",
    )

    feature_section = Div(
        Container(
            Div(
                Badge("Why teams switch", variant="light", cls="text-dark px-3 py-2 mb-3"),
                H2(
                    "Faststrap gives Python teams a cleaner path to premium product UI.",
                    cls="display-6 fw-bold",
                ),
                P(
                    "The point is not to imitate a front-end stack. The point is to keep Bootstrap's strengths, use HTMX where it wins, and add the visual confidence most Python UI layers never quite reach.",
                    cls="text-muted fs-5 mb-0",
                ),
                cls=f"text-center mb-5 {Fx.base} {Fx.fade_in}",
            ),
            FeatureGrid(*feature_items(), columns=3),
        ),
        id="features",
        cls="nova-section nova-section-light py-5 py-lg-6",
    )

    use_case_section = Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge(
                            "Built for real products",
                            variant="light",
                            cls="text-dark px-3 py-2 mb-3",
                        ),
                        H2(
                            "Not just buttons and cards. Real surfaces, real pages, real product weight.",
                            cls="display-6 fw-bold",
                        ),
                        P(
                            "Faststrap should feel equally at home on a launch page, an admin tool, or a client-facing product surface. The showcase layer needs to prove that.",
                            cls="text-muted fs-5 mb-0",
                        ),
                        cls=f"{Fx.base} {Fx.fade_in}",
                    ),
                    lg=5,
                    cls="mb-4 mb-lg-0",
                ),
                Col(Row(*use_case_cards()), lg=7),
                cls="align-items-center",
            )
        ),
        id="use-cases",
        cls="nova-section py-5",
    )

    search_section = Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge(
                            "Live component explorer",
                            variant="light",
                            cls="text-dark px-3 py-2 mb-3",
                        ),
                        H2("Search the Faststrap surface as you type.", cls="display-6 fw-bold"),
                        P(
                            "This is the kind of tiny product interaction that should come for free: fast, server-driven, and easy to reason about. No front-end state machine required.",
                            cls="text-muted fs-5 mb-4",
                        ),
                        Div(
                            Span(
                                Icon("lightning-charge-fill", cls="me-2 text-primary"),
                                "Powered by ActiveSearch",
                            ),
                            cls="nova-chip d-inline-flex align-items-center px-3 py-2",
                        ),
                        cls=f"{Fx.base} {Fx.fade_in}",
                    ),
                    lg=5,
                    cls="mb-4 mb-lg-0",
                ),
                Col(
                    Div(
                        ActiveSearch(
                            endpoint="/api/component-search",
                            target="#novaflow-search-results",
                            placeholder="Try 'dashboard', 'markdown', 'notification', 'data'...",
                            debounce=220,
                            cls="nova-search-input mb-4",
                        ),
                        Div(
                            Div(
                                Badge("Suggested", variant="light", cls="text-dark me-2"),
                                Span("DataTable", cls="nova-search-tag"),
                                Span("Chart", cls="nova-search-tag mx-2"),
                                Span("ThemeToggle", cls="nova-search-tag"),
                                Span("NotificationCenter", cls="nova-search-tag ms-2"),
                                cls="text-muted small mb-3 d-flex flex-wrap gap-2 align-items-center",
                            ),
                            Div(
                                Card(
                                    Div(
                                        H4("Start typing to explore components", cls="h5 fw-bold"),
                                        P(
                                            "This panel returns server-rendered cards that you can replace, extend, or wire into your own docs and internal tooling.",
                                            cls="text-muted mb-0",
                                        ),
                                    ),
                                    cls="border-0",
                                ),
                                id="novaflow-search-results",
                                cls="nova-search-results",
                            ),
                        ),
                        cls=f"nova-panel p-4 p-lg-5 {Fx.base} {Fx.slide_up}",
                    ),
                    lg=7,
                ),
                cls="align-items-center",
            )
        ),
        id="search",
        cls="nova-section py-5",
    )

    production_section = Div(
        Container(
            Row(
                Col(
                    Div(
                        Badge(
                            "Implementation contract",
                            variant="light",
                            cls="text-dark px-3 py-2 mb-3",
                        ),
                        H2(
                            "This is the bar Faststrap showcase apps should hit.",
                            cls="display-6 fw-bold text-white",
                        ),
                        P(
                            "A flagship sample should not just prove components exist. It should prove a Python team can ship a credible launch surface with theming, feedback loops, and product-grade rhythm.",
                            cls="fs-5 text-white-50 mb-4",
                        ),
                        Div(
                            Div(
                                Small(
                                    "Bootstrap-first structure",
                                    cls="text-uppercase text-white-50 fw-semibold",
                                ),
                                H4(
                                    "Rows, cards, spacing, and utility classes do the heavy lifting.",
                                    cls="h5 mt-2 mb-1 text-white",
                                ),
                                P(
                                    "Custom CSS only sharpens the atmosphere instead of fighting the framework.",
                                    cls="text-white-50 mb-0",
                                ),
                                cls="nova-mini-stat p-4",
                            ),
                            Div(
                                Small(
                                    "HTMX for the living parts",
                                    cls="text-uppercase text-white-50 fw-semibold",
                                ),
                                H4(
                                    "Search, toggles, and feedback stay server-driven and understandable.",
                                    cls="h5 mt-2 mb-1 text-white",
                                ),
                                P(
                                    "That keeps the codebase calmer while still feeling interactive.",
                                    cls="text-white-50 mb-0",
                                ),
                                cls="nova-mini-stat p-4",
                            ),
                            cls="d-grid gap-3",
                        ),
                        cls=f"{Fx.base} {Fx.fade_in}",
                    ),
                    lg=5,
                    cls="mb-4 mb-lg-0",
                ),
                Col(
                    Card(
                        Div(
                            Small(
                                "Checklist for premium samples",
                                cls="text-uppercase text-white-50 fw-semibold",
                            ),
                            H3(
                                "A showcase should read like a product surface, not a component lab.",
                                cls="h4 mt-2 mb-4 text-white",
                            ),
                            Div(
                                Div(
                                    Icon("check2-circle", cls="text-success fs-5 mt-1"),
                                    Div(
                                        Strong(
                                            "Clear visual hierarchy", cls="d-block text-white mb-1"
                                        ),
                                        Small(
                                            "Hero, supporting proof, product sections, and CTA all feel intentionally sequenced.",
                                            cls="text-white-50",
                                        ),
                                    ),
                                    cls="nova-checklist-item",
                                ),
                                Div(
                                    Icon("check2-circle", cls="text-success fs-5 mt-1"),
                                    Div(
                                        Strong(
                                            "Real interaction examples",
                                            cls="d-block text-white mb-1",
                                        ),
                                        Small(
                                            "Theme persistence, search, and form feedback demonstrate believable product behavior.",
                                            cls="text-white-50",
                                        ),
                                    ),
                                    cls="nova-checklist-item",
                                ),
                                Div(
                                    Icon("check2-circle", cls="text-success fs-5 mt-1"),
                                    Div(
                                        Strong(
                                            "Brandable without extra frameworks",
                                            cls="d-block text-white mb-1",
                                        ),
                                        Small(
                                            "Typography, color, and polish come from Faststrap plus local CSS instead of a parallel stack.",
                                            cls="text-white-50",
                                        ),
                                    ),
                                    cls="nova-checklist-item",
                                ),
                                cls="nova-checklist",
                            ),
                        ),
                        cls=f"nova-principle-card border-0 p-4 p-lg-5 h-100 {Fx.base} {Fx.slide_up}",
                    ),
                    lg=7,
                ),
                cls="align-items-center",
            )
        ),
        cls="nova-section nova-section-dark py-5",
    )

    pricing = Div(
        Container(
            Div(
                Badge("Simple pricing", variant="light", cls="text-dark px-3 py-2 mb-3"),
                H2(
                    "Choose the path from quick prototype to serious product.",
                    cls="display-6 fw-bold text-center",
                ),
                P(
                    "Pricing cards should feel like conversion surfaces, not placeholders. Faststrap gives you the primitives. The showcase layer should prove the finish.",
                    cls="nova-pricing-note fs-5 text-center mb-5",
                ),
                cls=f"{Fx.base} {Fx.fade_in}",
            ),
            PricingGroup(
                PricingTier(
                    "Starter",
                    0,
                    features=[
                        "Core Faststrap component surface",
                        "Built-in themes and effects",
                        "Good for demos, prototypes, and small launches",
                    ],
                    button_text="Start with Python",
                ),
                PricingTier(
                    "Growth",
                    49,
                    highlighted=True,
                    features=[
                        "DataTable, Chart, and dashboard surfaces",
                        "HTMX presets for interaction-heavy screens",
                        "Reusable layouts for SaaS, auth, and admin work",
                    ],
                    button_text="Build polished products",
                ),
                PricingTier(
                    "Scale",
                    199,
                    features=[
                        "Multi-team design systems in Python",
                        "SEO, PWA, auth, and deployment patterns",
                        "Reference-grade showcases and app-building guidance",
                    ],
                    button_text="Ship with confidence",
                ),
                title="Plans that map to real build maturity",
                subtitle="The value is not just components. It is how fast you can move from rough structure to a coherent product surface.",
            ),
        ),
        id="pricing",
        cls="nova-section nova-section-light py-5",
    )

    testimonials = Div(
        TestimonialSection(
            *[
                Testimonial(
                    quote=item["quote"],
                    author=item["author"],
                    role=item["role"],
                    rating=item["rating"],
                    cls=f"{Fx.base} {Fx.fade_in} {Fx.hover_lift}",
                )
                for item in TESTIMONIALS
            ],
            title="Teams do not want another UI science project.",
            subtitle="They want a stack that keeps them moving, keeps the markup honest, and still lets the product feel premium.",
            columns=3,
            cls="nova-testimonials",
        ),
        id="stories",
        cls="nova-section nova-section-dark py-5",
    )

    waitlist_form = Form(
        Row(
            Col(
                Input(
                    "email",
                    input_type="email",
                    placeholder="Work email",
                    required=True,
                    aria_label="Work email",
                ),
                md=5,
                cls="mb-3 mb-md-0",
            ),
            Col(
                Select(
                    "team_size",
                    ("solo", "Solo builder"),
                    ("small", "2-10 people", True),
                    ("mid", "11-50 people"),
                    ("large", "50+ people"),
                    aria_label="Team size",
                ),
                md=3,
                cls="mb-3 mb-md-0",
            ),
            Col(
                LoadingButton(
                    Span(Icon("send-fill", cls="me-2"), "Join the waitlist"),
                    endpoint="/api/waitlist",
                    target="#waitlist-result",
                    variant="primary",
                    cls="w-100 h-100",
                ),
                md=4,
            ),
            cls="g-3 align-items-stretch",
        ),
    )

    cta = Hero(
        "Ship product UI with more confidence and less ceremony.",
        subtitle=(
            "Faststrap works best when the examples prove the ceiling. This showcase starts that new bar: stronger visual language, cleaner interactions, and reference-grade composition."
        ),
        cta=Div(
            Div(waitlist_form, cls="nova-cta-card p-3 p-lg-4 mb-3"),
            Div(
                Span(
                    Icon("shield-check", cls="text-success"),
                    "Server-rendered by default",
                    cls="nova-cta-note",
                ),
                Span(
                    Icon("palette-fill", cls="text-primary"),
                    "Theme-aware surfaces",
                    cls="nova-cta-note",
                ),
                Span(
                    Icon("lightning-charge-fill", cls="text-warning"),
                    "HTMX-first interactions",
                    cls="nova-cta-note",
                ),
                cls="d-flex flex-wrap justify-content-center gap-2 mb-3",
            ),
            Div(id="waitlist-result"),
        ),
        align="center",
        container=False,
        cls="py-5 py-lg-6 text-white",
    )

    footer = FooterModern(
        brand=Div(
            Span(Icon("stars"), cls="nova-brand-mark me-3"),
            Span("NovaFlow", cls="fs-4 fw-bold"),
            cls="d-flex align-items-center",
        ),
        tagline="A flagship Faststrap showcase focused on premium Python-first product UI.",
        columns=FOOTER_COLUMNS,
        social_links=SOCIAL_LINKS,
        copyright_text="Copyright 2026 NovaFlow. Built as a Faststrap flagship showcase.",
        bg_variant="dark",
        text_variant="light",
        cls="nova-footer",
    )

    return Div(
        Style(SHOWCASE_CSS),
        ToastContainer(position="top-end", id="toast-container"),
        Div(
            LandingLayout(
                Div(nav, cls="nova-nav-wrap"),
                hero,
                logo_rail,
                momentum_strip,
                feature_section,
                use_case_section,
                search_section,
                production_section,
                pricing,
                testimonials,
                Div(Container(cta), id="cta", cls="nova-section nova-section-dark py-5"),
                navbar=None,
                footer=footer,
                fluid=True,
            ),
            cls="nova-shell",
        ),
        cls="nova-app",
        data_bs_theme=theme,
    )


@app.get("/api/component-search")
def component_search(q: str = "") -> Any:
    cards = search_result_cards(q)
    if not q.strip():
        return Card(
            Div(
                H4("Start typing to explore components", cls="h5 fw-bold"),
                P(
                    "Search for data surfaces, forms, feedback, content helpers, and newer flagship-ready features.",
                    cls="text-muted mb-0",
                ),
            ),
            cls="border-0 nova-search-empty",
        )

    if not cards:
        return Alert(
            f"No Faststrap surface matched '{q}'. Try 'data', 'theme', 'search', or 'dashboard'.",
            variant="warning",
        )

    return Row(*cards)


@app.post("/api/waitlist")
def join_waitlist(email: str = "", team_size: str = "") -> Any:
    normalized_email = email.strip()
    if "@" not in normalized_email or "." not in normalized_email.split("@")[-1]:
        return toast_response(
            content=Alert("Please enter a valid work email so we can reply.", variant="danger"),
            message="Waitlist signup needs a valid email.",
            variant="danger",
        )

    team_copy = {
        "solo": "Solo builder",
        "small": "2-10 people",
        "mid": "11-50 people",
        "large": "50+ people",
    }.get(team_size, "your team")

    return toast_response(
        content=Alert(
            f"Thanks, {normalized_email}. NovaFlow saved your request for {team_copy}.",
            variant="success",
        ),
        message="Waitlist request received.",
        variant="success",
    )


@app.post("/theme/toggle")
def toggle_theme(req) -> Any:
    next_theme = "light" if current_theme(req) == "dark" else "dark"
    req.session[THEME_COOKIE] = next_theme
    return hx_refresh()


if __name__ == "__main__":
    serve(port=5001)
