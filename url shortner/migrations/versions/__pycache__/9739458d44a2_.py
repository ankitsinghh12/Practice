"""empty message
Revision ID: 9739458d44a2
Revises: 
Create Date: 2022-08-14 23:03:20.238848
"""
from alembic import op
import sqlalchemy as sa



revision = '9739458d44a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  
    op.create_table('urlshortener',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('shorter', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
   


def downgrade():
    
    op.drop_table('urlshortener')
    