"""empty message

Revision ID: 65d1d959d95f
Revises: e217fdc63142
Create Date: 2020-06-21 06:41:05.167368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d1d959d95f'
down_revision = 'e217fdc63142'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'firstname',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('user', 'lastname',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'lastname',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('user', 'firstname',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###
