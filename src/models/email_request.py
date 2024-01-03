from typing import Optional
from pydantic import BaseModel


class EmailRequest(BaseModel):
    # All attributes
    name: str
    email: str
    subject: str
    message: str
    bytes: Optional[str] = None
