"""updated user class to match cognito

Revision ID: bf8621d7cb05
Revises: f4f955067bbd
Create Date: 2024-02-04 17:53:31.167304

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf8621d7cb05'
down_revision = 'f4f955067bbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_module', schema=None) as batch_op:
        batch_op.add_column(sa.Column('module_id', sa.String(length=16), nullable=False))
        batch_op.drop_constraint('user_module_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'module', ['module_id'], ['id'])
        batch_op.drop_column('class_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_module', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_id', mysql.VARCHAR(length=16), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_module_ibfk_2', 'module', ['class_id'], ['id'])
        batch_op.drop_column('module_id')

    # ### end Alembic commands ###
