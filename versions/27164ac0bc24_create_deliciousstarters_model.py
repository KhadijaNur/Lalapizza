"""Create DeliciousStarters model

Revision ID: 27164ac0bc24
Revises: fe2a315530cf
Create Date: 2024-01-20 10:58:56.783379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27164ac0bc24'
down_revision = 'fe2a315530cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delicious_starters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delicious_starters')
    # ### end Alembic commands ###
