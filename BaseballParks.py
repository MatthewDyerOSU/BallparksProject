from tkinter import *


# main:
mainWindow = Tk()
mainWindow.title("Ballparks of America")
mainWindow.configure(bg="black")

# photos
titlePhoto = PhotoImage(file="ballparks.png")
listPhoto = PhotoImage(file="listscreen.png")
# americanFamilyFieldPhoto = PhotoImage(file="americanFamilyField.png")
# angelStadiumPhoto = PhotoImage(file="angelsStadium.png")
# buschStadiumPhoto = PhotoImage(file="buschStadium.png")
# camdenYardsPhoto = PhotoImage(file="camdenYards.png")
# chaseFieldPhoto = PhotoImage(file="chaseField.png")c
# citiFieldPhoto = PhotoImage(file="citiFieldPhoto.png")
# citizensBankParkPhoto = PhotoImage(file="citizensBankPark.png")
# comericaParkPhoto = PhotoImage(file="comericaPark.png")
# coorsFieldPhoto = PhotoImage(file="coorsField.png")
# dodgerStadiumPhoto = PhotoImage(file="dodgerStadium.png")
# fenwayParkPhoto = PhotoImage(file="fenwayPark.png")
# globeLifeFieldPhoto = PhotoImage(file="globeLifeField.png")
# greatAmericanBallparkPhoto = PhotoImage(file="greatAmericanBallpark.png")
# guaranteedRateFieldPhoto = PhotoImage(file="guaranteedRateField.png")
# kaufmannStadiumPhoto = PhotoImage(file="kaufmannStadium.png")
# loanDepotParkPhoto = PhotoImage(file="loanDepotPark.png")
# minuteMaidParkPhoto = PhotoImage(file="minuteMaidPark.png")
# nationalsParkPhoto = PhotoImage(file="nationalsPark.png")
# oracleParkPhoto = PhotoImage(file="oraclePark.png")
# petcoParkPhoto = PhotoImage(file="petcoPark.png")
# pncParkPhoto = PhotoImage(file="pncPark.png")
# progressiveFieldPhoto = PhotoImage(file="progressiveField.png")
# rogersCentrePhoto = PhotoImage(file="rogersCentre.png")
# tmobileParkPhoto = PhotoImage(file="tmobilePark.png")
# targetFieldPhoto = PhotoImage(file="targetField.png")
# tropicanaFieldPhoto = PhotoImage(file="tropicanaField.png")
# truistParkPhoto = PhotoImage(file="truistPark.png")
# wrigleyFieldPhoto = PhotoImage(file="wrigleyField.png")
# yankeeStadiumPhoto = PhotoImage(file="yankeeStadium.png")




Label(mainWindow, image=titlePhoto, bg="black").grid(row=0, column=0, sticky=W)

