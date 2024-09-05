"""create account table

Revision ID: 8d05c23c6aec
Revises:
Create Date: 2021-11-25 20:48:34.237984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d05c23c6aec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Account',
        sa.Column('Id', sa.Integer, primary_ley = True),
        sa.Column('Name', sa.String(50), nullable = False),
        sa.Column('Description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('Account')
