import pandas as pd
import numpy as np
import sqlite3

df=pd.read_csv('Mall_Customers.csv')

def insert():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    insert_query="INSERT INTO user VALUES(?,?,?,?,?)"
    for i in range(0,200):                              # insert data row by row
        cursor.execute(insert_query, (df.values[i,0],df.values[i,1],df.values[i,2],df.values[i,3],df.values[i,4]))
        # df.values function converts data into numpy array and then stored
    connection.commit()
    connection.close()
    print("Inserted succesfully")
# select() is used to show data from data base
def select():
    connection=sqlite3.connect('data.db') ##connection to database
    cursor=connection.cursor()             ## create cursor object
    select_query="SELECT * FROM user"
    result=cursor.execute(select_query)     ## data store into result but in generator
    result=list(result)                     ## convert Data into list
    return  result                          ## return Result