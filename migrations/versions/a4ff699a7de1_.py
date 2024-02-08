"""empty message

Revision ID: a4ff699a7de1
Revises: cbc81c3b093c
Create Date: 2024-02-04 17:41:51.094633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4ff699a7de1'
down_revision = 'cbc81c3b093c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cognito_id', sa.String(length=36), nullable=False))
        batch_op.create_unique_constraint(None, ['cognito_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('cognito_id')

    # ### end Alembic commands ###