'''

指定された値が要素に含まれるかどうか
https://pg-chain.com/python-list-in

'''

import sqlite3

connection = sqlite3.connect('CRM_App.db')
cursor = connection.cursor()
sql = f"SELECT * FROM list"
users_tuple = cursor.execute(sql).fetchall()
connection.close()


def duplicate_check(check_name):
    # タプルの中に引数check_nameがあればTrueを返す
    if check_name in users_tuple:
        return True


def username_list():
    # ユーザーネームをリスト化
    name_list = []

    for indivisual_info in users_tuple:
        list(indivisual_info)
        name_list.append(indivisual_info[1])

    return name_list
