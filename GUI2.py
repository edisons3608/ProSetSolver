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
    return True

button1=Button(root, image=gray,command=redChange)
button1.place(x=0, y=0)
button2=Button(root, image=gray)
button2.place(x=55, y=0)

button3=Button(root, image=gray)
button3.place(x=0, y=55)

button4=Button(root, image=gray)
button4.place(x=55, y=55)

button5=Button(root, image=gray)
button5.place(x=0, y=110)

button6=Button(root, image=gray)
button6.place(x=55, y=110)

nextBtn = Button(root, text = "Next")
nextBtn.place(x=150,y=55)
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


MODE = 7
possible = list(powerset([i+1 for i in range(MODE)]))

modified = [];
for x in range(len(possible)):
    if len(possible[x]) > 1:
        modified.append(possible[x])

#print(modified)
def xorList(list1,list2):
    returnlist = []
    for x in range(len(list1)):
        returnlist.append(list1[x] ^ list2[x])

    return returnlist
p1 = [0,0,0,0,0,0]
p2 = [0,0,0,0,0,0]
p3 = [0,0,0,0,0,0]
p4 = [0,0,0,0,0,0]
p5 = [0,0,0,0,0,0]
p6 = [0,0,0,0,0,0]
p7 = [0,0,0,0,0,0]

input1 = ""
flag = True
counter = 8
while counter < 8:
    if counter == 1:
        p1[int(input1)-1] = 1
        
    elif counter == 2:
        p2[int(input1)-1] = 1
    elif counter == 3:
        p3[int(input1)-1] = 1
    elif counter == 4:
        p4[int(input1)-1] = 1
    elif counter == 5:
        p5[int(input1)-1] = 1
    elif counter == 6:
        p6[int(input1)-1] = 1
    elif counter == 7:
        p7[int(input1)-1] = 1
    

picDict = {1:p1, 2:p2, 3:p3, 4:p4, 5:p5, 6:p6, 7:p7}
for x in range(len(modified)):
    current = modified[x];
    picture = [0,0,0,0,0,0]
    for x in range(len(current)):
        picture = xorList(picture,picDict[current[x]])
    if picture == [0,0,0,0,0,0]:
        print(current)


root.mainloop()