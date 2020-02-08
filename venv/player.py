import round

class Player(object):
    def __init__(self):
        self.hand = []

    def pickCard(self, pickingFrom, round):
        if pickingFrom == "Draw Pile":
            self.hand.append(round.drawPile[0])
            round.drawPile.pop(0)
        elif pickingFrom == "Discard Pile":
            self.hand.append(round.discardPile[0])
            round.discardPile.pop(0)

    def dropCard(self, dropCard, round):
        for c in self.hand:
            if c.rank == dropCard.rank and c.suit == dropCard.suit:
                self.hand.remove(c)
                round.discardPile.insert(0, c)