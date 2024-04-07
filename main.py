master_pwd = input('What is the master password? ')
def view():
    with open('password.txt', 'r') as f:  # creating file with pwd
        for line in f.readlines():
            data = line.rstrip()
            user, pasw = data.split('|')


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:  # creating file with pwd
        f.write('Name: ' + name + '|' + 'Password: ' + pwd + '\n')


mode = input('Would you like to add a new password or view existing ones? (view / add) ').lower()
if mode == 'view':
    view()
elif mode == 'add':
    add()
else:
    print('Invalid mode')



