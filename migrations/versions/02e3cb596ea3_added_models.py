"""Added models

Revision ID: 02e3cb596ea3
Revises: 
Create Date: 2025-02-14 23:51:19.178195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02e3cb596ea3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('couriers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('district', sa.JSON(), nullable=False),
    sa.Column('active_order', sa.JSON(), nullable=True),
    sa.Column('avg_order_complete_time', sa.Float(), nullable=True),
    sa.Column('avg_day_orders', sa.Integer(), nullable=True),
    sa.Column('register_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('district', sa.JSON(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('courier_id', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('completed_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['courier_id'], ['couriers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('couriers')
    # ### end Alembic commands ###
