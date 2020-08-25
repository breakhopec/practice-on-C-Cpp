#coding=utf-8
import time

class User(object):

    def __init__(self, _file_path='user.txt'):
        self._auth = {}

        with open(_file_path) as _file_objects_r:
            self._infos = _file_objects_r.readlines()

        for _info in self._infos:
            pos = _info.find(':')
            self._auth[_info[:pos]] = _info[pos + 1:].strip()

        self._login_attempts = 0

    def login(self):
        self.login_username = input('username: ')

        while True:
            if self.login_username in self._auth.keys():
                self.login_password = input('password: ')

                if self._auth[self.login_username] == self.login_password:
                    print('welcom back')
                    self._guest_regist('successfully')
                    return True
                else:
                    print('permission denied.')
                    self._increment_login_attempts()

                if self._login_attempts == 3:
                    self._guest_regist('fail')
                    self._reset_login_attempts()
                    return False

            else:
                print('user do not exist.')
                return False

    def change_password(self):
        if self.login() == True:
            while True:
                new = input('input new password: ')
                confirm = input('confirm it: ')
                if new == confirm:
                    self._auth[self.login_username] = confirm
                    #self._write_back()

    def _guest_regist(self, status):
        with open('log.txt', 'a') as file_objects:
            file_objects.write('[ ' + time.ctime() + ' ] ')
            file_objects.write('%s login %s\n' % (self.login_username, status))

    def _increment_login_attempts(self):
        self._login_attempts += 1

    def _reset_login_attempts(self):
        self._login_attempts = 0


class Admin(User):

    def __init__(self):
        super().__init__('user.txt')
        self._userlist = self._auth
        super().__init__('admin.txt')

    def _guest_regist(self, status):
        with open('log.txt', 'a') as file_objects:
            file_objects.write('[ ' + time.ctime() + ' ] ')
            file_objects.write('%s login as ADMIN %s\n' % \
                    (self.login_username, status))

    def clean_log(self):
        if self.login() == True:
            with open('log.txt', 'w') as file_objects:
                file_objects.write('')

            self._admin_operation('clean log')
            print('clean log successfully')

    def make_user(self):
        if self.login() == True:
            self._new_username = input('new user: ')
            if self._is_name_used(self._new_username) == False:
                self._new_password = input('password: ')

                with open('user.txt', 'a') as file_objects:
                    file_objects.write('%s:%s\n' % \
                            (self._new_username, self._new_password))

                self._admin_operation('add a user ' + self._new_username)
                print('add new user successfully')

    def delete_user(self):
        pass
    
    def _admin_operation(self, operation):
        with open('admin_operation.txt', 'a') as file_objects:
            file_objects.write('[ ' + time.ctime() + ' ] ')
            file_objects.write('%s: %s\n' % (self.login_username, operation))

    def _is_name_used(self, name):
        if name in self._userlist.keys():
            print('this username exists')
            return True
        else:
            return False

