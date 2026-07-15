# Faststrap Deferred Work Tracker

**Created:** July 15, 2026
**Source:** Deep component audit + ModernToast analysis + gap analysis
**Purpose:** Track all work deferred beyond v0.8.1 so nothing gets lost

---

## How to Use This Document

Each item has:
- **ID:** Unique identifier for tracking
- **Tier:** 2 (next release), 3 (future), or ML/DS (milestone-gated)
- **Effort:** Low / Medium / High
- **Milestone:** Which roadmap milestone it belongs to (M1-M10)
- **Status:** Pending / In Progress / Shipped

---

## Section 1: ModernToast Rebuild (Deferred to v0.9)

The current ModernToast is a glass-styled alert, not a Sonner competitor. A full rebuild is needed to match industry standards.

### 1.1 Core Rebuild Features

| ID | Feature | Effort | Milestone | Status |
|----|---------|--------|-----------|--------|
| MT-01 | Stacked card animation (CSS `translateY` + `scale`) | Medium | v0.9 | Pending |
| MT-02 | Hover-to-expand stack behavior | Medium | v0.9 | Pending |
| MT-03 | Swipe-to-dismiss (touch events, momentum-based) | Medium | v0.9 | Pending |
| MT-04 | Pause timer on hover (`animation-play-state`) | Low | v0.9 | Pending |
| MT-05 | Action + Cancel button pair (primary + secondary) | Low | v0.9 | Pending |
| MT-06 | Loading toast state (`loading()` → `success()` transition) | Medium | v0.9 | Pending |
| MT-07 | HTMX-driven dismiss (replace inline `onclick`) | Low | v0.9 | Pending |
| MT-08 | Replace default `style="glass"` with `"soft"` | Low | v0.9 | Pending |

### 1.2 Enhancement Features

| ID | Feature | Effort | Milestone | Status |
|----|---------|--------|-----------|--------|
| MT-09 | `theme` param (light/dark/system auto-detect) | Medium | v0.9 | Pending |
| MT-10 | `richColors` mode (high-saturation variant backgrounds) | Low | v0.9 | Pending |
| MT-11 | `unstyled` mode (full CSS override) | Low | v0.9 | Pending |
| MT-12 | `visible_toasts` limit on stack (prevent overflow) | Low | v0.9 | Pending |
| MT-13 | `close_button` toggle (separate from `dismissible`) | Low | v0.9 | Pending |
| MT-14 | Per-toast position override | Medium | v0.9 | Pending |
| MT-15 | `toast.promise(async_fn, loading, success, error)` | Medium | v0.9 | Pending |
| MT-16 | `toast.custom(html_content)` escape hatch | Low | v0.9 | Pending |
| MT-17 | Expand/collapse animation on stack | Medium | v0.9 | Pending |
| MT-18 | CSS variable hooks for all toast tokens | Low | v0.9 | Pending |

### 1.3 Reference Implementations

- **Sonner** (Vercel/Next.js): https://github.com/emilkowalski/sonner
- **react-hot-toast**: https://github.com/timolins/react-hot-toast

Key patterns to replicate:
- `translateY` + `scale(0.95)` for stacked depth
- `transition: transform 0.3s ease, opacity 0.3s ease` for smooth animations
- Touch event handling for swipe-to-dismiss with velocity detection
- `animation-play-state: paused` on `:hover` for timer pause

---

## Section 2: Native Toast Fixes (Deferred to v0.9)

| ID | Fix | Effort | Milestone | Status |
|----|-----|--------|-----------|--------|
| T-01 | SimpleToast stacking logic (multiple toasts at same position) | Medium | v0.9 | Pending |
| T-02 | Toast HTMX integration (server-triggered toasts via route handlers) | Medium | v0.9 | Pending |
| T-03 | Toast programmatic API (`toast("Saved!", variant="success")` from Python) | Medium | v0.9 | Pending |
| T-04 | SimpleToast `max-width` as CSS variable instead of hardcoded | Low | v0.9 | Pending |

---

## Section 3: New Native Components (Tier 2 — v0.9)

### 3.1 Display Components

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| NC-01 | Skeleton / SkeletonText / SkeletonCircle / SkeletonCard | Medium | v0.9 | Pending |
| NC-02 | CountUp / AnimatedNumber (CSS `@property` animation) | Low | v0.9 | Pending |
| NC-03 | Rating / StarRating (CSS-only, radio + labels) | Low | v0.9 | Pending |
| NC-04 | SyntaxHighlight (Prism/Highlight.js theme wrapper) | Low | v0.9 | Pending |
| NC-05 | ColorSwatch (color display + copy-to-clipboard) | Low | v0.9 | Pending |

