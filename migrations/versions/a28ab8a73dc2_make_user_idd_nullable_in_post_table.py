"""Make user_idd nullable in Post table

Revision ID: a28ab8a73dc2
Revises: 128e3740f095
Create Date: 2026-05-02 13:01:43.053816

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "a28ab8a73dc2"
down_revision: Union[str, Sequence[str], None] = "128e3740f095"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("posts", "user_id", existing_type=sa.INTEGER(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("posts", "user_id", existing_type=sa.INTEGER(), nullable=False)
