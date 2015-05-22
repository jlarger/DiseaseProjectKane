import pickle

VIRUS_FILENAME = "virusList.pkl"
virusSaveList = dict()

def virusAdd():
    global virusSaveList
    virus = virusCreate()
    virusSaveList[virus.name] = virus
    saveGame()
    return virusSaveList
    
def loadGame():
    with open(VIRUS_FILENAME, 'rb') as saveVirus:
        state = pickle.load(saveVirus)
    return state

def saveGame():
    global gameState
    with open(VIRUS_FILENAME, 'wb') as saveVirus:
        pickle.dump(virusSaveList,saveVirus)