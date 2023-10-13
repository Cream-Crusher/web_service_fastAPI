from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select
from sqlalchemy.orm import selectinload

from application.models.quiz_model import Quiz
from application.services.category_service import get_or_create_category

URL_JSERVICE = 'https://jservice.io/api/random'
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


async def create_quiz(session: AsyncSession, question: dict) -> True | False:

    if await session.get(Quiz, question['id']) is not None:
        return False

    category = await get_or_create_category(session, question['category'])

    quiz = Quiz(
        id=question['id'],
        answer=question['answer'],
        question=question['question'],
        created_at=datetime.strptime(question['created_at'], DATE_FORMAT),
        updated_at=datetime.strptime(question['updated_at'], DATE_FORMAT),
        category_id=category.id,
    )

    session.add(quiz)

    return True


async def get_quiz(session: AsyncSession) -> Quiz:
    result = await session.execute(
        select(Quiz).options(selectinload(Quiz.category)).order_by(desc(Quiz.parsed_at))
    )
    quiz_list = result.scalars().all()
    quiz = quiz_list[1] if len(quiz_list) > 1 else None

    return quiz
