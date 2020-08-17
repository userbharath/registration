name = []
password = []

def register():
    name_of_user = input('Enter your  NEW name : ')
    if name_of_user in name:
        print('Alredy exist plz try other username')
        for i in range(500):

            name_of_user = input('Enter your  NEW name : ')

            if name_of_user not in name:
                name.append(name_of_user)
                break
            print('Already exist plz try other username')

    pass_of_user = input('Enter your NEW password : ')

    retype = input('Retype your NEW password : ')
    if retype == pass_of_user:
        print('successfully registered :)')
        if name_of_user not in name:
            name.append(name_of_user)
        password.append(pass_of_user)

    else:
        for i in range(3):
            retype = input(f'Retype your password (attempt {i + 1}) : ')
            if retype == pass_of_user:

                if name_of_user not in name:
                    name.append(name_of_user)

                password.append(pass_of_user)
                print('succesfully registered')
                break
        else:
            print('Too many attempts .. Denied !')


def login():
    nam = input('Enter your username : ')
    if nam in name:
        pas = input(f'hi {nam} enter your passcode : ')
        if pas in password:
            print('Login sucess')
        else:
            print('OOPs incorrect man')
            for i in range(3):
                re = input('Enter your password again : ')
                if re in password:
                    print(f'hi {nam} sucessfully loged in ')
                    break
            else:
                print('Too many attempts')

    else:
        print('you are not a user')


def update():
    try:
        i = 0
        n = input('Enter your username : ')

        ind_name = name.index(n)

        if n in name:

            p = input('Enter your old password : ')
            if p in password:

                new = input('Enter your new password : ')
                a = name.index(n)
                password[a] = new
                print('Sucessfully updated')
            else:
                for i in range(3):
                    p = input('Enter your old password : ')
                    if p in password:
                        new = input('Enter your new password : ')
                        a = name.index(n)
                        password[a] = new
                        print('Sucessfully updated')
                        break
                else:
                    print('Too many attempts')

        else:
            print('No username')
    except ValueError:
        print('list is empty')



for i in range(1000):
    print()
    print('''WELCOME TO CANARA BANK
              1 . Register 
              2 . Login 
              3 . Update''')
    n = int(input('Enter your operation : '))
    if n == 1 or 2 or 3:
        if n == 1:
            register()

        if n == 2:
            login()
        if n == 3:
            update()
    else:
        print('invalid option..select (1,2,3)')



