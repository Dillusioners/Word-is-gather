import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    a = random.randint(min, max)
    b = random.randint(min, max)
    print("Rolled dice and the values are ", a, " and ", b)
    if a == b:
        print("You died!")
    roll_again = input("Roll the dices again?")
