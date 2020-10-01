#Cards are given values from 2 to 14, where 14 is the ace
class Card:
    def __init__(self, suit, value):
        if suit not in ["Club","Heart","Diamond","Spade"]:
            raise Exception("Invalid card suite")
        self.suit = suit
        self.value = int(value)
    def getName(self):
        switcher = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace"
        }
        if (self.value in range(11,15)):
            named = switcher.get(self.value)
        else:
            named = str(self.value)
        return named + " of " + self.suit
    def compare(self, Card):
        if self.value == Card.value:
            return "Equal"
        elif self.value > Card.value:
            return "Greater"
        elif self.value < Card.value:
            return "Less"
    def __lt__(self, other):
         return self.value < other.value