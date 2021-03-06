"""log table

Revision ID: 6f4b8d5378ec
Revises: c6a2c8c9b1d4
Create Date: 2021-11-30 18:18:44.937900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4b8d5378ec'
down_revision = 'c6a2c8c9b1d4'
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
