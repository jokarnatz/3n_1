# exploring the 3n+1  problem ( Collatz Conjecture )
from menu import start_menu, create_menu
#from helper_modules.cls import cls

if __name__ == '__main__':
    while True:
        #cls()  # Clear screen before showing menu
        menu_dict = create_menu()
        start_menu(menu_dict)