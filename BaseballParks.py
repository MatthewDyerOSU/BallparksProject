from tkinter import *
from tkinter import ttk

# Main Window
mainWindow = Tk()
mainWindow.title("Ballparks of America")
mainWindow.configure(bg="black")

# photos
titlePhoto = PhotoImage(file="ballparks.png")
listPhoto = PhotoImage(file="listscreen.png")
americanFamilyFieldPhoto = PhotoImage(file="americanFamilyField.png")
angelsStadiumPhoto = PhotoImage(file="angelsStadium.png")
buschStadiumPhoto = PhotoImage(file="buschStadium.png")
camdenYardsPhoto = PhotoImage(file="camdenYards.png")
chaseFieldPhoto = PhotoImage(file="chaseField.png")
citiFieldPhoto = PhotoImage(file="citiField.png")
citizensBankParkPhoto = PhotoImage(file="citizensBankPark.png")
comericaParkPhoto = PhotoImage(file="comericaPark.png")
coorsFieldPhoto = PhotoImage(file="coorsField.png")
dodgersStadiumPhoto = PhotoImage(file="dodgerStadium.png")
fenwayParkPhoto = PhotoImage(file="fenwayPark.png")
globeLifeFieldPhoto = PhotoImage(file="globeLifeField.png")
greatAmericanBallparkPhoto = PhotoImage(file="greatAmericanBallpark.png")
guaranteedRateFieldPhoto = PhotoImage(file="guaranteedRateField.png")
kauffmanStadiumPhoto = PhotoImage(file="kauffmanStadium.png")
loanDepotParkPhoto = PhotoImage(file="loanDepotPark.png")
minuteMaidParkPhoto = PhotoImage(file="minuteMaidPark.png")
nationalsParkPhoto = PhotoImage(file="nationalsPark.png")
oracleParkPhoto = PhotoImage(file="oraclePark.png")
petcoParkPhoto = PhotoImage(file="petcoPark.png")
pncParkPhoto = PhotoImage(file="pncPark.png")
progressiveFieldPhoto = PhotoImage(file="progressiveField.png")
ringCentralColiseumPhoto = PhotoImage(file="ringCentralColiseum.png")
rogersCentrePhoto = PhotoImage(file="rogersCentre.png")
tmobileParkPhoto = PhotoImage(file="tmobilePark.png")
targetFieldPhoto = PhotoImage(file="targetField.png")
tropicanaFieldPhoto = PhotoImage(file="tropicanaField.png")
truistParkPhoto = PhotoImage(file="truistPark.png")
wrigleyFieldPhoto = PhotoImage(file="wrigleyField.png")
yankeeStadiumPhoto = PhotoImage(file="yankeeStadium.png")

Label(mainWindow, image=titlePhoto, bg="black").grid(row=0, column=0, sticky=W) # bg of main screen

# List Window

