from helper_modules.get_input import get_input
from collatz_iteration import run_iteration
from helper_modules.cls import cls
from time import sleep

# placeholder function for dataanalysis submenu -> def create_menu()
def foo():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    start_menu(create_menu())

def create_menu()->dict:
    menu_dict: dict = {
        1:run_iteration,
        2:foo, # palceholder for analysis-function submenu, comes later
        3: exit
    }
    return menu_dict

def start_menu(menu_dict) ->None:
    print("Choose an option:\n", "_" * 16)
    choice =  get_input("1: ....Run an iteration\n2: ..analyse data files\n3: ................exit\n", int, 1, value_list=[1,2,3])
    if choice == 3:
        print("Exiting...")
        sleep(0.5)
        cls()
    menu_dict[choice]()