import os
import sys
import colorama
from colorama import Fore, Back, Style
import random
import time
from people import People
from people_lists import generate_people, generated_people
from simulation import Simulation

colorama.init(autoreset=True)

title_art = """

 ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███   ▄▄▄       ▄████▄  ▄▄▄█████▓ ██▓ ▒█████   ███▄    █ 
▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒       ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ▒ ░   ░   ░ ░   ░         ░     ░░   ░   ░   ▒   ░          ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ 
 ░           ░             ░  ░   ░           ░  ░░ ░                ░      ░ ░           ░ 
                                                  ░                                         
 ▄████▄   ██░ ██  ▄▄▄       ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███                                
▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒                              
▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒                              
▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄                                
▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒                              
░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░                              
  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░                              
░         ░  ░░ ░  ░   ▒   ░      ░    ░    ░    ░     ░░   ░                               
░ ░       ░  ░  ░      ░  ░       ░    ░         ░  ░   ░                                   
░                                           ░                                               

"""


def main():
    while True:
        print(title_art)
        time.sleep(2)
        
        while True:
            test_input = input(Fore.CYAN + "\n\n\nHey, how did you get roped into this?.. well, since you're here.." + "\nWanna see a little experiment? (Y/N): \n" + Style.RESET_ALL).strip().lower()
            if test_input in ['y', 'n']:
                break    
            print("uhh.. I have no idea what you just said. Try again.")
                        
        match test_input:
            case 'y':
                while True:
                    generate_people()
                    while True:
                        user_choice3 = input(Fore.CYAN + "Are you happy with this assortment of people? (Y/N): \n" + Style.RESET_ALL).lower()
                        if user_choice3 in ['y', 'n']:
                            break
                        print("Either input a 'Y' or an 'N'")
                    
                    if user_choice3 == 'n':
                        continue
                        
                    user_choice1 = int(input(Fore.CYAN + "For how many rounds?: \n" + Style.RESET_ALL))
                    simulation = Simulation(generated_people)
                    simulation.run_simulation(max_rounds=user_choice1)
                    break           
            case 'n':
                sys.exit() 
       
        while True:                     
            user_choice2 = input(Fore.CYAN + "\n\n\nHey, wanna do that again? (Y/N): \n" + Style.RESET_ALL).lower()
            if user_choice2 in ['y', 'n']:
                break
            print("... No clue what you just said")

        if user_choice2 == 'n':
            sys.exit()
                


if __name__ == '__main__':
    main()