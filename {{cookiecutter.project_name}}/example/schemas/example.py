from typing import Optional
from pydantic import BaseModel


class Example(BaseModel):
    id: str
    name: str
    comment: Optional[str]

    class Config:
        orm_mode = True
