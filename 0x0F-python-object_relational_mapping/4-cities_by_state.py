#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    querry = db.cursor()
    querry.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = querry.fetchall()

    for state in states:
        print(state)
