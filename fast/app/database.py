from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.pool import Pool


import settings

# 以下のエラーの回避策として、pool_pre_ping=Trueをセット
#  (MySQLdb._exceptions.OperationalError) (2006, 'MySQL server has gone away')
# 参照 : https://docs.sqlalchemy.org/en/14/core/pooling.html#pool-disconnects-pessimistic
# 以下Pool関係のデフォルト値
# max_overflow=10
# pool_size=5
# pool_recycle = -1
# このエラー「Parent instance <Schedule at 0x7fdcb9572ac0> is not bound to a Session」が頻発しているので
# pool_recycle=-1に戻した
#
engine = create_engine(settings.DB_URL, echo=settings.DB_SQL_DEBUG, pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=-1)
current_sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()
# session=_sessionmaker
'''
# scoped_sessionを共有するのはやめた方が良い
session = scoped_session(current_sessionmaker)
Base.query = session.query_property()
'''
@event.listens_for(Pool, "checkout")
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except:
        raise exc.DisconnectionError()
    cursor.close()