# Entry button function
def openList():
    listWindow = Toplevel()
    listWindow.title("Explore the Parks!")
    listWindow.geometry("1080x800")
    listBackground = Label(listWindow, image=listPhoto)
    listBackground.place(x=0, y=0, relw=1, relh=1)
    mainWindow.withdraw()   #closes main window without closing program

    # Buttons for all the stadiums (maybe a function can create all of these without writing them all out?)
    americanFamilyFieldButton = Button(listWindow, text="American Family Field", command=openAmericanFamilyField).place(relx=0.5, rely=1/32, anchor=CENTER)
    angelsStadiumButton = Button(listWindow, text="Angel Stadium", command=openAngelsStadium).place(relx=0.5, rely=2/32, anchor=CENTER)
    buschStadiumButton = Button(listWindow, text="Busch Stadium", command=openBuschStadium).place(relx=0.5, rely=3/32, anchor=CENTER)
    camdenYardsButton = Button(listWindow, text="Camden Yards", command=openCamdenYards).place(relx=0.5, rely=4/32, anchor=CENTER)
    chaseFieldButton = Button(listWindow, text="Chase Field", command=openChaseField).place(relx=0.5, rely=5/32, anchor=CENTER)
    citiFieldButton = Button(listWindow, text="Citi Field", command=openCitiField).place(relx=0.5, rely=6/32, anchor=CENTER)
    citizensBankParkButton = Button(listWindow, text="Citizens Bank Park", command=openCitizensBankPark).place(relx=0.5, rely=7/32, anchor=CENTER)
    comericaParkButton = Button(listWindow, text="Comerica Park", command=openComericaPark).place(relx=0.5, rely=8/32, anchor=CENTER)
    coorsFieldButton = Button(listWindow, text="Coors Field", command=openCoorsField).place(relx=0.5, rely=9/32, anchor=CENTER)
    dodgersStadiumButton = Button(listWindow, text="Dodger Stadium", command=openDodgersStadium).place(relx=0.5, rely=10/32, anchor=CENTER)
    fenwayParkButton = Button(listWindow, text="Fenway Park", command=openFenwayPark).place(relx=0.5, rely=11/32, anchor=CENTER)
    globeLifeFieldButton = Button(listWindow, text="Globe Life Field", command=openGlobeLifeField).place(relx=0.5, rely=12/32, anchor=CENTER)
    greatAmericanBallparkButton = Button(listWindow, text="Great America Ballpark", command=openGreatAmericanBallpark).place(relx=0.5, rely=13/32, anchor=CENTER)
    guaranteedRateFieldButton = Button(listWindow, text="Guaranteed Rate Field", command=openGuaranteedRateField).place(relx=0.5, rely=14/32, anchor=CENTER)
    kauffmanStadiumButton = Button(listWindow, text="Kaufmann Stadium", command=openKauffmanStadium).place(relx=0.5, rely=15/32, anchor=CENTER)
    loanDepotParkButton = Button(listWindow, text="Loan Depot Park", command=openLoanDepotPark).place(relx=0.5, rely=16/32, anchor=CENTER)
    minuteMaidParkButton = Button(listWindow, text="Minute Maid Park", command=openMinuteMaidPark).place(relx=0.5, rely=17/32, anchor=CENTER)
    nationalsParkButton = Button(listWindow, text="Nationals Park", command=openNationalsPark).place(relx=0.5, rely=18/32, anchor=CENTER)
    oracleParkButton = Button(listWindow, text="Oracle Park", command=openOraclePark).place(relx=0.5, rely=19/32, anchor=CENTER)
    petcoParkButton = Button(listWindow, text="Petco Park", command=openPetcoPark).place(relx=0.5, rely=20/32, anchor=CENTER)
    pncParkButton = Button(listWindow, text="PNC Park", command=openPncPark).place(relx=0.5, rely=21/32, anchor=CENTER)
    progressiveFieldButton = Button(listWindow, text="Progressive Field", command=openProgressiveField).place(relx=0.5, rely=22/32, anchor=CENTER)
    ringCentralColiseum = Button(listWindow, text="RingCentral Coliseum", command=openRingCentralColiseum).place(relx=0.5, rely=23/32, anchor=CENTER)
    rogersCentreButton = Button(listWindow, text="Rogers Centre", command=openRogersCentre).place(relx=0.5, rely=24/32, anchor=CENTER)
    tmobileParkButton = Button(listWindow, text="T-Mobile Park", command=openTmobilePark).place(relx=0.5, rely=25/32, anchor=CENTER)
    targetFieldButton = Button(listWindow, text="Target Field", command=openTargetField).place(relx=0.5, rely=26/32, anchor=CENTER)
    tropicanaFieldButton = Button(listWindow, text="Tropicana Field", command=openTropicanaField).place(relx=0.5, rely=27/32, anchor=CENTER)
    truistParkButton = Button(listWindow, text="Truist Park", command=openTruistPark).place(relx=0.5, rely=28/32, anchor=CENTER)
    wrigleyFieldButton = Button(listWindow, text="Wrigley Field", command=openWrigleyField).place(relx=0.5, rely=29/32, anchor=CENTER)
    yankeeStadiumButton = Button(listWindow, text="Yankee Stadium", command=openYankeeStadium).place(relx=0.5, rely=30/32, anchor=CENTER)


# functions for all the stadium buttons
def openAmericanFamilyField():
    americanFamilyFieldWindow = Toplevel(bg="black")
    americanFamilyFieldWindow.title("American Family Field")
    americanFamilyFieldWindow.geometry("1080x800")
    americanFamilyFieldBackground = Label(americanFamilyFieldWindow, image=americanFamilyFieldPhoto)
    americanFamilyFieldBackground.place(x=0, y=0, relw=1, relh=1)
    americanFamilyFieldWindow.master.withdraw()

def openAngelsStadium():
    angelsStadiumWindow = Toplevel()
    angelsStadiumWindow.title("Angels Stadium")
    angelsStadiumWindow.geometry("1080x800")
    angelsStadiumBackground = Label(angelsStadiumWindow, image=angelsStadiumPhoto)
    angelsStadiumBackground.place(x=0, y=0, relw=1, relh=1)

def openBuschStadium():
    buschStadiumWindow = Toplevel()
    buschStadiumWindow.title("Busch Stadium")
    buschStadiumWindow.geometry("1080x800")
    buschStadiumBackground = Label(buschStadiumWindow, image=buschStadiumPhoto)
    buschStadiumBackground.place(x=0, y=0, relw=1, relh=1)

