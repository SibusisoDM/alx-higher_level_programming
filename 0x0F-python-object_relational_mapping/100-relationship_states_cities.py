#!/usr/bin/python3
"""This script adds the State "California" with the City "San Francisco" to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password db_name".format(sys.argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ca = State(name="California")
    sf = City(name="San Francisco")
    ca.cities.append(sf)

    session.add(ca)
    session.add(sf)
    session.commit()

    session.close()
