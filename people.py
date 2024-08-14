


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
        pass

    def calc_reaction_potential(self): # Calculate the reaction potential for this round
        pass

    def action(self): # Determine which action to take based on self traits
        pass
    
    def reaction(self): # Determine which reaction to take based on other actions and self traits
        pass

    def leaves(self): # Detmine if the person has stopped enjoying themselves and decided to leave
        pass