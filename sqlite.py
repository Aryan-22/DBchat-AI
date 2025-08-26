import sqlite3

## connect to sqllite
connection=sqlite3.connect("HERO.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info = """
CREATE TABLE HERO_STATS(
    HERO_NAME VARCHAR(25),
    ROLE VARCHAR(25),
    DIFFICULTY VARCHAR(10),
    WIN_RATE INT
)
"""

cursor.execute(table_info)

## Insert MLBB hero records
cursor.execute('''INSERT INTO HERO_STATS VALUES('Alucard','Fighter','Easy',78)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Gusion','Assassin','Hard',85)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Layla','Marksman','Easy',65)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Tigreal','Tank','Medium',72)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Angela','Support','Medium',80)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Kagura','Mage','Hard',83)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Chou','Fighter','Hard',88)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Miya','Marksman','Easy',70)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Franco','Tank','Medium',75)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Estes','Support','Easy',82)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Harith','Mage','Hard',79)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Aldous','Fighter','Medium',77)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Ling','Assassin','Hard',90)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Moskov','Marksman','Medium',76)''')
cursor.execute('''INSERT INTO HERO_STATS VALUES('Atlas','Tank','Hard',81)''')



## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from HERO_STATS''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
