import random

Playing = True
while Playing:
    dice_roll_choice = input("Would you like to roll dice? (y/n) ")
    if dice_roll_choice.upper() == "Y":
        int_1 = random.randint(1, 6)
        int_2 = random.randint(1, 6)
        print("You rolled a ", int_1, " and a ", int_2)
    if dice_roll_choice.upper() == "N":
        print("Thank you for playing!")
        break
    else:
        print("Please enter either y or n")