"""create models

Revision ID: e29b76565839
Revises: 
Create Date: 2024-08-19 13:48:33.436909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e29b76565839'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('str_username', sa.String(), nullable=False),
    sa.Column('qntd_seguidores', sa.String(), nullable=False),
    sa.Column('popularidade', sa.String(), nullable=False),
    sa.Column('audit_user_ip', sa.String(length=16), nullable=False),
    sa.Column('audit_created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('audit_updated_on', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('audit_user_login', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('str_display_name', sa.String(), nullable=False),
    sa.Column('str_username', sa.String(), nullable=False),
    sa.Column('str_password', sa.String(), nullable=False),
    sa.Column('str_email', sa.String(), nullable=False),
    sa.Column('audit_user_ip', sa.String(length=16), nullable=False),
    sa.Column('audit_created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('audit_updated_on', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('audit_user_login', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_user_email', 'user', ['str_email'], unique=True)
    op.create_index('idx_user_username', 'user', ['str_username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_user_username', table_name='user')
    op.drop_index('idx_user_email', table_name='user')
    op.drop_table('user')
    op.drop_table('Artists')
    # ### end Alembic commands ###
