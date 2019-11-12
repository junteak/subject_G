import sqlite3

from check_module import username_list


def dl_indivisual():

    while True:

        dl_user = input('\n Who dou you want to delete? > ')

        # nullかスペースか
        if len(dl_user) == 0 or dl_user.isspace() or len(dl_user) >= 20:
            print(' The username was not found.')

        # ユーザーの中に入力した人がいなかったら
        if dl_user not in username_list():

            print(' The username was not found.')

        else:
            break


    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM list WHERE name = '{dl_user}'"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()

    print(f'\n Deleted {dl_user}.\n')
