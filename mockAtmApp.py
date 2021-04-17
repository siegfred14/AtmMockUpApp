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

