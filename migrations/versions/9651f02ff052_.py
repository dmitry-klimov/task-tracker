"""empty message

Revision ID: 9651f02ff052
Revises: 
Create Date: 2022-08-14 19:50:17.516114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9651f02ff052'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('position', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['position'], ['positions.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parent_task', sa.Integer(), nullable=True),
    sa.Column('employee', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('due_to', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['employee'], ['employees.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_task'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('employees')
    op.drop_table('positions')
    # ### end Alembic commands ###
