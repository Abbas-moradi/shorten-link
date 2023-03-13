import shelve
from logs import log_prog

class Users:

    _login = {}
    path = 'storage\dbregister'

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.__password = password


        with shelve.open(Users.path) as shelf_file:
            if self.user_name in shelf_file:
                log_prog.logger_error('the user name has been exist!')
                print('the user name has been exist!')
            else:
                shelf_file[self.user_name] = self.__password
                log_prog.logger_info('the register has been successful...')
                print('the register has been successful...')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        if 8 < new_pass < 16:
            self.__password = new_pass

