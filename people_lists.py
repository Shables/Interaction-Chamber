import random
from people import People

people_names = ['Kurt', 'Avery', 'Gwyndolin', 'Frank', 'Sera', 'Cody', 'James', 'Jonathan', 'Bruce', 'Cynthia', 'Margaret', 'Cindy', 'Xi', 'Larry', 'Heather']

generated_people = []


for _ in range(5):
    name = random.choice(people_names)
    traits = [random.randint(0, 100) for _ in range(5)]
    generated_people.append(People(name, *traits))

print(generated_people)
