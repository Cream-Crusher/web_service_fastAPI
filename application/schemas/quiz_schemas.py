from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from application.schemas.category_schemas import CategoryGetDTO


class QuizCreateDTO(BaseModel):
    id: int

    answer: str
    question: str
    created_at: datetime
    updated_at: Optional[datetime]

    category: CategoryGetDTO


class QuestionsNumDTO(BaseModel):
    questions_num: int
