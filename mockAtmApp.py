# Automated Teller Machine Mock Project
from datetime import datetime
import random

# Database - I refactored code to try my knowledge with Lists
first_name = ["Siegfred", "Onyekachi", "Sam", "Ojochide"]
last_name = ["Tuoyo", "Ojodomo", "Dubois", "Onuche"]
balance = [4500, 5000, 5300, 10000]
account_numbers = [4653743234, 236453452, 6322198769, 5687456200]
allowedUsers = ['Siegfred', 'Kachi', 'Samantha', 'Ojochide']
allowedPassword = ["passSieg", "passKach", "passSam", "passChide"]


def welcome():
    print('Welcome to your ATM')
    choice = int(input("Choose \n 1. To Login \n 2. To Register \n 3. Exit \n ... "))
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
        print(f"Account Created Successfully! \n "
              f"Your Account Number Is -> {account_number} <- \n ******************")


# Add Account number tomorrow
# Register Function to create user profile/account
def register():
    print("********REGISTER********")
    create_first_name = input("Enter Your First Name...")
    create_last_name = input("Enter Your Last Name...")
    opening_balance = int(input("Enter Opening Balance..."))
    create_username = input("create a username...")
    if create_username in allowedUsers:
        print("Username Already in Use! \n Select Another")
        register()
    else:
        create_password = input("create a password...")
        confirm_password = input("Confirm Your Password...")
        if create_password == confirm_password:
            first_name.append(create_first_name)
            last_name.append(create_last_name)
            allowedUsers.append(create_username)
            allowedPassword.append(create_password)
            balance.append(opening_balance)
            account_number_generator(account_numbers)
            welcome()
        else:
            print("Password is not the same as confirmed password!")
            register()


# Login function to access user account and perform functions
def login():
    username = input('What is your username? \n')
    if username in allowedUsers:
        user_id = allowedUsers.index(username)
        account_num = account_numbers[user_id]
        name = first_name[user_id]
        current_balance = balance[user_id]
        password = input("Your Password? \n")
        if password == allowedPassword[user_id]:
            date_item()
            felicitations(name, account_num)
            operation(current_balance)
        else:
            print('Password incorrect, Please try again')
            login()
    else:
        print('INVALID USERNAME!. \n Please Try Again!')
        login()


# Date and Time added
def date_item():
    abuja_date = datetime.now().strftime("%d/%m/%Y")
    abuja_time = datetime.now().strftime("%H:%M:%S")
    print("Today is ", abuja_date)
    print("Time is ", abuja_time)


def felicitations(name, acc_number):
    print('\n Dear %s' % name)
    print('Welcome to Zuri Bank!')
    print(f"Your Account Number is {acc_number}")


# function to determine choices of operations
def operation(current_balance):
    selected_option = int(input('Please Select an Option: \n 1. Withdrawal \n '
                                '2. Cash Deposit \n 3. Check Balance \n '
                                '4. Complaint \n 5. Exit...\n'))

    if selected_option == 1:
        withdraw(current_balance)
    elif selected_option == 2:
        deposit(current_balance)
    elif selected_option == 3:
        print(f"Your Balance is \n ***** N{current_balance} *****")
        options(current_balance)
    elif selected_option == 4:
        input('What Issue Would You Like To Report? \n ...')
        print('\n Thank You For Contacting Us!')
        options(current_balance)
    elif selected_option == 5:
        print("Thank You for Banking with Us \n *****************")
        welcome()
    else:
        print("Wrong Input!!!")
        operation(current_balance)


# function to compute user withdrawals
def withdraw(bal):
    print("********WITHDRAWAL********")
    amount_to_withdraw = int(input('Enter Amount: \n'))
    if amount_to_withdraw > bal:
        print('Insufficient Balance')
        withdraw(bal)
    else:
        bal = bal - amount_to_withdraw
        print('Please Take your Cash')
        print('Your Balance is %i' % bal)
        options(bal)


# function to compute user deposits
def deposit(bal):
    print("********DEPOSIT********")
    amount_to_deposit = int(input('Enter Amount: \n'))
    bal = bal + amount_to_deposit
    print('Transaction Successful!')
    print('Your Ledger Balance is %i' % bal)
    options(bal)


# options to validate user choice
def options(entry):
    question = int(input("Do You Want to Perform Another Transaction?"
                         " 1.(Yes) 2.(No) ..."))
    if question == 1:
        operation(entry)
    elif question == 2:
        print("Please Take Your Card \n Thank You For Banking With Us! \n ********* \n ")
        welcome()
    else:
        print("Please Enter a Valid Entry!")


welcome()

