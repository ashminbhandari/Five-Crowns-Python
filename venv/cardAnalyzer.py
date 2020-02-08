class cardAnalyzer(object):
    def __init__(self, hand, round):

        "The card in a player's hand will be represented in a matrix, to check for runs and books"
        self.theMatrix = [[0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0]]

        "The collection of cards to analyze, jokers and wildcards will be left out"
        "We will work with the count of the jokers and wildcards rather than the cards themselves"
        self.collection = []

        "The joker count in the provided set of cards"
        self.jokerCount = 0

        "The wildcard count in the provided set of cards"
        self.wildcardCount = 0

        "Only adding cards that are not jokers or wildcard to the matrix"
        "If the card is a joker, adding to the joker count"
        "If the card is a wildcard, adding to the wildcard count"
        for c in hand:
            if c.suit != "Joker" and c.rank != round.nRound + 2:
                self.collection.append(c)
                self.theMatrix[c.getSuitValue()][c.getRankValue()-3] = self.theMatrix[c.getSuitValue()][c.getRankValue()-3] + 1

            if c.suit == "Joker":
                self.jokerCount = self.jokerCount + 1

            if c.rank == round.nRound + 2:
                self.wildcardCount = self.wildcardCount + 1

    "Finding horizontal meld to the left and to the right from the provided index"
    def findHorizontalMeld(self, xTotal, xMeld, i, j):
        "Setting a local jIndex variable matching 'j'"
        jIndex = j

        "Do while a 0 is not hit, moving towards the right. A 0 is hit means taht the run ends there"
        while jIndex < len(self.theMatrix[i]):

            "If hit 0, break out of the loop, we hit the end of a run"
            if self.theMatrix[i][jIndex] == 0:
                break

            "If not, add 1 to the size of the horizontal meld, aka run"
            xTotal = xTotal + 1

            "Append the indexes of the horizontal meld to xMeld as we find them"
            xMeld.append((i, jIndex))

            "Increase the jIndex so as to move towards the right"
            jIndex = jIndex + 1

        "We must also search towards the left from the index that was provided"
        "Only decrease jIndex for a search towards the left if the jIndex is greater than 0, otherwise, we means we are at the right edge of the matrix"
        if (j > 0):
            jIndex = j - 1

        "Do while a 0 is not hit, moving towards the left"
        while jIndex >= 0:

            "If a 0 was found, that means we hit the end of the run towards the left"
            if self.theMatrix[i][jIndex] == 0:
                break;

            "Adding up to the size of the meld that we are currently finding"
            xTotal = xTotal + 1

            "Append the indexes of the horizontal meld to xMeld"
            xMeld.append([i, jIndex])

            "Decrease the jIndex so as to move towards the left"
            jIndex = jIndex - 1

    "Finding the vertical meld, up and down from the provided index"
    def findVerticalMeld(self, yTotal, yMeld, i , j):
        "Starting at iIndex of 0"
        iIndex = 0

        "Move towards the vertical end of the matrix, add up the values of the matrix along the vertical"
        "This way we look for books in the hand, we get the size of the books as well the indexes"
        while(iIndex < len(self.theMatrix)):
            if self.theMatrix[iIndex][j] >= 1:
                yTotal = yTotal + self.theMatrix[iIndex][j]
                yMeld.append([iIndex,j])

            "Increase the iIndex so as to move towards the vertical end"
            iIndex = iIndex +  1

    "Converts matrix indexes to actual card values"
    def matrixIndexToCardValue(self, i, j):

        "The string that is to be returned"
        cardValue = ""

        "Adding 3 to the matrix index to get the appropriate string representation of the rank"
        if j + 3 == 10:
            cardValue = cardValue + "X"

        elif j + 3 == 11:
            cardValue = cardValue + "J"

        elif j + 3 == 12:
            cardValue = cardValue + "Q"

        elif j + 3 == 13:
            cardValue = cardValue + "K"

        else:
            cardValue = cardValue + j + 3


        "Getting the suit from the iIndex provided"
        if i == 0:
            cardValue = cardValue + "Spades"

        elif i == 1:
            cardValue = cardValue + "Clubs"

        elif i == 2:
            cardValue = cardValue + "Diamonds"

        elif i == 3:
            cardValue = cardValue + "Hearts"

        elif i == 4:
            cardValue = cardValue + "Tridents"

        return cardValue


    "Update matrix"
    def updateMatrix(self, meld, isY):
        "Iterate through the coordinates, which are for a meld, provided as the argument"
        for m in meld:

            "If the matrix value at that index is greater than or equal to 1, that means a decrement can be done then proceed"
            if self.theMatrix[m[0]][m[1]] >= 1:

                "If the meld coordinates provided are for a book"
                if isY:

                    "Set the matrix value at that index to 0"
                    self.theMatrix[m[0]][m[1]] = 0

                    "Getting the actual string values of the card from the matrix indexes"
                    self.booksMade.append(self.matrixIndexToCardValue((m[0], m[1])))

            else:
                self.theMatrix[m[0]][m[1]] = self.theMatrix[m[0]][m[1]] - 1

                self.runsMade.append(self.matrixIndexToCardValue([m[0]], m[1]))

    "First pass through the matrix"
    def passThrough(self, i, j, passNo):
        print(self.theMatrix)
        "Setting up a variable to hold the size of the run from the given index"
        xTotal = 0

        "Setting up a list variable to hold the actual indexes of the run found"
        xMeld = []

        "Finding the horizontal meld from the given index"
        self.findHorizontalMeld(xTotal, xMeld, i, j)

        "Setting up a variable to hold the size of a book from the given index"
        yTotal = 0

        "Setting up a list variable to hold the actual indexes of the book found"
        yMeld = []

        "Finding the vertical meld from the given index"
        self.findVerticalMeld(yTotal, yMeld, i, j)

        "This is where the prioritizing takes place, if the pass number is first"
        "If the xTotal is smaller than yTotal and itt is a meld, then it is to be given the priority"
        "After that we remove that meld from the matrix, a meld has been successfully identified"
        if passNo == 1:
            if xTotal < yTotal and xTotal >= 3:
                self.updateMatrix(xMeld, False)

            "Else, if the yTotal is smaller instead, we are to give it the priority"
            if yTotal < xTotal and yTotal >= 3:
                self.updateMatrix(yMeld, True)

        if passNo == 2:
            "Clear the indexes in the matrix if a run, else if a book too"
            if xTotal >= 3:
                self.updateMatrix(xMeld, False)

            elif yTotal >= 3:
                self.updateMatrix(yMeld, True)



    def passIII(self):
        "Only go through the mess if there are special cards to expend"
        if self.jokerCount + self.wildcardCount > 0:
            "The indexes at which the special cards are needed"
            needSpecialCards = []

            "List of consecutive indexes that need special card"
            temp = []

            "Iterate through all the horizontals along the matrix, and get indexes that need special cards"
            "0 through 4, the coordinates along the vertical"
            for i in range(5):

                "j to be incremented, it is the index along the horizontal"
                j = 0

                while j != len(self.theMatrix[i]):

                    "If joker is needed, that means an empty spot in the matrix, append it to needJookers"
                    if self.theMatrix[i][j] == 0:
                        temp.append((i,j))


                    elif self.theMatrix[i][j] == 1:
                        "If along this line we hit a 1, that means we stoped needing special cards from here on out"
                        needSpecialCards.append(temp)

                        "Clearing the temp list"
                        temp.clear();

                    "Incrementing j along the horizontal"
                    j = j + 1

                    "If we hit the horizontal end of the matrix"
                    if j == len(self.theMatrix[i]):

                        "Clear the temp list"
                        temp.clear()

            "Sorting the needSpecialCards list by length of sub-lists"
            needSpecialCards.sort(key=len)

    def matrixSum(self):
        "Initialize sum at 0"
        matrixSum = 0

        "Iterate through and add up the value at matrix indexes to the matrix sum above"
        for i in range(len(self.theMatrix)):
            for j in range(len(self.theMatrix[i])):
                matrixSum = matrixSum + self.theMatrix[i][j]

        "Return the matrix sum"
        return matrixSum

    def checkMatrix(self):

        "Set a variable to hold the matrix sum at the beginning"
        prevMatrixSum = 0

        "While loop until we don't get any changes int the matrix sum having passed through"
        "all indexes of the matrix with a for loop"
        while(prevMatrixSum != self.matrixSum()):

            "Storing the matrix sum at the beginning of the run through"
            prevMatrixSum = self.matrixSum()

            "Running throuhg all the indexes and applying passI to them"
            for i in range(len(self.theMatrix)):
                for j in range(len(self.theMatrix[i])):
                    self.passThrough(i,j,1)

        "While loop until we don't get any changes in the matrix sum having passed through"
        "all the indexes of the matrix with a for loop, apply passII"
        while(prevMatrixSum != self.matrixSum()):

            "Storing the matrix sum at the beginning of the run through"
            prevMatrixSum = matrixSum()

            "Running throuhg all the indexes and applying passII to them"
            for i in range(len(self.theMatrix)):
                for j in range(len(self.theMatrix[i])):
                    self.passThrough(i,j,2)

        "At the end of the run throughs, if the matrix sum is now 0, the user can go out"
        if self.matrixSum() == 0:
            return True

        return False









