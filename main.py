import random

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

class Deck:
    def __init__(self, input_deck="default"):
        if (input_deck == "default"):
            cards = []
            for x in range(4):
                switcher = {
                0: "Club",
                1: "Heart",
                2: "Diamond",
                3: "Spade"
                }
                suit = switcher.get(x)
                for y in range(2,15):
                    card = Card(suit, y)
                    cards.append(card)
            self.cards = cards
        else:
            if not all(isinstance(x, Card) for x in input_deck):
                raise Exception("Invalid deck passed")
            else:
                self.cards = input_deck

    def printAllVerbose(self):
        p = []
        for x in range(len(self.cards)):
            p.append(self.cards[x].getName())
        print(p, sep=",")
    def printAll(self):
        p = []
        for x in range(len(self.cards)):
            p.append(self.cards[x].value)
        print(p, sep=",")
    def shuffle(self):
        random.shuffle(self.cards)
    
cards = []
cards.append(Card("Club","14"))
cards.append(Card("Heart","13"))

d = Deck(cards)
d.printAll()
d.shuffle()
d.printAll()



#print(c.compare(c2))