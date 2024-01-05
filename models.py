
from typing import Optional
from pydantic import BaseModel

class EmailSchema(BaseModel):
    email_to: str
    cc: Optional[str] = ""
    bcc: Optional[str] = ""
    subject: str
    template: str
    template_data: dict
