"""empty message

Revision ID: eec960ad5259
Revises: 43a4d91b576c
Create Date: 2022-08-15 03:52:01.351619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eec960ad5259'
down_revision = '43a4d91b576c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('employees_position_fkey', 'employees', type_='foreignkey')
    op.create_foreign_key(None, 'employees', 'positions', ['position'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.drop_constraint('tasks_employee_fkey', 'tasks', type_='foreignkey')
    op.drop_constraint('tasks_parent_task_fkey', 'tasks', type_='foreignkey')
    op.create_foreign_key(None, 'tasks', 'employees', ['employee'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.create_foreign_key(None, 'tasks', 'tasks', ['parent_task'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.create_foreign_key('tasks_parent_task_fkey', 'tasks', 'tasks', ['parent_task'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('tasks_employee_fkey', 'tasks', 'employees', ['employee'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.create_foreign_key('employees_position_fkey', 'employees', 'positions', ['position'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###
