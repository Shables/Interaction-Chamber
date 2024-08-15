        # Checks if person made an action/reaction in the last round
        if not self.acted_this_round and not self.reacted_this_round:
            self.enjoyment -= random.randint(5, 15)

        if self.acted_this_round:
            self.enjoyment += random.randint(2, 8)
            if People.action(self) == 'rude':
                highest_trait = max(self.openness, self.conscientiousness, self.extraversion, self.agreeableness, self.neuroticism)
                if highest_trait != self.neuroticism:
                    self.enjoyment -= random.randint(5, 15)
            elif self.neuroticism == max(self.openness, self.conscientiousness, self.extraversion, self.agreeableness, self.neuroticism):
                self.enjoyment += random.randint(2, 8)

        if self.reacted_this_round:
            self.enjoyment += random.randint(2, 8)
            if People.reaction(self) == 'scowl':
                highest_trait = max(self.openness, self.conscientiousness, self.extraversion, self.agreeableness, self.neuroticism)
                if highest_trait != self.neuroticism:
                    self.enjoyment -= random.randint(5, 15)
            elif self.neuroticism == max(self.openness, self.conscientiousness, self.extraversion, self.agreeableness, self.neuroticism):
                self.enjoyment += random.randint(2, 8)

        self.enjoyment = max(0, min(self.enjoyment, 100))

        # Reset Flags
        self.acted_this_round = False
        self.reacted_this_round = False