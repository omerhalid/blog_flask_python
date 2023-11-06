"""contactWhoSentEmail model

Revision ID: c6c173a0d3bf
Revises: 824a0fdc6d38
Create Date: 2023-11-06 01:33:06.354758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6c173a0d3bf'
down_revision = '824a0fdc6d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_who_send_email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('is_sent_email', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_who_send_email')
    # ### end Alembic commands ###
