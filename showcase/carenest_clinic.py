"""Flagship showcase — CareNest Clinic.

Premium healthcare / clinic appointment website for Faststrap:

- AuthLayout for login and registration flows
- FormBuilder, FormErrorSummary, FloatingLabel, InputGroup for full form coverage
- Modal for appointment confirmation, NoticeAlert for status feedback
- Switch, Checkbox for patient preference forms
- ThemeToggle for dual light/dark support
- HTMX-first interactions (form submission, search, slot availability)
- Custom CSS for medical-grade clean aesthetic (light-first, teal/slate brand)
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H4,
    H5,
    A,
    Br,
    Button,
    Div,
    FastHTML,
    Form,
    Hr,
    Input,
    Li,
    Option,
    P,
    Select,
    Small,
    Span,
    Style,
    Textarea,
    Ul,
    serve,
)

from faststrap import (
    AuthLayout,
    Checkbox,
    Col,
    FilePreview,
    FloatingLabel,
    FormErrorSummary,
    Icon,
    InputGroupText,
    Modal,
    NoticeAlert,
    Row,
    Switch,
    ThemeToggle,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import LoadingButton, hx_refresh

THEME_KEY = "carenest_theme"

CARENEST_THEME = create_theme(
    primary="#0D9488",  # teal-600
    secondary="#1E293B",  # slate-800
    success="#16A34A",
    danger="#DC2626",
    warning="#D97706",
    info="#0EA5E9",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = """
/* ═══════════════════════════════════════════════════════════
   CareNest · Premium healthcare CSS
   Philosophy: clinical clarity — light-first, precision
   geometry (4-8px radii), trust-building visual restraint.
   ═══════════════════════════════════════════════════════════ */

/* ── Base shell ─────────────────────────────────────────── */
.cn-app {
  min-height: 100vh;
  background: #f0fafa;
  color: #0f172a;
  font-family: "Inter", "Outfit", system-ui, sans-serif;
}

.cn-app[data-bs-theme="dark"] {
  background:
    radial-gradient(ellipse at 0% 0%, rgba(13, 148, 136, 0.12), transparent 32%),
    linear-gradient(180deg, #071015 0%, #0a1520 60%, #0c1a26 100%);
  color: #e2e8f0;
}

/* ── Navbar ─────────────────────────────────────────────── */
.cn-nav-wrap {
  position: sticky;
  top: 0;
  z-index: 20;
  padding: 0;
  border-bottom: 1px solid rgba(15, 23, 42, 0.08);
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(20px) saturate(1.4);
  -webkit-backdrop-filter: blur(20px) saturate(1.4);
}

.cn-app[data-bs-theme="dark"] .cn-nav-wrap {
  background: rgba(7, 16, 21, 0.88);
  border-bottom-color: rgba(255, 255, 255, 0.06);
}

.cn-navbar {
  background: transparent;
  border: none;
  border-radius: 0;
  box-shadow: none;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.cn-navbar .nav-link {
  color: rgba(30, 41, 59, 0.78);
  font-size: 0.86rem;
  font-weight: 500;
  border-radius: 4px;
  padding: 0.4rem 0.8rem !important;
  transition: color 0.15s ease, background 0.15s ease;
}

.cn-navbar .nav-link:hover { color: #0D9488; background: rgba(13, 148, 136, 0.06); }

.cn-app[data-bs-theme="dark"] .cn-navbar .nav-link {
  color: rgba(203, 213, 225, 0.78);
}
.cn-app[data-bs-theme="dark"] .cn-navbar .nav-link:hover {
  color: #2DD4BF;
  background: rgba(13, 148, 136, 0.08);
}

.cn-navbar .btn { font-size: 0.84rem; font-weight: 600; border-radius: 5px; }
.cn-navbar .btn-primary { box-shadow: 0 4px 14px rgba(13, 148, 136, 0.28); }

/* Brand mark */
.cn-brand-mark {
  width: 1.9rem;
  height: 1.9rem;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0D9488, #0EA5E9);
  color: #fff;
  font-size: 0.88rem;
  box-shadow: 0 2px 10px rgba(13, 148, 136, 0.32);
  flex-shrink: 0;
}

/* ── Hero ───────────────────────────────────────────────── */
.cn-hero {
  position: relative;
  padding: 5rem 0 4.5rem;
  background:
    radial-gradient(ellipse at 10% 50%, rgba(13, 148, 136, 0.07), transparent 40%),
    linear-gradient(180deg, #f0fafa 0%, #ffffff 100%);
  border-bottom: 1px solid rgba(15, 23, 42, 0.06);
  overflow: hidden;
}

.cn-app[data-bs-theme="dark"] .cn-hero {
  background:
    radial-gradient(ellipse at 10% 50%, rgba(13, 148, 136, 0.12), transparent 40%),
    linear-gradient(180deg, #071015, #0c1624);
  border-bottom-color: rgba(255, 255, 255, 0.05);
}

/* Subtle cross-hatch bg pattern */
.cn-hero::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(13, 148, 136, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(13, 148, 136, 0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(ellipse at 80% 50%, rgba(0,0,0,0.5), transparent 70%);
}

.cn-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.32rem 0.72rem;
  border-radius: 4px;
  background: rgba(13, 148, 136, 0.08);
  border: 1px solid rgba(13, 148, 136, 0.16);
  color: #0D9488;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.cn-app[data-bs-theme="dark"] .cn-hero-badge {
  background: rgba(13, 148, 136, 0.12);
  border-color: rgba(13, 148, 136, 0.22);
  color: #2DD4BF;
}

.cn-display {
  font-size: clamp(2.4rem, 5.5vw, 4.2rem);
  line-height: 1.05;
  letter-spacing: -0.035em;
  font-weight: 800;
  color: #071015;
}

.cn-app[data-bs-theme="dark"] .cn-display { color: #f0f9ff; }

.cn-subtitle {
  max-width: 38rem;
  color: #475569;
  font-size: 1.025rem;
  line-height: 1.72;
}

.cn-app[data-bs-theme="dark"] .cn-subtitle { color: rgba(148, 163, 184, 0.88); }

/* ── Trust badges ───────────────────────────────────────── */
.cn-trust-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.9rem;
  border-radius: 5px;
  border: 1px solid rgba(15, 23, 42, 0.08);
  background: #fff;
  color: #334155;
  font-size: 0.8rem;
  font-weight: 600;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
}

.cn-app[data-bs-theme="dark"] .cn-trust-badge {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
  color: #cbd5e1;
}

/* ── Quick booking card ─────────────────────────────────── */
.cn-booking-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 10px;
  background: #fff;
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.9) inset,
    0 4px 16px rgba(15, 23, 42, 0.06),
    0 20px 48px rgba(15, 23, 42, 0.07);
}

.cn-app[data-bs-theme="dark"] .cn-booking-card {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(16px);
  box-shadow: 0 20px 56px rgba(0, 0, 0, 0.3);
}

.cn-booking-card .form-control,
.cn-booking-card .form-select {
  border-radius: 5px;
  border-color: rgba(15, 23, 42, 0.12);
  font-size: 0.9rem;
}

.cn-booking-card .form-control:focus,
.cn-booking-card .form-select:focus {
  border-color: rgba(13, 148, 136, 0.45);
  box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.1);
}

.cn-app[data-bs-theme="dark"] .cn-booking-card .form-control,
.cn-app[data-bs-theme="dark"] .cn-booking-card .form-select {
  border-color: rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.05);
  color: #f0f9ff;
}

/* ── Sections ───────────────────────────────────────────── */
.cn-section {
  padding: 5rem 0;
}

.cn-section-alt {
  background: #f8fafc;
  border-top: 1px solid rgba(15, 23, 42, 0.06);
  border-bottom: 1px solid rgba(15, 23, 42, 0.06);
}

.cn-app[data-bs-theme="dark"] .cn-section-alt {
  background: rgba(255, 255, 255, 0.016);
  border-color: rgba(255, 255, 255, 0.05);
}

.cn-section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.42rem;
  padding: 0.3rem 0.68rem;
  border-radius: 4px;
  background: rgba(13, 148, 136, 0.07);
  border: 1px solid rgba(13, 148, 136, 0.14);
  color: #0D9488;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.cn-app[data-bs-theme="dark"] .cn-section-label {
  background: rgba(13, 148, 136, 0.1);
  color: #2DD4BF;
}

