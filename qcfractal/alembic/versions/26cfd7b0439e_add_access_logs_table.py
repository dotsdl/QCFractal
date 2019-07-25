"""Add Access logs table

Revision ID: 26cfd7b0439e
Revises: 6adeb5d3032e
Create Date: 2019-07-23 16:06:28.766128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26cfd7b0439e'
down_revision = '6adeb5d3032e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('access_log', sa.Column('access_method', sa.String(), nullable=False))
    op.add_column('access_log', sa.Column('access_type', sa.String(), nullable=False))
    op.add_column('access_log', sa.Column('city', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('country', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('country_code', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('extra_params', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('ip_lat', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('ip_long', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('postal_code', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('subdivision', sa.String(), nullable=True))
    op.add_column('access_log', sa.Column('user_agent', sa.String(), nullable=True))
    op.create_index('access_type', 'access_log', ['access_date'], unique=False)
    op.drop_index('access_log_date', table_name='access_log')
    op.drop_column('access_log', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('access_log', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('access_log_date', 'access_log', ['access_date'], unique=False)
    op.drop_index('access_type', table_name='access_log')
    op.drop_column('access_log', 'user_agent')
    op.drop_column('access_log', 'subdivision')
    op.drop_column('access_log', 'postal_code')
    op.drop_column('access_log', 'ip_long')
    op.drop_column('access_log', 'ip_lat')
    op.drop_column('access_log', 'extra_params')
    op.drop_column('access_log', 'country_code')
    op.drop_column('access_log', 'country')
    op.drop_column('access_log', 'city')
    op.drop_column('access_log', 'access_type')
    op.drop_column('access_log', 'access_method')
    # ### end Alembic commands ###
