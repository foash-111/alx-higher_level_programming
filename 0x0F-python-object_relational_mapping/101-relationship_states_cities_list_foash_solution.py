#!/usr/bin/python3

"""
import class State and city and do quering with join on them
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    _Session = sessionmaker(bind=engine)
    session = _Session()

    joined_rows = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    state_list = []
    for row in joined_rows:
        current_state = "{}: {}".format(row.State.id, row.State.name)
        if current_state not in state_list:
            state_list.append(current_state)
            print(current_state)

        print("     {}: {}".format(row.City.id, row.City.name))

    session.close()
