#!/usr/bin/python3
"""
a script that lists all cities from the database
hbtn_0e_4_usa
Results must be sorted in ascending order by cities.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    querry = db.cursor()
    querry.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC;")
    states = querry.fetchall()

    for state in states:
        print(state)
