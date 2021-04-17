# Automated Teller Machine Mock Project
from datetime import datetime
import random

# Database
account_numbers = [4653743234, 236453452, 6322198769, 5687456200]
allowedUsers = ['Siegfred', 'Kachi', 'Samantha', 'Ojochide']
allowedPassword = ["passSieg", "passKach", "passSam", "passChide"]


def welcome():
    print('Welcome to your ATM')
    choice = int(input("Choose 1. To Login 2. To Register 3. Exit..."))
    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 3:
        exit()
    else:
        print("Invalid Entry")
        welcome()


# function to generate unique 10 digit account number
def account_number_generator(database):
    account_number = random.randint(0000000000, 9999999999)
    if account_number in database:
        account_number_generator(database)
    else:
        database.append(account_number)
        print(f"Account Created Successfully \n Your Account Number Is {account_number}")


# Add Account number tomorrow
# Register Function to create user profile/account
def register():
    create_username = input("create a username...")
    if create_username in allowedUsers:
        print("Username Already in Use! \n Select Another")
        register()
    else:
        create_password = input("create a password...")
        confirm_password = input("Confirm Your Password...")
        if create_password == confirm_password:
            allowedUsers.append(create_username)
            allowedPassword.append(create_password)
            account_number_generator(account_numbers)
            login()
        else:
            print("Password is not the same as confirmed password!")
            register()


# Login function to access user account and perform functions
def login():
    username = input('What is your username? \n')
    if username in allowedUsers:
        user_id = allowedUsers.index(username)
        account_num = account_numbers[user_id]
        password = input("Your Password? \n")
        if password == allowedPassword[user_id]:
            date_item()
            felicitations(username, account_num)
            operation()
        else:
            print('Password incorrect, Please try again')
            login()
    else:
        print('Name not found. Please Try Again')
        login()


# Date and Time added --python set timeout
def date_item():
    abuja_date = datetime.now().strftime("%d/%m/%Y")
    abuja_time = datetime.now().strftime("%H:%M:%S")
    print("Today is ", abuja_date)
    print("Time is ", abuja_time)


def felicitations(name, acc_number):
    print('\n Dear %s' % name)
    print('Welcome to Zuri Bank!')
    print(f"Your Account Number is {acc_number}")


# Operations
def operation():
    selected_option = int(input('Please Select an Option: \n 1. Withdrawal \n '
                                '2. Cash Deposit \n 3. Complaint \n 4. Exit...'))
    balance = 500

    if selected_option == 1:
        withdraw(selected_option, balance)
    elif selected_option == 2:
        deposit(selected_option, balance)
    elif selected_option == 3:
        input('What Issue Would You Like To Report? \n ...')
        print('\n Thank You For Contacting Us!')
        operation()
    elif selected_option == 4:
        print("Thank You for Banking with Us")
        exit()
    else:
        print("Wrong Input!!!")
        operation()

