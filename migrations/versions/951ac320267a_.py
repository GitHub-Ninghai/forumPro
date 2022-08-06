"""empty message

Revision ID: 951ac320267a
Revises: b091feb5047c
Create Date: 2022-08-04 18:14:43.608523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '951ac320267a'
down_revision = 'b091feb5047c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###