/* ── Specialty cards ────────────────────────────────────── */
.cn-specialty-card {
  position: relative;
  overflow: hidden;
  padding: 1.5rem 1.5rem 1.5rem 1.75rem;
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  cursor: pointer;
  color: #0f172a;
  text-decoration: none;
  display: block;
}

.cn-specialty-card::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 3px;
  background: linear-gradient(180deg, #0D9488, #0EA5E9);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.cn-specialty-card:hover::before { opacity: 1; }

.cn-specialty-card:hover {
  transform: translateY(-3px);
  border-color: rgba(13, 148, 136, 0.2);
  box-shadow: 0 10px 32px rgba(15, 23, 42, 0.08);
  color: #0f172a;
  text-decoration: none;
}

.cn-app[data-bs-theme="dark"] .cn-specialty-card {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.035);
  color: #e2e8f0;
}

.cn-app[data-bs-theme="dark"] .cn-specialty-card:hover {
  border-color: rgba(13, 148, 136, 0.25);
  color: #e2e8f0;
}

.cn-spec-icon {
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  margin-bottom: 0.875rem;
  background: rgba(13, 148, 136, 0.08);
  color: #0D9488;
}

.cn-app[data-bs-theme="dark"] .cn-spec-icon {
  background: rgba(13, 148, 136, 0.14);
  color: #2DD4BF;
}

/* ── Doctor cards ───────────────────────────────────────── */
.cn-doctor-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.cn-doctor-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 32px rgba(15, 23, 42, 0.08);
  border-color: rgba(13, 148, 136, 0.18);
}

