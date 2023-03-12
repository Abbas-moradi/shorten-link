import shelve
from admin.models import Users
from logs import log_prog
import getpass


def register():
    user_name = input('Enter your user name:').strip().lower()
    password = input('Enter your password:')
    user_register = Users(user_name, password)


def login():
    user_name = input('Enter your user name:')
    password = input('Enter your password:')
    path = 'D:\maktab sharif\week-06-practise\Maktab93-Python-main-02\self project\storage\dbregister'
    with shelve.open(path) as shelf_file:
        for k, v in shelf_file.items():
            if user_name != k and password != v:
                continue
            else:
                Users._login[user_name] = True
                print('Username logging')
                log_prog.logger_info(f'Username: {user_name} is logging')


def log_out():
    out = input('enter your user name: ')
    if Users._login[out] == True:
        log_prog.logger_info(f'Username {out} log out')
        print('Username log out')
        Users._login.pop(out)