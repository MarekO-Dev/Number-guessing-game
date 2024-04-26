class Prompt:
    def __init__ (self, text, box_w, box_h):

        self.text = text
        self.width = box_w
        self.height = box_h

    def draw (self):

        for row in range(0, self.height):
            print (row)


def you_win(start, reset):
    print(start)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                YOU ARE A WINNER !!!                |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(reset)

def you_loose(start, reset):
    print(start)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                YOU ARE A LOOSER !!!                |")
    print("|                   BIG POO POOO !                   |")
    print("|----------------------------------------------------|")
    print(reset)

def display_tries(red, green, orange, black, tries):
    print(black)
    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                MAKE YOUR TRY COUNT !               |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(black)
    print ("")
    match tries:
        case 3:
            print(green)
        case 2:
            print(orange)
        case 1:
            print(red)
        case _:
            return False
    print (f"Tries left: {tries}")
    print (black)

def main_menu(start, reset):
    print(start)
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
    print("|                                                    |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
    print(reset)