### 3.2 Form Components

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| NC-06 | ColorPicker (`<input type="color">` styled) | Low | v0.9 | Pending |
| NC-07 | TimePicker (`<input type="time">` styled) | Low | v0.9 | Pending |
| NC-08 | PhoneNumber (country code + validation) | Medium | v0.9 | Pending |
| NC-09 | TagsInput (type + Enter to add, HTMX-removable) | Medium | v0.9 | Pending |
| NC-10 | SignaturePad (canvas-based, JS required) | High | v0.9+ | Pending |

### 3.3 Feedback Components

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| NC-11 | Confetti (CSS-only success animation) | Low | v0.9 | Pending |
| NC-12 | InlineAlert / Banner (content-flow alert) | Low | v0.9 | Pending |

### 3.4 Navigation Components

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| NC-13 | AnchorNav (fixed sidebar with scroll tracking) | Medium | v0.9 | Pending |
| NC-14 | TreeView (hierarchical file/folder nav) | Medium | v0.9+ | Pending |

### 3.5 Layout Components

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| NC-15 | ScrollArea (custom scrollbar styling) | Low | v0.9 | Pending |

---

## Section 4: JS-Required Components (Tier 3 — v0.9+)

### 4.1 `faststrap[htmx]` Bundle

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| JS-01 | InfiniteList (generalized infinite scroll) | Medium | v0.9+ | Pending |
| JS-02 | SortableList (drag-to-reorder, SortableJS) | High | v0.9+ | Pending |
| JS-03 | FileUpload (drag-drop, preview, progress, chunked) | High | v0.9+ | Pending |
| JS-04 | ImageCrop (client-side cropping) | High | v0.9+ | Pending |
| JS-05 | RichTextEditor (Quill/TinyMCE integration) | High | v1.0 | Pending |
| JS-06 | CodeEditor (Monaco/CodeMirror integration) | High | v1.0 | Pending |
| JS-07 | Spreadsheet (editable grid, Luckysheet) | High | v1.0 | Pending |
| JS-08 | ChatBox (SSE real-time chat) | High | v0.9+ | Pending |
| JS-09 | KanbanBoard (drag-drop columns) | High | v0.9+ | Pending |

### 4.2 `faststrap[charts]` Bundle

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| CH-01 | Sparkline (tiny inline charts, CSS/SVG) | Low | v0.9 | Pending |
| CH-02 | DonutChart (SVG ring, CSS `conic-gradient`) | Low | v0.9 | Pending |
| CH-03 | GaugeChart (semi-circle gauge, SVG + CSS) | Low | v0.9 | Pending |
| CH-04 | FunnelChart (marketing funnel, CSS-only) | Low | v0.9+ | Pending |
| CH-05 | HeatmapCalendar (GitHub-style, CSS Grid) | Low | v0.9 | Pending |
| CH-06 | SankeyDiagram (D3 integration) | High | v1.0 | Pending |
| CH-07 | Treemap (D3 integration) | High | v1.0 | Pending |
| CH-08 | NetworkGraph (D3/Cytoscape integration) | High | v1.0 | Pending |

### 4.3 `faststrap[mobile]` Bundle

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| MO-01 | BottomSheet (mobile-native slide-up) | Medium | v0.9+ | Pending |
| MO-02 | PullToRefresh (touch gesture) | Medium | v0.9+ | Pending |
| MO-03 | SwipeableCard (Tinder-style swipe) | Medium | v0.9+ | Pending |
| MO-04 | HapticButton (`navigator.vibrate()`) | Low | v0.9+ | Pending |
| MO-05 | SafeArea (`env(safe-area-inset-*)` wrapper) | Low | v0.9+ | Pending |
| MO-06 | TouchRipple (Material Design feedback, CSS-only) | Low | v0.9+ | Pending |

---

## Section 5: ML/DS Components (Milestone-Gated)

These are the flagship differentiators. Specs are written in `docs/components/display/`.

### 5.1 Wave 1: Data Visualization (M3)

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| ML-01 | DistributionPlot (histogram + KDE, pandas) | Medium | M3 | Pending |
| ML-02 | CorrelationMatrix (heatmap, DataFrame) | Medium | M3 | Pending |
| ML-03 | LiveChart (SSE-powered, Chart.js) | High | M3 | Pending |
| ML-04 | LiveMetric (SSE metric card with trend) | Medium | M3 | Pending |

