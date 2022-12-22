#!/usr/bin/python3
"""
Lists the first State objects from the database hbtn_0e_6_usa.
our script should take 3 arguments: mysql username,
mysql password and database name
must import State and Base from (model_state)
If the table states is empty, print Nothing followed by a new line
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
