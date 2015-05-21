import random, pylab

def roulette(numberGuess,oddOrEvenGuess,colorGuess):
    number = random.randint(0,37)
    if meetsReqs(numberGuess,oddOrEvenGuess,colorGuess) == True:
        if number == numberGuess and evenOrOdd(number)==oddOrEvenGuess and whatColor(number) == colorGuess:
            print number, evenOrOdd(number), whatColor(number), "Winner!"
        else:
            print number, evenOrOdd(number), whatColor(number), "Loser!"
    else:
        return "please fix your guesses to make sure they are actual choices!"
    
    
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
    if numberBeingTested == 37 or 0:
        return "green"
    listOfRedNums = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,28,30,32,34,36]
    for numberInListRed in listOfRedNums:
        if numberBeingTested == numberInListRed:
            return "red"
    listOfBlackNums = [2,4,6,8,10,11,13,15,17,20,22,24,26,29,31,33,35]
    for numberInListBlack in listOfBlackNums:
        if numberBeingTested == numberInListBlack:
            return  "black"




    