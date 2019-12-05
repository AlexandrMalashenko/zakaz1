"""users history1

Revision ID: 70543256d48a
Revises: 09cc04d1caa1
Create Date: 2019-11-25 17:07:13.180086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70543256d48a'
down_revision = '09cc04d1caa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_history_user_timestamp', table_name='history_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_history_user_timestamp', 'history_user', ['timestamp'], unique=False)
    # ### end Alembic commands ###
