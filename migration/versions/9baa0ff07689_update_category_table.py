"""Update Category table

Revision ID: 9baa0ff07689
Revises: 5b3611c8a8e9
Create Date: 2023-10-13 20:41:14.252524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9baa0ff07689'
down_revision: Union[str, None] = '5b3611c8a8e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'quizzes',
        sa.Column('parsed_at', sa.DateTime, onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_column('quizzes', 'parsed_at')
