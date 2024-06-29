#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)

    _Session = sessionmaker(bind=engine)
    session = _Session()

    rows = session.query(State).all()

    for row in rows:
        print(str(row.id) + ": " + row.name)



# only 1 Base, only one channel to all destinations.
# 
#                                                 class table1(Base)     
#                                                /
# 1------BASE = declarative_Base()-----> tables /-----calss table2(Base)   
#                                               \
#                                                \                      
#                                                 class table3(Base)        
#                       


# import BASE, classes Tables

#     if __name__ == "__main__"                                    
#-----------                           
#  engine   | ---------->   Base.metadata.create_all(engin) -----> Session = sessionmaker(bind=engine)
#-----------                                                            |
#                                                                       v
#                                                              seso = Session()     
#                                                               |
#                                                               v  
#                                                      rows = seso.query(Table 'class')....         
