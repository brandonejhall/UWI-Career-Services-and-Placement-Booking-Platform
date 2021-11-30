"""ref_number_added

Revision ID: 9e57846cc284
Revises: b0f0c5987897
Create Date: 2021-11-26 14:08:57.252764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e57846cc284'
down_revision = 'b0f0c5987897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('ref_num', sa.String(), nullable=True))
    op.create_index(op.f('ix_appointments_ref_num'), 'appointments', ['ref_num'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_appointments_ref_num'), table_name='appointments')
    op.drop_column('appointments', 'ref_num')
    # ### end Alembic commands ###