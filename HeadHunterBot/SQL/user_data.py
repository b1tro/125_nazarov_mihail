import sqlite3 as sql

data_base = sql.connect('user_data.db')
cursor = data_base.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user_resume(
user_id TEXT PRIMARY KEY,
user_name TEXT,
register_time TEXT,
text TEXT,
salary TEXT,
area TEXT,
metro TEXT,
experience TEXT,
employment TEXT,
schedule TEXT)
""")
data_base.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS adapted_user_resume(
user_id TEXT PRIMARY KEY,
user_name TEXT,
register_time TEXT,
text TEXT,
salary TEXT,
area TEXT,
metro TEXT,
experience TEXT,
employment TEXT,
schedule TEXT,
vacancy_search_order TEXT,
vacancy_search_fields TEXT,
only_with_salary TEXT,
period TEXT,
page TEXT,
premium TEXT)
""")
data_base.commit()

def add_resume_to_base(resume_data : tuple):
    cursor.execute("INSERT INTO user_resume VALUES(?,?,?,?,?,?,?,?,?,?)", resume_data)
    data_base.commit()

def add_adapted_resume_to_base(adapted_resume_data : tuple):
    cursor.execute("INSERT INTO adapted_user_resume VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", adapted_resume_data)
    data_base.commit()

def is_resume_exists(user_id):
    cursor.execute("SELECT * FROM user_resume WHERE user_id = ?", (user_id,))
    if cursor.fetchone() == None:
        return False
    return True

def send_resume(user_id):
    cursor.execute("SELECT text, salary, area, metro, experience, employment, schedule, user_id FROM user_resume WHERE user_id = ?", (user_id,))
    user_resume = cursor.fetchall()
    return list(user_resume[0])

def is_adapted_resume_exists(user_id):
    cursor.execute("SELECT * FROM adapted_user_resume WHERE user_id = ?", (user_id,))
    if cursor.fetchone() == None:
        return False
    return True
def send_adapted_resume(user_id):
    cursor.execute("SELECT text, salary, area, metro, experience, employment, schedule, vacancy_search_order, vacancy_search_fields, only_with_salary, period, page, premium FROM adapted_user_resume WHERE user_id = ?",(user_id,))
    user_adapted_resume = cursor.fetchall()
    return list(user_adapted_resume[0])