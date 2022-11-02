import json
import random
import os

def register():
    name = input("Please enter your name:")
    age = int(input("Please enter your age:"))
    password = input("Please enter your password:")
    phone = input("Please enter your phone number:")
    email = input("Please enter your email:")
    if age < 18 or age > 100:
        print("You are not eligible to register")
        return False
    elif len(password) < 8:
        print("Password must be at least 8 characters long")
        return False
    elif len(phone) != 10:
        print("Phone number must be 10 digits long")
        return False
    elif "@" not in email:
        print("Email must contain @")
        return False
    else:
        id = ""
        for i in range(1,10):
            noob = random.randint(1,9)
            rand = str(noob)
            id = id + rand

        filename = "ids/" + id + ".json"
        print("Your ID is: " + id + "\n")

        data = {
            "name": name,
            "age": age,
            "password": password,
            "id": id,
            'tickets': 0,
        }

        jsonObj = json.dumps(data)
        with open(filename, "w") as f:
            f.write(jsonObj)

def login():
    try:
        id = input("Please enter your ID:")
        password = input("Please enter your password:")
        filename = "ids/" + id + ".json"
        with open(filename, "r") as f:
            data = json.load(f)
            if data["password"] == password:
                print("Welcome " + data["name"] + "!")
                return True
            else:
                print("Wrong password")
                return False
    except Exception as e:
        print("Error: " + str(e))

def logout():
    print("Logout successful!")

def exit():
    print("Goodbye!")

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Book Tickets")
    print("4. Cancel Tickets")
    print("5. Logout")
    print("6. Exit")

def bookTicket():
    number = int(input("Enter the number of people you want to take along with you: "))
    fare = int(input("Type 1 to book a normal ticket or 2 to book a premium ticket: "))
    while fare != 1 and fare != 2:
        fare = int(input("Type 1 to book a normal ticket or 2 to book a premium ticket: "))
    if fare == 1:
        price = number * 50
        print("The total price will be ", str(number), " * 50 = ", str(price), ".")
        fee_for_1 = 50
        premium = False
    elif fare == 2:
        price = number * 100
        print("The total price will be ", str(number), " * 100 = ", str(price), ".")
        fee_for_1 = 100
        premium = True

    transaction = ""
    seats = []
    for i in range(1, 10):
        randomnum = random.randint(1, 9)
        rand = str(randomnum)
        transaction = transaction + rand

    for i in range(1, number):
        randomnum2 = random.randint(1, 30)
        for j in range(0, len(seats)):
            if randomnum2 != j:
                seats.append(randomnum2)
            else:
                i = i - 1


    data = {
        "number": number,
        "fee_for_1": fee_for_1,
        "transaction": transaction,
        'premium': premium,
        'seats': seats,
    }
    filename = "tickets/" + transaction + ".json"
    print("Your transaction ID is: " + transaction + "\n")
    jsonObj = json.dumps(data)
    with open(filename, "w") as f:
        f.write(jsonObj)


def cancelTicket():
    id = int(input("Enter the transaction id:- "))
    try:
        if os.path.exists('ids'):
            if os.path.exists('tickets/' + id + '.json'):
                os.remove('tickets/' + id + '.json')
                print("Deleted the ticket.")
        else:
            main()
    except Exception as e:
        print("Deleted the ticket")

def main():
    while True:
        menu()
        choice = int(input("Please enter your choice:"))
        if choice == 1:
            register()
        elif choice == 2:
            if login():
                while True:
                    menu()
                    choice = int(input("Please enter your choice:"))
                    if choice == 3:
                        bookTicket()
                    if choice == 4:
                        cancelTicket()
                    elif choice == 5:
                        logout()
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid ID or password!")
        elif choice == 6:
            exit()
            break
        else:
            print("Please login or register if you do not have an account.")

def execute():
    try:
        if not os.path.exists('ids'):
            os.makedirs('ids')
            if not os.path.exists('tickets'):
                os.makedirs('tickets')
                main()
        else:
            main()
    except Exception as e:
        print("Error: " + str(e))

execute()