#!/usr/bin/python3

"""
import class State and city and do quering with join on them
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    # get all states with related city (power of relationship)
    data = session.query(State).order_by(State.id).all()
    for state in data:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    # ends my connection
    session.close()
