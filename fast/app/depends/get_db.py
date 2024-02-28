from collections.abc import Generator
from sqlalchemy.orm import scoped_session

from database import current_sessionmaker


def get_db() -> Generator:
    db = scoped_session(current_sessionmaker)()
    try:
        yield db
    finally:
        db.close()

'''
# withを使った例
def get_db():
    with scoped_session(current_sessionmaker) as db:
        yield db
'''
