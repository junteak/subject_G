'''
自動的にidを取得する
https://www.dbonline.jp/sqlite/table/index9.html

'''

import sqlite3


def main():
    connection = sqlite3.connect('CRM_App.db')

    sql = """ CREATE TABLE list (
                id integer primary key autoincrement,
                name text,
                age integer)
    """

    cursor = connection.cursor()

    cursor.execute(sql)

    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