def openCamdenYards():
    camdenYardsWindow = Toplevel()
    camdenYardsWindow.title("Camden Yards")
    camdenYardsWindow.geometry("1080x800")
    camdenYardsBackground = Label(camdenYardsWindow, image=camdenYardsPhoto)
    camdenYardsBackground.place(x=0, y=0, relw=1, relh=1)

def openChaseField():
    chaseFieldWindow = Toplevel()
    chaseFieldWindow.title("Chase Field")
    chaseFieldWindow.geometry("1080x800")
    chaseFieldBackground = Label(chaseFieldWindow, image=chaseFieldPhoto)
    chaseFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openCitiField():
    citiFieldWindow = Toplevel()
    citiFieldWindow.title("Citi Field")
    citiFieldWindow.geometry("1080x800")
    citiFieldBackground = Label(citiFieldWindow, image=citiFieldPhoto)
    citiFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openCitizensBankPark():
    citizensBankParkWindow = Toplevel()
    citizensBankParkWindow.title("Citizens Bank Park")
    citizensBankParkWindow.geometry("1080x800")
    citizensBankParkBackground = Label(citizensBankParkWindow, image=citizensBankParkPhoto)
    citizensBankParkBackground.place(x=0, y=0, relw=1, relh=1)

def openComericaPark():
    comericaParkWindow = Toplevel()
    comericaParkWindow.title("Comerica Park")
    comericaParkWindow.geometry("1080x800")
    comericaParkBackground = Label(comericaParkWindow, image=comericaParkPhoto)
    comericaParkBackground.place(x=0, y=0, relw=1, relh=1)

def openCoorsField():
    coorsFieldWindow = Toplevel()
    coorsFieldWindow.title("Coors Field")
    coorsFieldWindow.geometry("1080x800")
    coorsFieldBackground = Label(coorsFieldWindow, image=coorsFieldPhoto)
    coorsFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openDodgersStadium():
    dodgersStadiumWindow = Toplevel()
    dodgersStadiumWindow.title("Dodgers Stadium")
    dodgersStadiumWindow.geometry("1080x800")
    dodgersStadiumBackground = Label(dodgersStadiumWindow, image=dodgersStadiumPhoto)
    dodgersStadiumBackground.place(x=0, y=0, relw=1, relh=1)

def openFenwayPark():
    fenwayParkWindow = Toplevel()
    fenwayParkWindow.title("Fenway Park")
    fenwayParkWindow.geometry("1080x800")
    fenwayParkBackground = Label(fenwayParkWindow, image=fenwayParkPhoto)
    fenwayParkBackground.place(x=0, y=0, relw=1, relh=1)

def openGlobeLifeField():
    globeLifeFieldWindow = Toplevel()
    globeLifeFieldWindow.title("Globe Life Field")
    globeLifeFieldWindow.geometry("1080x800")
    globeLifeFieldBackground = Label(globeLifeFieldWindow, image=globeLifeFieldPhoto)
    globeLifeFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openGreatAmericanBallpark():
    greatAmericanBallparkWindow = Toplevel()
    greatAmericanBallparkWindow.title("Great American Ballpark")
    greatAmericanBallparkWindow.geometry("1080x800")
    greatAmericanBallparkBackground = Label(greatAmericanBallparkWindow, image=greatAmericanBallparkPhoto)
    greatAmericanBallparkBackground.place(x=0, y=0, relw=1, relh=1)

def openGuaranteedRateField():
    guaranteedRateFieldWindow = Toplevel()
    guaranteedRateFieldWindow.title("Guaranteed Rate Field")
    guaranteedRateFieldWindow.geometry("1080x800")
    guaranteedRateFieldBackground = Label(guaranteedRateFieldWindow, image=guaranteedRateFieldPhoto)
    guaranteedRateFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openKauffmanStadium():
    kauffmanStadiumWindow = Toplevel()
    kauffmanStadiumWindow.title("Kauffman Stadium")
    kauffmanStadiumWindow.geometry("1080x800")
    kauffmanStadiumBackground = Label(kauffmanStadiumWindow, image=kauffmanStadiumPhoto)
    kauffmanStadiumBackground.place(x=0, y=0, relw=1, relh=1)

def openLoanDepotPark():
    loanDepotParkWindow = Toplevel()
    loanDepotParkWindow.title("loanDepot Park")
    loanDepotParkWindow.geometry("1080x800")
    loanDepotParkBackground = Label(loanDepotParkWindow, image=loanDepotParkPhoto)
    loanDepotParkBackground.place(x=0, y=0, relw=1, relh=1)

def openMinuteMaidPark():
    minuteMaidParkWindow = Toplevel()
    minuteMaidParkWindow.title("Minute Maid Park")
    minuteMaidParkWindow.geometry("1080x800")
    minuteMaidParkBackground = Label(minuteMaidParkWindow, image=minuteMaidParkPhoto)
    minuteMaidParkBackground.place(x=0, y=0, relw=1, relh=1)

