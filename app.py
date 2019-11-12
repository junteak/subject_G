'''

todo 年齢のところ 文字、少数、受け入れない。
toDo Add,Upd,delete の名前のところで、数字をうけつけないようにする。

rowに自動的にidを取得するコマンド https://www.dbonline.jp/sqlite/table/index9.html

'''

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

            else:

                break

        while True:

            str_age = input(" New user age... > ")

            if len(str_age) == 0 or str_age.isspace():

                print(" Age can't be blank.")

            else:

                age = int(str_age)

                if age >= 0 and age <= 150:

                    break

                else:
                    print(' Enter the correct age.')

        add(age, name)

        main()

    if command == 'u' or command == 'U':

        show()

        pre_name = input('\n Who you want to update? > ')

        # if len(pre_name) == 0 or pre_name.isspace():
        #
        #     print(" Username can't be blank.")
        #     main()

        if pre_name not in username_list():

            print(" Username doesn't exist")
            main()

        elif pre_name in username_list():

            while True:

                upd_name = input(' New user name ? > ')

                if len(upd_name) == 0 or upd_name.isspace():  # 何も文字がないかlen(name) == 0、空白だった場合 issapse()

                    print(" Username can't be blank.")

                elif len(upd_name) >= 20:

                    print(" Username must be less than 20 letters")

                else:

                    break

        while True:

            str_upd_age = input(" New user age... > ")

            if len(str_upd_age) == 0 or str_upd_age.isspace():

                print(" Age can't be blank.")

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
