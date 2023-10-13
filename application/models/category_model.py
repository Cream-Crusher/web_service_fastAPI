from sqlalchemy import String, Column, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from application.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)

    title = Column(String(50), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    clues_count = Column(Integer)
