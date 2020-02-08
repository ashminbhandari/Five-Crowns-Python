import card, random

class Deck(object):
    "Building decks according to how many the user wants"
    def build(self, howMany):

        "The array that holds the list of cards"
        self.cards = []

        for x in range(howMany):
            for suit in ["Spades", "Clubs", "Diamonds", "Hearts", "Tridents"]:
                for rank in ["3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]:
                    self.cards.append(card.Card(rank, suit))

            "Adding three jokers to the deck"
            self.cards.append(card.Card("1", "Joker"))
            self.cards.append(card.Card("2", "Joker"))
            self.cards.append(card.Card("3", "Joker"))

    "Print out the deck to the console"
    def print(self):
        for c in self.cards:
            c.show()

    "Shuffle the deck"
    def shuffleDeck(self):
        random.shuffle(self.cards)



