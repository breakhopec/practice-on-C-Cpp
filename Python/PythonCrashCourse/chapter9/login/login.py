#cooding=utf-8
import user1
def main():
    new_user = user1.User('root', '123')
    #user1.login()
    root = user1.Admin('root', 'abcd')
    root._privileges.show_privileges()

if __name__ == '__main__':
    main()