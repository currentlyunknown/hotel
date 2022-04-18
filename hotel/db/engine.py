from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

from .models import Base

engine: Engine = None
DBSession = sessionmaker()


def init_db(database_uri: str):
    engine = create_engine(database_uri)
    Base.metadata.bind = engine
    DBSession.bind = engine
