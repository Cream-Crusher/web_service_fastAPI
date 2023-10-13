from sqlalchemy import String, Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from application.database import Base


class Quiz(Base):
    __tablename__ = 'quizzes'

    id: Mapped[int] = mapped_column(primary_key=True)

    answer = Column(String(50), index=True)
    question = Column(String(500), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship('Сategory')
