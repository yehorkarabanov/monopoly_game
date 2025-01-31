"""Init Database

Revision ID: 5e387f75b6d6
Revises: 
Create Date: 2025-01-31 16:50:36.607150

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e387f75b6d6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actions',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('groups',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tiles',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('tile_position', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('tile_position')
    )
    op.create_table('properties',
    sa.Column('tile_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('house_price', sa.Float(), nullable=False),
    sa.Column('base_rent', sa.Float(), nullable=False),
    sa.Column('one_house_rent', sa.Float(), nullable=False),
    sa.Column('two_houses_rent', sa.Float(), nullable=False),
    sa.Column('three_houses_rent', sa.Float(), nullable=False),
    sa.Column('four_houses_rent', sa.Float(), nullable=False),
    sa.Column('hotel_rent', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tile_id'], ['tiles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tile_id')
    )
    op.create_table('railways',
    sa.Column('tile_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('one_owned_rent', sa.Float(), nullable=False),
    sa.Column('two_owned_rent', sa.Float(), nullable=False),
    sa.Column('three_owned_rent', sa.Float(), nullable=False),
    sa.Column('four_owned_rent', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tile_id'], ['tiles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tile_id')
    )
    op.create_table('specialtiles',
    sa.Column('tile_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('action_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['action_id'], ['actions.id'], ),
    sa.ForeignKeyConstraint(['tile_id'], ['tiles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tile_id')
    )
    op.create_table('utilities',
    sa.Column('tile_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('one_company_owned_multiplier', sa.Integer(), nullable=False),
    sa.Column('two_companies_owned_multiplier', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tile_id'], ['tiles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tile_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utilities')
    op.drop_table('specialtiles')
    op.drop_table('railways')
    op.drop_table('properties')
    op.drop_table('tiles')
    op.drop_table('groups')
    op.drop_table('actions')
    # ### end Alembic commands ###
