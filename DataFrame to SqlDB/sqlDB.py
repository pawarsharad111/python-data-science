import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

# created table according to malll csv file
CREATE_QUERY="CREATE TABLE  IF NOT EXISTS user(ID INT, Gendre TEXT, Age INT, Income INT, Spend INT)"
cursor.execute(CREATE_QUERY)

connection.commit()
connection.close()