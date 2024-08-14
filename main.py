import os
import sys
import colorama
from colorama import Fore, Back, Style
import random
import time
from people import People
from people_lists import generated_people
from simulation import Simulation

colorama.init(autoreset=True)

def main():
    while True:
        test_input = input(Fore.CYAN + "\n\n\nHey, how did you get roped into this?.. well, since you're here.." + "\nWanna see a little experiment? (Y/N): ").strip().lower()
        match test_input:
            case 'y':
                user_choice1 = int(input("For how many rounds?: "))
                simulation = Simulation(generated_people)
                simulation.run_simulation(max_rounds=user_choice1)
            case 'n':
                sys.exit()
            case _:
                print("uhh.. I have no idea what you just said. Try again.")
        user_choice2 = input(Fore.CYAN + "\n\n\nHey, wanna do that again? (Y/N): ").lower()
        match user_choice2:
            case 'y':
                main()
            case 'n':
                sys.exit()
            case _:
                print("... No clue what you just said")



if __name__ == '__main__':
    main()