"""create example table

Revision ID: d318fa28aa64
Revises: 
Create Date: 2022-05-21 22:17:40.408232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d318fa28aa64"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "examples",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("comment", sa.String, nullable=True),
    )


def downgrade():
    op.drop_table("examples")
