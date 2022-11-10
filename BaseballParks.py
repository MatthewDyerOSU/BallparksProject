# Non-functional Requirements:
    # Usability: The software should be pleasant and easy to use to inspire users to continue to use it as a source of MLB ballpark information
    # Reliability: It is important for the functions of this software to work reliably so that users develop trust in the product.
    # Memorability: Users should be able to navigate and use the application without having to revisit the documentation

from tkinter import *
from tkinter import Tk, Text
from re import sub
import requests
import json



if __name__ == '__main__':

    # Window List as a stack for managing backtracking
    windowList = []

    # Main Window
    mainWindow = Tk()
    mainWindow.title("Ballparks of America")
    # mainWindow.configure(bg="black")
    windowList.append(mainWindow)
    # mainHelpText = Text(mainWindow, height=30, width=100)
    appWidth = 800
    appHeight = 600
    screenWidth = mainWindow.winfo_screenwidth()
    screenHeight = mainWindow.winfo_screenheight()
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    mainWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    # Used by back button to reopen second to last window on stack
    def reopenLastWindow():
        windowList[-2].deiconify()
        windowList.pop().withdraw()

    def getHistory(searchTerm):
        searchURL = 'http://localhost:8080/{}'.format(searchTerm)

        try:
            response = requests.get(searchURL)
            response_dny = json.loads(response.text)
            history = response_dny['history']
            # print(history)
            return history
        except:
            # print('unable to retreive stadium history')
            return 'unable to retrieve stadium history'


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
        listWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        listBackground = Label(listWindow, image=listPhoto)
        listBackground.place(x=0, y=0, relw=1, relh=1)
        mainWindow.withdraw()   #closes main window without closing program
        windowList.append(listWindow)
        backToMainButton = Button(listWindow, text="Back", width=22, command=reopenLastWindow, cursor="sb_left_arrow").place(relx=1/4, rely=1/7, anchor=CENTER)
        searchButton = Button(listWindow, text="Search!", width=22, command=openSearchWindow, cursor="target").place(relx=2/4, rely=1/7, anchor=CENTER)
        helpButton = Button(listWindow, text="Click Here for HELP", width=22, command=openHelpWindow, cursor="question_arrow").place(relx=3/4, rely=1/7, anchor=CENTER)

        # Buttons for all the stadiums (maybe a function can create all of these without writing them all out?)
        americanFamilyFieldButton = Button(listWindow, height=3, width=14, text="American\n Family Field", command=openAmericanFamilyField, cursor="target").place(relx=1/7, rely=2/7, anchor=CENTER)
        angelsStadiumButton = Button(listWindow, height=3, width=14, text="Angel Stadium", command=openAngelsStadium, cursor="target").place(relx=2/7, rely=2/7, anchor=CENTER)
        buschStadiumButton = Button(listWindow, height=3, width=14, text="Busch Stadium", command=openBuschStadium, cursor="target").place(relx=3/7, rely=2/7, anchor=CENTER)
        camdenYardsButton = Button(listWindow, height=3, width=14, text="Camden Yards", command=openCamdenYards, cursor="target").place(relx=4/7, rely=2/7, anchor=CENTER)
        chaseFieldButton = Button(listWindow, height=3, width=14, text="Chase Field", command=openChaseField, cursor="target").place(relx=5/7, rely=2/7, anchor=CENTER)
        citiFieldButton = Button(listWindow, height=3, width=14, text="Citi Field", command=openCitiField, cursor="target").place(relx=6/7, rely=2/7, anchor=CENTER)
        citizensBankParkButton = Button(listWindow, height=3, width=14, text="Citizens Bank Park", command=openCitizensBankPark, cursor="target").place(relx=1/7, rely=3/7, anchor=CENTER)
        comericaParkButton = Button(listWindow, height=3, width=14, text="Comerica Park", command=openComericaPark, cursor="target").place(relx=2/7, rely=3/7, anchor=CENTER)
        coorsFieldButton = Button(listWindow, height=3, width=14, text="Coors Field", command=openCoorsField, cursor="target").place(relx=3/7, rely=3/7, anchor=CENTER)
        dodgersStadiumButton = Button(listWindow, height=3, width=14, text="Dodger Stadium", command=openDodgersStadium, cursor="target").place(relx=4/7, rely=3/7, anchor=CENTER)
        fenwayParkButton = Button(listWindow, height=3, width=14, text="Fenway Park", command=openFenwayPark, cursor="target").place(relx=5/7, rely=3/7, anchor=CENTER)
        globeLifeFieldButton = Button(listWindow, height=3, width=14, text="Globe Life Field", command=openGlobeLifeField, cursor="target").place(relx=6/7, rely=3/7, anchor=CENTER)
        greatAmericanBallparkButton = Button(listWindow, height=3, width=14, text="Great America\n Ballpark", command=openGreatAmericanBallpark, cursor="target").place(relx=1/7, rely=4/7, anchor=CENTER)
        guaranteedRateFieldButton = Button(listWindow, height=3, width=14, text="Guaranteed\n Rate Field", command=openGuaranteedRateField, cursor="target").place(relx=2/7, rely=4/7, anchor=CENTER)
        kauffmanStadiumButton = Button(listWindow, height=3, width=14, text="Kaufmann Stadium", command=openKauffmanStadium, cursor="target").place(relx=3/7, rely=4/7, anchor=CENTER)
        loanDepotParkButton = Button(listWindow, height=3, width=14, text="Loan Depot Park", command=openloanDepotPark, cursor="target").place(relx=4/7, rely=4/7, anchor=CENTER)
        minuteMaidParkButton = Button(listWindow, height=3, width=14, text="Minute Maid Park", command=openMinuteMaidPark, cursor="target").place(relx=5/7, rely=4/7, anchor=CENTER)
        nationalsParkButton = Button(listWindow, height=3, width=14, text="Nationals Park", command=openNationalsPark, cursor="target").place(relx=6/7, rely=4/7, anchor=CENTER)
        oracleParkButton = Button(listWindow, height=3, width=14, text="Oracle Park", command=openOraclePark, cursor="target").place(relx=1/7, rely=5/7, anchor=CENTER)
        petcoParkButton = Button(listWindow, height=3, width=14, text="Petco Park", command=openPetcoPark, cursor="target").place(relx=2/7, rely=5/7, anchor=CENTER)
        pncParkButton = Button(listWindow, height=3, width=14, text="PNC Park", command=openPncPark, cursor="target").place(relx=3/7, rely=5/7, anchor=CENTER)
        progressiveFieldButton = Button(listWindow, height=3, width=14, text="Progressive Field", command=openProgressiveField, cursor="target").place(relx=4/7, rely=5/7, anchor=CENTER)
        ringCentralColiseum = Button(listWindow, height=3, width=14, text="RingCentral\n Coliseum", command=openRingCentralColiseum, cursor="target").place(relx=5/7, rely=5/7, anchor=CENTER)
        rogersCentreButton = Button(listWindow, height=3, width=14, text="Rogers Centre", command=openRogersCentre, cursor="target").place(relx=6/7, rely=5/7, anchor=CENTER)
        tmobileParkButton = Button(listWindow, height=3, width=14, text="T-Mobile Park", command=openTMobilePark, cursor="target").place(relx=1/7, rely=6/7, anchor=CENTER)
        targetFieldButton = Button(listWindow, height=3, width=14, text="Target Field", command=openTargetField, cursor="target").place(relx=2/7, rely=6/7, anchor=CENTER)
        tropicanaFieldButton = Button(listWindow, height=3, width=14, text="Tropicana Field", command=openTropicanaField, cursor="target").place(relx=3/7, rely=6/7, anchor=CENTER)
        truistParkButton = Button(listWindow, height=3, width=14, text="Truist Park", command=openTruistPark, cursor="target").place(relx=4/7, rely=6/7, anchor=CENTER)
        wrigleyFieldButton = Button(listWindow, height=3, width=14, text="Wrigley Field", command=openWrigleyField, cursor="target").place(relx=5/7, rely=6/7, anchor=CENTER)
        yankeeStadiumButton = Button(listWindow, height=3, width=14, text="Yankee Stadium", command=openYankeeStadium, cursor="target").place(relx=6/7, rely=6/7, anchor=CENTER)
    

    # Help window        
    def openHelpWindow():
        helpWindow = Toplevel()
        helpWindow.title("HELP")
        helpWindow.geometry("300x70")
        helpText = Label(helpWindow, text="Click 'Explore the Parks!' to see a list of MLB ballparks\n Click on the name of a ballpark to go it's page\n Click on 'Search!' to search for a ballpark\nClick on back to go back!")
        helpText.pack()

    # refactor: plan to turn all stadium functions into 1 function
    # functions for all the stadium buttons
    def openAmericanFamilyField():
        americanFamilyFieldWindow = Toplevel()
        americanFamilyFieldWindow.title("American Family Field")
        americanFamilyFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        americanFamilyFieldBackground = Label(americanFamilyFieldWindow, image=americanFamilyFieldPhoto)
        americanFamilyFieldBackground.place(x=0, y=0, relw=1, relh=1)
        americanFamilyFieldHistory = Text(americanFamilyFieldWindow, width=20, height=6)
        americanFamilyFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        americanFamilyFieldHistory.insert('1.0', getHistory("American Family Field"))
        windowList[-1].withdraw()
        windowList.append(americanFamilyFieldWindow)
        backButton = Button(americanFamilyFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openAngelsStadium():
        angelsStadiumWindow = Toplevel()
        angelsStadiumWindow.title("Angels Stadium")
        angelsStadiumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        angelsStadiumBackground = Label(angelsStadiumWindow, image=angelsStadiumPhoto)
        angelsStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        angelsStadiumHistory = Text(angelsStadiumWindow, width=20, height=6)
        angelsStadiumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        angelsStadiumHistory.insert('1.0', getHistory("Angel Stadium"))
        windowList[-1].withdraw()
        windowList.append(angelsStadiumWindow)
        backButton = Button(angelsStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openBuschStadium():
        buschStadiumWindow = Toplevel()
        buschStadiumWindow.title("Busch Stadium")
        buschStadiumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        buschStadiumBackground = Label(buschStadiumWindow, image=buschStadiumPhoto)
        buschStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        buschStadiumHistory = Text(buschStadiumWindow, width=20, height=6)
        buschStadiumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        buschStadiumHistory.insert('1.0', getHistory("Busch Stadium"))
        windowList[-1].withdraw()
        windowList.append(buschStadiumWindow)
        backButton = Button(buschStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCamdenYards():
        camdenYardsWindow = Toplevel()
        camdenYardsWindow.title("Camden Yards")
        camdenYardsWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        camdenYardsBackground = Label(camdenYardsWindow, image=camdenYardsPhoto)
        camdenYardsBackground.place(x=0, y=0, relw=1, relh=1)
        camdenYardsHistory = Text(camdenYardsWindow, width=20, height=6)
        camdenYardsHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        camdenYardsHistory.insert('1.0', getHistory("Camden Yards"))
        windowList[-1].withdraw()
        windowList.append(camdenYardsWindow)
        backButton = Button(camdenYardsWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openChaseField():
        chaseFieldWindow = Toplevel()
        chaseFieldWindow.title("Chase Field")
        chaseFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        chaseFieldBackground = Label(chaseFieldWindow, image=chaseFieldPhoto)
        chaseFieldBackground.place(x=0, y=0, relw=1, relh=1)
        chaseFieldHistory = Text(chaseFieldWindow, width=20, height=6)
        chaseFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        chaseFieldHistory.insert('1.0', getHistory("Chase Field"))
        windowList[-1].withdraw()
        windowList.append(chaseFieldWindow)
        backButton = Button(chaseFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCitiField():
        citiFieldWindow = Toplevel()
        citiFieldWindow.title("Citi Field")
        citiFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        citiFieldBackground = Label(citiFieldWindow, image=citiFieldPhoto)
        citiFieldBackground.place(x=0, y=0, relw=1, relh=1)
        citiFieldHistory = Text(citiFieldWindow, width=20, height=6)
        citiFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        citiFieldHistory.insert('1.0', getHistory("Citi Field"))
        windowList[-1].withdraw()
        windowList.append(citiFieldWindow)
        backButton = Button(citiFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCitizensBankPark():
        citizensBankParkWindow = Toplevel()
        citizensBankParkWindow.title("Citizens Bank Park")
        citizensBankParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        citizensBankParkBackground = Label(citizensBankParkWindow, image=citizensBankParkPhoto)
        citizensBankParkBackground.place(x=0, y=0, relw=1, relh=1)
        citizensBankParkHistory = Text(citizensBankParkWindow, width=20, height=6)
        citizensBankParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        citizensBankParkHistory.insert('1.0', getHistory("Citizens Bank Park"))
        windowList[-1].withdraw()
        windowList.append(citizensBankParkWindow)
        backButton = Button(citizensBankParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openComericaPark():
        comericaParkWindow = Toplevel()
        comericaParkWindow.title("Comerica Park")
        comericaParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        comericaParkBackground = Label(comericaParkWindow, image=comericaParkPhoto)
        comericaParkBackground.place(x=0, y=0, relw=1, relh=1)
        comericaParkHistory = Text(comericaParkWindow, width=20, height=6)
        comericaParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        comericaParkHistory.insert('1.0', getHistory("Comerica Park"))
        windowList[-1].withdraw()
        windowList.append(comericaParkWindow)
        backButton = Button(comericaParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openCoorsField():
        coorsFieldWindow = Toplevel()
        coorsFieldWindow.title("Coors Field")
        coorsFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        coorsFieldBackground = Label(coorsFieldWindow, image=coorsFieldPhoto)
        coorsFieldBackground.place(x=0, y=0, relw=1, relh=1)
        coorsFieldHistory = Text(coorsFieldWindow, width=20, height=6)
        coorsFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        coorsFieldHistory.insert('1.0', getHistory("Coors Field"))
        windowList[-1].withdraw()
        windowList.append(coorsFieldWindow)
        backButton = Button(coorsFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openDodgersStadium():
        dodgersStadiumWindow = Toplevel()
        dodgersStadiumWindow.title("Dodgers Stadium")
        dodgersStadiumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        dodgersStadiumBackground = Label(dodgersStadiumWindow, image=dodgersStadiumPhoto)
        dodgersStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        dodgersStadiumHistory = Text(dodgersStadiumWindow, width=20, height=6)
        dodgersStadiumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        dodgersStadiumHistory.insert('1.0', getHistory("Dodgers Stadium"))
        windowList[-1].withdraw()
        windowList.append(dodgersStadiumWindow)
        backButton = Button(dodgersStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openFenwayPark():
        fenwayParkWindow = Toplevel()
        fenwayParkWindow.title("Fenway Park")
        fenwayParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        fenwayParkBackground = Label(fenwayParkWindow, image=fenwayParkPhoto)
        fenwayParkBackground.place(x=0, y=0, relw=1, relh=1)
        fenwayParkHistory = Text(fenwayParkWindow, width=20, height=6)
        fenwayParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        fenwayParkHistory.insert('1.0', getHistory("Fenway Park"))
        windowList[-1].withdraw()
        windowList.append(fenwayParkWindow)
        backButton = Button(fenwayParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGlobeLifeField():
        globeLifeFieldWindow = Toplevel()
        globeLifeFieldWindow.title("Globe Life Field")
        globeLifeFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        globeLifeFieldBackground = Label(globeLifeFieldWindow, image=globeLifeFieldPhoto)
        globeLifeFieldBackground.place(x=0, y=0, relw=1, relh=1)
        globeLifeFieldHistory = Text(globeLifeFieldWindow, width=20, height=6)
        globeLifeFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        globeLifeFieldHistory.insert('1.0', getHistory("Globe Life Field"))
        windowList[-1].withdraw()
        windowList.append(globeLifeFieldWindow)
        backButton = Button(globeLifeFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGreatAmericanBallpark():
        greatAmericanBallparkWindow = Toplevel()
        greatAmericanBallparkWindow.title("Great American Ballpark")
        greatAmericanBallparkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        greatAmericanBallparkBackground = Label(greatAmericanBallparkWindow, image=greatAmericanBallparkPhoto)
        greatAmericanBallparkBackground.place(x=0, y=0, relw=1, relh=1)
        greatAmericanBallparkHistory = Text(greatAmericanBallparkWindow, width=20, height=6)
        greatAmericanBallparkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        greatAmericanBallparkHistory.insert('1.0', getHistory("Great American Ballpark"))
        windowList[-1].withdraw()
        windowList.append(greatAmericanBallparkWindow)
        backButton = Button(greatAmericanBallparkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openGuaranteedRateField():
        guaranteedRateFieldWindow = Toplevel()
        guaranteedRateFieldWindow.title("Guaranteed Rate Field")
        guaranteedRateFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        guaranteedRateFieldBackground = Label(guaranteedRateFieldWindow, image=guaranteedRateFieldPhoto)
        guaranteedRateFieldBackground.place(x=0, y=0, relw=1, relh=1)
        guaranteedRateFieldHistory = Text(guaranteedRateFieldWindow, width=20, height=6)
        guaranteedRateFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        guaranteedRateFieldHistory.insert('1.0', getHistory("Guaranteed Rate Field"))
        windowList[-1].withdraw()
        windowList.append(guaranteedRateFieldWindow)
        backButton = Button(guaranteedRateFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openKauffmanStadium():
        kauffmanStadiumWindow = Toplevel()
        kauffmanStadiumWindow.title("Kauffman Stadium")
        kauffmanStadiumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        kauffmanStadiumBackground = Label(kauffmanStadiumWindow, image=kauffmanStadiumPhoto)
        kauffmanStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        kauffmanStadiumHistory = Text(kauffmanStadiumWindow, width=20, height=6)
        kauffmanStadiumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        kauffmanStadiumHistory.insert('1.0', getHistory("Kauffman Stadium"))
        windowList[-1].withdraw()
        windowList.append(kauffmanStadiumWindow)
        backButton = Button(kauffmanStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openloanDepotPark():
        loanDepotParkWindow = Toplevel()
        loanDepotParkWindow.title("loanDepot Park")
        loanDepotParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        loanDepotParkBackground = Label(loanDepotParkWindow, image=loanDepotParkPhoto)
        loanDepotParkBackground.place(x=0, y=0, relw=1, relh=1)
        loanDepotParkHistory = Text(loanDepotParkWindow, width=20, height=6)
        loanDepotParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        loanDepotParkHistory.insert('1.0', getHistory("loanDepot Park"))
        windowList[-1].withdraw()
        windowList.append(loanDepotParkWindow)
        backButton = Button(loanDepotParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openMinuteMaidPark():
        minuteMaidParkWindow = Toplevel()
        minuteMaidParkWindow.title("Minute Maid Park")
        minuteMaidParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        minuteMaidParkBackground = Label(minuteMaidParkWindow, image=minuteMaidParkPhoto)
        minuteMaidParkBackground.place(x=0, y=0, relw=1, relh=1)
        minuteMaidParkHistory = Text(minuteMaidParkWindow, width=20, height=6)
        minuteMaidParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        minuteMaidParkHistory.insert('1.0', getHistory("Minute Maid Park"))
        windowList[-1].withdraw()
        windowList.append(minuteMaidParkWindow)
        backButton = Button(minuteMaidParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openNationalsPark():
        nationalsParkWindow = Toplevel()
        nationalsParkWindow.title("Nationals Park")
        nationalsParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        nationalsParkBackground = Label(nationalsParkWindow, image=nationalsParkPhoto)
        nationalsParkBackground.place(x=0, y=0, relw=1, relh=1)
        nationalsParkHistory = Text(nationalsParkWindow, width=20, height=6)
        nationalsParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        nationalsParkHistory.insert('1.0', getHistory("Nationals Park"))
        windowList[-1].withdraw()
        windowList.append(nationalsParkWindow)
        backButton = Button(nationalsParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openOraclePark():
        oracleParkWindow = Toplevel()
        oracleParkWindow.title("Oracle Park")
        oracleParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        oracleParkBackground = Label(oracleParkWindow, image=oracleParkPhoto)
        oracleParkBackground.place(x=0, y=0, relw=1, relh=1)
        oracleParkHistory = Text(oracleParkWindow, width=20, height=6)
        oracleParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        oracleParkHistory.insert('1.0', getHistory("Oracle Park"))
        windowList[-1].withdraw()
        windowList.append(oracleParkWindow)
        backButton = Button(oracleParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openPetcoPark():
        petcoParkWindow = Toplevel()
        petcoParkWindow.title("Petco Park")
        petcoParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        petcoParkBackground = Label(petcoParkWindow, image=petcoParkPhoto)
        petcoParkBackground.place(x=0, y=0, relw=1, relh=1)
        petcoParkHistory = Text(petcoParkWindow, width=20, height=6)
        petcoParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        petcoParkHistory.insert('1.0', getHistory("Petco Park"))
        windowList[-1].withdraw()
        windowList.append(petcoParkWindow)
        backButton = Button(petcoParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openPncPark():
        pncParkWindow = Toplevel()
        pncParkWindow.title("PNC Park")
        pncParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        pncParkBackground = Label(pncParkWindow, image=pncParkPhoto)
        pncParkBackground.place(x=0, y=0, relw=1, relh=1)
        pncParkHistory = Text(pncParkWindow, width=20, height=6)
        pncParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        pncParkHistory.insert('1.0', getHistory("PNC Park"))
        windowList[-1].withdraw()
        windowList.append(pncParkWindow)
        backButton = Button(pncParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openProgressiveField():
        progressiveFieldWindow = Toplevel()
        progressiveFieldWindow.title("Progressive Field")
        progressiveFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        progressiveFieldBackground = Label(progressiveFieldWindow, image=progressiveFieldPhoto)
        progressiveFieldBackground.place(x=0, y=0, relw=1, relh=1)
        progressiveFieldHistory = Text(progressiveFieldWindow, width=20, height=6)
        progressiveFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        progressiveFieldHistory.insert('1.0', getHistory("Progressive Field"))
        windowList[-1].withdraw()
        windowList.append(progressiveFieldWindow)
        backButton = Button(progressiveFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openRingCentralColiseum():
        ringCentralColiseumWindow = Toplevel()
        ringCentralColiseumWindow.title("RingCentral Coliseum")
        ringCentralColiseumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        ringCentralColiseumBackground = Label(ringCentralColiseumWindow, image=ringCentralColiseumPhoto)
        ringCentralColiseumBackground.place(x=0, y=0, relw=1, relh=1)
        ringCentralColiseumHistory = Text(ringCentralColiseumWindow, width=20, height=6)
        ringCentralColiseumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        ringCentralColiseumHistory.insert('1.0', getHistory("RingCentral Coliseum"))
        windowList[-1].withdraw()
        windowList.append(ringCentralColiseumWindow)
        backButton = Button(ringCentralColiseumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openRogersCentre():
        rogersCentreWindow = Toplevel()
        rogersCentreWindow.title("Rogers Centre")
        rogersCentreWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        rogersCentreBackground = Label(rogersCentreWindow, image=rogersCentrePhoto)
        rogersCentreBackground.place(x=0, y=0, relw=1, relh=1)
        rogersCentreHistory = Text(rogersCentreWindow, width=20, height=6)
        rogersCentreHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        rogersCentreHistory.insert('1.0', getHistory("Rogers Centre"))
        windowList[-1].withdraw()
        windowList.append(rogersCentreWindow)
        backButton = Button(rogersCentreWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTMobilePark():
        tmobileParkWindow = Toplevel()
        tmobileParkWindow.title("T-Mobile Park")
        tmobileParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        tmobileParkBackground = Label(tmobileParkWindow, image=tmobileParkPhoto)
        tmobileParkBackground.place(x=0, y=0, relw=1, relh=1)
        tmobileParkHistory = Text(tmobileParkWindow, width=20, height=6)
        tmobileParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        tmobileParkHistory.insert('1.0', getHistory("T-Mobile Park"))
        windowList[-1].withdraw()
        windowList.append(tmobileParkWindow)
        backButton = Button(tmobileParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTargetField():
        targetFieldWindow = Toplevel()
        targetFieldWindow.title("Target Field")
        targetFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        targetFieldBackground = Label(targetFieldWindow, image=targetFieldPhoto)
        targetFieldBackground.place(x=0, y=0, relw=1, relh=1)
        targetFieldHistory = Text(targetFieldWindow, width=20, height=6)
        targetFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        targetFieldHistory.insert('1.0', getHistory("Target Field"))
        windowList[-1].withdraw()
        windowList.append(targetFieldWindow)
        backButton = Button(targetFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTropicanaField():
        tropicanaFieldWindow = Toplevel()
        tropicanaFieldWindow.title("Tropicana Field")
        tropicanaFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        tropicanaFieldBackground = Label(tropicanaFieldWindow, image=tropicanaFieldPhoto)
        tropicanaFieldBackground.place(x=0, y=0, relw=1, relh=1)
        tropicanaFieldHistory = Text(tropicanaFieldWindow, width=20, height=6)
        tropicanaFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        tropicanaFieldHistory.insert('1.0', getHistory("Tropicana Field"))
        windowList[-1].withdraw()
        windowList.append(tropicanaFieldWindow)
        backButton = Button(tropicanaFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openTruistPark():
        truistParkWindow = Toplevel()
        truistParkWindow.title("Truist Park")
        truistParkWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        truistParkBackground = Label(truistParkWindow, image=truistParkPhoto)
        truistParkBackground.place(x=0, y=0, relw=1, relh=1)
        truistParkHistory = Text(truistParkWindow, width=20, height=6)
        truistParkHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        truistParkHistory.insert('1.0', getHistory("Truist Park"))
        windowList[-1].withdraw()
        windowList.append(truistParkWindow)
        backButton = Button(truistParkWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openWrigleyField():
        wrigleyFieldWindow = Toplevel()
        wrigleyFieldWindow.title("Wrigley Field")
        wrigleyFieldWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        wrigleyFieldBackground = Label(wrigleyFieldWindow, image=wrigleyFieldPhoto)
        wrigleyFieldBackground.place(x=0, y=0, relw=1, relh=1)
        wrigleyFieldHistory = Text(wrigleyFieldWindow, width=20, height=6)
        wrigleyFieldHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        wrigleyFieldHistory.insert('1.0', getHistory("Wrigley Field"))
        windowList[-1].withdraw()
        windowList.append(wrigleyFieldWindow)
        backButton = Button(wrigleyFieldWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openYankeeStadium():
        yankeeStadiumWindow = Toplevel()
        yankeeStadiumWindow.title("Yankee Stadium")
        yankeeStadiumWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        yankeeStadiumBackground = Label(yankeeStadiumWindow, image=yankeeStadiumPhoto)
        yankeeStadiumBackground.place(x=0, y=0, relw=1, relh=1)
        yankeeStadiumHistory = Text(yankeeStadiumWindow, width=20, height=6)
        yankeeStadiumHistory.place(relx=2/11 , rely=1/4, relw=3/5, relh=3/5)
        yankeeStadiumHistory.insert('1.0', getHistory("Yankee Stadium"))
        windowList[-1].withdraw()
        windowList.append(yankeeStadiumWindow)
        backButton = Button(yankeeStadiumWindow, text="Back", command=reopenLastWindow, cursor="sb_left_arrow").place(relx=0.1, rely=0.1, anchor=CENTER)

    def openSearchWindow():
        searchWindow = Toplevel()
        searchWindow.title("Search!")
        searchWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
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