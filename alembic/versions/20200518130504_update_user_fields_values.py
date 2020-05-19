"""update user fields values

Revision ID: ab7fb1ae4bb
Revises: 00000000
Create Date: 2020-05-18 13:05:04.615771

"""

# revision identifiers, used by Alembic.
import sqlalchemy as sa
from alembic import op
revision = 'ab7fb1ae4bb'
down_revision = '00000000'


def upgrade():
    op.execute('''UPDATE user
                    SET point_balance=5000
                    WHERE user_id=1
    ''')

    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
                  VALUES
                        (2, 'LOCATION', 'USA')
    ''')

    op.execute('''UPDATE user
                        SET tier='Silver'
                        WHERE user_id=3
    ''')


def downgrade():
    op.execute("TRUNCATE TABLE user")
    op.execute("TRUNCATE TABLE rel_user")
