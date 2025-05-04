import uuid
from typing import Optional


def generate_code(
    prefix: Optional[str] = None,
    length: Optional[int] = None,
):
    prefix = f"{prefix}-" if prefix else ""
    length = length if length else 6
    return f"{prefix}{uuid.uuid4().hex[:length].upper()}"
