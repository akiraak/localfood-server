"""Add Spot

Revision ID: ccd743634efa
Revises: ebdae40a586b
Create Date: 2022-03-12 22:11:12.974195

"""
from alembic import op
import sqlalchemy as sa
import models


# revision identifiers, used by Alembic.
revision = 'ccd743634efa'
down_revision = 'ebdae40a586b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=32), server_default='', nullable=False),
    sa.Column('geopoint', models.spot.Geometry(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_spot_filename'), 'spot', ['filename'], unique=False)
    op.create_index(op.f('ix_spot_geopoint'), 'spot', ['geopoint'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_spot_geopoint'), table_name='spot')
    op.drop_index(op.f('ix_spot_filename'), table_name='spot')
    op.drop_table('spot')
    # ### end Alembic commands ###
