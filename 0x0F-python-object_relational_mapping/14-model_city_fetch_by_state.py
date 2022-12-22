#!/usr/bin/python3
"""
A script that prints all city objects from the db

"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State, City).filter(State.id == City.state_id).all()

    for city, state in session.query(City, State) \
                            .filter(City.state_id == State.id) \
                            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
