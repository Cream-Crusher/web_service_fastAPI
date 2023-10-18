import requests

URL_JSERVICE = 'https://jservice.io/api/random'


async def get_questions(questions_num: int):
    params = {
        'count': questions_num,
    }
    response = requests.get(URL_JSERVICE, params=params)
    response.raise_for_status()

    return response.json()
