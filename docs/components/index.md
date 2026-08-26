# Component Index

Faststrap currently registers **159 UI components** across forms, display, feedback, navigation, layout, and patterns. Use this page as a scan-friendly map before reaching for custom HTML.

!!! tip "Discovery API"
    You can also inspect components programmatically with `list_components()`, `find_components()`, and `list_component_metadata()`. See the [Component Registry](../api/registry.md).

## Forms

| Component | Docs | Notes |
| --- | --- | --- |
| `Button` | [Button](forms/button.md) | Standard actions, links, loading states. |
| `ButtonGroup`, `ButtonToolbar` | [ButtonGroup](forms/buttongroup.md) | Grouped button controls. |
| `CalendarDatePicker` | [CalendarDatePicker](forms/calendar-date-picker.md) | Single native date picker. |
| `Checkbox`, `Radio`, `Switch`, `CloseButton` | [Checkbox & Switch](forms/checks.md) | Boolean controls and close button helper. |
| `DateRangePicker` | [DateRangePicker](forms/date-range-picker.md) | Start/end date filter. |
| `ExportButton` | [ExportButton](forms/export-button.md) | Export links and POST forms. |
| `FileInput` | [FileInput](forms/file-input.md) | File upload control. |
| `FilterBar` | [FilterBar](forms/filter-bar.md) | Dashboard/filter composition. |
| `FloatingActionButton`, `GradientButton` | [Action Buttons](forms/action-buttons.md) | Opinionated premium action buttons. |
| `FloatingLabel` | [FloatingLabel](forms/floatinglabel.md) | Bootstrap floating labels. |
| `FormBuilder` | [Form Builder](forms/form-builder.md) | Pydantic v2 form generation. |
| `FormSection` | [FormSection](forms/form-section.md) | Grouped form sections with headings and actions. |
| `FormErrorSummary`, `FormGroup`, `FormGroupFromErrors` | [FormGroup](forms/formgroup.md) | Validation and grouped field rendering. |
| `FormWizard`, `WizardStep` | [FormWizard](forms/form-wizard.md) | Multi-step form flow. |
| `InlineEditor` | [InlineEditor](forms/inline-editor.md) | HTMX-friendly inline editing. |
| `Input` | [Input](forms/input.md) | Text inputs and textareas. |
| `InputGroup`, `InputGroupText` | [InputGroup](forms/inputgroup.md) | Appended/prepended input content. |
| `LiveValidationField`, `ValidationMessage` | [Live Validation](forms/live-validation.md) | HTMX live validation helpers. |
| `MultiSelect` | [MultiSelect](forms/multi-select.md) | Native multi-select. |
| `Range` | [Checkbox & Switch](forms/checks.md) | Basic range input. |
| `RangeSlider` | [RangeSlider](forms/range-slider.md) | Single/dual range slider. |
| `SearchableSelect` | [SearchableSelect](forms/searchable-select.md) | Server-side searchable select. |
| `Select` | [Select](forms/select.md) | Native select control. |
| `ThemeToggle` | [ThemeToggle](forms/theme-toggle.md) | Dark/light theme control. |
| `ToggleGroup` | [ToggleGroup](forms/toggle-group.md) | Toggle button groups. |

## Display

