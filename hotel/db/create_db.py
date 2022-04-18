from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from .models import Base
from .sample_data import customers, rooms


def create_db(database_uri: str):
    engine = create_engine(database_uri)
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Insert a few customers into the customers table
        session.add_all(customers)

        # Insert a few rooms into the rooms table
        session.add_all(rooms)
        session.commit()
