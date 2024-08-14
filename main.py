import os
import sys
import colorama
import random
import time
from people import People
from people_lists import generated_people
from simulation import Simulation

def main():
    while True:
        test_input = input("Hey, how did you get roped into this?.. well, since you're here.." + "\nWanna see a little experiment? (Y/N): ").strip().lower()
        match test_input:
            case 'y':
                user_choice1 = int(input("For how many rounds?: "))
                simulation = Simulation(generated_people)
                simulation.run_simulation(max_rounds=user_choice1)
            case 'n':
                sys.exit()
            case _:
                print("uhh.. I have no idea what you just said. Try again.")



if __name__ == '__main__':
    main()