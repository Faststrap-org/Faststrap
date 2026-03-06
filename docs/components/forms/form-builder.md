# Form.from_pydantic (Beta)

`Form.from_pydantic()` generates a Bootstrap-styled form from a Pydantic model.

## Import

```python
from faststrap import Form
```

## Basic Usage

```python
from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    email: EmailStr
    age: int
    marketing_opt_in: bool = False

form = Form.from_pydantic(Signup, action="/signup")
```

## Supported Field Mapping (MVP)

- `str` -> text input
- `EmailStr` -> email input
- `int` -> number input
- `float` -> number input (`step="any"`)
- `bool` -> checkbox
- `Literal[...]` -> select
- `Enum` -> select

## Options

- `include=[...]` include only selected fields
- `exclude=[...]` remove selected fields
- `submit_label="Submit"` customize button text
- `submit_variant="primary"` customize button style