| Component | Docs | Notes |
| --- | --- | --- |
| `Avatar`, `AvatarGroup` | [Avatar](display/avatar.md) | People/team identity surfaces. |
| `Badge`, `BadgeGroup` | [Badge](display/badge.md) | Labels, pills, and grouped badges. |
| `Card` | [Card](display/card.md) | Base content surface. |
| `Carousel`, `CarouselItem` | [Carousel](display/carousel.md) | Bootstrap slideshow. |
| `Chart` | [Chart](display/chart.md) | Matplotlib, Plotly, Altair, SVG/HTML wrapper. |
| `CodeBlock`, `JsonViewer`, `KeyValueList`, `RecordDetail` | [Structured Display](display/structured-display.md) | Data/dev-app primitives for code, JSON, and records. |
| `DataCard` | [DataCard](display/data-card.md) | Structured metadata card for models, datasets, and entities. |
| `DataTable` | [DataTable](display/data-table.md) | Search, sort, pagination, server-side table flows. |
| `EmptyState` | [Empty State](display/empty_state.md) | Empty data placeholders. |
| `Figure` | [Figure](display/figure.md) | Images with captions. |
| `FilePreview` | [FilePreview](display/file-preview.md) | Generic file preview shell with safe fallback. |
| `FlipCard`, `GlowCard`, `RevealCard`, `TiltCard` | [Visual Cards](display/visual-cards.md) | CSS-only premium visual cards. |
| `Icon` | [Icon](display/icon.md) | Bootstrap Icons helper. |
| `Image` | [Image](display/image.md) | Responsive image utilities. |
| `KPICard` | [KPI Card](display/kpi-card.md) | Multiple metrics in one card. |
| `MapView` | [MapView](display/map-view.md) | Optional Leaflet map. |
| `Markdown` | [Markdown](display/markdown.md) | Optional sanitized Markdown rendering. |
| `Math` | [Math](display/math.md) | KaTeX-based LaTeX math/chemistry rendering. |
| `Mermaid` | [Mermaid](display/mermaid.md) | Mermaid diagram container. |
| `MetricCard` | [Metric Card](display/metric-card.md) | Single metric with delta. |
| `ResultCard` | [Result Card](display/result-card.md) | Success/error/result feedback surface. |
| `SSETarget` | [SSETarget](display/sse-target.md) | Server-sent event target. |
| `Sheet` | [Sheet](display/sheet.md) | Mobile bottom sheet over `Drawer`. |
| `StatCard` | [Stat Card](display/stat_card.md) | Dashboard stat card. |
| `StatusBadge` | [StatusBadge](display/status-badge.md) | Status-aware badge. |
| `Stepper`, `StepperStep` | [Stepper](display/stepper.md) | Step progress UI. |
| `Svg` | [SVG](display/svg.md) | Sanitized SVG renderer. |
| `Table`, `THead`, `TBody`, `TRow`, `TCell` | [Table](display/table.md) | Static tables and aliases. |
| `TextClamp` | [TextClamp](display/text-clamp.md) | Expandable long text preview. |
| `Timeline`, `TimelineItem` | [Timeline](display/timeline.md) | Chronological events. |
| `TrendCard` | [Trend Card](display/trend-card.md) | Metric with sparkline slot. |

## Feedback

| Component | Docs | Notes |
| --- | --- | --- |
| `Alert`, `NoticeAlert` | [Alert](feedback/alert.md) | Inline feedback and notices. |
| `ConfirmAction`, `ConfirmDialog` | [Modal](feedback/modal.md) | Destructive confirmations. |
| `ErrorDialog` | [Error Dialog](feedback/error-dialog.md) | Recoverable modal errors. |
| `ErrorPage` | [Error Page](feedback/error-page.md) | Full-page error states. |
| `ErrorToast`, `InfoToast`, `NoticeToast`, `SuccessToast`, `WarningToast` | [Notification Presets](feedback/notification-presets.md) | Toast/alert presets. |
| `InstallPrompt` | [Install Prompt](feedback/install-prompt.md) | PWA install guidance. |
| `Modal` | [Modal](feedback/modal.md) | Bootstrap modal wrapper. |
| `ModernToast`, `ModernToastStack` | [ModernToast](feedback/modern-toast.md) | Opinionated polished toast surface. |
| `NotificationCenter` | [Notification Center](feedback/notification-center.md) | Dropdown notification hub. |
| `Placeholder`, `PlaceholderButton`, `PlaceholderCard` | [Placeholder](feedback/placeholder.md) | Skeleton loading placeholders. |
| `Popover`, `Tooltip` | [Tooltip & Popover](feedback/overlays.md) | Bootstrap overlays. |
| `Progress`, `ProgressBar` | [Progress](feedback/progress.md) | Progress indicators. |
| `DotsLoader`, `RingLoader`, `WaveLoader`, `PulseLoader`, `PolygonLoader`, `TypewriterLoader`, `ShadowLoader`, `ProgressRing` | [CSS Loaders](feedback/loaders.md) | Additional CSS-only loading indicators. |
| `SimpleToast`, `Toast`, `ToastContainer` | [Toast](feedback/toast.md) | Bootstrap toasts. |
| `Spinner` | [Spinner](feedback/spinner.md) | Loading spinners. |

