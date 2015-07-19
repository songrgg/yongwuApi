from contextlib import contextmanager

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

DBSession = scoped_session(sessionmaker())
Base = declarative_base()


class JobModel(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    company = Column(String(200))


if __name__ == '__main__':
    temp_engine = create_engine(
        "mysql+pymysql://root:yongwu@mysql/?charset=utf8")
    conn = temp_engine.connect()
    conn.execute("CREATE DATABASE yongwu CHARACTER SET utf8 COLLATE utf8_bin;")
    conn.close()
    engine = create_engine(
        "mysql+pymysql://root:yongwu@mysql/yongwu?charset=utf8")
    Base.metadata.create_all(engine)
