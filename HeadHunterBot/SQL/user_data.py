import sqlite3 as sql

data_base = sql.connect('user_data.db')
cursor = data_base.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
user_id TEXT PRIMARY KEY,
text TEXT,
salary TEXT,
area TEXT,
metro TEXT,
experience TEXT,
employment TEXT,
schedule TEXT)
""")
data_base.commit()

def add_resume_to_base(resume_data : tuple):
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (resume_data[0],))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?)", resume_data)
        data_base.commit()