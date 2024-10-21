"""empty message

Revision ID: 6df9a5698e11
Revises: 3fea1bea38f2
Create Date: 2024-10-21 12:33:29.022088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6df9a5698e11'
down_revision: Union[str, None] = '3fea1bea38f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cuisines',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('recipes', sa.Column('cuisine', sa.String(length=30), nullable=False))
    op.create_foreign_key(None, 'recipes', 'cuisines', ['cuisine'], ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_column('recipes', 'cuisine')
    op.drop_table('cuisines')
    # ### end Alembic commands ###
