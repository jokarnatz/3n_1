from sys import  exit
from time import sleep
from typing import get_origin, get_args

def  get_input(prompt: str, datatype: type, *min_value: int, **value_list: list):
    while True:
        try:
            origin = get_origin(datatype)
            args = get_args(datatype)
            if origin == list:
                value = input(prompt).split()
                if args and args[0] == int:
                    value = [int(i) for i in value]
                    if min_value:
                        for v in value:
                            if v < min_value[0]:
                                raise ValueError(f'All values must be at least {min_value[0]}.')
                    return datatype(value)
                elif datatype == list:
                    value = input(prompt).split()
                    return datatype(value)
            else:
                value = datatype(input(prompt))
                if min_value:
                    if value < min_value[0]:
                        raise ValueError(f'Value must be at least {min_value[0]}.')
                elif value_list:
                    if value not in value_list:
                        raise ValueError(f'Value must be in {value_list}.\n')
                return value
            
        except (ValueError, TypeError):
            print('Invalid input. Please try again.')
        except KeyboardInterrupt:
            print('\nExiting')
            sleep(0.5)
            exit(0)
        except EOFError:
            print('\nInput stream ended. Exiting.')
            exit(0)
        except Exception as e:
            print(f'An error occurred: {e}')
            # Don't loop infinitely on unknown errors
            exit(1)

if __name__ == '__main__':
    value = get_input('Enter a (list of) non-negative integer(s) (space-separated): ', list[int], 0)
    print(' '.join(map(str, value)))