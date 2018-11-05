"""Basic address book functionality:"""
from src.action import *
from src.query import *


def main():
    """Get user input and pass it to action"""
    user_input = get_query()
    while user_input != 'q':
        if user_input == 'a':
            add_record(get_record())
        else:
            search(user_input)
        print('')
        user_input = get_query()


if __name__ == '__main__': main()
