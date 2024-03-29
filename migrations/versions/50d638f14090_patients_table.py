"""patients table

Revision ID: 50d638f14090
Revises: 4f9b456c2e8d
Create Date: 2023-08-24 19:42:53.647095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d638f14090'
down_revision = '4f9b456c2e8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dentist_id', sa.Integer(), nullable=False),
    sa.Column('initials', sa.String(length=16), nullable=True),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['dentist_id'], ['dentists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_patients_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_patients_initials'), ['initials'], unique=False)
        batch_op.create_index(batch_op.f('ix_patients_last_name'), ['last_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_patients_last_name'))
        batch_op.drop_index(batch_op.f('ix_patients_initials'))
        batch_op.drop_index(batch_op.f('ix_patients_first_name'))

    op.drop_table('patients')
    # ### end Alembic commands ###
