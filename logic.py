import random
  
'''
make counters to keep track of...
X number currently infected
X number immune
number recovered
X number dead
  
figure out how to use age specifically (if at all?)

functions:
 X make infected True
 make dead True
    
    
'''
   
class Virus(object):
    def __init__(self, infectionLength, infectivity):
    #self.infectionLength = input by user
    #self.infectivity = input by user
        pass
  
class Person(object):
      
    ageRange = range(0-80)
       
    def __init__(self, vaccinated, infected, alive, age, immune, previouslyInfected):
        self.vaccinated == True
        self.infected == False
        self.alive == True
        self.age = random.random(0, 81)
        self.immune == False
        self.previouslyInfected
            
def main():
    popList = []
    infected = 0
    totalInfected = 0
    range(popList) = population #population is input by user                           for person in range(population):
    #percent(or number)Infected = input by user                                                       popList.append(Person())                                                                  
    #percent(or number)Vaccinated = input by user
    #vaccineEffectiveness = input by user
      
    numberImmune = numberVaccinated + numberPrevoiuslyInfected
    numberRecovered = 0
    numberDead = 0
    
    for person in popList:
        if infected == True:
            rNaughtCounter = rNaught
            while rNaughtCounter > 0:
                person = random.choice(popList)
                if person.vaccinated == False and person.previouslyInfected == False and person.infected == False:
                    person.infected == True
                    rNaughtCounter -= 1
            
     
    def checkIfFatal(person):
        deadPerInfected = rNaught
        while deadPerInfected > 0:
            selectedPerson = random.choice(popList)
            if selectedPerson.infected == True:
                numberDead += 1
                population -= 1
                numberInfected = numberInfected - 1
                dead += 1
                deadPerInfected -= 1
                
    for person in popList:
  
        if infected == True:
            numberInfected += 1
            totalNumberInfected +=1
        if self.alive == False:
            numberDead += 1
