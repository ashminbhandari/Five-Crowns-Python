import display, pygame



class Card(object):

    "Initializer for card object. Each card object has a rank and a suit"
    def __init__(self, rank, suit):

        "The rank of the card"
        self.rank = rank

        "The suit of the card"
        self.suit = suit

        "From the rank and the suit, we set up the rect for the card"
        self.cardImage = pygame.image.load("images/"+rank+suit+".png")

    "Show itself to the console"
    def show(self):
        print ("{} of {}".format(self.rank, self.suit))

    "Get the rank value"
    def getRankValue(self):
        if self.rank == "X":
            return 10

        elif self.rank == "J":
            return 11

        elif self.rank == "Q":
            return 12

        elif self.rank =="K":
            return 13

        elif self.suit != "Joker":
            return int(self.rank)

    "Get the suit  value"
    def getSuitValue(self):
        if self.suit == "Spades":
            return 0

        elif self.suit == "Clubs":
            return 1

        elif self.suit == "Diamonds":
            return 2

        elif self.suit == "Hearts":
            return 3

        elif self.suit == "Tridents":
            return 4

