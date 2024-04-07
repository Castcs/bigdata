"""empty message

Revision ID: 968dfc30dca2
Revises: 
Create Date: 2024-04-01 22:27:23.780212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '968dfc30dca2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salary_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rateType', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('pct10', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('pct25', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('median', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('pct75', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('pct90', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('stFips', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('area', sa.String(), nullable=True))
        batch_op.drop_column('StFips')
        batch_op.drop_column('Pct10')
        batch_op.drop_column('Pct25')
        batch_op.drop_column('Area')
        batch_op.drop_column('Pct75')
        batch_op.drop_column('Median')
        batch_op.drop_column('Pct90')
        batch_op.drop_column('RateType')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salary_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('RateType', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Pct90', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Median', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Pct75', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Area', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Pct25', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('Pct10', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('StFips', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('area')
        batch_op.drop_column('stFips')
        batch_op.drop_column('pct90')
        batch_op.drop_column('pct75')
        batch_op.drop_column('median')
        batch_op.drop_column('pct25')
        batch_op.drop_column('pct10')
        batch_op.drop_column('rateType')

    # ### end Alembic commands ###
