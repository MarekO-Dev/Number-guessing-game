import os
import random
import libs.constants as constants
from time import sleep as sleep
from libs.textboxes import *
from libs.game_state import *

MAX_ROWS = os.get_terminal_size().lines
MAX_COLS = os.get_terminal_size().columns
LEVEL_CURRENT = load_game()[0]
LEVEL_MAX = 10
TRIES = load_game()[1]

def start_game():
    # roll number to guess
    os.system("clear")

    loaded_game_state = load_game()

    LEVEL_CURRENT = loaded_game_state[0]
    TRIES = loaded_game_state[1]

    if TRIES <= 0:
        save_game("1", "3")
        you_loose(constants.Colours)
        sleep(5)
        main() # Somewhere here is the bug... when player loses (When player runs out of tries) it goes to main menu but when player choses 3. Exit it will not work

    number_to_guess = random.randint(1, round((LEVEL_CURRENT*1.5))+1)
    print("CURRENT LEVEL: ", LEVEL_CURRENT)
    print("NUMBER TO GUESS: ", number_to_guess)
    player_guess = get_guess(constants.Colours)
    print("Analyzing...")
    sleep(0.3)
    print(">")
    if player_guess == str(number_to_guess):
        print("YOU HAVE MADE IT")
        new_level = LEVEL_CURRENT + 1
        if new_level == 11:
            new_level = 10
        save_game(str(new_level), str(TRIES))
        start_game()
    else:
        if int(player_guess) < int(number_to_guess):
            outcome_no_luck_higher(constants.Colours)
            sleep(5)
        elif int(player_guess) > int(number_to_guess):
            outcome_no_luck_lower(constants.Colours)
            sleep(5)
        new_tries = TRIES - 1

        if new_tries <= 0:
            save_game(str(LEVEL_CURRENT), str(new_tries))
            main()
        else:
            save_game(str(LEVEL_CURRENT), str(new_tries))
            start_game()# OR Somewhere here is the bug... when player loses (When player runs out of tries) it goes to main menu but when player choses 3. Exit it will not work
def start_custom_game(level):
    # roll number to guess
    os.system("clear")

    LEVEL_CURRENT = level

    number_to_guess = random.randint(1, round((LEVEL_CURRENT*1.5))+1)
    print("CURRENT LEVEL: ", LEVEL_CURRENT)
    print("NUMBER TO GUESS: ", number_to_guess)
    player_guess = get_guess(constants.Colours)
    print("Analyzing...")
    sleep(0.3)
    print(">")
    if player_guess == str(number_to_guess):
        you_win(constants.Colours)
        sleep(5)
        main()
    else:
        if int(player_guess) < int(number_to_guess):
            outcome_no_luck_higher(constants.Colours)
            sleep(5)
        elif int(player_guess) > int(number_to_guess):
            outcome_no_luck_lower(constants.Colours)
            sleep(5)
        main()

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
        case "2":
            level_needed = input("ENTER LEVEL U WANT: ")
            start_custom_game(int(level_needed))
        case "3":
            return
        case "999":
            save_game("1", "3")
            return False
        case _:
            return
#START GAME
main()
