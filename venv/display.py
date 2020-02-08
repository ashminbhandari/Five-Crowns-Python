import sys, pygame, pygame.mixer
import data
import card
import deck
import round
import cardAnalyzer


class ScreenDisplay(object):
    "Setting the screen size"
    screenSize = width, height = 2048, 1536

    "Background image path"
    bgImage = "images/bg.jpg"

    "Name of the game to be displayed"
    gameName = "Five Crowns"

    "Font to be used in the game --> OstrichSans-Heavy"
    font = "fonts/OstrichSans-Heavy.otf"

    "Background music to be used in the game"
    bgMusic = "sounds/Aphex Twin - Stone in Focus.mp3"

    "Deck image"
    deckImage = "images/deck.png"

    "Click sound"
    clickSound = "sounds/click.wav"

    "Will hold the images of the cards"
    cardImages = []

    "Loop for main menu, true at first"
    inMainMenu = True

    "Loop for setting up players, false at first"
    inSetup = False

    "The main round loop"
    inRound = False

    def mainMenuLoop(self):
        "First, we set up the surface"
        "Initializing pygame"
        pygame.init()

        "Setting up the screen"
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        "Setting up the background music"
        pygame.mixer.init()
        pygame.mixer.music.load(self.bgMusic)
        pygame.mixer.music.play(-1)

        "Setting the game name as caption"
        pygame.display.set_caption(self.gameName)

        "Loading up and converting the background image so as to be able to display it"
        bgImage = pygame.image.load(self.bgImage).convert()

        "So as to be able to display the 'Five Crowns' title at the center at the top of the screen"
        fiveCrownsFont = pygame.font.Font(self.font, 150)
        fiveCrownsText = fiveCrownsFont.render("Five Crowns", True, (0,0,0))
        fiveCrownsTextRect = fiveCrownsText.get_rect()
        fiveCrownsTextRect.centerx = bgImage.get_rect().centerx - 60
        fiveCrownsTextRect.y = 20

        "So as to be able to display the 'start game' button to the screen"
        startGameFont = pygame.font.Font(self.font, 75)
        startGameText = startGameFont.render("Start Game", True, (0, 0, 0))
        startGameTextRect = startGameText.get_rect()

        "So as to be ablt to display the 'exit game' button to the screen"
        exitGameFont = pygame.font.Font(self.font, 75)
        exitGameText = exitGameFont.render("Exit", True, (0, 0, 0))
        exitGameTextRect = exitGameText.get_rect()

        "Blitting out the game title and the buttons to the screen"
        screen.blit(bgImage, (0, 0))
        screen.blit(fiveCrownsText, fiveCrownsTextRect)
        startGameButton = screen.blit(startGameText, (bgImage.get_rect().centery + 60, bgImage.get_rect().centerx - 550))
        exitGameButton = screen.blit(exitGameText, (bgImage.get_rect().centery + 150, bgImage.get_rect().centerx - 450))

        "Go into the main menu loop, wait for events to happen and react accordingly"
        while (self.inMainMenu):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if exitGameButton.collidepoint(mousePos):
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime = 600)
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mousePos = pygame.mouse.get_pos()
                    if startGameButton.collidepoint(mousePos):
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime = 600)
                        self.inMainMenu = False
                        self.inSetup = True
            pygame.display.update()

    def setup(self):
            "Setting up the screen"
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
            "Loading up and converting the background image so as to be able to display it"
            bgImage = pygame.image.load(self.bgImage).convert()

            "Blitting out the game title and the buttons to the screen"
            screen.blit(bgImage, (0, 0))

            "Loading up the fonts"
            menuFont = pygame.font.Font(self.font, 70)
            buttonFont = pygame.font.Font(self.font, 100)

            "So as to be ablt to display the 'exit game' button to the screen"
            exitGameText = buttonFont.render("X", True, (0, 0, 0))
            exitGameTextRect = exitGameText.get_rect()
            exitGameTextRect.centerx = bgImage.get_rect().centerx + 860
            exitGameButton = screen.blit(exitGameText, exitGameTextRect)

            "Increase button text"
            increaseText = buttonFont.render("+", True, (0,0,0))

            "Decrease button text"
            decreaseText = buttonFont.render("-", True, (0, 0, 0))

            "Creating an increase player and increase CPU player button using increase text"
            increasePlayersButton = screen.blit(increaseText, (bgImage.get_rect().centery - 155, bgImage.get_rect().centerx - 650))
            increaseCPUPlayersButton = screen.blit(increaseText, (bgImage.get_rect().centery + 100, bgImage.get_rect().centerx - 650))

            "Creatin a decrease player and decrease CPU player button using decrease text"
            decreasePlayersButton = screen.blit(decreaseText, (bgImage.get_rect().centery - 155, bgImage.get_rect().centerx - 495))
            decreaseCPUPlayersButton = screen.blit(decreaseText, (bgImage.get_rect().centery + 100, bgImage.get_rect().centerx - 495))

            "Increase and decrease number of deck button"
            increaseDeckButton = screen.blit(increaseText, (bgImage.get_rect().centery + 350, bgImage.get_rect().centerx - 650))
            decreaseDeckButton = screen.blit(decreaseText, (bgImage.get_rect().centery + 355, bgImage.get_rect().centerx - 495))

            "Next page button"
            nextPageText = menuFont.render("NEXT", True, (0,0,0))
            nextPageButton = screen.blit(nextPageText, (bgImage.get_rect().centery + 1050, bgImage.get_rect().centerx - 30))

            while(self.inSetup):
                "Getting all the events that happen on the screen"
                events = pygame.event.get()

                "For events that happen"
                for event in events:

                    "Listening for quit events"
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    "Listening for mouse presses"
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                        "Getting the mouse's position"
                        mousePos = pygame.mouse.get_pos()

                        "If the exit game button was pressed, then exit"
                        if exitGameButton.collidepoint(mousePos):
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime = 600)
                            pygame.quit()
                            sys.exit()

                        "If the increase human players button was pressed, move forward accordingly"
                        if increasePlayersButton.collidepoint(mousePos):

                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime = 600)

                            "Only add if the total of the two types of players doesn't exeed 7"
                            if((data.Data.nHumanPlayers + data.Data.nCPUPlayers >= 2 and data.Data.nHumanPlayers + data.Data.nCPUPlayers < 7 and data.Data.nHumanPlayers >= 0)):
                                data.Data.nHumanPlayers = data.Data.nHumanPlayers + 1

                        "If the decrease human players button was pressed, move forward accordingly"
                        if decreasePlayersButton.collidepoint(mousePos):

                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime = 600)

                            "Only decrease within the range as given below"
                            if((data.Data.nHumanPlayers + data.Data.nCPUPlayers > 2 and data.Data.nHumanPlayers + data.Data.nCPUPlayers <= 7 and data.Data.nHumanPlayers >= 1)):
                                data.Data.nHumanPlayers = data.Data.nHumanPlayers - 1

                        "If the increase CPU playerse button was pressed"
                        if increaseCPUPlayersButton.collidepoint(mousePos):

                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            "Only add if the total of the two types of players doesn't exeed 7"
                            if ((data.Data.nHumanPlayers + data.Data.nCPUPlayers >= 2 and data.Data.nHumanPlayers + data.Data.nCPUPlayers < 7 and data.Data.nCPUPlayers >= 0)):
                                data.Data.nCPUPlayers = data.Data.nCPUPlayers + 1

                        "If the decrease CPU players button was pressed"
                        if decreaseCPUPlayersButton.collidepoint(mousePos):

                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            "Only decrease within the range as given below"
                            if ((data.Data.nHumanPlayers + data.Data.nCPUPlayers > 2 and data.Data.nHumanPlayers + data.Data.nCPUPlayers <= 7) and data.Data.nCPUPlayers >= 1):
                                data.Data.nCPUPlayers = data.Data.nCPUPlayers - 1

                        "If the increase deck button was clicked"
                        if increaseDeckButton.collidepoint(mousePos):
                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            "Increase the deck size, only allow 2 to 4 decks"
                            if(data.Data.nDecks >= 1 and data.Data.nDecks <= 3):
                                data.Data.nDecks = data.Data.nDecks + 1

                        "If the dcrease deck button was clicked"
                        if decreaseDeckButton.collidepoint(mousePos):
                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            "Decrease the deck size, only allow 2 to 4 decks"
                            if (data.Data.nDecks >= 2 and data.Data.nDecks <= 4):
                                data.Data.nDecks = data.Data.nDecks - 1

                        "If the next page button was clicked"
                        if nextPageButton.collidepoint(mousePos):
                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            "Change inSetup bool to false so as to get out of this while loop and the in round bool to true"
                            self.inSetup = False
                            self.inRound = True


                "Blitting the background here causes a cool effect"
                screen.blit(bgImage, (0, 0))

                "Number of human players prompt"
                humanText = menuFont.render("Human", True, (0, 0, 0))
                screen.blit(humanText, (bgImage.get_rect().centery - 200, bgImage.get_rect().centerx - 700))

                "AI prompt"
                AIText = menuFont.render("AI", True, (0, 0, 0))
                screen.blit(AIText, (bgImage.get_rect().centery + 100, bgImage.get_rect().centerx - 700))

                "Deck prompt"
                increaseDeckText = menuFont.render("DECK", True, (0, 0, 0))
                screen.blit(increaseDeckText,  (bgImage.get_rect().centery + 330, bgImage.get_rect().centerx - 700))

                "Updating the  number of human players"
                nPlayersText = menuFont.render("{}".format(data.Data.nHumanPlayers), True, (0, 0, 0))
                screen.blit(nPlayersText, (bgImage.get_rect().centery - 145, bgImage.get_rect().centerx - 550))

                "Updating the number of CPU players"
                nCPUPlayersText = menuFont.render("{}".format(data.Data.nCPUPlayers), True, (0, 0, 0))
                screen.blit(nCPUPlayersText, (bgImage.get_rect().centery + 110, bgImage.get_rect().centerx - 550))

                "Updating the number of decks"
                nDecksText = menuFont.render("{}".format(data.Data.nDecks), True, (0,0,0))
                screen.blit(nDecksText, (bgImage.get_rect().centery + 360, bgImage.get_rect().centerx - 550))


                "Adding the increase, decrease, exit and next buttons back in"
                "Increase human players"
                screen.blit(increaseText, (bgImage.get_rect().centery - 155, bgImage.get_rect().centerx - 650))

                "Increase AI players"
                screen.blit(increaseText, (bgImage.get_rect().centery + 100, bgImage.get_rect().centerx - 650))

                "Increase number of decks to be used"
                screen.blit(increaseText, (bgImage.get_rect().centery + 350, bgImage.get_rect().centerx - 650))

                "Decrease deck button"
                screen.blit(decreaseText, (bgImage.get_rect().centery + 355, bgImage.get_rect().centerx - 495))

                "Decrease human players button"
                screen.blit(decreaseText, (bgImage.get_rect().centery - 155, bgImage.get_rect().centerx - 495))

                "Decrease CPU players button"
                screen.blit(decreaseText, (bgImage.get_rect().centery + 100, bgImage.get_rect().centerx - 495))

                "Next page button"
                screen.blit(nextPageText, (bgImage.get_rect().centery + 1050, bgImage.get_rect().centerx - 30))

                "Exit game button"
                screen.blit(exitGameText, exitGameTextRect)

                "Update the display"
                pygame.display.update()


    def round(self):
        "Setting up the screen"
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        "Loading up and converting the background image so as to be able to display it"
        bgImage = pygame.image.load(self.bgImage).convert()
        screen.blit(bgImage, (0, 0))

        "Setting up the round"
        theRound = round.Round()
        theRound.setupRound()

        "The font to use, size 70"
        theFont = pygame.font.Font(self.font, 70)

        "Smaller display font"
        smallFont = pygame.font.Font(self.font, 40)


        "Whose turn is it at first"
        whoseTurn = 0

        "Which card is to be dropped"
        dropCard = ""

        "Which pile to pick from"
        pickingFrom = ""

        "Printing out the players cards"
        while(self.inRound):
            "The player count"
            i = 1

            "The x-coordinate to draw in, starting at 20"
            x = 20

            "The y-coordinate to start drawing at"
            y = 0

            "A list of button and card tuples"
            buttonCardPlayerTupleList = []

            for p in theRound.playersList:
                screen.blit(smallFont.render("Player {}".format(i), True, (0, 0, 0)), (x,y))
                x = x + 200
                for c in p.hand:
                    theButton = screen.blit(c.cardImage, (x,y))
                    buttonCardPlayerTuple = (theButton, c, i)
                    buttonCardPlayerTupleList.append(buttonCardPlayerTuple)
                    x = x + 80
                x = 20
                i = i + 1
                y = y + 155

            "The x-coordinate to drawing the draw pile at"
            x = 1700

            "The y-coordinate to drawing the draw pile at"
            y = 450

            "Drawing the draw pile"
            deckImage = pygame.image.load(self.deckImage).convert()
            drawPileButton = screen.blit(deckImage, (x,y))

            "Drawing draw pile text"
            screen.blit(smallFont.render("Draw pile", True, (0, 0, 0)), (x, y - 50))

            "Y-coordinate to draw the discard pile at"
            y = 700

            "Drawing the discard pile"
            discardPileButton = screen.blit(theRound.discardPile[0].cardImage, (x, y))

            "Draing discard pile text"
            screen.blit(smallFont.render("Discard pile", True, (0, 0, 0)), (x, y - 50))

            "Y-coordinate to darw the picked card at"
            y = 200

            "Drawing out the discard pile text"
            screen.blit(smallFont.render("Drop card", True, (0, 0, 0)), (x, y - 50))

            "Drawing out the go button"
            screen.blit(smallFont.render("Player {}'s turn".format(whoseTurn + 1), True, (0, 0, 0)), (1700, -1))

            "Drawing out the go button"
            goButton = screen.blit(smallFont.render("GO", True, (0, 0, 0)), (1700, 1000))



            "For events that happen"
            for event in pygame.event.get():

                "Listening for quit events"
                if event.type == pygame.QUIT:
                    pygame.quit()

                "Listening for mouse presses"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    "Getting the mouse's position"
                    mousePos = pygame.mouse.get_pos()

                    for BCPT in buttonCardPlayerTupleList:
                        if(BCPT[0].collidepoint(mousePos) and BCPT[2] == whoseTurn + 1):
                            "Make a sound"
                            pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                            dropCard = BCPT[1]

                            screen.blit(BCPT[1].cardImage, (x, y))

                    if discardPileButton.collidepoint(mousePos):
                        "Make a sound"
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                        "Blitting the background"
                        screen.blit(bgImage, (0, 0))

                        "The selection arrow which denotes which pile you are picking from"
                        selectionArrow = screen.blit(theFont.render("*", True, (0, 0, 0)), (1600, 700))

                        "Blitting the drop card, only if it has already been se"
                        if(dropCard != ""):
                            screen.blit(dropCard.cardImage, (1700, 200))

                        pickingFrom = "Discard Pile"

                    if drawPileButton.collidepoint(mousePos):
                        "Make a sound"
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                        "Blitting the background"
                        screen.blit(bgImage, (0, 0))

                        "The selection arrow which denotes which pile you are picking from"
                        selectionArrow = screen.blit(theFont.render("*", True, (0, 0, 0)), (1600, 450))

                        "Blitting the drop card only if it has been set"
                        if(dropCard != ""):
                            screen.blit(dropCard.cardImage, (1700,200))

                        pickingFrom = "Draw Pile"

                    if goButton.collidepoint(mousePos):
                        "Make a sound"
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.clickSound), maxtime=600)

                        "Picking the card from the chose pile"
                        theRound.playersList[whoseTurn].pickCard(pickingFrom, theRound)

                        if(dropCard != ""):
                            theRound.playersList[whoseTurn].dropCard(dropCard,theRound)

                        screen.blit(bgImage, (0,0))

                        "The next players turn"
                        whoseTurn = whoseTurn + 1

                        "If all players took turn, player 1's turn"
                        if (data.Data.nCPUPlayers + data.Data.nHumanPlayers == whoseTurn):
                            whoseTurn = 0

                        c = cardAnalyzer.cardAnalyzer(theRound.playersList[whoseTurn].hand, theRound)

                        print(c.checkMatrix())



                pygame.display.update()


myDisplay = ScreenDisplay()
myDisplay.mainMenuLoop()
myDisplay.setup()
myDisplay.round()













