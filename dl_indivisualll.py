import sqlite3


def dl_indivisual():
    dl_user = input('\n Who dou you want to delete? > ')
    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM list WHERE name = '{dl_user}'"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()
    print(f'\n Deleted {dl_user}.\n')
