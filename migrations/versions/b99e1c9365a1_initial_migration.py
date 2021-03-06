"""Initial migration

Revision ID: b99e1c9365a1
Revises: 5d00c5c87531
Create Date: 2019-12-04 10:39:52.911530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99e1c9365a1'
down_revision = '5d00c5c87531'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'blogs', 'blogs', ['blog'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'blog')
    # ### end Alembic commands ###
