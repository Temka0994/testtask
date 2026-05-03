"""Update columns in tables

Revision ID: 128e3740f095
Revises: c9191d224492
Create Date: 2026-05-01 16:54:52.360412

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "128e3740f095"
down_revision: Union[str, Sequence[str], None] = "c9191d224492"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "posts", "tags", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.alter_column(
        "users", "maiden_name", existing_type=sa.VARCHAR(length=50), nullable=True
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "users", "maiden_name", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "posts", "tags", existing_type=sa.VARCHAR(length=200), nullable=False
    )
