"""users login out

Revision ID: 5d8eeee8dcaf
Revises: aa7042f2782a
Create Date: 2019-11-22 11:14:01.963758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d8eeee8dcaf'
down_revision = 'aa7042f2782a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_balance', table_name='user')
    op.create_index(op.f('ix_user_balance'), 'user', ['balance'], unique=False)
    op.drop_index('ix_user_password', table_name='user')
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.create_index('ix_user_password', 'user', ['password'], unique=True)
    op.drop_index(op.f('ix_user_balance'), table_name='user')
    op.create_index('ix_user_balance', 'user', ['balance'], unique=True)
    # ### end Alembic commands ###
