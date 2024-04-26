def get_guess(colours):

    print(colours.GREEN)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    guess = input(f"|                     YOUR GUESS:{colours.RED} ")
    print(f"{colours.GREEN}|                                                    |")
    print("|----------------------------------------------------|")
    print(colours.BLACK)
    return guess


def you_win(colours):
    print(colours.GREEN)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                YOU ARE A WINNER !!!                |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(colours.BLACK)

def you_loose(colours):
    print(colours.RED)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                YOU ARE A LOOSER !!!                |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(colours.BLACK)

def display_tries(colours):
    print(colours.BLACK)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print(f"|             {colours.RED} MAKE YOUR TRY COUNT ! {colours.BLACK}              |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(colours.BLACK)
    print ("")
    match tries:
        case 3:
            print(colours.GREEN)
        case 2:
            print(colours.ORANGE)
        case 1:
            print(colours.RED)
        case _:
            return False
    print (f"Tries left: NOTRIES") ## tries
    print (colours.BLACK)

def main_menu(colours):
    print(colours.BLACK)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                    MAIN MENU                       |")
    print("|                                                    |")
    print("|====================================================|")
    print("|                                                    |")
    print("|                                                    |")
    print("|                1. New Game                         |")
    print("|                2. Select Level                     |")
    print("|                                                    |")
    print("|                3. Exit                             |")
    print("|              999. Reset Progress                   |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(colours.BLACK)
