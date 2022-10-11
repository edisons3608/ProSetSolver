from itertools import chain, combinations

from tkinter import *
from PIL import ImageTk,Image


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
root.geometry("250x200")
app = Window(root)

root.wm_title("ProSet Solver")

red = ImageTk.PhotoImage(Image.open("images/red.png").resize((50,50)),master=root)
green = ImageTk.PhotoImage(Image.open("images/green.png").resize((50,50)),master=root)
yellow = ImageTk.PhotoImage(Image.open("images/yellow.png").resize((50,50)),master=root)
blue = ImageTk.PhotoImage(Image.open("images/blue.png").resize((50,50)),master=root)
purple = ImageTk.PhotoImage(Image.open("images/purple.png").resize((50,50)),master=root)
orange = ImageTk.PhotoImage(Image.open("images/orange.png").resize((50,50)),master=root)
gray = ImageTk.PhotoImage(Image.open("images/gray.png").resize((50,50)),master=root)

global redState, greenState, yellowState, blueState,purpleState, orangeState
redState = 0
greenState = 0
yellowState = 0
blueState = 0
purpleState = 0
orangeState = 0


def redChange():
    global redState

    if redState == 0:
        button1.config(image = red)
        redState = 1
    else:
        button1.config(image = gray)
        redState = 0
def greenChange():
    global greenState

    if greenState == 0:
        button2.config(image = green)
        greenState = 1
    else:
        button2.config(image = gray)
        greenState = 0
def yellowChange():
    global yellowState

    if yellowState == 0:
        button3.config(image = yellow)
        yellowState = 1
    else:
        button3.config(image = gray)
        yellowState = 0
def blueChange():
    global blueState

    if blueState == 0:
        button4.config(image = blue)
        blueState = 1
    else:
        button4.config(image = gray)
        blueState = 0
def purpleChange():
    global purpleState

    if purpleState == 0:
        button5.config(image = purple)
        purpleState = 1
    else:
        button5.config(image = gray)
        purpleState = 0
def orangeChange():
    global orangeState

    if orangeState == 0:
        button6.config(image = orange)
        orangeState = 1
    else:
        button6.config(image = gray)
        orangeState = 0
#print(modified)
def xorList(list1,list2):
    returnlist = []
    for x in range(len(list1)):
        returnlist.append(list1[x] ^ list2[x])

    return returnlist
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

p1 = [0,0,0,0,0,0]
p2 = [0,0,0,0,0,0]
p3 = [0,0,0,0,0,0]
p4 = [0,0,0,0,0,0]
p5 = [0,0,0,0,0,0]
p6 = [0,0,0,0,0,0]
p7 = [0,0,0,0,0,0]





nextState = 1
def nextBtn():
    global nextState,p1,p2,p3,p4,p5,p6,p7
    #print(nextState)
    if nextState == 1:
        p1 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    
    elif nextState == 2:
        p2 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    elif nextState == 3:
        p3 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    elif nextState == 4:
        p4 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    elif nextState == 5:
        p5 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    elif nextState == 6:
        p6 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    elif nextState == 7:
        p7 = [redState, greenState, yellowState, blueState, purpleState, orangeState]
    if redState == 1:
        redChange()
    if greenState == 1:
        greenChange()
    if yellowState == 1:
        yellowChange()
    if blueState == 1:
        blueChange()
    if purpleState == 1:
        purpleChange()
    if orangeState == 1:
        orangeChange()
    
    nextState += 1
    if nextState > 7:
        MODE = 7
        possible = list(powerset([i+1 for i in range(MODE)]))

        modified = [];
        for x in range(len(possible)):
            if len(possible[x]) > 1:
                modified.append(possible[x])

        picDict = {1:p1, 2:p2, 3:p3, 4:p4, 5:p5, 6:p6, 7:p7}
        for x in range(len(modified)):
            current = modified[x];
            picture = [0,0,0,0,0,0]
            for x in range(len(current)):
                picture = xorList(picture,picDict[current[x]])
            if picture == [0,0,0,0,0,0]:
                print(current)
                
button1=Button(root, image=gray,command=redChange)
button1.place(x=0, y=0)

button2=Button(root, image=gray,command=greenChange)
button2.place(x=55, y=0)

button3=Button(root, image=gray,command=yellowChange)
button3.place(x=0, y=55)

button4=Button(root, image=gray,command=blueChange)
button4.place(x=55, y=55)

button5=Button(root, image=gray,command=purpleChange)
button5.place(x=0, y=110)

button6=Button(root, image=gray,command=orangeChange)
button6.place(x=55, y=110)

nextBtn = Button(root, text = "Next",command=nextBtn)
nextBtn.place(x=150,y=55)







root.mainloop()