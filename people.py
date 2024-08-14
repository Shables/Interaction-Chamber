import random


class People():
    def __init__(self, name, openness=0, conscientiousness=0, extraversion=0, agreeableness=0, neuroticism=0):
        self.name = name
        self._openness = openness
        self._conscientiousness = conscientiousness
        self._extraversion = extraversion
        self._agreeableness = agreeableness
        self._neuroticism = neuroticism
        self._action_potential = 0
        self._reaction_potential = 0
        self._enjoyment = 100 # Starts with full enjoyment

    def __str__(self):
        return f"Name = {self.name}, Openness = {self._openness}, Conscientiousness = {self._conscientiousness}, Extraversion = {self._extraversion}, Agreeableness = {self._agreeableness}, Neuroticism = {self._neuroticism}."

    @property
    def openness(self):
        return self._openness
    
    @openness.setter
    def openness(self, value):
        self._openness = (min(value, 100))

    @property
    def conscientiousness(self):
        return self._conscientiousness
    
    @conscientiousness.setter
    def conscientiousness(self, value):
        self._conscientiousness = (min(value, 100))

    @property
    def extraversion(self):
        return self._extraversion
    
    @extraversion.setter
    def extraversion(self, value):
        self._extraversion = (min(value, 100))

    @property
    def agreeableness(self):
        return self._agreeableness
    
    @agreeableness.setter
    def agreeableness(self, value):
        self._agreeableness = (min(value, 100))

    @property
    def neuroticism(self):
        return self._neuroticism
    
    @neuroticism.setter
    def neuroticism(self, value):
        self._neuroticism = (min(value, 100))

    @property
    def action_potential(self):
        return self._action_potential
    
    @action_potential.setter
    def action_potential(self, value):
        self._action_potential = (min(value, 100))

    @property
    def reaction_potential(self):
        return self._reaction_potential
    
    @reaction_potential.setter
    def reaction_potential(self, value):
        self._reaction_potential = (min(value, 100))

    @property
    def enjoyment(self):
        return self._enjoyment
    
    @enjoyment.setter
    def enjoyment(self, value):
        self._enjoyment = (min(value, 100))


    def calc_action_potential(self): # Calculate the action potential for this round
        self.action_potential = ((self.openness * 1.0) // 10) + ((self.conscientiousness * 1.2) // 10) + ((self.extraversion * 1.5) // 10) + ((self.agreeableness * 0.8) // 10) + ((self.neuroticism * 1.3) // 10)

    def calc_reaction_potential(self): # Calculate the reaction potential for this round
        self.reaction_potential = ((self.openness * 1.3) // 10) + ((self.conscientiousness * 1.5) // 10) + ((self.extraversion * 0.8) // 10) + ((self.agreeableness * 1.0) // 10) + ((self.neuroticism * 1.2) // 10)


    def calc_enjoyment(self):
        pass # We want this function to check if the person either made an action or reaction in the past round, if not, loses between 5-10 enjoyment points
             # For every rude action in the round, loses between 5-10 points if any trait except neurotic is their highest trait
             # Conversely, for every not rude action in the round, loses between 1-5 points if neurotic is their highest trait
             # Finally, for every action or reaction taken -- that person gains 10 enjoyment points.

    def action(self): # Determine which action to take based on self traits
        actions = ['rude', 'joke', 'compliment', 'flirt', 'silly']
        weights = [
            self.neuroticism,
            self.conscientiousness,
            self.agreeableness,
            self.extraversion,
            self.openness
        ]
        return random.choices(actions, weights=weights)[0]

    def reaction(self): # Determine which reaction to take based on other actions and self traits
        reactions = ['laugh', 'smile', 'agree', 'disagree', 'scowl']
        weights = [
            self.openness,
            self.extraversion,
            self.agreeableness,
            self.conscientiousness,
            self.neuroticism
        ]
        return random.choices(reactions, weights=weights)[0]

    def leaves(self): # Determine if the person has stopped enjoying themselves and decided to leave
        if self._enjoyment <= 0:
            print(f"{self.name} has stopped enjoying themselves and has decided to leave...")
        