"""added order and orderitem tables

Revision ID: 8e35694be576
Revises: fb488e2be728
Create Date: 2021-06-02 12:05:48.526629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e35694be576'
down_revision = 'fb488e2be728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user', sa.BigInteger(), nullable=True),
    sa.Column('first_name', sa.Unicode(length=20), nullable=True),
    sa.Column('last_name', sa.Unicode(length=20), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('address', sa.Unicode(length=100), nullable=True),
    sa.Column('zipcode', sa.String(length=10), nullable=True),
    sa.Column('place', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('paid_amount', sa.Numeric(), nullable=False),
    sa.Column('stripe_token', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderitem',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('order', sa.BigInteger(), nullable=True),
    sa.Column('product', sa.BigInteger(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('quantity', sa.Integer(), server_default='1', nullable=True),
    sa.ForeignKeyConstraint(['order'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('gino_admin_users')
    op.drop_table('gino_admin_history')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gino_admin_history',
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('route', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('log_message', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('object_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='gino_admin_history_pkey')
    )
    op.create_table('gino_admin_users',
    sa.Column('login', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('added_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('login', name='gino_admin_users_pkey')
    )
    op.drop_table('orderitem')
    op.drop_table('order')
    # ### end Alembic commands ###
