from fastapi import Depends, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from application.database import get_session
from application.schemas.quiz_schemas import QuizCreateDTO, QuestionsNumDTO

from application.services.quiz_service import try_create_quiz, try_get_prev_quiz
from application.services.question_service import get_questions

from typing import Optional

router = APIRouter()


@router.post('/quiz/', response_model=Optional[QuizCreateDTO], tags=['Quiz'])
async def post_quiz(questions_num: QuestionsNumDTO, session: AsyncSession = Depends(get_session)):
    questions_num = questions_num.questions_num

    while questions_num != 0:
        questions = await get_questions(questions_num)

        for question in questions:
            is_created = await try_create_quiz(session, question)
            if is_created:
                questions_num -= 1

    await session.commit()

    prev_added_quiz = await try_get_prev_quiz(session)

    return prev_added_quiz
