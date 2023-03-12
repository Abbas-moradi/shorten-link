from link_shortner.callback import *
from logs import log_prog
import shelve
import re

class Shorten:

    path = 'D:\maktab sharif\week-06-practise\Maktab93-Python-main-02\self project\storage\shorten'

    def __init__(self, link, short_link):
        self.link = link
        self.short_link = short_link

        with shelve.open(Shorten.path) as shelf_shortner:
            if self.short_link in shelf_shortner:
                print('link has been exist...!!!')
                log_prog.logger_error('link has been exist...!!!')
            else:
                shelf_shortner[self.short_link] = self.link
                print(f'The shortner link is :{self.short_link}')
                log_prog.logger_info('The short link has been save')

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
        if not re.match(pattern, link):
            raise Exception("Invalid link address")
        self._link = link



