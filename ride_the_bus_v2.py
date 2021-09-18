import random

def ride_the_bus(gamesToPlay, numberOfCardsInPyramid):

    wins = 0
    gamesPlayed = 0
    winPercentage = 0

    while(gamesPlayed != gamesToPlay):
        
        pyramidCards = numberOfCardsInPyramid
        guess = " "
        points = 0
        arr = []
        for x in range(1,53):
            arr.append(x)

        random.shuffle(arr)
        deck = arr[:(52-pyramidCards)]
        pyramid = arr[(52-pyramidCards):]
        gamesPlayed +=1

        for x in range(0, 52-pyramidCards):
            if(pyramid[points] < 7):
                guess = "HIGHER"
            elif(pyramid[points] > 7):
                guess = "LOWER"
            else:
                choice = random.randrange(0,1)
                if(choice == 1):
                    guess = 'HIGHER'
                else:
                    guess = 'LOWER'
            if((guess == "HIGHER" and deck[0] > pyramid[0]) or (guess =="LOWER" and deck[0] < pyramid[0])):
                pyramid[points] = deck[0]
                points+=1
            else:
                pyramid[points] = deck[0]
                points = 0 
            if(points == numberOfCardsInPyramid):
                wins+=1
                break
            deck.pop(0)
    winPercentage=(wins/gamesPlayed)*100

    print("Games Played:", gamesPlayed, "Win Percentage:", winPercentage, "%")

def playGame():
    try:
        games = int(input("Enter how many games the computer should play: "))
        assert(games>0 and games<=1000000), "Invalid number of games"
    except Exception as e:
        print(e)
        exit()   
    except TypeError:
        print("Invalid type")
        exit()
    try:
        pyramid = int(input("Enter how many cards to be in the pyramid: "))
        assert(pyramid > 0 and pyramid <= 26), "Invalid number of cards in Pyramid, must be at size(deck)/2"
    except Exception as e:
        print(e)
        exit()
    except TypeError:
        print("Invalid Type")
        exit()
    
    ride_the_bus(games, pyramid)

playGame()






