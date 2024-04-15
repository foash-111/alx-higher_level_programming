#!/usr/bin/python3


"""first step to orm using sqlalchemy"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
import sys

args = sys.argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(args[1], args[2], args[3]), pool_pre_ping = True)

Base = declarative_base()

class State(Base):
    """As a table in mysql and contains id, name """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement = True, primary_key = True)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
