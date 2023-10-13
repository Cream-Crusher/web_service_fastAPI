from sqlalchemy.ext.asyncio import AsyncSession
from application.models.category_model import Category

from datetime import datetime

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


async def get_or_create_category(session: AsyncSession, category):
    result = await session.get(Category, category['id'])

    if result is None:
        result = Category(
            id=category['id'],
            title=category['title'],
            created_at=datetime.strptime(category['created_at'], DATE_FORMAT),
            updated_at=datetime.strptime(category['updated_at'], DATE_FORMAT),
            clues_count=category['clues_count']
        )
        session.add(result)
        await session.commit()

    return result
