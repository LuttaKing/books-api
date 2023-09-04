"""added username

Revision ID: aa812ac1ec69
Revises: 5857139642e2
Create Date: 2023-09-04 17:25:48.082307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa812ac1ec69'
down_revision: Union[str, None] = '5857139642e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
