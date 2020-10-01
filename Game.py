from Deck import Deck
from Card import Card

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
