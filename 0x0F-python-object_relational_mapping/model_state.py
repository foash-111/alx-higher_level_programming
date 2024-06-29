#!/usr/bin/python3
""" this module connect the database with python using argv
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 1 channel


class State(Base):  # we can have more than destination.
    """ class to create the first table"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
