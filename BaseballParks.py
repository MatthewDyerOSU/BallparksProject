# Non-functional Requirements:
    # Usability: The software should be pleasant and easy to use to inspire users to continue to use it as a source of MLB ballpark information
    # Reliability: It is important for the functions of this software to work reliably so that users develop trust in the product.
    # Memorability: Users should be able to navigate and use the application without having to revisit the documentation

from tkinter import *
from tkinter import Tk, Text
from re import sub

if __name__ == '__main__':

    # Window List as a stack for managing backtracking
    windowList = []

    # Main Window
    mainWindow = Tk()
    mainWindow.title("Ballparks of America")
    mainWindow.configure(bg="black")
    windowList.append(mainWindow)
    mainHelpText = Text(mainWindow, height=30, width=100)

    # Used by back button to reopen second to last window on stack
    def reopenLastWindow():
        windowList[-2].deiconify()
        windowList.pop().withdraw()

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
        listWindow = Toplevel(bg="black")
        listWindow.title("Explore the Parks!")
        listWindow.geometry("1080x800")
        listBackground = Label(listWindow, image=listPhoto)
        listBackground.place(x=0, y=0, relw=1, relh=1)
        mainWindow.withdraw()   #closes main window without closing program
        windowList.append(listWindow)
        helpButton = Button(listWindow, text="Click Here for HELP", command=openHelpWindow, cursor="question_arrow").place(relx=0.9, rely=0.1, anchor=CENTER)
        searchButton = Button(listWindow, text="Search!", padx=50, pady=30, command=openSearchWindow, cursor="target").place(relx=0.1, rely=0.8, anchor=CENTER)

        # Buttons for all the stadiums (maybe a function can create all of these without writing them all out?)
        americanFamilyFieldButton = Button(listWindow, text="American Family Field", command=openAmericanFamilyField, cursor="target").place(relx=0.5, rely=1/32, anchor=CENTER)
        angelsStadiumButton = Button(listWindow, text="Angel Stadium", command=openAngelsStadium, cursor="target").place(relx=0.5, rely=2/32, anchor=CENTER)
        buschStadiumButton = Button(listWindow, text="Busch Stadium", command=openBuschStadium, cursor="target").place(relx=0.5, rely=3/32, anchor=CENTER)
        camdenYardsButton = Button(listWindow, text="Camden Yards", command=openCamdenYards, cursor="target").place(relx=0.5, rely=4/32, anchor=CENTER)
        chaseFieldButton = Button(listWindow, text="Chase Field", command=openChaseField, cursor="target").place(relx=0.5, rely=5/32, anchor=CENTER)
        citiFieldButton = Button(listWindow, text="Citi Field", command=openCitiField, cursor="target").place(relx=0.5, rely=6/32, anchor=CENTER)
        citizensBankParkButton = Button(listWindow, text="Citizens Bank Park", command=openCitizensBankPark, cursor="target").place(relx=0.5, rely=7/32, anchor=CENTER)
        comericaParkButton = Button(listWindow, text="Comerica Park", command=openComericaPark, cursor="target").place(relx=0.5, rely=8/32, anchor=CENTER)
        coorsFieldButton = Button(listWindow, text="Coors Field", command=openCoorsField, cursor="target").place(relx=0.5, rely=9/32, anchor=CENTER)
        dodgersStadiumButton = Button(listWindow, text="Dodger Stadium", command=openDodgersStadium, cursor="target").place(relx=0.5, rely=10/32, anchor=CENTER)
        fenwayParkButton = Button(listWindow, text="Fenway Park", command=openFenwayPark, cursor="target").place(relx=0.5, rely=11/32, anchor=CENTER)
        globeLifeFieldButton = Button(listWindow, text="Globe Life Field", command=openGlobeLifeField, cursor="target").place(relx=0.5, rely=12/32, anchor=CENTER)
        greatAmericanBallparkButton = Button(listWindow, text="Great America Ballpark", command=openGreatAmericanBallpark, cursor="target").place(relx=0.5, rely=13/32, anchor=CENTER)
        guaranteedRateFieldButton = Button(listWindow, text="Guaranteed Rate Field", command=openGuaranteedRateField, cursor="target").place(relx=0.5, rely=14/32, anchor=CENTER)
        kauffmanStadiumButton = Button(listWindow, text="Kaufmann Stadium", command=openKauffmanStadium, cursor="target").place(relx=0.5, rely=15/32, anchor=CENTER)
        loanDepotParkButton = Button(listWindow, text="Loan Depot Park", command=openloanDepotPark, cursor="target").place(relx=0.5, rely=16/32, anchor=CENTER)
        minuteMaidParkButton = Button(listWindow, text="Minute Maid Park", command=openMinuteMaidPark, cursor="target").place(relx=0.5, rely=17/32, anchor=CENTER)
        nationalsParkButton = Button(listWindow, text="Nationals Park", command=openNationalsPark, cursor="target").place(relx=0.5, rely=18/32, anchor=CENTER)
        oracleParkButton = Button(listWindow, text="Oracle Park", command=openOraclePark, cursor="target").place(relx=0.5, rely=19/32, anchor=CENTER)
        petcoParkButton = Button(listWindow, text="Petco Park", command=openPetcoPark, cursor="target").place(relx=0.5, rely=20/32, anchor=CENTER)
        pncParkButton = Button(listWindow, text="PNC Park", command=openPncPark, cursor="target").place(relx=0.5, rely=21/32, anchor=CENTER)
        progressiveFieldButton = Button(listWindow, text="Progressive Field", command=openProgressiveField, cursor="target").place(relx=0.5, rely=22/32, anchor=CENTER)
        ringCentralColiseum = Button(listWindow, text="RingCentral Coliseum", command=openRingCentralColiseum, cursor="target").place(relx=0.5, rely=23/32, anchor=CENTER)
        rogersCentreButton = Button(listWindow, text="Rogers Centre", command=openRogersCentre, cursor="target").place(relx=0.5, rely=24/32, anchor=CENTER)
        tmobileParkButton = Button(listWindow, text="T-Mobile Park", command=openTMobilePark, cursor="target").place(relx=0.5, rely=25/32, anchor=CENTER)
        targetFieldButton = Button(listWindow, text="Target Field", command=openTargetField, cursor="target").place(relx=0.5, rely=26/32, anchor=CENTER)
        tropicanaFieldButton = Button(listWindow, text="Tropicana Field", command=openTropicanaField, cursor="target").place(relx=0.5, rely=27/32, anchor=CENTER)
        truistParkButton = Button(listWindow, text="Truist Park", command=openTruistPark, cursor="target").place(relx=0.5, rely=28/32, anchor=CENTER)
        wrigleyFieldButton = Button(listWindow, text="Wrigley Field", command=openWrigleyField, cursor="target").place(relx=0.5, rely=29/32, anchor=CENTER)
        yankeeStadiumButton = Button(listWindow, text="Yankee Stadium", command=openYankeeStadium, cursor="target").place(relx=0.5, rely=30/32, anchor=CENTER)

    # Back button on list screen, goes to main
        backToMainButton = Button(listWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)\

    # Help window        
    def openHelpWindow():
        helpWindow = Toplevel()
        helpWindow.title("HELP")
        helpWindow.geometry("300x70")
        helpText = Label(helpWindow, text="Click 'Explore the Parks!' to see a list of MLB ballparks\n Click on the name of a ballpark to go it's page\n Click on 'Search!' to search for a ballpark\nClick on back to go back!")
        helpText.pack()

    # functions for all the stadium buttons
    def openAmericanFamilyField():
        americanFamilyFieldWindow = Toplevel()
        americanFamilyFieldWindow.title("American Family Field")
        americanFamilyFieldWindow.geometry("1080x800")
        americanFamilyFieldBackground = Label(americanFamilyFieldWindow, image=americanFamilyFieldPhoto)
        americanFamilyFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(americanFamilyFieldWindow)
        backButton = Button(americanFamilyFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openAngelsStadium():
        angelsStadiumWindow = Toplevel()
        angelsStadiumWindow.title("Angels Stadium")
        angelsStadiumWindow.geometry("1080x800")
        angelsStadiumBackground = Label(angelsStadiumWindow, image=angelsStadiumPhoto)
        angelsStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(angelsStadiumWindow)
        backButton = Button(angelsStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openBuschStadium():
        buschStadiumWindow = Toplevel()
        buschStadiumWindow.title("Busch Stadium")
        buschStadiumWindow.geometry("1080x800")
        buschStadiumBackground = Label(buschStadiumWindow, image=buschStadiumPhoto)
        buschStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(buschStadiumWindow)
        backButton = Button(buschStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCamdenYards():
        camdenYardsWindow = Toplevel()
        camdenYardsWindow.title("Camden Yards")
        camdenYardsWindow.geometry("1080x800")
        camdenYardsBackground = Label(camdenYardsWindow, image=camdenYardsPhoto)
        camdenYardsBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(camdenYardsWindow)
        backButton = Button(camdenYardsWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openChaseField():
        chaseFieldWindow = Toplevel()
        chaseFieldWindow.title("Chase Field")
        chaseFieldWindow.geometry("1080x800")
        chaseFieldBackground = Label(chaseFieldWindow, image=chaseFieldPhoto)
        chaseFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(chaseFieldWindow)
        backButton = Button(chaseFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCitiField():
        citiFieldWindow = Toplevel()
        citiFieldWindow.title("Citi Field")
        citiFieldWindow.geometry("1080x800")
        citiFieldBackground = Label(citiFieldWindow, image=citiFieldPhoto)
        citiFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(citiFieldWindow)
        backButton = Button(citiFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCitizensBankPark():
        citizensBankParkWindow = Toplevel()
        citizensBankParkWindow.title("Citizens Bank Park")
        citizensBankParkWindow.geometry("1080x800")
        citizensBankParkBackground = Label(citizensBankParkWindow, image=citizensBankParkPhoto)
        citizensBankParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(citizensBankParkWindow)
        backButton = Button(citizensBankParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openComericaPark():
        comericaParkWindow = Toplevel()
        comericaParkWindow.title("Comerica Park")
        comericaParkWindow.geometry("1080x800")
        comericaParkBackground = Label(comericaParkWindow, image=comericaParkPhoto)
        comericaParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(comericaParkWindow)
        backButton = Button(comericaParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCoorsField():
        coorsFieldWindow = Toplevel()
        coorsFieldWindow.title("Coors Field")
        coorsFieldWindow.geometry("1080x800")
        coorsFieldBackground = Label(coorsFieldWindow, image=coorsFieldPhoto)
        coorsFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(coorsFieldWindow)
        backButton = Button(coorsFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openDodgersStadium():
        dodgersStadiumWindow = Toplevel()
        dodgersStadiumWindow.title("Dodgers Stadium")
        dodgersStadiumWindow.geometry("1080x800")
        dodgersStadiumBackground = Label(dodgersStadiumWindow, image=dodgersStadiumPhoto)
        dodgersStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(dodgersStadiumWindow)
        backButton = Button(dodgersStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openFenwayPark():
        fenwayParkWindow = Toplevel()
        fenwayParkWindow.title("Fenway Park")
        fenwayParkWindow.geometry("1080x800")
        fenwayParkBackground = Label(fenwayParkWindow, image=fenwayParkPhoto)
        fenwayParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(fenwayParkWindow)
        backButton = Button(fenwayParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGlobeLifeField():
        globeLifeFieldWindow = Toplevel()
        globeLifeFieldWindow.title("Globe Life Field")
        globeLifeFieldWindow.geometry("1080x800")
        globeLifeFieldBackground = Label(globeLifeFieldWindow, image=globeLifeFieldPhoto)
        globeLifeFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(globeLifeFieldWindow)
        backButton = Button(globeLifeFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGreatAmericanBallpark():
        greatAmericanBallparkWindow = Toplevel()
        greatAmericanBallparkWindow.title("Great American Ballpark")
        greatAmericanBallparkWindow.geometry("1080x800")
        greatAmericanBallparkBackground = Label(greatAmericanBallparkWindow, image=greatAmericanBallparkPhoto)
        greatAmericanBallparkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(greatAmericanBallparkWindow)
        backButton = Button(greatAmericanBallparkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGuaranteedRateField():
        guaranteedRateFieldWindow = Toplevel()
        guaranteedRateFieldWindow.title("Guaranteed Rate Field")
        guaranteedRateFieldWindow.geometry("1080x800")
        guaranteedRateFieldBackground = Label(guaranteedRateFieldWindow, image=guaranteedRateFieldPhoto)
        guaranteedRateFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(guaranteedRateFieldWindow)
        backButton = Button(guaranteedRateFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openKauffmanStadium():
        kauffmanStadiumWindow = Toplevel()
        kauffmanStadiumWindow.title("Kauffman Stadium")
        kauffmanStadiumWindow.geometry("1080x800")
        kauffmanStadiumBackground = Label(kauffmanStadiumWindow, image=kauffmanStadiumPhoto)
        kauffmanStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(kauffmanStadiumWindow)
        backButton = Button(kauffmanStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openloanDepotPark():
        loanDepotParkWindow = Toplevel()
        loanDepotParkWindow.title("loanDepot Park")
        loanDepotParkWindow.geometry("1080x800")
        loanDepotParkBackground = Label(loanDepotParkWindow, image=loanDepotParkPhoto)
        loanDepotParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(loanDepotParkWindow)
        backButton = Button(loanDepotParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openMinuteMaidPark():
        minuteMaidParkWindow = Toplevel()
        minuteMaidParkWindow.title("Minute Maid Park")
        minuteMaidParkWindow.geometry("1080x800")
        minuteMaidParkBackground = Label(minuteMaidParkWindow, image=minuteMaidParkPhoto)
        minuteMaidParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(minuteMaidParkWindow)
        backButton = Button(minuteMaidParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openNationalsPark():
        nationalsParkWindow = Toplevel()
        nationalsParkWindow.title("Nationals Park")
        nationalsParkWindow.geometry("1080x800")
        nationalsParkBackground = Label(nationalsParkWindow, image=nationalsParkPhoto)
        nationalsParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(nationalsParkWindow)
        backButton = Button(nationalsParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openOraclePark():
        oracleParkWindow = Toplevel()
        oracleParkWindow.title("Oracle Park")
        oracleParkWindow.geometry("1080x800")
        oracleParkBackground = Label(oracleParkWindow, image=oracleParkPhoto)
        oracleParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(oracleParkWindow)
        backButton = Button(oracleParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openPetcoPark():
        petcoParkWindow = Toplevel()
        petcoParkWindow.title("Petco Park")
        petcoParkWindow.geometry("1080x800")
        petcoParkBackground = Label(petcoParkWindow, image=petcoParkPhoto)
        petcoParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(petcoParkWindow)
        backButton = Button(petcoParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openPncPark():
        pncParkWindow = Toplevel()
        pncParkWindow.title("PNC Park")
        pncParkWindow.geometry("1080x800")
        pncParkBackground = Label(pncParkWindow, image=pncParkPhoto)
        pncParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(pncParkWindow)
        backButton = Button(pncParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openProgressiveField():
        progressiveFieldWindow = Toplevel()
        progressiveFieldWindow.title("Progressive Field")
        progressiveFieldWindow.geometry("1080x800")
        progressiveFieldBackground = Label(progressiveFieldWindow, image=progressiveFieldPhoto)
        progressiveFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(progressiveFieldWindow)
        backButton = Button(progressiveFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openRingCentralColiseum():
        ringCentralColiseumWindow = Toplevel()
        ringCentralColiseumWindow.title("RingCentral Coliseum")
        ringCentralColiseumWindow.geometry("1080x800")
        ringCentralColiseumBackground = Label(ringCentralColiseumWindow, image=ringCentralColiseumPhoto)
        ringCentralColiseumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(ringCentralColiseumWindow)
        backButton = Button(ringCentralColiseumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openRogersCentre():
        rogersCentreWindow = Toplevel()
        rogersCentreWindow.title("Rogers Centre")
        rogersCentreWindow.geometry("1080x800")
        rogersCentreBackground = Label(rogersCentreWindow, image=rogersCentrePhoto)
        rogersCentreBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(rogersCentreWindow)
        backButton = Button(rogersCentreWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTMobilePark():
        tmobileParkWindow = Toplevel()
        tmobileParkWindow.title("T-Mobile Park")
        tmobileParkWindow.geometry("1080x800")
        tmobileParkBackground = Label(tmobileParkWindow, image=tmobileParkPhoto)
        tmobileParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(tmobileParkWindow)
        backButton = Button(tmobileParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTargetField():
        targetFieldWindow = Toplevel()
        targetFieldWindow.title("Target Field")
        targetFieldWindow.geometry("1080x800")
        targetFieldBackground = Label(targetFieldWindow, image=targetFieldPhoto)
        targetFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(targetFieldWindow)
        backButton = Button(targetFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTropicanaField():
        tropicanaFieldWindow = Toplevel()
        tropicanaFieldWindow.title("Tropicana Field")
        tropicanaFieldWindow.geometry("1080x800")
        tropicanaFieldBackground = Label(tropicanaFieldWindow, image=tropicanaFieldPhoto)
        tropicanaFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(tropicanaFieldWindow)
        backButton = Button(tropicanaFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTruistPark():
        truistParkWindow = Toplevel()
        truistParkWindow.title("Truist Park")
        truistParkWindow.geometry("1080x800")
        truistParkBackground = Label(truistParkWindow, image=truistParkPhoto)
        truistParkBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(truistParkWindow)
        backButton = Button(truistParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openWrigleyField():
        wrigleyFieldWindow = Toplevel()
        wrigleyFieldWindow.title("Wrigley Field")
        wrigleyFieldWindow.geometry("1080x800")
        wrigleyFieldBackground = Label(wrigleyFieldWindow, image=wrigleyFieldPhoto)
        wrigleyFieldBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(wrigleyFieldWindow)
        backButton = Button(wrigleyFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openYankeeStadium():
        yankeeStadiumWindow = Toplevel()
        yankeeStadiumWindow.title("Yankee Stadium")
        yankeeStadiumWindow.geometry("1080x800")
        yankeeStadiumBackground = Label(yankeeStadiumWindow, image=yankeeStadiumPhoto)
        yankeeStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        windowList[-1].withdraw()
        windowList.append(yankeeStadiumWindow)
        backButton = Button(yankeeStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openSearchWindow():
        searchWindow = Toplevel()
        searchWindow.title("Search!")
        searchWindow.geometry("500x300")
        # Update the list window
        def update(data):
            searchList.delete(0, END)
            for item in data:
                searchList.insert(END, item)
        # Checks entry against the list
        def check(event):
            entry = searchEntry.get()   # Grab what was typed
            if entry == '':
                data = stadiumList
            else:
                data = []
                for item in stadiumList:
                    if entry.lower() in item.lower():
                        data.append(item)
            update(data)
        # Retrieves the stadium window that matches the listbox selection
        def getWindow(event):
            selection = sub(r"-", " ", searchList.get(ANCHOR))
            windowString = "open" + selection.replace(" ", "")
            return globals()[windowString](), searchWindow.destroy()
            
        searchLabel = Label(searchWindow, text="Enter name to search!", font=("Helvetica",14), fg="grey")
        searchLabel.pack(pady=20)
        searchEntry = Entry(searchWindow, font=("Helvetica", 20))
        searchEntry.pack()
        searchList = Listbox(searchWindow, width=50)
        searchList.pack(pady=40)
        stadiumList = ["American Family Field", "Angel Stadium", "Busch Stadium", "Camden Yards", "Chase Field", "Citi Field", "Citizens Bank Park", "Comerica Park", "Coors Field", 
                    "Dodger Stadium", "Fenway Park", "Globe Life Field", "Great American Ballpark", "Guaranteed Rate Field", "Kauffman Stadium", "loanDepot Park", 
                    "Minute Maid Park", "Nationals Park", "Oracle Park", "Petco Park", "PNC Park", "Progressive Field", "RingCentral Coliseum", "Rogers Centre",
                    "T-Mobile Park", "Target Field", "Tropicana Field", "Truist Park", "Wrigley Field", "Yankee Stadium"]
        update(stadiumList)
        searchList.bind("<<ListboxSelect>>", getWindow)
        searchEntry.bind("<KeyRelease>", check)

    # create entry button
    entryButton = Button(mainWindow, text="Explore the Parks!", padx=100, pady=80, command=openList, cursor="target").place(relx=0.5, rely=0.5, anchor=CENTER)

    helpButton = Button(mainWindow, text="Click Here for HELP", command=openHelpWindow, cursor="question_arrow").place(relx=0.9, rely=0.1, anchor=CENTER)

    # run main loop
    mainWindow.mainloop()