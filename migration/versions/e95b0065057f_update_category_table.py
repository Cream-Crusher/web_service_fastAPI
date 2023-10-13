"""Update Category table

Revision ID: e95b0065057f
Revises: 9baa0ff07689
Create Date: 2023-10-13 20:50:18.205482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e95b0065057f'
down_revision: Union[str, None] = '9baa0ff07689'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('quizzes', 'parsed_at')
    op.add_column(
        'quizzes',
        sa.Column('parsed_at', sa.DateTime, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_column('quizzes', 'parsed_at')
    op.add_column(
        'quizzes',
        sa.Column('parsed_at', sa.DateTime, onupdate=sa.func.now())
    )