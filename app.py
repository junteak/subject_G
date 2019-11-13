'''

rowに自動的にidを取得するコマンド https://www.dbonline.jp/sqlite/table/index9.html

'''

import sqlite3
import sys

from add import add
from check_module import username_list
from dl_all import dl_all
from dl_indivisualll import dl_indivisual
from show import show
from upd import upd


def main():

    print('''
==== Welcome to CRM application ====
 [S]how: Show all users info
 [A]dd new user
 [U]pdate the existing user
 [D]elete the exsisting user
 [F]ind User
 [Q]uit CRM app
====================================''')

    command = input(' Your Command > ')

    if command == 's' or command == 'S':

        show()
        main()

    if command == 'a' or command == 'A':

        while True:

            name = input("\n New user name is... > ")

            if len(name) == 0 or name.isspace():  # 何も文字がないかlen(name) == 0、空白だった場合 issapse()

                print(" Username can't be blank.")
                main()

            if len(name) >= 20:

                print(" Username must be less than 20 letters")

            if name in username_list():

                print(" Username can't be duplicated")

            if name.isdigit():  # 数字かどうか判断

                print(" User name must be consisted by letters.")

            else:

                break


        while True:

            str_age = input(" New user age... > ")

            if len(str_age) == 0 or str_age.isspace():

                print(" Age can't be blank.")

            if not str_age.isdecimal():  # 数字でなければ

                print(' Age must be Arabic Positive Numerals')

            else:

                age = int(str_age)


                if age >= 0 and age <= 150:

                    break

                else:
                    print(' Enter the correct age.')  # 正の数字でなければ

        add(age, name)

        main()

    if command == 'u' or command == 'U':

        show()

        pre_name = input('\n Who you want to update? > ')

        if pre_name not in username_list():

            print(" Username doesn't exist")
            main()

        elif pre_name in username_list():  # なぜここは if ではなく elif でないといけないか

            while True:

                upd_name = input(' New user name ? > ')

                if len(upd_name) == 0 or upd_name.isspace():  # 何も文字がないかlen(name) == 0、空白だった場合 issapse()

                    print(" Username can't be blank.")

                if len(upd_name) >= 20:

                    print(" Username must be less than 20 letters")

                if upd_name.isdigit():  # 数字かどうか判断

                    print(" User name must be consisted by letters.")

                else:

                    break

        while True:

            str_upd_age = input(" New user age... > ")

            if len(str_upd_age) == 0 or str_upd_age.isspace():

                print(" Age can't be blank.")

            if not str_upd_age.isdecimal():  # 数字でなければ

                print(' Age must be Arabic Positive Numerals')

            else:

                upd_age = int(str_upd_age)

                if upd_age >= 0 and upd_age <= 150:

                    break

                else:
                    print(' Enter the correct age.')

        upd(pre_name, upd_age, upd_name)

        main()

    if command == 'd' or command == 'D':

        print('\n 1.Delete individually 2.Delete all')
        num = input(' Your command > ')

        if num == '1':

            show()
            dl_indivisual()
            main()

        if num == '2':

            dl_all()
            main()

        else:

            print(' Command not found.')
            main()

    if command == 'f' or command == 'F':  # 終了

        find_name = input('\n Who you want to find? > ')

        if find_name not in username_list():
            print(f" {find_name} doesn't exist")
            main()

        if find_name in username_list():
            print()
            connection = sqlite3.connect('CRM_App.db')
            cursor = connection.cursor()
            sql = f"SELECT name, age FROM list WHERE name = '{find_name}'"
            user_tuple = cursor.execute(sql).fetchone()  # fetchoneにすると単体のタプルが取得できる
            connection.close()
            user_list = list(user_tuple)
            print(f" Name: {user_list[0]} | Age: {user_list[1]}")
            main()

    if command == 'q' or command == 'Q':  # 終了

        print('''
          Quitted PRM. 
          Bye!
            ''')

        sys.exit()  # 終了


    else:
        print(' Command not found.')
        main()


if __name__ == '__main__':
    main()
