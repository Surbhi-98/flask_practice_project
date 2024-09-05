"""Add a column

Revision ID: bc23011d0b84
Revises: 8d05c23c6aec
Create Date: 2021-11-26 15:18:03.347168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc23011d0b84'
down_revision = '8d05c23c6aec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('Account', 'last_transaction_date')
