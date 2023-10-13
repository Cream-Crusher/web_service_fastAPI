from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CategoryGetDTO(BaseModel):
    id: int

    title: str
    created_at: datetime
    updated_at: Optional[datetime]
    clues_count: int
