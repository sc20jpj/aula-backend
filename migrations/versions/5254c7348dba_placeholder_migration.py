"""Placeholder migration

Revision ID: 5254c7348dba
Revises: 47e8e12ea44c
Create Date: 2024-02-14 19:19:08.078742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5254c7348dba'
down_revision = '47e8e12ea44c'
branch_labels = None
depends_on = None


def upgrade():

    op.drop_table('user_module')

    pass


def downgrade():
    pass
