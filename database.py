from model import Base, Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///stores.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_place(name, country, city, street):
    """Add a store to the DB."""
    place = Place(name=name, country=country, city=city, street=street)
    session.add(place)
    session.commit()

def query_all():
	return session.query(Place).all()

def get_place(name):
    """Find the first store in the DB, by thr name."""
    return session.query(Place).filter_by(name=name).first()

def query_by_place(city):
	return session.query(Place).filter_by(city=city).all()

def remove_place(name):
    session.query(Place).filter_by(name=name).first().remove()
    session.commit()

# add_store('abcd', '05000', 'Jerusalem', 'gfds')
# add_store('1234', '12365', 'Jerusalem', 'sd')
# add_store('asdf', '05000', 'Haifa', 'ds')
# add_store('abcd', '05000', 'Haifa', 'qw')