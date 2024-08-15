import random
import colorama
import time
from colorama import Fore, Back, Style
from people_lists import generated_people
import pygame

sim_complete_sound = 'audio/trill_complete.wav'
person_leaving_sound = 'audio/grumble.wav'
colorama.init(autoreset=True)

def play_sound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    

class Simulation():
    def __init__(self, people):
        self.people = people
        self.round_number = 0

    def run_simulation(self, max_rounds):
        while self.round_number < max_rounds and len(self.people) > 1:
            self.round_number += 1
            print(Fore.GREEN + f"\nRound {self.round_number} of {max_rounds} has begun!")
            for person in self.people:
                person.acted_this_round = False
                person.reacted_this_round = False
            self.action_phase()
            self.reaction_phase()
            self.evaluation_phase()
        else:
            play_sound(sim_complete_sound)
            print(Fore.WHITE + Back.CYAN + "SIMULATION COMPLETE".center(50))
            time.sleep(2)
            print("Press Enter to be taken back to main loop")
            input()

    def action_phase(self):
        print(Fore.YELLOW + "Action Phase: ")
        self.actions = {}
        for person in self.people:
            person.calc_action_potential()
            if random.random() < person.action_potential / 100:
                action = person.action()
                self.actions[person.name] = action
                print(Fore.BLUE + f"{person.name} does {action} action")
                person.action_potential = 0
                person.acted_this_round = True
            else:
                print(f"{person.name} does no action this round.")
                person.acted_this_round = False

    def reaction_phase(self):
        print(Fore.YELLOW + "Reaction Phase: ")
        self.reactions = {}
        for person in self.people:
            person.calc_reaction_potential()
            if random.random() < person.reaction_potential / 100:
                reaction = person.reaction()
                self.reactions[person.name] = reaction             
                print(Fore.MAGENTA + f"{person.name} reacts with {reaction} reaction")
                person.reaction_potential = 0
                person.reacted_this_round = True
            else:
                print(f"{person.name} doesn't react.")
                person.reacted_this_round = False

    def evaluation_phase(self):
        print(Fore.YELLOW + "Evaluation Phase: ")
        for person in self.people:
            person.calc_enjoyment(self.people, self.actions, self.reactions)
            print(f"{person.name} currently has {person.enjoyment} enjoyment")
            
            if person.leaves():
                try:               
                    play_sound(person_leaving_sound)
                except Exception as e:
                    print(f"AN ERROR OCCURED: ")
                
                print(Fore.RED + f"!!! {person.name} is removed from the simulation. !!!".center(50))
                print("* {:<20} -- Openness: {:<3}, Conscientiousness: {:<3}, Extraversion: {:<3}, Agreeableness: {:<3}, Neuroticism: {:<3}".format(person.name, person.openness, person.conscientiousness, person.extraversion, person.agreeableness, person.neuroticism))             
                self.people.remove(person)
                time.sleep(2)
                print(Fore.WHITE + Back.CYAN + "### Press Enter To Continue ###".center(50))
                input()    

                for person in self.people:        
                    print("* {:<20} -- Openness: {:<3}, Conscientiousness: {:<3}, Extraversion: {:<3}, Agreeableness: {:<3}, Neuroticism: {:<3}".format(person.name, person.openness, person.conscientiousness, person.extraversion, person.agreeableness, person.neuroticism))  
                print(Fore.WHITE + Back.CYAN + "### Press Enter Once More To Continue ###".center(50))
                input()