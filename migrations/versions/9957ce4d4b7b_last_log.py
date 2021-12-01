"""last log

Revision ID: 9957ce4d4b7b
Revises: 34c8c08c2cc1
Create Date: 2021-11-30 18:55:45.968820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9957ce4d4b7b'
down_revision = '34c8c08c2cc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('event', sa.String(), nullable=True))
    op.create_index(op.f('ix_log_event'), 'log', ['event'], unique=False)
    op.drop_column('log', 'Event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('log', sa.Column('Event', sa.INTEGER(), nullable=False))
    op.drop_index(op.f('ix_log_event'), table_name='log')
    op.drop_column('log', 'event')
    # ### end Alembic commands ###
