import pickle
#make sure to use virusCreate()
#VIRUS_FILENAME is the variable holding the file where virusList is saved
VIRUS_FILENAME = "virusList.pkl"
#dictionary of viruses
virusList = dict()
# add viruses To virusList and saves it
def virusAdd():
    global virusList
    virus = virusCreate()
    virusList[virus.name] = virus
    saveVirus()
    return virusList
#used at the beginning of main() to load all viruses to program from VIRUS_FILENAME
def loadVirus():
    with open(VIRUS_FILENAME, 'rb') as saveVirus:
        state = pickle.load(saveVirus)
    return state
# used whenever you need to save something this function can be used to save a virus to list at anytime.
def saveVirus():
    global virusList
    with open(VIRUS_FILENAME, 'wb') as saveVirus:
        pickle.dump(virusList,saveVirus)