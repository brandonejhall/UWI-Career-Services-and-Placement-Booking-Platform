"""Log_table 

Revision ID: 621fe72841f8
Revises: fe712a1f24ca
Create Date: 2021-11-30 19:01:28.213157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '621fe72841f8'
down_revision = 'fe712a1f24ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logged', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_log_storage_logged'), 'log_storage', ['logged'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_log_storage_logged'), table_name='log_storage')
    op.drop_table('log_storage')
    # ### end Alembic commands ###
