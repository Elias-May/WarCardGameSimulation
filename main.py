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
        self.cards = []
        self.discarded = []
        self.new = False
        if (input_deck == "default"):
            self.new = True
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
        deck = []
        for x in range(len(self.cards)):
            deck.append(self.cards[x].value)
        dis = []
        for x in range(len(self.discarded)):
            dis.append(self.discarded[x].value)
        print("Deck", deck, sep=":")
        print("Discarded", dis, sep=":")
    def shuffle(self):
        self.cards = self.cards + self.discarded
        self.discarded = []
        random.shuffle(self.cards)
    def shuffleNonDiscarded(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
    def split(self, ace_split="default"):
        if not self.new:
            raise Exception("Cant split this deck")
        self.new = False
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
    def add(self, cards):
        if not all(isinstance(x, Card) for x in cards):
            raise Exception("Invalid cards passed")
        self.discarded += cards
    def pop(self, number=1):
        popped = []
        for x in range(number):
            if(len(self.cards)<=0):
                self.shuffle()
                if(len(self.cards)<=0):
                    return "Loss"
                popped.append(self.cards.pop())
            else:
                popped.append(self.cards.pop())
        return popped

class Game:
    def __init__(self, ace_split="default"):
        self.playing = True
        self.turns = 0
        self.p1 = ""
        self.p2 = ""
        d = Deck()
        decks = d.split(ace_split)
        self.p1 = decks[0]
        self.p2 = decks[1]
    def printAll(self):
        print("P1:")
        self.p1.printAll()
        print("P2:")
        self.p2.printAll()
    def fight(self, wager=None):
        if wager is None: 
            wager = []
        #print("wagerStart", len(wager))
        if not (self.playing):
            raise Exception("This game is over")
        card1 = self.p1.pop()
        if(card1=="Loss"):
            return "p2"  
        card1 = card1[0] 
        card2 = self.p2.pop()
        if(card2=="Loss"):
            return "p1" 
        card2 = card2[0] 
        wager.append(card1)
        wager.append(card2)
        if(card1.compare(card2)=="Less"):
            #print("wager", len(wager))
            for x in wager:
                if type(x) != Card:
                    raise Exception("Card in wager error")
            self.p2.add(wager)
            return "ok"
        if(card1.compare(card2)=="Greater"):
            #print("wager", len(wager))
            self.p1.add(wager)
            for x in wager:
                if type(x) != Card:
                    raise Exception("Card in wager error")
            return "ok"
        if(card1.compare(card2)=="Equal"):
            return self.war(wager)
    def war(self, wager):
        #print("war")
        p1wager = self.p1.pop(3)
        if(p1wager=="Loss"):
            return "p2"
        p2wager = self.p2.pop(3)
        if(p2wager=="Loss"):
            return "p1"
        wager += p1wager
        wager += p2wager
        return self.fight(wager)
    def playAll(self):
        status = 'ok'
        while(status == 'ok'):
            #g.printAll()
            self.turns += 1
            status = self.fight()
        return [status, self.turns]


g = Game()
#g.printAll()
##print(g.fight())
#g.printAll()
print(g.playAll())
