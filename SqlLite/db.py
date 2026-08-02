# SQLite is a lightweight, serverless, and self-contained relational database 
# engine that runs inside your application rather than as a separate background process

import sqlite3
from fastapi import FastAPI

app=FastAPI()

#db open
conn=sqlite3.connect("test.db",check_same_thread=False)

#sql running
cursor=conn.cursor()

#Query running
cursor.execute("""
create table if not exists todos(
    id  INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
    )

""")

#chanes commit
conn.commit()

@app.get("/home")
def getHome():
    return {
        "message":"SQLite Connected"
    }