import random
from colorama import Fore, Style
from people import People

people_names = ['Kurt', 'Avery', 'Gwyndolin', 'Frank', 'Sera', 'Cody', 'James', 'Jonathan', 'Bruce', 'Cynthia', 'Margaret', 'Cindy', 'Xi', 'Larry', 'Heather', 'Scott', 'Tatiana', 'Penelope', 'Lucy', 'Mark', 'Gary', 'Marisol', 'Wyatt', 'Phoebe', 'Chloe', 'Vivienne', 'Naomi', 'Rhiannon', 'Liam', 'Xavier', 'Trisha', 'Suzette', 'Gavin', 'Diego', 'Santiago', 'Delainey', 'Greg', 'Bianca', 'Oliver']
generated_people = []


def generate_people():
    person_number = 1
    generated_people.clear()
    unique_names = random.sample(people_names, 10)
    for name in unique_names:
        traits = [random.randint(0, 100) for _ in range(5)]
        generated_people.append(People(name, *traits))
    for person in generated_people:
        print(Fore.MAGENTA + f"Person {person_number} Generated:" + Style.RESET_ALL)
        print("* {:<20} -- Openness: {:<3}, Conscientiousness: {:<3}, Extraversion: {:<3}, Agreeableness: {:<3}, Neuroticism: {:<3}".format(
            person.name, person.openness, person.conscientiousness, person.extraversion, person.agreeableness, person.neuroticism))
        person_number += 1