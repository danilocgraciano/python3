"""Add Unique Constraint on Game.name

Revision ID: de2188c9c111
Revises: 
Create Date: 2019-02-08 13:35:04.688956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de2188c9c111'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'games', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'games', type_='unique')
    # ### end Alembic commands ###
