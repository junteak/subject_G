import sqlite3


def dl_all():
    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()
