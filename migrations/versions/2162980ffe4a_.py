"""empty message

Revision ID: 2162980ffe4a
Revises: 366205b1362c
Create Date: 2020-09-29 00:31:25.100933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2162980ffe4a'
down_revision = '366205b1362c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'todos', 'todolist', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###
