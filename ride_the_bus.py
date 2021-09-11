import random

def ride_the_bus(gamesToPlay, numberOfCardsInPyramid):
    try:
        assert(gamesToPlay>0 and gamesToPlay<=1000000), "Invalid number of games"
    except Exception as e:
        print(e)
        exit()
    try:
        assert(numberOfCardsInPyramid > 0 and numberOfCardsInPyramid <= 26), "Invalid number of cards in Pyramid, must be at size(deck)/2"
    except Exception as e:
        print(e)
        exit()

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

ride_the_bus(100000, 26)

