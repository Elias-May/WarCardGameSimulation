from Deck import Deck
from Card import Card

class Game:
    def __init__(self, ace_split="default"):
        self.playing = True
        self.turns = 0
        d = Deck()
        self.p1_deck, self.p2_deck = d.split(ace_split)

    def printAll(self):
        print("P1:")
        self.p1_deck.printAll()
        print("P2:")
        self.p2_deck.printAll()

    def playAll(self):
        status = 'ok'
        while(status == 'ok'):
            self.turns += 1
            status = self.fight()
        return [status, self.turns]

    def fight(self, wager=None):
        if wager is None: 
            wager = []
        if not (self.playing):
            raise Exception("This game is over")

        # Draw the first card from each deck. If we can't, then the other player won.
        card1 = self.p1_deck.pop()
        if(card1==[]):
            return "p2"  
        card1 = card1[0] 
        card2 = self.p2_deck.pop()
        if(card2==[]):
            return "p1" 
        card2 = card2[0]

        wager.append(card1)
        wager.append(card2)

        if(card1.compare(card2)=="Less"):
            self.p2_deck.add(wager)
            return "ok"
        if(card1.compare(card2)=="Greater"):
            self.p1_deck.add(wager)
            return "ok"
        if(card1.compare(card2)=="Equal"):
            wager = self.war(wager)
            return self.fight(wager)

    def war(self, wager):
        p1wager = self.p1_deck.pop(3)
        p2wager = self.p2_deck.pop(3)
        wager += p1wager
        wager += p2wager
        return wager
