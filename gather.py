import random
import os
import json

def register():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    password = input("Please enter your password: ")
    id = ""
    for i in range(9):
        temp = random.randint(1,9)
        rand = str(temp)
        id = id + rand

    filename = "ids/" + id + ".json"
    print("Your ID is: " + id + "\nYour ID is important. Make sure that you don't forget it!\nYou start with an amount of $1000")

    with open(filename, "a") as o:
        temp = {
            "name": name,
            "age": age,
            "password": password,
            "ID": id,
            "amount": 1000
        }
        o.write(json.dumps(temp))

def login():
    id = input("Please enter your ID: ")
    filename = "ids/" + id + ".json"
    with open(filename, "r") as o:
        if o:
            print("Welcome back!")
            check = input("Enter your password to confirm it's you: ")
            temp = json.load(o)
            if(check == temp["password"]):
                return id, True
            else:
                print("Wrong Password!")
        else:
            print("Invalid ID")

#Withdrawal Function
def withdraw(amount, isLoggedIn, logged_id):
    if not isLoggedIn:
        print("You are not logged in!\nSelect '2' in menu to log in")
        return 0

    filename = "ids/" + logged_id + ".json"
    with open(filename, "r") as o:
        temp = json.load(o)
    if temp["amount"] < amount:
        print("Insufficient funds")
        return False
    else:
        temp["amount"] = temp["amount"] - amount
        with open(filename, "w") as o:
            o.truncate(0)
            o.write(json.dumps(temp))

#Deposit Function
def deposit(amount, isLoggedIn, logged_id):
    if not isLoggedIn:
        print("You are not logged in!\nSelect '2' in menu to log in")
        return 0

    filename = "ids/" + logged_id + ".json"
    with open(filename, "r") as o:
        temp = json.load(o)

    temp["amount"] = temp["amount"] + amount

    with open(filename, "w") as o:
        o.truncate(0)
        o.write(json.dumps(temp))

def main():
    isLoggedIn = False
    logged_id = ""
    if not os.path.exists('ids'):
        os.system('mkdir ids')
    while 1:
        print("Welcome to the bank!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("4. Withdraw")
        print("5. Deposit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            logged_id, isLoggedIn = login()
        elif choice == "3":
            print("Thank you for using the bank!")
            return 0
        elif choice == "4":
            amount = int(input("Please enter the amount you want to withdraw: "))
            withdraw(amount, isLoggedIn, logged_id)
        elif choice == "5":
            amount = int(input("Please enter the amount you want to deposit: "))
            deposit(amount, isLoggedIn, logged_id)

if __name__ == '__main__':
    main()
