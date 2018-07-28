"""empty message

Revision ID: 2ad2c08664e7
Revises: 
Create Date: 2018-07-27 21:29:18.363245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad2c08664e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=10), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pre_flop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('P1C1', sa.String(length=10), nullable=False),
    sa.Column('P1C2', sa.String(length=10), nullable=False),
    sa.Column('P2C1', sa.String(length=10), nullable=False),
    sa.Column('P2C2', sa.String(length=10), nullable=False),
    sa.Column('P1_winner_rate', sa.Integer(), nullable=False),
    sa.Column('P2_winner_rate', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pre_flop')
    op.drop_table('card')
    # ### end Alembic commands ###
