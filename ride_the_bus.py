import random

def ride_the_bus(gamesToPlay, numberOfCardsInPyramid):
    guess = " "
    points = 0
    wins = 0
    losses = 0
    gamesPlayed = 0
    points = 0
    winPercentage = 0
    pyramidCards = numberOfCardsInPyramid
    while(gamesPlayed != gamesToPlay):
        arr = []
        for x in range(1,53):
            arr.append(x)

        random.shuffle(arr)
        deck = arr[numberOfCardsInPyramid:]
        pyramid = arr[:numberofCardsInPyramid]
        gamesPlayed +=1
        for x in range(0, 42):
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

ride_the_bus(10000, 10)

