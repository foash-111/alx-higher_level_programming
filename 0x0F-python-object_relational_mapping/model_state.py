#!/usr/bin/python3

"""
This module demonstrates the first step in using SQLAlchemy for ORM (Object-Relational Mapping).
It defines a simple SQLAlchemy model for a 'states' table and sets up the database connection.

Usage:
    python3 6-model_state.py <username> <password> <database_name>

This script creates a 'states' table in the specified MySQL database with two columns:
- 'id': An auto-incrementing integer serving as the primary key.
- 'name': A string column that cannot be null.

The script uses SQLAlchemy's declarative base system to define the 'State' model and
creates the table in the database.

Requirements:
    - Python 3.x
    - SQLAlchemy
    - MySQL server

Author: Foash
Date: 2024-04-15
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

# Parse command-line arguments for database connection
args = sys.argv

# Create a SQLAlchemy engine with connection pooling and pre-ping enabled
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(args[1], args[2], args[3]), pool_pre_ping=True)

# Define the base class for declarative model definitions
Base = declarative_base()

class State(Base):
    """
    Represents the 'states' table in the database.

    Attributes:
        id (int): An auto-incrementing integer serving as the primary key.
        name (str): A string column that cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

# Create the 'states' table in the database
Base.metadata.create_all(engine)
