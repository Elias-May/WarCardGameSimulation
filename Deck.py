import random
from Card import Card, Suit


class Deck:
    def __init__(self, input_deck="default"):
        self.cards = []
        self.discarded = []
        self.new = False # probably should be "complete" instead of "new"
        if (input_deck == "default"):
            self.new = True
            self.cards = self.__gen_cards()
        else:
            if not all(isinstance(x, Card) for x in input_deck):
                raise Exception("Invalid deck passed")
            else:
                self.cards = input_deck

    def __gen_cards(self):
        cards = []
        for x in range(4):
            switcher = {
                0: Suit.CLUB,
                1: Suit.DIAMOND,
                2: Suit.HEART,
                3: Suit.SPADE
            }
            suit = switcher.get(x)
            for y in range(2,15):
                card = Card(suit, y)
                cards.append(card)
        return cards

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
            aces, self.cards = self.__get_aces(self.cards)
            for _ in range(ace_split): # TODO maybe move this into its own method
                first.append(aces.pop())
            second.extend(aces)
            while (len(self.cards) > 0):
                if (len(first) > len(second)):
                    second.append(self.cards.pop())
                else:
                    first.append(self.cards.pop())
            return [Deck(first), Deck(second)]

    # Returns a list of the aces, and the original deck without aces
    # Does not mutate.
    def __get_aces(self, deck):
        aces = []
        remove_indices = []
        for x in range(len(self.cards)):
            if self.cards[x].value == 14:
                aces.append(self.cards[x])
                remove_indices.append(x)
        #easy way to remove unwanted indexes all at once below
        deck_without_aces = [card for (index, card) in enumerate(self.cards) if index not in remove_indices]
        return aces, deck_without_aces

    def add(self, cards):
        if not all(isinstance(x, Card) for x in cards):
            raise Exception("Invalid cards passed")
        self.discarded += cards

    def pop(self, number=1):
        popped = []
        for _ in range(number):
            if(len(self.cards)<=0):
                self.shuffle()
                if(len(self.cards)<=0):
                    return []
                popped.append(self.cards.pop())
            else:
                popped.append(self.cards.pop())
        return popped
