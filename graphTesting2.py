import random, pylab

import matplotlib.pyplot as plt


def roulette(simulations):
    simulationRange = range(1,simulations+1)
    moneyRange = []
    moneyTotal = 100
    moneyBet = 1
    colorChoices = ["red","green","black"]
    oddEvenChoice = ["odd","even"]
    gamesPlayed = 0
    while gamesPlayed != simulations:
        numberGuess = random.randint(0,37)
        oddOrEvenGuess = random.choice(oddEvenChoice)
        colorGuess = random.choice(colorChoices)
        number = random.randint(0,37)
        if meetsReqs(numberGuess,oddOrEvenGuess,colorGuess) == True:
            if numberGuess != "none":
                if number == numberGuess: 
                    moneyTotal =moneyTotal + (moneyBet * 35)
                    #print number,"equals", numberGuess,"money left:" ,moneyTotal 
                else:
                    moneyTotal = moneyTotal - moneyBet
                    #print number," does not equal ", numberGuess," money left: ",moneyTotal
                if whatColor(number) == colorGuess:
                    if whatColor(number) == "green":
                        moneyTotal = moneyTotal + (moneyBet * 17.5) - 1
                        #print "your color guess was right! money left: ", moneyTotal
                    moneyTotal = moneyTotal + (moneyBet * 1)
                    #print "your color guess was right! money left: ", moneyTotal
                else:
                    moneyTotal = moneyTotal - moneyBet
                    #print "your color guess was not correct! Bad luck! money left: ",moneyTotal
                if evenOrOdd(number) == oddOrEvenGuess:
                    moneyTotal = moneyTotal + (moneyBet * 1)
                    moneyRange.append(moneyTotal)
                    gamesPlayed += 1
                    #print "your even/odd guess was right! money left: ", moneyTotal
                else:
                    moneyRange.append(moneyTotal)
                    gamesPlayed += 1
                    moneyTotal = moneyTotal - moneyBet
                    #print"your even/odd guess was not correct!", "money left:" ,moneyTotal, "better luck next time!"
                
        else:
            return "please fix your guesses to make sure they are actual choices!"
            
    plt.plot(simulationRange,moneyRange)
    plt.show()

    
def meetsReqs(numberGuess,oddOrEvenGuess,colorGuess):
    if numberGuess > 37:
        return False
    if checkEvenOddInput(oddOrEvenGuess) == False:
        return False
    if checkColorInput(colorGuess) == False:
        return False
    return True
def checkColorInput(colorGuess):
    if colorGuess.lower() == "red":
        return True
    elif colorGuess.lower() == "black":
        return True
    elif colorGuess.lower() == "green":
        return True
    else:
        return False
    
def checkEvenOddInput(oddOrEvenGuess):
    if oddOrEvenGuess.lower() == 'odd':
        return True
    elif oddOrEvenGuess.lower() == 'even':
        return True
    else:
        return False

def evenOrOdd(number):
    if number % 2 == 0:
        return "even"
    return "odd"

def whatColor(numberBeingTested):
    if numberBeingTested == 37 or numberBeingTested == 0:
        return "green"
    listOfRedNums = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,28,30,32,34,36]
    for numberInListRed in listOfRedNums:
        if numberBeingTested == numberInListRed:
            return "red"
    listOfBlackNums = [2,4,6,8,10,11,13,15,17,20,22,24,26,29,31,33,35]
    for numberInListBlack in listOfBlackNums:
        if numberBeingTested == numberInListBlack:
            return  "black"
    
def withPeople(numberOfPeople,simulations):
    simulationRange = range(1,simulations+1)
    counter = 0
    listOfPersons = []
    while counter != numberOfPeople:
        listOfPersons.append(roulette(simulations))
        counter += 1
    plt.plot(simulationRange,listOfPersons)
    plt.show()
    