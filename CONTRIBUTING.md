# Contributing to FastStrap

Thanks for your interest! Here's how to contribute:

## Development Setup
```bash
git clone https://github.com/Evayoung/Faststrap.git
cd Faststrap
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Building a Component

1. Copy `src/faststrap/components/forms/button.py` as template
2. Place in appropriate subdirectory:
   - `forms/` - Buttons, inputs, selects
   - `display/` - Cards, badges, avatars
   - `feedback/` - Alerts, toasts, modals
   - `navigation/` - Navbars, tabs, breadcrumbs
3. Add tests in `tests/test_components/test_<component>.py`
4. Update `__init__.py` to export your component
5. Run tests: `pytest`
6. Submit PR!

## Code Style

- Use type hints everywhere
- Follow existing patterns (see `button.py`)
- Write docstrings with examples
- Run linters: `black .` and `ruff check .`
- Must include `_convert_attrs()` for HTMX support

## Questions?

Open an issue or discussion!