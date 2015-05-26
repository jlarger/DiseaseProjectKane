import Tkinter
from Tkinter import *
import sys

window = Tk()
window.geometry('300x90')
window.configure(background='White')
window.title('Disease Project')

def quit():
    window.destroy()
    pass
    return

def NewVirus():
    root = Tk()
    root.geometry('500x500')
    root.configure(background ='White')
    root.title('New Virus')
    
    VirusNameTemp = StringVar()
    InfectionRateTemp = StringVar()
    MortalityRateTemp = StringVar()
    RNoughtTemp = StringVar()
    ContagiousVirusTemp = StringVar()
    
    def getInformation():
        VirusName = VirusNameTemp.get()
        InfectionRate = InfectionRateTemp.get()
        MortalityRate = MortalityRateTemp.get()
        RNought = RNoughtTemp.get()
        ContagiousVirus = ContagiousVirusTemp.get()
        savedLabel = Label(root, text='Virus Saved').pack(fill=X)
        return VirusName, InfectionRate, MortalityRate, RNought, ContagiousVirus
        
        
        
    VirusNameLabel = Label(root,text ='Virus Name').pack(fill = X)
    VirusNameEntry = Entry(root,textvariable=VirusNameTemp).pack()
    
    InfectionRateLabel = Label(root,text = 'Infection Rate').pack(fill = X)
    InfectionRateEntry = Entry(root,textvariable=InfectionRateTemp).pack()
    
    MortalityRateLabel = Label(root,text = 'Mortality Rate').pack(fill = X)
    MortalityRateEntry = Entry(root,textvariable=MortalityRateTemp).pack()
    
    RNoughtLabel = Label(root,text = 'RNought').pack(fill = X)
    RNoughtEntry = Entry(root,textvariable=RNoughtTemp).pack()
    
    ContagiousVirusLabel = Label(root, text = 'Contagious Rate').pack(fill = X)
    ContagiousVirusEntry = Entry(root,textvariable=ContagiousVirusTemp).pack()
    
    ContagiousVirusInfoLabel = Label(root, text = 'From: Very Low - Very High').pack(fill = X)
    
    BlankLabel = Label(root, text = '              ').pack(fill = X)
    
    MoreInformationOnVirus = Label(root, text = 'All Information On Virus').pack(fill = X)
    MoreInformationOnVirusEntry = Entry(root,width=50).pack()
    
    BlankLabel = Label(root, text = '              ').pack(fill = X)
    
    getButton = Button(root, text = 'Save Virus',command = getInformation).pack()
    
    root.mainloop()
    
    
    
def LoadVirus():
    toor = Tk()
    toor.geometry('500x500')
    toor.configure(background = 'White')
    toor.title('Load Virus')
    
    BlankLabel = Label(toor, text = '              ').pack(fill = X)
    
    List1 = Listbox(toor)
    List1.insert(1,'DISEASE')
    List1.insert(2,'Polio')
    List1.insert(3, "Ebola")
    List1.pack()
    
    BlankLabel = Label(toor, text = '              ').pack(fill = X)
    
    InfectedPeopleLabel = Label(toor, text='Infected People').pack(fill=X)
    InfectedPeopleEntry = Entry(toor).pack()
    
    BlankLabel = Label(toor, text = '              ').pack(fill = X)
    
    TotalPopulationLabel = Label(toor, text='Total Population').pack(fill=X)
    TotalPopulationEntry = Entry(toor).pack()
    
    BlankLabel = Label(toor, text = '              ').pack(fill = X)
    
    TimeLabel = Label(toor, text='Time').pack(fill=X)
    TimeEntry = Entry(toor).pack()
    
    BlankLabel = Label(toor, text = '              ').pack(fill = X)
    
    LoadButton = Button(toor, text='Calculate').pack()
    
    toor.title('Load Virus')
    


NewVirusButton = Button(window, text = 'New Virus', command = NewVirus).pack(fill=X)
LoadVirusButton = Button(window, text = 'Load Virus', command = LoadVirus).pack(fill=X)
ExitButton = Button(window, text = 'Exit', command = quit).pack(fill = X)

window.mainloop()
