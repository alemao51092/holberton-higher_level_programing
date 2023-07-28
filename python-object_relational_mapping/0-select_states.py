#!/usr/bin/python3
"This script lists all states from the db 'hbtn_0e_usa'"
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    fetchs = cur.fetchall()
    for x in fetchs:
        print(x)

    db.close()