# Entry button function
def openList():
    listWindow = Toplevel(bg="black")
    listWindow.title("Explore the Parks!")
    listWindow.geometry("1080x1011")
    # Label(listWindow, image=listPhoto, bg="black").grid(row=0, column=0, sticky=W)
    listBackground = Label(listWindow, image=listPhoto)
    listBackground.place(x=0, y=0, relw=1, relh=1)
    mainWindow.withdraw()
    #americanFamilyFieldButton = Button(listWindow, text="American Family Field").grid(row=0, column=0, sticky=W)
    americanFamilyFieldButton = Button(listWindow, text="American Family Field").place(relx=0.5, rely=0.033, anchor=CENTER)
    angelStadiumButton = Button(listWindow, text="Angel Stadium").place(relx=0.5, rely=0.066, anchor=CENTER)
    buschStadiumButton = Button(listWindow, text="Busch Stadium").place(relx=0.5, rely=0.1, anchor=CENTER)
    camdenYardsButton = Button(listWindow, text="Camden Yards").place(relx=0.5, rely=0.633, anchor=CENTER)
    chaseFieldButton = Button(listWindow, text="Chase Field").place(relx=0.5, rely=0.133, anchor=CENTER)
    citiFieldButton = Button(listWindow, text="Citi Field").place(relx=0.5, rely=0.166, anchor=CENTER)
    citizensBankParkButton = Button(listWindow, text="Citizens Bank Park").place(relx=0.5, rely=0.2, anchor=CENTER)
    comericaParkButton = Button(listWindow, text="Comerica Park").place(relx=0.5, rely=0.233, anchor=CENTER)
    coorsFieldButton = Button(listWindow, text="Coors Field").place(relx=0.5, rely=0.266, anchor=CENTER)
    dodgerStadiumButton = Button(listWindow, text="Dodger Stadium").place(relx=0.5, rely=0.3, anchor=CENTER)
    fenwayParkButton = Button(listWindow, text="Fenway Park").place(relx=0.5, rely=0.333, anchor=CENTER)
    globeLifeFieldButton = Button(listWindow, text="Globe Life Field").place(relx=0.5, rely=0.366, anchor=CENTER)
    greatAmericanBallparkButton = Button(listWindow, text="Great America Ballpark").place(relx=0.5, rely=0.4, anchor=CENTER)
    guaranteedRateFieldButton = Button(listWindow, text="Guaranteed Rate Field").place(relx=0.5, rely=0.433, anchor=CENTER)
    kaufmannStadiumButton = Button(listWindow, text="Kaufmann Stadium").place(relx=0.5, rely=0.466, anchor=CENTER)
    loanDepotParkButton = Button(listWindow, text="Loan Depot Park").place(relx=0.5, rely=0.5, anchor=CENTER)
    minuteMaidParkButton = Button(listWindow, text="Minute Maid Park").place(relx=0.5, rely=0.533, anchor=CENTER)
    nationalsParkButton = Button(listWindow, text="Nationals Park").place(relx=0.5, rely=0.566, anchor=CENTER)
    oracleParkButton = Button(listWindow, text="Oracle Park").place(relx=0.5, rely=0.6, anchor=CENTER)
    petcoParkButton = Button(listWindow, text="Petco Park").place(relx=0.5, rely=0.666, anchor=CENTER)
    pncParkButton = Button(listWindow, text="PNC Park").place(relx=0.5, rely=0.7, anchor=CENTER)
    progressiveFieldButton = Button(listWindow, text="Progressive Field").place(relx=0.5, rely=0.733, anchor=CENTER)
    rogersCentreButton = Button(listWindow, text="Rogers Centre").place(relx=0.5, rely=0.766, anchor=CENTER)
    tmobileParkButton = Button(listWindow, text="T-Mobile Park").place(relx=0.5, rely=0.8, anchor=CENTER)
    targetFieldButton = Button(listWindow, text="Target Field").place(relx=0.5, rely=0.833, anchor=CENTER)
    tropicanaFieldButton = Button(listWindow, text="Tropicana Field").place(relx=0.5, rely=0.866, anchor=CENTER)
    truistParkButton = Button(listWindow, text="Truist Park").place(relx=0.5, rely=0.9, anchor=CENTER)
    wrigleyFieldButton = Button(listWindow, text="Wrigley Field").place(relx=0.5, rely=0.933, anchor=CENTER)
    yankeeStadiumButton = Button(listWindow, text="Yankee Stadium").place(relx=0.5, rely=0.966, anchor=CENTER)

    # def americanFamilyField
    # def angelStadium
    # def buschStadium
    # def camdenYards
    # def chaseField
    # def citiField
    # def citizensBankPark
    # def comericaPark
    # def coorsField
    # def dodgerStadium
    # def fenwayPark
    # def globeLifeField
    # def greatAmericanBallpark
    # def guaranteedRateField
    # def kaufmannStadium
    # def loanDepotPark
    # def minuteMaidPark
    # def nationalsPark
    # def oraclePark
    # def petcoPark
    # def pncPark
    # def progressiveField
    # def rogersCentre
    # def tmobilePark
    # def targetField
    # def tropicanaField
    # def truistPark
    # def wrigleyField
    # def yankeeStadium


# create entry button
entryButton = Button(mainWindow, text="Explore the Parks!", padx=100, pady=80, command=openList).place(relx=0.5, rely=0.5, anchor=CENTER)


# run main loop
mainWindow.mainloop()