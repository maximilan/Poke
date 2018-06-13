from tkinter import *
top = Tk()
c = Canvas(top,width=500,height=500,bg = "white")
c.pack()
graphic = list()
colors = list()
schwarz = [6,7,8,9,25,30,44,51,64,71,83,92,102,108,112,122,127,128,133,142,147,148,153,157,159,160,163,164,174,177,179,185,186,187,190,194,196,199,206,209,214,215,218,226,230,235,237,245,246,247]
schwarz2 = [255,256,266,267,268,274,275,288,289,290,293,294,309,314,330,331,332,333]
rot = [39,58,59,78,79,97,98,100,117,120,137,140]
gelb = [119,138,139,158,207,208,227,228,229,248,249,250,269,270]
weiss = [107,310,313]
for q in range(0,17):
    for i in range(0,20):
        id1 = c.create_rectangle(i*5+3,q*5+3,i*5+8,q*5+8,fill="white",outline="white")
        graphic.append(id1)

def yellow(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'yellow', outline = 'yellow')
        colors.append(x[i]-1)
def black(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'black', outline = 'black')
        colors.append(x[i]-1)
def orange():
    for i in range(len(graphic)):
        c.itemconfig(graphic[i], fill = 'orange', outline = 'orange')
        colors.append([i])
def white(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'white', outline = 'white')
        colors.append(x[i]-1)
def red(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'red', outline = 'red')
        colors.append(x[i]-1)
def norm():
    orange()
    black(schwarz)
    black(schwarz2)
    red(rot)
    yellow(gelb)
    white(weiss)
norm()
top.mainloop()
