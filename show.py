import sqlite3


def show():
    print()
    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM list"
    users_tuple = cursor.execute(sql).fetchall()
    connection.close()

    for indivisual_info in users_tuple:
        list(indivisual_info)
        print(f' Name: {indivisual_info[1]} / '
              f'age: {indivisual_info[2]}')
