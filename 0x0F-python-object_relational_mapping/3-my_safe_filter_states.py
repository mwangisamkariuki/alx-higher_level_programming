#!/usr/bin/python3
"""
This script is safe from sql injection
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    querry = db.cursor()
    querry.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = querry.fetchall()
    for row in rows:
        print(row)
    querry.close()
    db.close()