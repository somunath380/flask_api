import sqlite3
import pandas as pd

conn=sqlite3.connect('testdb.db')
df=pd.read_csv('bank_branches.csv')
df.to_sql('banks',conn,if_exists='replace',index=False)

curr=conn.cursor()

_sql = '''SELECT * FROM banks'''

curr.execute(_sql)

res = curr.fetchall()

print(res)