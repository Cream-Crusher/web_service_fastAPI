import requests

from application.services.quiz_service import URL_JSERVICE


async def get_questions(questions_num: int):
    params = {
        'count': questions_num,
    }
    response = requests.get(URL_JSERVICE, params=params)
    response.raise_for_status()

    return response.json()
