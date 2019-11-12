import sqlite3


def upd(pre_name, upd_age, upd_name):
    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"UPDATE list SET name='{upd_name}', age = '{upd_age}' WHERE name = '{pre_name}' "
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print(f'\n updated Name: {upd_name} | Age {upd_age}')
