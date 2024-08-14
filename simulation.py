import random
import colorama
from colorama import Fore, Back, Style
from people_lists import generated_people

colorama.init(autoreset=True)

class Simulation():
    def __init__(self, people):
        self.people = people
        self.round_number = 0

    def run_simulation(self, max_rounds):
        while self.round_number < max_rounds and len(self.people) > 1:
            self.round_number += 1
            print(Fore.GREEN + f"Round {self.round_number} of {max_rounds} has begun!")
            self.action_phase()
            self.reaction_phase()
            self.evaluation_phase()

    def action_phase(self):
        print(Fore.YELLOW + "Action Phase: ")
        for person in self.people:
            person.calc_action_potential()
            if random.random() < person.action_potential / 100:
                action = person.action()
                print(Fore.BLUE + f"{person.name} does {action} action")
                person.action_potential = 0
                person.acted_this_round = True
            else:
                print(f"{person.name} does no action this round.")
            

    def reaction_phase(self):
        print(Fore.YELLOW + "Reaction Phase: ")
        for person in self.people:
            person.calc_reaction_potential()
            if random.random() < person.reaction_potential / 100:
                reaction = person.reaction()              
                print(Fore.MAGENTA + f"{person.name} reacts with {reaction} reaction")
                person.reaction_potential = 0
                person.reacted_this_round = True
            else:
                print(f"{person.name} doesn't react.")


    def evaluation_phase(self):
        print(Fore.YELLOW + "Evaluation Phase: ")
        for person in self.people:
            person.calc_enjoyment()
            print(f"{person.name} currently has {person.enjoyment} enjoyment")
            if person.leaves():
                print(Fore.RED + f"{person.name} is removed from the simulation.")
                self.people.remove(person)