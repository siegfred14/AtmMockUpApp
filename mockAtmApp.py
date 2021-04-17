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