def openNationalsPark():
    nationalsParkWindow = Toplevel()
    nationalsParkWindow.title("Nationals Park")
    nationalsParkWindow.geometry("1080x800")
    nationalsParkBackground = Label(nationalsParkWindow, image=nationalsParkPhoto)
    nationalsParkBackground.place(x=0, y=0, relw=1, relh=1)

def openOraclePark():
    oracleParkWindow = Toplevel()
    oracleParkWindow.title("Oracle Park")
    oracleParkWindow.geometry("1080x800")
    oracleParkBackground = Label(oracleParkWindow, image=oracleParkPhoto)
    oracleParkBackground.place(x=0, y=0, relw=1, relh=1)

def openPetcoPark():
    petcoParkWindow = Toplevel()
    petcoParkWindow.title("Petco Park")
    petcoParkWindow.geometry("1080x800")
    petcoParkBackground = Label(petcoParkWindow, image=petcoParkPhoto)
    petcoParkBackground.place(x=0, y=0, relw=1, relh=1)

def openPncPark():
    pncParkWindow = Toplevel()
    pncParkWindow.title("PNC Park")
    pncParkWindow.geometry("1080x800")
    pncParkBackground = Label(pncParkWindow, image=pncParkPhoto)
    pncParkBackground.place(x=0, y=0, relw=1, relh=1)

def openProgressiveField():
    progressiveFieldWindow = Toplevel()
    progressiveFieldWindow.title("Progressive Field")
    progressiveFieldWindow.geometry("1080x800")
    progressiveFieldBackground = Label(progressiveFieldWindow, image=progressiveFieldPhoto)
    progressiveFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openRingCentralColiseum():
    ringCentralColiseumWindow = Toplevel()
    ringCentralColiseumWindow.title("RingCentral Coliseum")
    ringCentralColiseumWindow.geometry("1080x800")
    ringCentralColiseumBackground = Label(ringCentralColiseumWindow, image=ringCentralColiseumPhoto)
    ringCentralColiseumBackground.place(x=0, y=0, relw=1, relh=1)

def openRogersCentre():
    rogersCentreWindow = Toplevel()
    rogersCentreWindow.title("Rogers Centre")
    rogersCentreWindow.geometry("1080x800")
    rogersCentreBackground = Label(rogersCentreWindow, image=rogersCentrePhoto)
    rogersCentreBackground.place(x=0, y=0, relw=1, relh=1)

def openTmobilePark():
    tmobileParkWindow = Toplevel()
    tmobileParkWindow.title("T-Mobile Park")
    tmobileParkWindow.geometry("1080x800")
    tmobileParkBackground = Label(tmobileParkWindow, image=tmobileParkPhoto)
    tmobileParkBackground.place(x=0, y=0, relw=1, relh=1)

def openTargetField():
    targetFieldWindow = Toplevel()
    targetFieldWindow.title("Target Field")
    targetFieldWindow.geometry("1080x800")
    targetFieldBackground = Label(targetFieldWindow, image=targetFieldPhoto)
    targetFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openTropicanaField():
    tropicanaFieldWindow = Toplevel()
    tropicanaFieldWindow.title("Tropicana Field")
    tropicanaFieldWindow.geometry("1080x800")
    tropicanaFieldBackground = Label(tropicanaFieldWindow, image=tropicanaFieldPhoto)
    tropicanaFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openTruistPark():
    truistParkWindow = Toplevel()
    truistParkWindow.title("Truist Park")
    truistParkWindow.geometry("1080x800")
    truistParkBackground = Label(truistParkWindow, image=truistParkPhoto)
    truistParkBackground.place(x=0, y=0, relw=1, relh=1)

def openWrigleyField():
    wrigleyFieldWindow = Toplevel()
    wrigleyFieldWindow.title("Wrigley Field")
    wrigleyFieldWindow.geometry("1080x800")
    wrigleyFieldBackground = Label(wrigleyFieldWindow, image=wrigleyFieldPhoto)
    wrigleyFieldBackground.place(x=0, y=0, relw=1, relh=1)

def openYankeeStadium():
    yankeeStadiumWindow = Toplevel()
    yankeeStadiumWindow.title("Yankee Stadium")
    yankeeStadiumWindow.geometry("1080x800")
    yankeeStadiumBackground = Label(yankeeStadiumWindow, image=yankeeStadiumPhoto)
    yankeeStadiumBackground.place(x=0, y=0, relw=1, relh=1)

def backToMain(): # back button to main screen
    pass

def backToList(): # back button to list screen
    pass

# create entry button
entryButton = Button(mainWindow, text="Explore the Parks!", padx=100, pady=80, command=openList).place(relx=0.5, rely=0.5, anchor=CENTER)

# run main loop
mainWindow.mainloop()