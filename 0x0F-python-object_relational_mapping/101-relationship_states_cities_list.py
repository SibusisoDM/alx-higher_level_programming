#!/usr/bin/env python3
"""Lists all State objects, and corresponding City objects, from the database
hbtn_0e_101_usa, sorted by states.id and cities.id"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State, City).join(City).order_by(State.id, City.id).all()

    for state, city in states_cities:
        print("{}: {} -> {}".format(state.id, state.name, city.id, city.name))
