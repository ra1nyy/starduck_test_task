"""add record table

Revision ID: 8b6df6523bd0
Revises: 
Create Date: 2024-08-09 22:52:14.469086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b6df6523bd0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'records',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('bib_number', sa.String(), index=True),
        sa.Column('channel_id', sa.String()),
        sa.Column('timestamp', sa.Time()),
        sa.Column('group_number', sa.String()),
    )


def downgrade():
    op.drop_table('records')