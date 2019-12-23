
import sqlite3

m269_database="./m269_database.db"

def query(q):
    """Applies an sql query to the M269 database"""

    connection=sqlite3.connect(m269_database)

    cursor=connection.cursor()
    cursor.execute(q)

    u=cursor.fetchall()

    cursor.close()

    return u

def show(q):
    """Applies an sql query to the M269 database and prints the result"""

    connection=sqlite3.connect(m269_database)

    cursor=connection.cursor()
    cursor.execute(q)

    columnNames=[n[0] for n in cursor.description]
    rows=cursor.fetchall()

    numberOfColumns=len(columnNames)

    cursor.close()

    # For each column, get the width of the widest element (including
    # the header)

    columnWidths=[]
    for cn in range(numberOfColumns):
        if rows==[]:
            columnWidths.append(len(columnNames[cn])+2)
        else:
            maxWidth=max(len(columnNames[cn]), 
                         max([len(str(cw[cn])) for cw in rows])) 
            columnWidths.append(maxWidth+2)

    # Now print the columns
    print

    # Headers
    print('|'.join([(' '+columnNames[i]).ljust(columnWidths[i]) 
                        for i in range(numberOfColumns)]))
    # Separators
    print('|'.join(['-'*columnWidths[i] for i in range(numberOfColumns)]))
    # rows
    for row in rows:
        print('|'.join([(' '+str(row[i])).ljust(columnWidths[i]) 
                        for i in range(numberOfColumns)]))

    print

