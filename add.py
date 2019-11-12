import sqlite3


def add(age, name):
    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f'INSERT INTO list (name, age) VALUES (? ,?)'
    cursor.execute(sql, (name, age))
    connection.commit()
    connection.close()
    print(f' added {name}, {age}-year-old')
