import os
def cls() -> int:
    return os.system('cls') if os.name == 'nt' else os.system('clear')

