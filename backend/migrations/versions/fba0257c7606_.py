"""empty message

Revision ID: fba0257c7606
Revises: 968dfc30dca2
Create Date: 2024-04-01 22:44:38.097876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fba0257c7606'
down_revision = '968dfc30dca2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salary_data', schema=None) as batch_op:
        batch_op.alter_column('pct10',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('pct25',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('median',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('pct75',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('pct90',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salary_data', schema=None) as batch_op:
        batch_op.alter_column('pct90',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('pct75',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('median',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('pct25',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('pct10',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###