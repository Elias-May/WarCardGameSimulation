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
    def __lt__(self, other):
         return self.value < other.value

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
    def sort(self):
        self.cards.sort()
    def split(self, ace_split="default"):
        self.shuffle()
        if (ace_split == "default"):
            first = self.cards[:len(self.cards)//2]
            second = self.cards[len(self.cards)//2:]
            return [Deck(first), Deck(second)]
        else:
            if not (ace_split in range(5)):
                raise Exception("Invalid # of aces specified")
            first = []
            second = []
            aces = []
            remove_indices = []
            for x in range(len(self.cards)):
                if self.cards[x].value == 14:
                    aces.append(self.cards[x])
                    remove_indices.append(x)
            #easy way to remove unwanted indexes all at once below
            self.cards = [i for j, i in enumerate(self.cards) if j not in remove_indices]
            for x in range(ace_split):
                first.append(aces.pop())
            second.extend(aces)
            while (len(self.cards) > 0):
                if (len(first) > len(second)):
                    second.append(self.cards.pop())
                else:
                    first.append(self.cards.pop())
            return [Deck(first), Deck(second)]




#cards = []
#cards.append(Card("Club","14"))
#cards.append(Card("Heart","13"))

for x in range(10):
    d = Deck()
    #d.printAll()
    decks = d.split(4)
    decks[0].sort()
    decks[1].sort()
    decks[0].printAll()
    decks[1].printAll()
    print(len(decks[0].cards))
    print(len(decks[1].cards))
    '''if (sum([1 for card in decks[0].cards if card.value == 14])) != 4:
        raise Exception("err")
    if (sum([1 for card in decks[1].cards if card.value == 14])) != 0:
        raise Exception("err")'''
    if len(decks[0].cards) != 26:
        raise Exception("err")
    if len(decks[1].cards) != 26:
        raise Exception("err")




#print(c.compare(c2))