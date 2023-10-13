"""Create Category and Quiz table

Revision ID: 5b3611c8a8e9
Revises: 068cadf4bef7
Create Date: 2023-10-13 16:19:24.583702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b3611c8a8e9'
down_revision: Union[str, None] = '068cadf4bef7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'quizzes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('answer', sa.String(50), index=True),
        sa.Column('question', sa.String(500), index=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False)
    )
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), index=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('clues_count', sa.Integer)
    )


def downgrade() -> None:
    op.drop_table('quizzes')
    op.drop_table('categories')
