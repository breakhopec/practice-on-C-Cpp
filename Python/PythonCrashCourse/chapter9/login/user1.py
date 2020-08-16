#coding=utf-8

class User(object):

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._login_attempts = 0

    def _increment_login_attempts(self):
        self._login_attempts += 1

    def _reset_login_attempts(self):
        self._login_attempts = 0

    def login(self):
        while self._login_attempts < 3:
            tmp_name = input('username: ')
            tmp_pwd = input('password: ')
            if self._username == tmp_name and \
                    self._password == tmp_pwd:
                print('welcom back')
                break
            else:
                print('permission denied, try again please')
                self._increment_login_attempts()

        self._reset_login_attempts()


class Admin(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self._privileges = Privilege()

class Privilege(object):

    def __init__(self):
        self._privileges = ['add post', 'del post', 'ban user']

    def show_privileges(self):
        for privilege in self._privileges:
            print(privilege, end='  ')
        print('')
