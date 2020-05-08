import csv
import random
import os


print('Welcome to SN BANK')
print('*' * 18)


print('Please choose an option''\n 1 Staff Login''\n 2 Close App')
choice = int(input('>: '))

while choice == 1:
    username = str(input('username: '))
    password = str(input('password: '))


    def login_check():
        with open('staff.txt', 'r') as file:
            staff_list = csv.reader(file)
            user_details(staff_list)
            file.close()


    def user_details(file):
        for row in file:
            if row[0] == username:
                user_confirmed = [row[0],row[1]]
                password_checker(user_confirmed)
                break


    def password_checker(user_confirmed):
        if user_confirmed[1] == password:
            print('Login Successful!')
        else:
            print('User details incorrect''\nTry Again')
            print('Please choose an option''\n 1 Staff Login''\n 2 Close App')
            choice = int(input('>: '))
    login_check()

    while True:
        session = open('session.txt', 'w')

        print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
        option = int(input('>: '))
        if option == 1:
            account_name = str(input('Account Name: ')).lower()
            opening_balance = float(input('Opening Balance: '))
            account_type = str(input('Account Type: ')).lower()
            account_email = input('Account email: ')
            account_number = ''.join(map(str, [random.randint(1,9) for a in range(0,10)]))
            customer_details = open('customer.txt', 'w+')
            customer_details.write('Account Name: %s\n' % account_name)
            customer_details.write('Opening Balance: %s\n' % opening_balance)
            customer_details.write('Account Type: %s\n' % account_type)
            customer_details.write('Account email: %s\n' % account_email)
            customer_details.write('Account Number: %s\n' % account_number)
            customer_details.close()

            print(f'Your Account Number is {account_number}')
            print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
            option = int(input('>: '))

        if option == 2:
            input('input your Account Number: ')
            account_details = open('customer.txt', 'r')
            print(account_details.read())

            print('Please chose an option''\n1. Create new bank account''\n2. Check Account Details''\n3. Logout')
            option = int(input('>: '))

        if option == 3:
            session.close()
            os.remove("session.txt")
            print('Please choose an option''\n 1 Staff Login''\n 2 Close App')
            choice = int(input('>: '))


while choice == 2:
    print('Program Terminated''\nThank You and Good Bye')
    break
