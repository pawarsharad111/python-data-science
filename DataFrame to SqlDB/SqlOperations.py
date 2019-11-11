from app import insert, select
import numpy
import pandas as pd
# insert function insert data from frames  to SQL user table
insert()    # this function call when you want to insert data from data frame to sql tables
arr=select()
## this function converts arr values into data frame
sqlData=pd.DataFrame(data=arr,columns="ID Gendre Age Income Spend".split())
print(sqlData)