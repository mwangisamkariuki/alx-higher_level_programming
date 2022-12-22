#!/usr/bin/python3
"""
This script is safe from sql injection
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    querry = db.cursor()
    querry.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY \
    id ASC", (argv[4]))
    states = querry.fetchall()
    for state in states:
        print(states)
    querry.close()
    db.close()
