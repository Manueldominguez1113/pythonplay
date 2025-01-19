import sqlite3
DATABASE_Path = "city.db"
conn = sqlite3.connect(DATABASE_Path)
cursor = conn.cursor()

sql = (
    '''
    CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL    
    )
    '''
)

cursor.execute(sql)