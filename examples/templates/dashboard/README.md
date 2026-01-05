# Production Dashboard Template

A complete, production-ready admin dashboard showcasing Faststrap's full capabilities.

## Features

### ✅ 6 Complete Pages
1. **Dashboard** - Overview with stats, charts, and recent orders
2. **Orders** - Full order management with filters and pagination
3. **Products** - Product catalog with stock management
4. **Customers** - Customer relationship management
5. **Analytics** - Analytics dashboard (placeholder for charts)
6. **Settings** - Account and preference management

### ✅ Fully Mobile Responsive
- **Desktop (≥992px)**: Full sidebar (260px) with labels
- **Tablet (768-991px)**: Collapsed sidebar (80px) with icons only
- **Mobile (<768px)**: Off-canvas sidebar that slides in

### ✅ Professional Features
- Collapsible sidebar navigation
- Responsive data tables
- Search and filter functionality
- Pagination
- Stat cards with trends
- Progress indicators
- Modal-ready components
- HTMX-ready for dynamic updates

### ✅ Production-Ready
- Clean, professional design
- Consistent spacing and typography
- Hover effects and transitions
- Icon-based navigation
- Badge status indicators
- Responsive grid layouts

## Quick Start

```bash
cd examples/templates/dashboard
python main.py
```

Then open http://localhost:5099

## Pages Overview

### 1. Dashboard (/)
- 4 stat cards (Revenue, Users, Orders, Conversion)
- Revenue chart placeholder
- Traffic sources with progress bars
- Recent orders table

### 2. Orders (/orders)
- Full orders table with all fields
- Status filter dropdown
- Search functionality
- Pagination
- View/Edit actions

### 3. Products (/products)
- Product catalog table
- Stock status indicators
- Category display
- Add/Edit/Delete actions

### 4. Customers (/customers)
- Customer list with contact info
- Order history
- Total spent tracking
- VIP/Active/Inactive status
- Quick actions (View, Email)

### 5. Analytics (/analytics)
- Placeholder for chart integrations
- Info alert with integration instructions
- Card-based layout for future charts

### 6. Settings (/settings)
- Profile settings form
- Theme preferences
- Language selection
- Save functionality ready

## Mobile Responsiveness

### Sidebar Behavior
```css
/* Desktop: Full sidebar */
@media (min-width: 992px) {
    sidebar: 260px width with labels
}

/* Tablet: Icon-only sidebar */
@media (max-width: 991px) {
    sidebar: 80px width, icons only
}

/* Mobile: Off-canvas sidebar */
@media (max-width: 767px) {
    sidebar: Hidden, opens as offcanvas (280px)
}
```

### Table Responsiveness
- Tables use Bootstrap's `responsive=True`
- Non-essential columns hidden on smaller screens
- Horizontal scroll on mobile when needed

### Grid Responsiveness
- Stat cards: 1 col (mobile) → 2 cols (tablet) → 4 cols (desktop)
- Content cards: Stack on mobile, side-by-side on desktop

## Customization

### Change Theme Colors

```python
dashboard_theme = create_theme(
    primary="#YOUR_COLOR",
    secondary="#YOUR_COLOR",
    success="#YOUR_COLOR",
    # ... other colors
)
```

### Add Real Data

Replace sample data arrays with database queries:

```python
# Replace this:
recent_orders = [...]

# With this:
recent_orders = db.query("SELECT * FROM orders ORDER BY date DESC LIMIT 5")
```

### Add Charts

Integrate with Matplotlib, Plotly, or Chart.js:

```python
# Example with Plotly
import plotly.graph_objects as go

def create_revenue_chart():
    fig = go.Figure(data=[go.Scatter(x=[1,2,3], y=[4,5,6])])
    return fig.to_html(include_plotlyjs='cdn')

# In your route:
chart_html = create_revenue_chart()
```

### Add HTMX Interactivity

Make tables update dynamically:

```python
Button(
    "Refresh",
    hx_get="/api/orders",
    hx_target="#orders-table",
    hx_swap="innerHTML"
)
```

## File Structure

```
dashboard/
├── main.py           # Complete multi-page dashboard
├── README.md         # This file
└── static/           # (Optional) Custom assets
```

## Components Used

- `Card` - Content containers
- `Table`, `THead`, `TBody`, `TRow`, `TCell` - Data tables
- `Badge` - Status indicators
- `Button` - Actions
- `Dropdown` - Menus and filters
- `Icon` - Visual elements
- `Progress` - Progress bars
- `Input`, `Select` - Form controls
- `Pagination` - Page navigation
- `Alert` - Notifications
- `Container`, `Row`, `Col` - Grid layout

## Next Steps

1. **Connect Database** - Replace sample data with real data
2. **Add Authentication** - Protect routes with login
3. **Implement HTMX** - Add dynamic updates
4. **Add Charts** - Integrate charting library
5. **Add Forms** - Create/Edit functionality
6. **Add Modals** - Confirmation dialogs
7. **Deploy** - Deploy to production

## Tips

- Use `set_component_defaults()` for consistent styling
- Add `hx_*` attributes for HTMX interactions
- Use Bootstrap utility classes for quick adjustments
- Keep sidebar navigation consistent across pages
- Test on real mobile devices

## Production Checklist

- [ ] Replace sample data with database
- [ ] Add authentication/authorization
- [ ] Implement CRUD operations
- [ ] Add form validation
- [ ] Add error handling
- [ ] Add loading states
- [ ] Test on mobile devices
- [ ] Optimize images
- [ ] Add analytics tracking
- [ ] Security audit

## License

MIT - Use freely in your projects!