## Navigation

| Component | Docs | Notes |
| --- | --- | --- |
| `Accordion`, `AccordionItem` | [Accordion](navigation/accordion.md) | Expand/collapse content groups. |
| `BottomNav`, `BottomNavItem` | [BottomNav](navigation/bottom-nav.md) | Mobile bottom navigation. |
| `Breadcrumb` | [Breadcrumb](navigation/breadcrumb.md) | Page hierarchy. |
| `Collapse` | [Collapse](../components/feedback/collapse.md) | Collapsible content. |
| `CommandPalette`, `CommandItem` | [CommandPalette](navigation/command-palette.md) | Command menu surface. |
| `Drawer` | [Drawer](navigation/drawer.md) | Offcanvas drawer. |
| `Dropdown`, `DropdownItem`, `DropdownDivider` | [Dropdown](navigation/dropdown.md) | Menus and split buttons. |
| `GlassNavbar`, `GlassNavItem` | [GlassNavbar](navigation/glass-navbar.md) | Glassmorphism navbar. |
| `ListGroup`, `ListGroupItem` | [ListGroup](navigation/listgroup.md) | List navigation/content. |
| `MegaMenu` | [MegaMenu](navigation/mega_menu.md) | Large dropdown navigation panel. |
| `Navbar` | [Navbar](navigation/navbar.md) | Standard Bootstrap navbar. |
| `Pagination` | [Pagination](navigation/pagination.md) | Page navigation. |
| `ProfileDropdown` | [ProfileDropdown](navigation/profile-dropdown.md) | Authenticated user menu. |
| `Scrollspy` | [Scrollspy](navigation/scrollspy.md) | Scroll-linked nav. |
| `SearchBar` | [SearchBar](navigation/search-bar.md) | Global search input with HTMX support. |
| `SidebarNavbar`, `SidebarNavItem` | [SidebarNavbar](navigation/sidebar-navbar.md) | Dashboard sidebar navigation. |
| `Tabs`, `TabPane` | [Tabs](navigation/tabs.md) | Tabbed interfaces. |

## Layout And Patterns

| Component | Docs | Notes |
| --- | --- | --- |
| `AspectRatio` | [AspectRatio](layout/aspect-ratio.md) | Ratio-constrained container. |
| `Col`, `Container`, `Row` | [Grid](layout/grid.md) | Bootstrap layout primitives. |
| `DashboardGrid` | [DashboardGrid](layout/dashboard-grid.md) | Responsive dashboard grids. |
| `Hero` | [Hero](layout/hero.md) | Landing hero sections. |
| `PageHeader` | [PageHeader](layout/page-header.md) | Page title, subtitle, status, and action row. |
| `ParallaxSection` | [ParallaxSection](layout/parallax-section.md) | CSS-only background image section. |
| `SectionHeader` | [SectionHeader](layout/section-header.md) | Section title and subtitle. |
| `Separator` | [Separator](layout/separator.md) | Semantic divider. |
| `SplitPane` | [SplitPane](layout/split_pane.md) | Resizable two-pane layout. |
| `Stack`, `Cluster`, `Center` | [Layout Primitives](layout/primitives.md) | Common flexbox compositions without custom utility strings. |
| `Switcher` | [Switcher](layout/switcher.md) | Responsive side-by-side to stacked layout. |
| `Feature`, `FeatureGrid` | [Feature Grid](patterns/feature-grid.md) | Feature sections. |
| `FooterModern` | [Footer Modern](patterns/footer-modern.md) | Marketing footer. |
| `NavbarModern` | [Navbar Modern](patterns/navbar-modern.md) | Premium navbar pattern. |
| `PricingTier`, `PricingGroup` | [Pricing](patterns/pricing.md) | SaaS pricing sections. |
| `Testimonial`, `TestimonialSection` | [Testimonial Section](patterns/testimonial-section.md) | Social proof sections. |
