import sqlite3
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

cursor.execute("""CREATE TABLE IF NOT EXISTS user_saved_vacancies(
user_id TEXT,
information TEXT PRIMARY KEY)
""")
data_base.commit()

# cursor.execute("DROP TABLE user_saved_vacancies")
# data_base.commit()

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

def is_adapted_resume_exists(user_id):
    cursor.execute("SELECT * FROM adapted_user_resume WHERE user_id = ?", (user_id,))
    if cursor.fetchone() == None:
        return False
    return True

def send_resume(user_id):
    cursor.execute("SELECT text, salary, area, metro, experience, employment, schedule, user_id FROM user_resume WHERE user_id = ?", (user_id,))
    user_resume = cursor.fetchall()
    return list(user_resume[0])

def send_resume_to_update(user_id):
    cursor.execute("SELECT text, salary, area, metro, experience, employment, schedule FROM user_resume WHERE user_id = ?", (user_id,))
    user_resume = cursor.fetchall()
    return list(user_resume[0])

def send_adapted_resume(user_id):
    cursor.execute("SELECT text, salary, area, metro, experience, employment, schedule, vacancy_search_order, vacancy_search_fields, only_with_salary, period, page, premium FROM adapted_user_resume WHERE user_id = ?",(user_id,))
    user_adapted_resume = cursor.fetchall()
    return list(user_adapted_resume[0])

def update_resume(user_id, parametr, value):
    cursor.execute(f"UPDATE user_resume SET {parametr} = ? WHERE user_id = {user_id}", (value,))
    data_base.commit()

def update_adapted_resume(adapted_resume, user_id):
    cursor.execute(f"UPDATE adapted_user_resume SET (text, salary, area, metro, experience, employment, schedule) = (?,?,?,?,?,?,?) WHERE user_id ={user_id}", adapted_resume)
    data_base.commit()

def delete_resume(user_id):
    cursor.execute(f"DELETE FROM user_resume WHERE user_id={user_id}")
    cursor.execute(f"DELETE FROM adapted_user_resume WHERE user_id={user_id}")
    data_base.commit()

def save_vacancy(vacancy_information : list):
    try:
        cursor.execute('INSERT INTO user_saved_vacancies (user_id,information) VALUES(?,?) ' , tuple(vacancy_information))
        data_base.commit()
    except sqlite3.IntegrityError:
        pass

class get_saved_vacancy():
    number = 0
    def get_saved_vacancies(user_id, number):
        cursor.execute('SELECT information FROM user_saved_vacancies WHERE user_id=?', (user_id,))
        saved_vacancies = cursor.fetchall()
        try:
            check = saved_vacancies[0]
        except (IndexError, TypeError, AttributeError) as errors:
            return "Вы еще не сохранили ни одной вакансии!"
        try:
            current_vacancy = list(saved_vacancies[number])
            return current_vacancy[0]
        except IndexError:
            get_saved_vacancy.number = -1
            return False

    def get_number(self):
        self.number+=1
        return self.number

    def get_current_number(self):
        return self.number

def delete_saved_vanancy(user_id, info):
    cursor.execute('DELETE FROM user_saved_vacancies WHERE information = ? AND user_id = ?', (info,user_id,))
    data_base.commit()
