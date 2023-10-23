def password_protected(func):
    password = '2905'

    def wrapper():
        entered_password = input('Please enter the password: ')
        if entered_password == password:
            func()  
        else:
            print('Wrong password. Access to the function is closed.')

    return wrapper


@password_protected
def func():
    print('Access to the function is open.')


func()
