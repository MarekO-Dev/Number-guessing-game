import os
from time import sleep as sleep
import random
import libs.constants as constants
from libs.textboxes import *
import db

def save_game(current_level):
    savefile = open("save_file.sv", "w")
    savefile.write(current_level)
    print("SAVING GAME...")
    sleep(1)
    savefile.close()
def load_game():
    savefile = open("save_file.sv", "r")
    output = savefile.read()
    print("LOADING GAME...")
    sleep(1)
    savefile.close()
    return output

MAX_ROWS = os.get_terminal_size().lines
MAX_COLS = os.get_terminal_size().columns
LEVEL_CURRENT = int(load_game())
LEVEL_MAX = 10

def start_game():
    # roll number to guess
    os.system("clear")
    LEVEL_CURRENT = int(load_game())
    print("CURRENT LEVEL: ", LEVEL_CURRENT)

    number_to_guess = random.randint(1, round((LEVEL_CURRENT*1.5))+1)
    print("NUMBER TO GUESS: ", number_to_guess)
    player_guess = get_guess(constants.Colours)
    print("Analyzing...")
    sleep(1)
    if player_guess == str(number_to_guess):
        print("YOU HAVE MADE IT")
        new_level = LEVEL_CURRENT + 1
        if new_level == 11:
            new_level = 10
        save_game(str(new_level))
        start_game()
    else:
        print("No luck this time!")

def main():
    # clear screen
    os.system("clear")
    # show menu
    main_menu(constants.Colours)
    # make user select option
    user_input = input("            Your option is: ")
    match str(user_input):
        case "1":
            start_game()
        case "1":
            start_game()
        case "3":
            return False
        case "999":
            save_game("1")
            return False




main()
