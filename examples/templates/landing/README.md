# Landing Page Template

A modern, conversion-optimized landing page template for SaaS products.

## Features

- ✅ **Hero Section** - Eye-catching hero with code preview
- ✅ **Features Grid** - 6 feature cards with icons
- ✅ **Pricing Cards** - Flexible pricing tiers
- ✅ **Statistics** - Social proof with key metrics
- ✅ **CTA Section** - Strong call-to-action
- ✅ **Footer** - Multi-column footer with links
- ✅ **Responsive Design** - Mobile-first approach
- ✅ **SEO Optimized** - Proper meta tags and semantic HTML

## Quick Start

```bash
# From the Faststrap root directory
cd examples/templates/landing
python main.py
```

Then open http://localhost:5001 in your browser.

## Components Used

- `Card` - For feature and pricing cards
- `Button` - For CTAs
- `Badge` - For "New" indicator
- `Icon` - For visual elements
- `Container`, `Row`, `Col` - For responsive layout

## Customization

### Change Theme

Edit the `landing_theme` in `main.py`:

```python
landing_theme = create_theme(
    primary="#YOUR_BRAND_COLOR",
    secondary="#YOUR_SECONDARY_COLOR",
)
```

### Update Content

All content is in the component functions:
- `Hero()` - Main headline and CTA
- `Features()` - Feature cards
- `Pricing()` - Pricing tiers
- `Stats()` - Statistics
- `CTA()` - Call-to-action
- `Footer()` - Footer links

### Add Sections

Create new section functions:

```python
def Testimonials():
    return Div(
        Container(
            # ... your testimonial content
        ),
        cls="py-5"
    )

# Add to main route:
@rt("/")
def get():
    return Html(
        Body(
            Hero(),
            Features(),
            Testimonials(),  # New section
            Pricing(),
            # ...
        )
    )
```

## Best Practices

1. **Above the Fold** - Keep hero section concise and compelling
2. **Social Proof** - Add testimonials, logos, or statistics
3. **Clear CTA** - Make primary action obvious
4. **Mobile First** - Test on mobile devices
5. **Fast Loading** - Optimize images and assets
6. **SEO** - Update meta tags with your content

## Conversion Tips

- Use action-oriented button text ("Get Started" vs "Learn More")
- Add urgency ("Limited time", "Join 1000+ developers")
- Show benefits, not features ("Save 10 hours/week" vs "Fast rendering")
- Include trust signals (testimonials, logos, stats)
- Make pricing transparent
- Reduce friction (no credit card, free tier)

## Deploy

This template works great on:
- **Railway** - `railway up`
- **Vercel** - Add `vercel.json` config
- **Fly.io** - Add `fly.toml` config
- **DigitalOcean App Platform**
- **Heroku**

## License

MIT - Use freely in your projects!
