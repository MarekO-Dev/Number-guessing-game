import os
import platform
import sys
import sysconfig
from rich import print
from rich import inspect
from rich.console import Console

console = Console()

def print_system_info():
    print("os.name                      ",  os.name)
    print("sys.platform                 ",  sys.platform)
    print("platform.system()            ",  platform.system())
    print("sysconfig.get_platform()     ",  sysconfig.get_platform())
    print("platform.machine()           ",  platform.machine())
    print("platform.architecture()      ",  platform.architecture())

def outcome_no_luck_higher(colours):
    print(
    "[bold yellow on black]|--------------------------------------------------------|" "\n|                                                        |"
    "\n|                                                        |"
    "\n|                No luck this time                       |"
    "\n|             The number was [italic red]HIGHER[/italic red]                      |"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|--------------------------------------------------------|[/bold yellow on black]")



def outcome_no_luck_lower(colours):

    print(
    "[bold yellow on black]|--------------------------------------------------------|" "\n|                                                        |"
    "\n|                                                        |"
    "\n|                No luck this time                       |"
    "\n|             The number was [italic red]LOWER[/italic red]                       |"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|--------------------------------------------------------|[/bold yellow on black]")


def get_guess(colours, tries, level):


    print(
    "[bold green on black]|--------------------------------------------------------|"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|========================================================|[/bold green on black]")
    display_tries(colours, tries)
    display_player_info(level)
    #os.system("echo '\033[30C'")
    guess = input(" \033[6;24H \033[0;33;40m \b\b\b Your guess: ")
    os.system("echo '\033[10;H' \033[0m")
    return guess


def you_win_message(colours):

    print("|--------------------------------------------------------|")
    print("|                                                        |")
    print("|                YOU ARE A WINNER !!!                    |")
    print("|                                                        |")
    print("|--------------------------------------------------------|")


def you_loose(colours):

    print("|--------------------------------------------------------|")
    print("|                                                        |")
    print("|                YOU ARE A LOOSER !!!                    |")
    print("|                                                        |")
    print("|--------------------------------------------------------|")

def display_player_info(level):
    print(
    "[bold green on black]|                                                        |"
    "\n|                                                        |"
    f"\n|                    Current level: [blink]{level}[/blink]                    |" ## tries
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|--------------------------------------------------------|")

def display_tries(colours, tries):
    clr = colours.BLACK
    match tries:
        case 3:
            clr = "bold green on black"
        case 2:
            clr = "bold yellow on black"
        case 1:
            clr = "bold red on black"
        case _:
            return False
    print(
    "[bold green on black]|                                                        |"
    "\n|                                                        |"
    f"\n|                     Tries left: [{clr}]{tries}[/{clr}]                      |" ## tries
    "\n|                                                        |"
    "\n|                                                        |"
    "\n|--------------------------------------------------------|")


def main_menu(colours):

    print("|----------------------------------------------------|")
    print("|                                                    |")
    print("|                   MAIN MENU                        |")
    print("|                                                    |")
    print("|====================================================|")
    print("|                                                    |")
    print("|                                                    |")
    print("|                [1]. New Game                       |")
    print("|                [2]. Custom Level                   |")
    print("|                                                    |")
    print("|                [3]. Exit                           |")
    print("|              [999]. Reset Progress                 |")
    print("|                                                    |")
    print("|----------------------------------------------------|")
