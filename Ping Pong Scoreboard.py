from appJar import gui

global Serve
global Serve_First
global Fault
Serve = 0
Fault = 0
Serve_First = "Home"

def Setup_press(button):
    #Set which player starts the game
    global Serve_First
    Serve_First = app.getOptionBox("Serve First")
    press("Reset")
    app.hideSubWindow("Setup")


def Check_Serve():
    #Check how many times a player has served and changes it if they have served twice
    global Serve
    global Fault
    Serve += 1
    if Serve == 2:
        Serve = 0
        Fault = 0
        if app.getLabel("Serve") == "   Serve ->":
            app.setLabel("Serve", "<- Serve   ")
        elif app.getLabel("Serve") == "<- Serve   ":
            app.setLabel("Serve", "   Serve ->")

def press(button):
    global Serve
    global Fault
    if button == "+1 Home":
        app.setLabel("HomeScore", int(app.getLabel("HomeScore")) + 1)
    elif button == "+1 Away":
        app.setLabel("AwayScore", int(app.getLabel("AwayScore")) + 1 )
    elif button == "Fault":
        Fault += 1
        if Fault == 2:
            #Changes gives a point to a play if the other player has 2 faults
            Fault = 0
            Serve = 1
            if app.getLabel("Serve") == "<- Serve   ":
                #press("+1 Away")
                app.setLabel("AwayScore", int(app.getLabel("AwayScore")) + 1)
            else:
                #press("+1 Home")
                app.setLabel("HomeScore", int(app.getLabel("HomeScore")) + 1 )
    if button == "Reset":
        #Reset the score board
        app.setLabel("HomeScore", "0")
        app.setLabel("AwayScore", "0")
        if Serve_First == "Home":
            app.setLabel("Serve", "<- Serve   ")
        else:
            app.setLabel("Serve", "   Serve ->")
        Serve = 0
    elif button == "Setup":
        app.showSubWindow("Setup")
    elif button == "Close":
        app.stop()
    else:
        Check_Serve()

app = gui("Score Board")

#Set default backround and font size
app.setBg("Green")
app.setFont(size=60)

#Create the scoreboard
app.addLabel("firstspace", " ", 0, 0)
app.addLabel("title", "Pin Pong Scorboard", 0, 1)
app.addLabel("secondspace", " ", 0, 2)
app.addLabel("HomeTitle", "Home", 1, 0)
app.addLabel("awayspace", " ", 1, 1)
app.addLabel("AwayTitle", "Away", 1, 2)
app.addLabel("HomeScore", "0", 2, 0)
app.addLabel("Serve", "<- Serve   ", 2, 1)
app.addLabel("AwayScore", "0", 2, 2)
app.addButton("+1 Home", press, 3, 0)
app.addButtons(["Reset", "Fault"], press, 3, 1)
app.addButton("+1 Away", press, 3, 2)
app.addButtons(["Setup", "Close"], press, 4, 1)

#Change the color of the buttons and labels
app.setLabelFg("HomeTitle", "Red")
app.setLabelFg("HomeScore", "Red")
app.setLabelFg("AwayTitle", "Blue")
app.setLabelFg("AwayScore", "Blue")
app.setButtonBg("+1 Home", "Green")
app.setButtonBg("+1 Away", "Green")
app.setButtonBg("Reset", "Green")
app.setButtonBg("Close", "Green")
app.setButtonBg("Fault", "Green")
app.setButtonBg("Setup", "Green")
app.setButtonFg("+1 Home", "Red")
app.setButtonFg("+1 Away", "Blue")

#Setup window
app.startSubWindow("Setup")
app.addLabel("Setup Serve Title", "Who serves first?")
app.addOptionBox("Serve First", ["Home", "Away"])
app.addButton("Set Options", Setup_press)

#Format the objects in the setup window
app.setBg("Green")
app.setLabelBg("Setup Serve Title", "Green")
app.setOptionBoxBg("Serve First", "Green")
app.setButtonBg("Set Options", "Green")
app.stopSubWindow()

app.go()