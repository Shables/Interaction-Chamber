import os
import sys
import colorama


def main():
    while True:
        test_input = input("Hey, it looks like you might be learning some things.", "\n Do me a favor and say, do we want to continue or nah? (Y/N): ").strip().lower()
        match test_input:
            case 'y':
                continue
            case 'n':
                sys.exit()
            case _:
                print("uhh.. Try again.")



if __name__ == '__main__':
    main()