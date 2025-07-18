"""Changed type 'avg_order_complete' and 'avg_day_orders'

Revision ID: 23af65063159
Revises: 2c9627d4cbb7
Create Date: 2025-07-15 16:09:24.370469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '23af65063159'
down_revision: Union[str, None] = '2c9627d4cbb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('couriers', sa.Column('avg_order_complete_time', postgresql.INTERVAL(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('couriers', 'avg_order_complete_time')
    # ### end Alembic commands ###
