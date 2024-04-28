import os
import platform
import sys
import sysconfig

import random
import libs.constants as constants
from libs.textboxes import *
from libs.game_state import *
from time import sleep as sleep

DEBUG_MODE = True
level_max = constants.GameSettings.MAX_LEVEL

def advance_level(level_current, tries):
    new_level = level_current + 1

    save_game(str(new_level), str(tries))
    start_game()

def start_game():

    # BUG: When a player wins previous game
    # in this game console colour will be changed to black for some reason

    os.system("clear")
    loaded_game_state = load_game()
    level_current = loaded_game_state[0]
    tries = loaded_game_state[1]

    if tries <= 0:
        you_loose(constants.Colours)
        save_game("1", "3")
        sleep(5)
        main()

    # roll new number to guess
    number_to_guess = random.randint(1, round(((level_current*2)+3))+1)
    if DEBUG_MODE:
        print(number_to_guess)
    # ask for player guess
    player_guess = get_guess(constants.Colours, tries, level_current)

    sleep(0.3)

    # check outcome
    match (int(player_guess) == int(number_to_guess)):
        case True:

            ### PLAYER ATTEMPT SUCCESS

            you_win_message(constants.Colours)

            sleep(2)
            advance_level(level_current, tries)
            if new_level >= 11:
                new_level = level_max

        case False:

            ### PLAYER ATTEMPT FAILED
            player_guess_less = int(player_guess) < int(number_to_guess)
            player_guess_more = int(player_guess) > int(number_to_guess)
            match player_guess_more | player_guess_less:
                case True:
                    if player_guess_more:
                        sleep(1)
                        outcome_no_luck_lower(constants.Colours)
                        tries = tries - 1

                        sleep(0.3)
                        if tries <= 0:
                            save_game("1", "3")
                            sleep(1)
                            main()
                        else:
                            save_game(str(level_current), str(tries))
                            sleep(1)
                            start_game()
                    elif player_guess_less:
                        sleep(1)
                        outcome_no_luck_higher(constants.Colours)
                        tries = tries - 1

                        sleep(0.3)
                        if tries <= 0:
                            save_game("1", "3")
                            sleep(1)
                            main()
                        else:
                            save_game(str(level_current), str(tries))
                            sleep(1)
                            start_game()


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
            return
            #level_needed = input("ENTER LEVEL U WANT: ")
            #start_custom_game(int(level_needed))
        case "3":
            return
        case "999":
            save_game("1", "3")
            return False
        case _:
            return
#START GAME
if __name__ == "__main__":
    main()
