import deck, data, player



class Round(object):
    def dealCards(self):

        "The round number"
        self.nRound = 1

        "The list of players"
        self.playersList = []


        "Dealing out cards from the deck to players"
        for i in range(data.Data.nHumanPlayers + data.Data.nCPUPlayers):
            self.playersList.append(player.Player())

        for p in self.playersList:
            for i in range(self.nRound + 2):
                p.hand.append(self.myDeck.cards[0])
                self.myDeck.cards.pop(0)




    def instantiatePiles(self):
        "Instantiating the draw and discard pile"
        "The cards that remain in deck will be the draw pile"
        self.drawPile = self.myDeck.cards

        "The card at the top of the draw pile will be one card in the discard pile"
        self.discardPile = []
        self.discardPile.append(self.drawPile[0])

        "Removing the top card from the draw pile having given it to the discard pile"
        self.drawPile.pop(0)


    def setupRound(self):

        "Setting up the deck"
        self.myDeck = deck.Deck()
        self.myDeck.build(data.Data.nDecks)

        "Shuffling the deck"
        self.myDeck.shuffleDeck()

        "Deal the cards"
        self.dealCards()

        "Instantiate the piles"
        self.instantiatePiles()



