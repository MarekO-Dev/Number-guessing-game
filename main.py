import os
import random
import libs.constants as constants
import libs.textboxes as tboxes
import db

you_win = tboxes.Prompt("You win!", 100, 30)
you_win.draw()
TRIES = 3
def try_again():
    print("------")
    print(".             Would you like to try again?            .")
    print("                       Yes / No                        ")
    print("                                                       ")
    print("------")
    print("")
    answer = input()

    match str(answer).lower():
        case "yes" | "y" | "ye" | "ya" | "1":
            new_game()
        case "no" | "nah" | "n" | "0":
            return False
        case "brutal":
            new_game(minimum = random.randint(1,100), maximum = random.randint(101, 500))
        case _:
            print("Unknown answer try again! ")
            try_again()

def you_win():
    global TRIES
    os.system("clear")
    tboxes.you_win(constants.Colours.GREEN, constants.Colours.BLACK)
    TRIES = 3
    #main() # This works but try again is an option
    try_again()

def you_lost():
    global TRIES
    os.system("clear")
    tboxes.you_loose(constants.Colours.RED, constants.Colours.BLACK)
    TRIES = 3

    #main() # This works but try again is an option
    try_again()

def subtract_tries():
    global TRIES

    TRIES -= 1

def guess (number_to_guess):
    os.system("clear")
    os.system(f"echo \033[1m {constants.Colours.WHITE} \033[0m")

    global TRIES
    print(f"{number_to_guess}")
    tboxes.display_tries(
        constants.Colours.RED,
        constants.Colours.GREEN,
        constants.Colours.ORANGE,
        constants.Colours.BLACK,
        TRIES
    )
    player_guess = input("Your guess: ")
    if str(player_guess) == str(number_to_guess):
        you_win()
    else:
        subtract_tries()
        if TRIES <= 0:
            os.system(f"echo {constants.Colours.RED}")
            you_lost()
        else:
            guess(number_to_guess)



def new_game ():
    random_number = random.randint(1, 3)
    guess(random_number)

def main_menu ():
    os.system("clear")
    tboxes.main_menu(constants.Colours.BLACK, constants.Colours.BLACK)
    option = input("Your option: ")

    return option


def main():
    match main_menu():
        case "1":
            new_game()
        case "2":
            os.system("clear")
            print("Not implemented yet")
            main()
        case "3":
            return False
        case _:
            print("Please choose a valid option! ")
            main()

main()
