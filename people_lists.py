import random
from people import People

people_names = ['Kurt', 'Avery', 'Gwyndolin', 'Frank', 'Sera', 'Cody', 'James', 'Jonathan', 'Bruce', 'Cynthia', 'Margaret', 'Cindy', 'Xi', 'Larry', 'Heather']
generated_people = []


def generate_people():
    person_number = 1
    generated_people.clear()
    unique_names = random.sample(people_names, 5)
    for name in unique_names:
        traits = [random.randint(0, 100) for _ in range(5)]
        generated_people.append(People(name, *traits))
    for person in generated_people:
        print(f"Person {person_number} Generated: \n", person)
        person_number += 1