/* Sharp top accent bar */
.cn-doctor-card::before {
  content: "";
  display: block;
  height: 2px;
  background: linear-gradient(90deg, #0D9488, rgba(14, 165, 233, 0.3));
}

.cn-app[data-bs-theme="dark"] .cn-doctor-card {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
}

.cn-doctor-card .text-muted { color: #64748b !important; }
.cn-app[data-bs-theme="dark"] .cn-doctor-card .text-muted {
  color: rgba(148, 163, 184, 0.8) !important;
}

.cn-doctor-avatar {
  width: 3.2rem;
  height: 3.2rem;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.cn-avail-slot {
  display: inline-flex;
  padding: 0.3rem 0.65rem;
  border-radius: 4px;
  font-size: 0.78rem;
  font-weight: 600;
  border: 1px solid rgba(13, 148, 136, 0.2);
  background: rgba(13, 148, 136, 0.06);
  color: #0D9488;
  cursor: pointer;
  transition: background 0.15s ease, border-color 0.15s ease;
}

.cn-avail-slot:hover {
  background: rgba(13, 148, 136, 0.12);
  border-color: rgba(13, 148, 136, 0.3);
}

.cn-app[data-bs-theme="dark"] .cn-avail-slot {
  color: #2DD4BF;
  border-color: rgba(13, 148, 136, 0.22);
  background: rgba(13, 148, 136, 0.08);
}

/* ── Stat cards ─────────────────────────────────────────── */
.cn-stat-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
}

.cn-app[data-bs-theme="dark"] .cn-stat-card {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
}

/* ── Process steps ──────────────────────────────────────── */
.cn-step {
  display: flex;
  gap: 1.1rem;
  align-items: flex-start;
}

.cn-step-num {
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 6px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0D9488, #0EA5E9);
  color: #fff;
  font-size: 0.8rem;
  font-weight: 800;
  flex-shrink: 0;
  letter-spacing: 0.01em;
}

/* ── Notice alerts ──────────────────────────────────────── */
.cn-app .alert {
  border-radius: 6px;
  border-left-width: 3px;
}

/* ── Form area ──────────────────────────────────────────── */
.cn-form-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 10px;
  background: #fff;
  box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
}

.cn-app[data-bs-theme="dark"] .cn-form-card {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(16px);
}

.cn-form-card .form-label {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  color: #334155;
}

.cn-app[data-bs-theme="dark"] .cn-form-card .form-label { color: #94a3b8; }

.cn-form-card .form-control,
.cn-form-card .form-select {
  border-radius: 5px;
  border-color: rgba(15, 23, 42, 0.12);
  font-size: 0.9rem;
  min-height: 2.75rem;
}

.cn-form-card .form-control:focus,
.cn-form-card .form-select:focus {
  border-color: rgba(13, 148, 136, 0.45);
  box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.1);
}

.cn-app[data-bs-theme="dark"] .cn-form-card .form-control,
.cn-app[data-bs-theme="dark"] .cn-form-card .form-select {
  border-color: rgba(255, 255, 255, 0.09);
  background: rgba(255, 255, 255, 0.04);
  color: #f0f9ff;
}

.cn-form-card .btn-primary { border-radius: 5px; min-height: 2.8rem; font-weight: 600; }

/* ── Testimonial cards ──────────────────────────────────── */
.cn-testimonial {
  position: relative;
  border: 1px solid rgba(15, 23, 42, 0.08);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

.cn-testimonial:hover {
  box-shadow: 0 8px 28px rgba(15, 23, 42, 0.08);
  transform: translateY(-2px);
}

.cn-testimonial::after {
  content: "\201C";
  position: absolute;
  top: 0.75rem;
  right: 1.25rem;
  font-size: 3rem;
  line-height: 1;
  color: rgba(13, 148, 136, 0.1);
  font-weight: 900;
}

.cn-app[data-bs-theme="dark"] .cn-testimonial {
  border-color: rgba(255, 255, 255, 0.07);
  background: rgba(255, 255, 255, 0.04);
}

/* ── Footer ─────────────────────────────────────────────── */
.cn-footer {
  border-top: 1px solid rgba(15, 23, 42, 0.07) !important;
  background: #f8fafc !important;
}

.cn-app[data-bs-theme="dark"] .cn-footer {
  background: rgba(7, 16, 21, 0.9) !important;
  border-top-color: rgba(255, 255, 255, 0.06) !important;
}

/* ── Auth layout overrides ──────────────────────────────── */
.cn-app .auth-layout-card {
  border-radius: 10px !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  box-shadow: 0 4px 20px rgba(15, 23, 42, 0.07), 0 20px 52px rgba(15, 23, 42, 0.06) !important;
}

.cn-app[data-bs-theme="dark"] .auth-layout-card {
  border-color: rgba(255, 255, 255, 0.07) !important;
  background: rgba(10, 18, 26, 0.96) !important;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4) !important;
}

/* ── Responsive ─────────────────────────────────────────── */
@media (max-width: 991.98px) {
  .cn-hero { padding: 3.5rem 0 3rem; }
  .cn-display { font-size: clamp(2rem, 9vw, 3rem); letter-spacing: -0.025em; }
  .cn-section { padding: 3.5rem 0; }
}

@media (max-width: 575.98px) {
  .cn-display { font-size: clamp(1.8rem, 10vw, 2.6rem); }
  .cn-hero { padding: 2.75rem 0 2.5rem; }
}
"""

# ── Sample data ───────────────────────────────────────────────────────────────
SPECIALTIES = [
    {
        "icon": "heart-pulse",
        "title": "Cardiology",
        "desc": "Expert heart care, ECG, echo, and stress testing.",
        "patients": "2,400+",
    },
    {
        "icon": "lungs",
        "title": "Pulmonology",
        "desc": "Respiratory health, asthma management, spirometry.",
        "patients": "1,800+",
    },
    {
        "icon": "person-arms-up",
        "title": "Orthopedics",
        "desc": "Joint care, sports injuries, physiotherapy.",
        "patients": "3,100+",
    },
    {
        "icon": "eye",
        "title": "Ophthalmology",
        "desc": "Eye exams, vision correction, retinal care.",
        "patients": "2,650+",
    },
    {
        "icon": "activity",
        "title": "Neurology",
        "desc": "Brain and nervous system disorders, migraines.",
        "patients": "1,200+",
    },
    {
        "icon": "bandaid",
        "title": "Dermatology",
        "desc": "Skin conditions, mole checks, cosmetic care.",
        "patients": "3,800+",
    },
]

DOCTORS = [
    {
        "initials": "AO",
        "name": "Dr. Adaeze Okonkwo",
        "specialty": "Cardiologist",
        "rating": "4.9",
        "reviews": 218,
        "color": "bg-primary text-white",
        "slots": ["9:00", "11:30", "14:00"],
    },
    {
        "initials": "MJ",
        "name": "Dr. Marcus Jensen",
        "specialty": "Pulmonologist",
        "rating": "4.8",
        "reviews": 176,
        "color": "bg-info text-white",
        "slots": ["10:00", "13:30", "16:00"],
    },
    {
        "initials": "SN",
        "name": "Dr. Sunita Nair",
        "specialty": "Neurologist",
        "rating": "4.9",
        "reviews": 142,
        "color": "bg-success text-white",
        "slots": ["8:30", "12:00", "15:30"],
    },
    {
        "initials": "CL",
        "name": "Dr. Clara Lopes",
        "specialty": "Dermatologist",
        "rating": "5.0",
        "reviews": 304,
        "color": "bg-warning text-dark",
        "slots": ["9:30", "11:00", "14:30"],
    },
]

STATS = [
    {"value": "12,000+", "label": "Patients served", "icon": "people"},
    {"value": "48", "label": "Specialist doctors", "icon": "person-badge"},
    {"value": "98%", "label": "Satisfaction rate", "icon": "star"},
    {"value": "< 24h", "label": "Avg. booking time", "icon": "clock"},
]

TESTIMONIALS = [
    {
        "text": "The online booking system is seamless. I had an appointment with Dr. Okonkwo within hours of registering — the experience felt genuinely premium.",
        "name": "Emeka Adeyemi",
        "role": "Patient · Cardiology",
    },
    {
        "text": "CareNest's dermatology team identified my condition within the first visit. The follow-up system and clear treatment plan gave me real peace of mind.",
        "name": "Fatima Al-Hassan",
        "role": "Patient · Dermatology",
    },
    {
        "text": "As someone who avoids hospitals, this clinic changed my view. Staff are warm, the environment is clean, and the doctors actually listen.",
        "name": "Oluwaseun Bello",
        "role": "Patient · Orthopedics",
    },
]

FORM_ERRORS_DEMO = {
    "full_name": "Full name is required",
    "email": "Enter a valid email address",
    "phone": "Phone number must be 10 digits",
}


# ── Route helpers ─────────────────────────────────────────────────────────────
def theme_from_req(req) -> str:
    return req.session.get(THEME_KEY) or req.cookies.get(THEME_KEY, "light")


def cn_theme_toggle(theme: str, cls: str = "") -> Any:
    return ThemeToggle(
        current_theme=theme,
        endpoint="/theme/toggle",
        toggle_id="carenest-theme-toggle",
        cls=cls,
    )


# ── Page sections ─────────────────────────────────────────────────────────────
def cn_navbar(theme: str) -> Div:
    return Div(
        Div(
            Div(
                # Brand
                A(
                    Div(Icon("plus-circle"), cls="cn-brand-mark"),
                    Span(
                        Span("Care", cls="fw-800"),
                        Span("Nest", cls="text-primary"),
                        cls="fs-5 fw-bold ms-2 text-decoration-none text-body",
                    ),
                    href="/",
                    cls="d-flex align-items-center text-decoration-none",
                ),
                # Toggle button
                Button(
                    Span(cls="navbar-toggler-icon"),
                    cls="navbar-toggler border-0 shadow-none",
                    **{"data-bs-toggle": "collapse", "data-bs-target": "#cn-nav-collapse"},
                ),
                # Links
                Div(
                    A("Services", href="#specialties", cls="nav-link"),
                    A("Doctors", href="#doctors", cls="nav-link"),
                    A("Book Online", href="#book", cls="nav-link"),
                    A("Patient Info", href="#patient-info", cls="nav-link"),
                    A("Contact", href="#contact", cls="nav-link"),
                    cls="collapse navbar-collapse",
                    id="cn-nav-collapse",
                ),
                # Actions
                Div(
                    cn_theme_toggle(theme, cls="me-2"),
                    A("Sign In", href="/login", cls="btn btn-outline-secondary btn-sm me-2"),
                    A("Book Now", href="#book", cls="btn btn-primary btn-sm"),
                    cls="d-flex align-items-center ms-auto",
                ),
                cls="container d-flex align-items-center gap-3",
            ),
            cls="cn-navbar navbar",
        ),
        cls="cn-nav-wrap",
    )


def cn_hero() -> Div:
    today = date.today()

    booking_form = Div(
        Div(
            H4("Book an Appointment", cls="fw-700 mb-0 fs-5"),
            Small("Free slots available today", cls="text-success fw-600"),
            cls="d-flex align-items-center justify-content-between mb-3",
        ),
        Form(
            Div(
                Div(
                    Div("Specialty", cls="form-label fw-600 small mb-1"),
                    Select(
                        Option("Select specialty…", value="", selected=True, disabled=True),
                        *[Option(s["title"]) for s in SPECIALTIES],
                        cls="form-select",
                        name="specialty",
                        id="booking-specialty",
                    ),
                    cls="col-12 col-sm-6",
                ),
                Div(
                    Div("Preferred Date", cls="form-label fw-600 small mb-1"),
                    Input(
                        "pref_date",
                        input_type="date",
                        cls="form-control",
                        value=str(today + timedelta(days=1)),
                        min=str(today),
                        id="booking-date",
                    ),
                    cls="col-12 col-sm-6",
                ),
                Div(
                    Div("Doctor (optional)", cls="form-label fw-600 small mb-1"),
                    Select(
                        Option("Any available doctor", value=""),
                        *[Option(d["name"]) for d in DOCTORS],
                        cls="form-select",
                        name="doctor",
                        id="booking-doctor",
                    ),
                    cls="col-12",
                ),
                Div(
                    LoadingButton(
                        "Search Available Slots",
                        endpoint="/search-slots",
                        loading_text="Searching…",
                        cls="btn btn-primary w-100",
                        id="booking-search-btn",
                    ),
                    cls="col-12 mt-1",
                ),
                cls="row g-3",
            ),
            action="/book",
            method="post",
        ),
        cls="cn-booking-card p-4",
    )

    return Div(
        Div(
            Row(
                Col(
                    Div(
                        Span(
                            Icon("shield-check"),
                            " HIPAA Compliant · Fully Certified",
                            cls="cn-hero-badge",
                        ),
                        H1(
                            "Healthcare you can trust, care you'll love", cls="cn-display mt-3 mb-3"
                        ),
                        P(
                            "CareNest connects you with top specialists in your area. Same-day appointments, digital health records, and a care team that puts you first.",
                            cls="cn-subtitle mb-4",
                        ),
                        Div(
                            A("Book Appointment", href="#book", cls="btn btn-primary btn-lg me-3"),
                            A(
                                "Meet Our Doctors",
                                href="#doctors",
                                cls="btn btn-outline-secondary btn-lg",
                            ),
                            cls="d-flex flex-wrap gap-2 mb-4",
                        ),
                        Div(
                            *[
                                Span(Icon(b["icon"]), f" {b['label']}", cls="cn-trust-badge")
                                for b in [
                                    {"icon": "patch-check", "label": "Board Certified"},
                                    {"icon": "clock", "label": "Same-day Slots"},
                                    {"icon": "shield-lock", "label": "Private & Secure"},
                                ]
                            ],
                            cls="d-flex flex-wrap gap-2",
                        ),
                        cls="position-relative",
                    ),
                    md=7,
                ),
                Col(booking_form, md=5, cls="mt-4 mt-md-0"),
                cls="g-5 align-items-center",
                cols=1,
                cols_md=2,
            ),
            cls="container",
        ),
        cls="cn-hero",
    )


def cn_stats() -> Div:
    return Div(
        Div(
            Row(
                *[
                    Col(
                        Div(
                            Div(Icon(s["icon"]), cls="text-primary fs-4 mb-2"),
                            Div(s["value"], cls="fw-800 fs-2 lh-1"),
                            Div(s["label"], cls="text-muted small mt-1"),
                            cls="cn-stat-card p-4 text-center h-100",
                        ),
                        md=3,
                        sm=6,
                    )
                    for s in STATS
                ],
                cls="g-4",
                cols=2,
                cols_md=4,
            ),
            cls="container",
        ),
        cls="cn-section py-4",
        id="stats",
    )


def cn_specialties() -> Div:
    return Div(
        Div(
            Div(
                Span(Icon("grid"), " Our Specialties", cls="cn-section-label"),
                H2("Expert care across 12 specialties", cls="mt-3 mb-2 fw-800"),
                P(
                    "Our multidisciplinary team ensures you get the right specialist for your condition — fast.",
                    cls="text-muted",
                    style="max-width:40rem",
                ),
                cls="mb-5",
            ),
            Row(
                *[
                    Col(
                        A(
                            Div(Icon(s["icon"]), cls="cn-spec-icon"),
                            H5(s["title"], cls="fw-700 mb-1"),
                            P(s["desc"], cls="text-muted small mb-2 lh-base"),
                            Span(
                                Icon("people"),
                                f" {s['patients']} patients",
                                cls="small fw-600 text-primary",
                            ),
                            href="#book",
                            cls="cn-specialty-card h-100",
                        ),
                        md=4,
                        sm=6,
                        cls="mb-4",
                    )
                    for s in SPECIALTIES
                ],
                cls="g-2",
            ),
            cls="container",
        ),
        cls="cn-section cn-section-alt",
        id="specialties",
    )


def cn_doctors() -> Div:
    return Div(
        Div(
            Div(
                Span(Icon("people"), " Our Team", cls="cn-section-label"),
                H2("Meet our leading specialists", cls="mt-3 mb-2 fw-800"),
                P(
                    "Experienced, empathetic, and board-certified across all major disciplines.",
                    cls="text-muted",
                    style="max-width:36rem",
                ),
                cls="mb-5",
            ),
            Row(
                *[
                    Col(
                        Div(
                            # Top accent is the ::before pseudo element in CSS
                            Div(
                                Div(
                                    Span(
                                        d["initials"], cls=f"cn-doctor-avatar fw-bold {d['color']}"
                                    ),
                                    Div(
                                        Div(d["name"], cls="fw-700 lh-sm"),
                                        Div(d["specialty"], cls="text-muted small"),
                                        Div(
                                            Icon("star-fill", cls="text-warning"),
                                            Span(f" {d['rating']}"),
                                            Span(
                                                f" ({d['reviews']} reviews)", cls="text-muted small"
                                            ),
                                        ),
                                    ),
                                    cls="d-flex gap-3 align-items-center mb-3",
                                ),
                                Hr(cls="my-2", style="opacity:0.08"),
                                Div("Today's availability", cls="small fw-600 text-muted mb-2"),
                                Div(
                                    *[Span(slot, cls="cn-avail-slot") for slot in d["slots"]],
                                    cls="d-flex flex-wrap gap-2",
                                ),
                                A(
                                    Icon("calendar-plus"),
                                    " Book with Dr. ",
                                    d["name"].split()[-1],
                                    href="#book",
                                    cls="btn btn-outline-primary btn-sm w-100 mt-3",
                                    style="border-radius:5px",
                                ),
                                cls="p-4",
                            ),
                            cls="cn-doctor-card h-100",
                        ),
                        md=6,
                        lg=3,
                    )
                    for d in DOCTORS
                ],
                cls="g-4",
                cols=2,
                cols_md=3,
            ),
            cls="container",
        ),
        cls="cn-section",
        id="doctors",
    )


def cn_how_it_works() -> Div:
    steps = [
        (
            "1",
            "search",
            "Find your specialist",
            "Browse by specialty or symptom, filter by availability and rating.",
        ),
        (
            "2",
            "calendar-check",
            "Choose a time slot",
            "Pick a date and time that fits your schedule — same day often available.",
        ),
        (
            "3",
            "person-badge",
            "Complete your profile",
            "Provide medical history in a secure, HIPAA-compliant intake form.",
        ),
        (
            "4",
            "check-circle",
            "Attend your appointment",
            "In-clinic or video consultation with a board-certified specialist.",
        ),
    ]
    return Div(
        Div(
            Div(
                Span(Icon("lightning"), " How It Works", cls="cn-section-label"),
                H2("From search to care in under 5 minutes", cls="mt-3 mb-2 fw-800"),
                P("We removed every barrier between you and your doctor.", cls="text-muted"),
                cls="mb-5",
            ),
            Row(
                *[
                    Col(
                        Div(
                            Div(
                                Div(num, cls="cn-step-num me-3"),
                                Div(
                                    Div(title, cls="fw-700 mb-1"),
                                    Div(desc, cls="text-muted small lh-base"),
                                ),
                                cls="cn-step",
                            ),
                            cls="h-100",
                        ),
                        md=3,
                        sm=6,
                    )
                    for num, icon, title, desc in steps
                ],
                cls="g-4",
                cols=2,
                cols_sm=2,
                cols_lg=4,
            ),
            cls="container",
        ),
        cls="cn-section cn-section-alt",
        id="how-it-works",
    )


def cn_book_form() -> Div:
    """Full appointment booking form demonstrating FloatingLabel, InputGroup, Switch, Checkbox, NoticeAlert."""
    info_alert = NoticeAlert(
        "Your information is end-to-end encrypted and never shared with third parties without your consent.",
        kind="info",
        cls="mb-4",
    )

    return Div(
        Div(
            Div(
                Span(Icon("calendar-plus"), " Book Appointment", cls="cn-section-label"),
                H2("Schedule your visit", cls="mt-3 mb-2 fw-800"),
                P(
                    "Complete the form below and we'll confirm your slot within 30 minutes.",
                    cls="text-muted",
                    style="max-width:40rem",
                ),
                cls="mb-5",
            ),
            Row(
                Col(
                    Div(
                        # Status notice
                        info_alert,
                        # Form
                        Form(
                            # Error Summary demo
                            Div(id="form-errors-container"),
                            Row(
                                Col(
                                    FloatingLabel(
                                        "full_name",
                                        label="Full Name",
                                        required=True,
                                        placeholder="Your full name",
                                        id="fl-fullname",
                                    ),
                                    md=6,
                                ),
                                Col(
                                    FloatingLabel(
                                        "email",
                                        label="Email Address",
                                        input_type="email",
                                        required=True,
                                        placeholder="you@email.com",
                                        id="fl-email",
                                    ),
                                    md=6,
                                ),
                                cls="g-3 mb-3",
                            ),
                            Row(
                                Col(
                                    Div(
                                        InputGroupText(Icon("telephone"), cls=""),
                                        Input(
                                            "phone",
                                            input_type="tel",
                                            cls="form-control",
                                            placeholder="08012345678",
                                            id="phone-input",
                                        ),
                                        cls="input-group",
                                        style="border-radius:5px;overflow:hidden",
                                    ),
                                    md=6,
                                ),
                                Col(
                                    FloatingLabel(
                                        "dob",
                                        label="Date of Birth",
                                        input_type="date",
                                        required=True,
                                        id="fl-dob",
                                    ),
                                    md=6,
                                ),
                                cls="g-3 mb-3",
                            ),
                            Row(
                                Col(
                                    Div("Specialty", cls="form-label fw-600 small"),
                                    Select(
                                        Option(
                                            "Select a specialty…",
                                            value="",
                                            disabled=True,
                                            selected=True,
                                        ),
                                        *[Option(s["title"]) for s in SPECIALTIES],
                                        cls="form-select",
                                        name="specialty",
                                        id="form-specialty",
                                        required=True,
                                    ),
                                    md=6,
                                ),
                                Col(
                                    Div("Preferred Doctor", cls="form-label fw-600 small"),
                                    Select(
                                        Option("Any available", value=""),
                                        *[Option(d["name"]) for d in DOCTORS],
                                        cls="form-select",
                                        name="doctor",
                                        id="form-doctor",
                                    ),
                                    md=6,
                                ),
                                cls="g-3 mb-3",
                            ),
                            Row(
                                Col(
                                    FloatingLabel(
                                        "pref_date",
                                        label="Preferred Date",
                                        input_type="date",
                                        required=True,
                                        value=str(date.today() + timedelta(days=1)),
                                        id="fl-date",
                                    ),
                                    md=6,
                                ),
                                Col(
                                    Div("Visit Type", cls="form-label fw-600 small"),
                                    Select(
                                        Option("In-Clinic Visit"),
                                        Option("Video Consultation"),
                                        cls="form-select",
                                        name="visit_type",
                                        id="visit-type",
                                    ),
                                    md=6,
                                ),
                                cls="g-3 mb-3",
                            ),
                            Div(
                                Div("Reason for Visit / Symptoms", cls="form-label fw-600 small"),
                                Textarea(
                                    cls="form-control",
                                    name="reason",
                                    rows="3",
                                    placeholder="Briefly describe your symptoms or reason for visiting…",
                                    id="reason-textarea",
                                ),
                                cls="mb-3",
                            ),
                            Hr(cls="my-4", style="opacity:0.07"),
                            Div(
                                Div("Patient Preferences", cls="fw-700 mb-3"),
                                Switch(
                                    "sms_reminders",
                                    label="Receive SMS appointment reminders",
                                    checked=True,
                                    switch_id="sms-switch",
                                ),
                                Switch(
                                    "email_updates",
                                    label="Receive email health updates",
                                    checked=True,
                                    switch_id="email-switch",
                                ),
                                Checkbox(
                                    "terms",
                                    label="I agree to the Terms of Service and Privacy Policy",
                                    required=True,
                                    checkbox_id="terms-cb",
                                ),
                                cls="mb-4",
                            ),
                            LoadingButton(
                                "Confirm Appointment",
                                endpoint="/book/submit",
                                loading_text="Booking…",
                                cls="btn btn-primary w-100",
                                id="confirm-booking-btn",
                            ),
                            action="/book/submit",
                            method="post",
                        ),
                        cls="cn-form-card p-4 p-md-5",
                    ),
                    lg=8,
                ),
                    Col(
                        # Info sidebar
                        Div(
                            Div(Icon("info-circle"), " What to expect", cls="fw-700 mb-3"),
                            Div(
                                *[
                                    Div(
                                        Div(Icon("check-lg", cls="text-primary me-2")),
                                        Div(txt, cls="small text-muted lh-base"),
                                        cls="d-flex gap-2 mb-3",
                                    )
                                    for txt in [
                                        "Confirmation email sent within 30 minutes of booking.",
                                        "SMS reminder 24 hours and 1 hour before your appointment.",
                                        "Digital intake form sent 12 hours in advance.",
                                        "Free cancellation up to 2 hours before your visit.",
                                        "In-clinic or video option changeable up to 4 hours prior.",
                                    ]
                                ]
                            ),
                            cls="cn-form-card p-4 mb-4",
                        ),
                        Div(
                            Div(Icon("file-earmark-medical"), " Sample Records", cls="fw-700 mb-3"),
                            FilePreview(
                                src="https://via.placeholder.com/400x300?text=Lab+Results",
                                title="Lab Results (PDF)",
                                height="120px",
                            ),
                            cls="cn-form-card p-4",
                        ),
                    Div(
                        Div(Icon("telephone"), " Need help booking?", cls="fw-700 mb-2"),
                        P(
                            "Our care coordinators are available Mon–Sat, 8am–8pm.",
                            cls="small text-muted mb-3",
                        ),
                        A(
                            Icon("telephone-fill"),
                            " 0800-CARENEST",
                            href="tel:08002273637",
                            cls="btn btn-outline-primary w-100",
                            style="border-radius:5px;font-weight:600",
                        ),
                        cls="cn-form-card p-4",
                    ),
                    lg=4,
                    cls="mt-4 mt-lg-0",
                ),
                cls="g-5",
                cols=1,
                cols_md=2,
            ),
            cls="container",
        ),
        cls="cn-section",
        id="book",
    )


def cn_testimonials() -> Div:
    return Div(
        Div(
            Div(
                Span(Icon("chat-quote"), " Patient Stories", cls="cn-section-label"),
                H2("Real experiences, real outcomes", cls="mt-3 mb-2 fw-800"),
                cls="mb-5",
            ),
            Row(
                *[
                    Col(
                        Div(
                            P(f'"{t["text"]}"', cls="mb-3 lh-lg"),
                            Hr(style="opacity:0.06"),
                            Div(
                                Div(
                                    Span(
                                        t["name"][0],
                                        cls="d-inline-flex align-items-center justify-content-center rounded-2 bg-primary text-white fw-bold me-2",
                                        style="width:2rem;height:2rem;font-size:0.8rem",
                                    ),
                                    Div(
                                        Div(t["name"], cls="fw-600 small"),
                                        Div(t["role"], cls="text-muted", style="font-size:0.75rem"),
                                    ),
                                    cls="d-flex align-items-center",
                                ),
                                Div(
                                    *[Icon("star-fill", cls="text-warning") for _ in range(5)],
                                    cls="d-flex align-items-center gap-1",
                                ),
                                cls="d-flex align-items-center justify-content-between",
                            ),
                            cls="cn-testimonial p-4 h-100",
                        ),
                        md=4,
                    )
                    for t in TESTIMONIALS
                ],
                cls="g-4",
            ),
            cls="container",
        ),
        cls="cn-section cn-section-alt",
        id="patient-info",
    )


def cn_footer() -> Div:
    return Div(
        Div(
            Row(
                Col(
                    Div(
                        Div(
                            Div(Icon("plus-circle"), cls="cn-brand-mark me-2"),
                            Span(
                                Span("Care", cls="fw-800"),
                                Span("Nest", cls="text-primary"),
                                cls="fs-5 fw-bold",
                            ),
                            cls="d-flex align-items-center mb-3",
                        ),
                        P(
                            "Connecting patients with certified specialists. Premium care, delivered with compassion.",
                            cls="text-muted small lh-lg",
                            style="max-width:20rem",
                        ),
                        Div(
                            A(Icon("facebook"), href="#", cls="text-muted me-3 fs-5"),
                            A(Icon("twitter-x"), href="#", cls="text-muted me-3 fs-5"),
                            A(Icon("instagram"), href="#", cls="text-muted me-3 fs-5"),
                            A(Icon("linkedin"), href="#", cls="text-muted fs-5"),
                            cls="mt-3",
                        ),
                    ),
                    md=4,
                ),
                Col(
                    Div("Specialties", cls="fw-700 small mb-3 text-uppercase tracking-wide"),
                    Ul(
                        *[
                            Li(
                                A(
                                    s["title"],
                                    href="#specialties",
                                    cls="text-muted small text-decoration-none hover-primary",
                                ),
                                cls="mb-2",
                            )
                            for s in SPECIALTIES[:4]
                        ],
                        cls="list-unstyled",
                    ),
                    md=2,
                ),
                Col(
                    Div("Patient Services", cls="fw-700 small mb-3 text-uppercase"),
                    Ul(
                        *[
                            Li(
                                A(link, href="#", cls="text-muted small text-decoration-none"),
                                cls="mb-2",
                            )
                            for link in [
                                "Book Appointment",
                                "Patient Portal",
                                "Pre-Visit Form",
                                "Lab Results",
                                "Health Records",
                            ]
                        ],
                        cls="list-unstyled",
                    ),
                    md=2,
                ),
                Col(
                    Div("Contact", cls="fw-700 small mb-3 text-uppercase"),
                    Div(
                        Div(
                            Icon("geo-alt"),
                            " 12 Awolowo Road, Ikoyi, Lagos",
                            cls="text-muted small mb-2",
                        ),
                        Div(Icon("telephone"), " 0800-CARENEST", cls="text-muted small mb-2"),
                        Div(Icon("envelope"), " hello@carenest.ng", cls="text-muted small mb-2"),
                        Div(Icon("clock"), " Mon–Sat 8am–8pm", cls="text-muted small"),
                    ),
                    md=4,
                ),
                cls="g-5",
            ),
            Hr(cls="my-4", style="opacity:0.07"),
            Div(
                Small(
                    "© 2026 CareNest Health Technologies. All rights reserved.", cls="text-muted"
                ),
                Div(
                    A("Privacy Policy", href="#", cls="text-muted small text-decoration-none me-3"),
                    A("Terms of Use", href="#", cls="text-muted small text-decoration-none me-3"),
                    A("HIPAA Notice", href="#", cls="text-muted small text-decoration-none"),
                ),
                cls="d-flex flex-wrap align-items-center justify-content-between gap-2",
            ),
            cls="container",
        ),
        cls="cn-footer py-5",
        id="contact",
    )


# ── Confirmation modal ────────────────────────────────────────────────────────
def booking_confirm_modal() -> Any:
    return Modal(
        Div(
            Div(
                Div(Icon("check-circle-fill", cls="text-success"), style="font-size:2.5rem"),
                H4("Appointment Confirmed!", cls="fw-700 mt-3 mb-1"),
                P(
                    "We've sent your confirmation to your email. You'll receive an SMS reminder 24 hours before your visit.",
                    cls="text-muted small",
                ),
                cls="text-center mb-4",
            ),
            Hr(style="opacity:0.07"),
            Row(
                Col(
                    Span("Specialty:", cls="small text-muted"),
                    Br(),
                    Span("Cardiology", cls="fw-600"),
                    md=6,
                ),
                Col(
                    Span("Date:", cls="small text-muted"),
                    Br(),
                    Span("Tomorrow, 11:30 AM", cls="fw-600"),
                    md=6,
                ),
                cls="g-3",
            ),
        ),
        modal_id="booking-confirm-modal",
        title="Booking Summary",
        centered=True,
        footer=Div(
            Button(
                "Close",
                **{"data-bs-dismiss": "modal"},
                cls="btn btn-outline-secondary btn-sm",
                style="border-radius:5px",
            ),
            A("Add to Calendar", href="#", cls="btn btn-primary btn-sm", style="border-radius:5px"),
            cls="d-flex gap-2 justify-content-end",
        ),
    )


# ── Login page ────────────────────────────────────────────────────────────────
def login_page(errors: dict | None = None) -> Div:
    return Div(
        Style(CSS),
        Div(
            FormErrorSummary(errors) if errors else None,
            AuthLayout(
                FloatingLabel(
                    "email",
                    label="Email Address",
                    input_type="email",
                    required=True,
                    placeholder=" ",
                    id="login-email",
                ),
                FloatingLabel(
                    "password",
                    label="Password",
                    input_type="password",
                    required=True,
                    placeholder=" ",
                    id="login-password",
                ),
                Div(
                    Checkbox(
                        "remember", label="Remember me for 30 days", checkbox_id="login-remember"
                    ),
                    A(
                        "Forgot password?",
                        href="/forgot-password",
                        cls="text-primary small text-decoration-none",
                    ),
                    cls="d-flex align-items-center justify-content-between",
                ),
                LoadingButton(
                    "Sign In",
                    endpoint="/login",
                    loading_text="Signing in…",
                    cls="btn btn-primary w-100 mt-2",
                    id="login-btn",
                ),
                title="Welcome back",
                subtitle="Sign in to manage your appointments and health records",
                brand_name="CareNest",
                action="/login",
                method="post",
                footer_text="Don't have an account?",
                footer_link="/register",
                footer_link_text="Create one — it's free",
            ),
            cls="cn-app min-vh-100 d-flex align-items-center justify-content-center",
            style="background:#f0fafa",
        ),
    )


# ── App factory ───────────────────────────────────────────────────────────────
app = FastHTML()
add_bootstrap(
    app,
    theme=CARENEST_THEME,
    font_family="Inter",
)


def create_app() -> FastHTML:
    @app.post("/theme/toggle")
    def toggle_theme(req) -> Any:
        req.session[THEME_KEY] = "dark" if theme_from_req(req) == "light" else "light"
        return hx_refresh()

    @app.get("/")
    def index(req) -> Any:
        theme = theme_from_req(req)
        return (
            Style(CSS),
            Div(
                cn_navbar(theme),
                cn_hero(),
                cn_stats(),
                cn_specialties(),
                cn_doctors(),
                cn_how_it_works(),
                cn_book_form(),
                cn_testimonials(),
                cn_footer(),
                booking_confirm_modal(),
                data_bs_theme=theme,
                cls="cn-app",
            ),
        )

    @app.get("/login")
    def login_get(req) -> Any:
        theme = theme_from_req(req)
        return Div(
            Style(CSS),
            Div(
                cn_navbar(theme),
                Div(
                    AuthLayout(
                        FloatingLabel(
                            "email",
                            label="Email Address",
                            input_type="email",
                            required=True,
                            placeholder=" ",
                            id="login-email",
                        ),
                        FloatingLabel(
                            "password",
                            label="Password",
                            input_type="password",
                            required=True,
                            placeholder=" ",
                            id="login-password",
                        ),
                        Div(
                            Checkbox("remember", label="Remember me", checkbox_id="login-remember"),
                            A(
                                "Forgot password?",
                                href="#",
                                cls="text-primary small text-decoration-none",
                            ),
                            cls="d-flex align-items-center justify-content-between",
                        ),
                        LoadingButton(
                            "Sign In",
                            endpoint="/login",
                            loading_text="Signing in…",
                            cls="btn btn-primary w-100 mt-2",
                            id="login-btn",
                        ),
                        title="Welcome back",
                        subtitle="Sign in to your CareNest account",
                        brand_name="CareNest",
                        action="/login",
                        method="post",
                        footer_text="Don't have an account?",
                        footer_link="/register",
                        footer_link_text="Create one — it's free",
                    ),
                    cls="py-5",
                ),
                data_bs_theme=theme,
                cls="cn-app min-vh-100",
            ),
        )

    @app.post("/login")
    def login_post(req) -> Any:
        # Demo: show validation error summary
        errors = {
            "email": "No account found with this email address.",
            "password": "Password is incorrect.",
        }
        theme = theme_from_req(req)
        return Div(
            Style(CSS),
            Div(
                cn_navbar(theme),
                Div(
                    FormErrorSummary(
                        errors, title="Sign-in failed — please check the fields below"
                    ),
                    AuthLayout(
                        FloatingLabel(
                            "email",
                            label="Email Address",
                            input_type="email",
                            required=True,
                            placeholder=" ",
                            id="login-email-err",
                        ),
                        FloatingLabel(
                            "password",
                            label="Password",
                            input_type="password",
                            required=True,
                            placeholder=" ",
                            id="login-password-err",
                        ),
                        LoadingButton(
                            "Try Again",
                            endpoint="/login",
                            loading_text="Signing in…",
                            cls="btn btn-primary w-100 mt-2",
                            id="login-retry-btn",
                        ),
                        title="Welcome back",
                        subtitle="Sign in to your CareNest account",
                        brand_name="CareNest",
                        action="/login",
                        method="post",
                    ),
                    cls="py-5 container",
                ),
                data_bs_theme=theme,
                cls="cn-app min-vh-100",
            ),
        )

    @app.post("/book/submit")
    def book_submit(req) -> Any:
        # Return success notice + trigger modal via HTMX response header
        return NoticeAlert(
            "Your appointment request has been received! Check your email for confirmation.",
            kind="success",
        )

    return app


create_app()

if __name__ == "__main__":
    serve(port=5012)
