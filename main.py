import os
import sys
import colorama
import random
import time
from people import People


def main():
    while True:
        test_input = input("Hey, how did you get roped into this?.. well, since you're here.." + "\nWanna see a little experiment? (Y/N): ").strip().lower()
        match test_input:
            case 'y':
                continue
            case 'n':
                sys.exit()
            case _:
                print("uhh.. I have no idea what you just said. Try again.")



if __name__ == '__main__':
    main()