import random
from people_lists import generated_people

class Simulation():
    def __init__(self, people):
        self.people = people
        self.round_number = 0

    def run_simulation(self, max_rounds):
        if self.round_number < max_rounds and len(self.people) > 1:
            self.round_number += 1
            print(f"Round {self.round_number} of {max_rounds} has begun!")
            self.action_phase()
            self.reaction_phase()
            self.evaluation_phase()

    def action_phase(self):
        print("Action Phase: ")
        for person in self.people:
            person.calc_action_potential()
            if random.random() < person.action_potential / 100:
                action = person.action()
                print(f"{person.name} does {person.action} action")
            else:
                print(f"{person.name} does no action this round.")
            

    def reaction_phase(self):
        print("Reaction Phase: ")
        for person in self.people:
            person.calc_reaction_potential()
            if random.random() < person.reaction_potential / 100:
                reaction = person.reaction()
                
                print(f"{person.name} reacts with {person.reaction} reaction")
            else:
                print(f"{person.name} doesn't react.")


    def evaluation_phase(self):
        print("Evaluation Phase: ")
        for person in self.people:
            person.calc_enjoyment()
            print(f"{person.name} currently has {self._enjoyment} enjoyment")
            if person.leaves():
                print(f"{person.name} is removed from the simulation.")
                self.people.remove(person)