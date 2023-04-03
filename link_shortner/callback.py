import shelve
from logs import log_prog
from admin.models import Users
from link_shortner.model import Shorten
import shortuuid

def shortner():
    user_name = input('enter your user name: ')
    if Users._login[user_name] != True:
        log_prog.logger_error('The user is not logged in')
        print('The user is not logged in')
        return False
    linked = input('Type your link: ')
    x_short = shortuuid.uuid()[6:12]
    log_prog.logger_info('creat the short cod')
    link_shortner ='https://www.shortner.ir/' + x_short
    link = Shorten(linked, link_shortner)

def private():
    user_cod = input('type your short cod: ')
    if 5 < len(user_cod) < 10:
        linked = input('Type your link: ')
        log_prog.logger_info('creat the short cod')
        link_shortner ='https://www.shortner.ir/' + user_cod
        link = Shorten(linked, link_shortner)
    else:
        print('Your cod is very short/long...!!!')
        log_prog.logger_info('Your cod is very short/long...!!!')
        private()

def remove():
    remove_dict = {}
    user_name = input('enter your user name: ')
    if Users._login[user_name] != True:
        log_prog.logger_error('The user is not logged in')
        return 'The user is not logged in'
    path = 'storage\shorten'
    with shelve.open(path) as file_short:
        index = 0
        for key, value in file_short.items():
            print(f'{index}. {key} --> {value}')
            remove_dict[index] = key
            index += 1
        log_prog.logger_info(f'the list shortner show by {user_name}')
        try:
            remove_index = int(input('Enter item index for remove: '))
            file_short.pop(remove_dict[remove_index])
            print('Remove successful...')
            log_prog.logger_info(f'Item {remove_dict[remove_index]} remove successful...')
        except Exception(IndexError, ValueError):
            print('Item not found')
            log_prog.logger_error('Item not found')

def show():
    user_name = input('enter your user name: ')
    if Users._login[user_name] != True:
        log_prog.logger_error('The user is not logged in')
        return 'The user is not logged in'
    path = 'storage\shorten'
    with shelve.open(path) as file_short:
        index = 0
        for key, value in file_short.items():
            print(f'{index}. {key} --> {value}')
            index += 1
        log_prog.logger_info(f'the list shortner show by {user_name}')

def show_by_link():
    user_name = input('enter your user name: ')
    if Users._login[user_name] != True:
        log_prog.logger_error('The user is not logged in')
        return 'The user is not logged in'
    path = 'storage\shorten'
    short_link = input('Enter your short link: ')
    try:
        with shelve.open(path) as file_short:
            print(file_short[short_link])
            log_prog.logger_info(f'Link {short_link} show by {user_name}')
    except (Exception, ValueError, IndexError):
        print('Link not found...!!!')
        log_prog.logger_error('Link not found')

