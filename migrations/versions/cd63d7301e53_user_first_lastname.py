"""user first lastname

Revision ID: cd63d7301e53
Revises: 4a9ec06a650c
Create Date: 2020-05-09 22:54:04.704930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd63d7301e53'
down_revision = '4a9ec06a650c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_answer_optId', table_name='answer')
    op.add_column('user', sa.Column('firstName', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('lastName', sa.String(length=64), nullable=True))
    op.drop_index('ix_user_urole', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    #op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('user', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_urole', 'user', ['urole'], unique=1)
    op.drop_column('user', 'lastName')
    op.drop_column('user', 'firstName')
    op.create_index('ix_answer_optId', 'answer', ['optId'], unique=1)
    # ### end Alembic commands ###
