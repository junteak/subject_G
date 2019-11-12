import sqlite3


def dl_indivisual():
    while True:

        dl_user = input('\n Who dou you want to delete? > ')

        if len(dl_user) >= 20:

            print(" Username should be less than 20 letters")

        elif len(dl_user) == 0 or dl_user.isspace():

            print(' Username should not be blank. ')

        else:
            break


    connection = sqlite3.connect('CRM_App.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM list WHERE name = '{dl_user}'"
    cursor.execute(sql).fetchall()
    connection.commit()
    connection.close()

    print(f'\n Deleted {dl_user}.\n')