### 5.2 Wave 2: ML Model Evaluation (M4)

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| ML-05 | ConfusionMatrix (sklearn-compatible) | Medium | M4 | Pending |
| ML-06 | ROCCurve (ROC + AUC, multi-class) | Medium | M4 | Pending |
| ML-07 | FeatureImportance (bar chart, sklearn/SHAP) | Medium | M4 | Pending |
| ML-08 | ModelMetrics (composed evaluation dashboard) | High | M4 | Pending |

### 5.3 Wave 3: Real-time & Geospatial (M5)

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| ML-09 | TimeSeriesPlot (line + moving average) | Medium | M5 | Pending |
| ML-10 | GeoMap (iframe embed + coordinates) | Medium | M5 | Pending |

---

## Section 6: Layout & Navigation Primitives (M6)

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| LN-01 | SplitPane (resizable two-pane layout) | High | M6 | Pending |
| LN-02 | MegaMenu (premium expanded navigation) | High | M6 | Pending |
| LN-03 | Switcher (responsive adaptive panels) | Medium | M6 | Pending |

---

## Section 7: Data Bridges (M7)

| ID | Component | Effort | Milestone | Status |
|----|-----------|--------|-----------|--------|
| DB-01 | DataTable.from_query() with SQLAlchemy | High | M7 | Pending |
| DB-02 | Form.from_pydantic() (auto-generate from Pydantic) | Medium | M7 | Pending |

---

## Section 8: Technical Debt (Ongoing)

| ID | Item | Effort | Milestone | Status |
|----|------|--------|-----------|--------|
| TD-01 | Extract INIT_SCRIPT to separate `faststrap-init.js` file | Medium | v0.9 | Pending |
| TD-02 | Clean up `components/advance/` orphaned directory | Low | v0.8.1 | Pending |
| TD-03 | Clean up `components/patterns.py` flat file vs package | Low | v0.8.1 | Pending |
| TD-04 | Component defaults serialization (`.faststrap.toml`) | Medium | v0.9+ | Pending |
| TD-05 | Migration guide for v0.5→v0.8 upgrades | Medium | v0.9 | Pending |

---

## Section 9: Documentation Gaps (Ongoing)

| ID | Gap | Effort | Milestone | Status |
|----|-----|--------|-----------|--------|
| DOC-01 | ROADMAP_EXPANDED.md full rewrite to v0.8.0 reality | High | v0.8.1 | Pending |
| DOC-02 | Interactive component playground / live docs | High | M10 | Pending |
| DOC-03 | Video tutorials | High | M10 | Pending |
| DOC-04 | Real-time dashboard cookbook (SSE + HTMX tutorial) | Medium | M5 | Pending |
| DOC-05 | Extension registry documentation | Medium | M8 | Pending |

---

## Section 10: Roadmap Milestones (from ROADMAP.md)

| Milestone | Name | Key Deliverables | Gate |
|-----------|------|------------------|------|
| M1 | v0.8.1 Ship | Form alias fix, SimpleToast fixes, 5 new components, doc fixes | pytest 860+, black, ruff, mypy |
| M2 | Documentation Overhaul | All stale docs corrected, specs written | No stale data in any doc |
| M3 | ML/DS Visualization Wave | LiveChart, LiveMetric, DistributionPlot, CorrelationMatrix | 4 components, 40+ tests each |
| M4 | ML Model Evaluation | ConfusionMatrix, ROCCurve, FeatureImportance, ModelMetrics | sklearn/SHAP compatible |
| M5 | Real-time Data Layer | TimeSeriesPlot, GeoMap, SSE cookbook | Complete tutorial |
| M6 | Layout Expansion | SplitPane, MegaMenu, Switcher | Mobile responsive verified |
| M7 | ORM Bridge | DataTable.from_query() with SQLAlchemy | SQLite + PostgreSQL |
| M8 | CLI Scaffolding | faststrap init --template= | 5 templates |
| M9 | Accessibility Compliance | ARIA validation, contrast checker | WCAG report in doctor CLI |
| M10 | v1.0 | 200+ components, 95%+ coverage, playground | All quality gates pass |

---

## Summary Statistics

| Category | Count |
|----------|-------|
| ModernToast rebuild features | 18 |
| Native toast fixes | 4 |
| New native components (Tier 2) | 15 |
| JS-required components (Tier 3) | 23 |
| ML/DS components | 10 |
| Layout/navigation primitives | 3 |
| Data bridges | 2 |
| Technical debt items | 5 |
| Documentation gaps | 5 |
| **Total deferred items** | **85** |

---

*This tracker is the canonical reference for all work deferred beyond v0.8.1. Update status as items move through the pipeline. Cross-reference with `audits/faststrap_component_audit_2026-07-15.md` for detailed descriptions and rationale.*
