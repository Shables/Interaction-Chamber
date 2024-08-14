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
        for person in self.people:
            person.calc_action_potential()
            if random.random() < person.action_potential / 100:
                action = person.action()
            

    def reaction_phase(self):
        pass

    def evaluation_phase(self):
        pass