from tkinter import *

class Glumanda():
        global colors
        colors = list()
        def yellow(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'yellow', outline = 'yellow')
                colors.append(x[i]-1)
        def black(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'black', outline = 'black')
                colors.append(x[i]-1)
        def gray(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'gray64', outline = 'gray64')
                colors.append(x[i]-1)
        def red(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'red', outline = 'red')
                colors.append(x[i]-1)
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def orange(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'orange', outline = 'orange')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,20):
                    for q in range(0,20):
                            id1 = self.canvas.create_rectangle(350+q*5,50+i*5,350+q*5+5,50+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [6,7,8,9,25,30,44,51,64,71,83,92,102,108,112,122,127,128,133,142,147,148,153,157,159,160,163,164,174,177,179,185,186,187,190,194,196,199,206,209,214,215,218,226,230,235,237,245,246,247]
            schwarz2 = [255,256,266,267,268,274,275,288,289,290,293,294,309,314,330,331,332,333]
            rot = [39,58,59,78,79,97,98,100,117,120,137,140]
            gelb = [119,138,139,158,207,208,227,228,229,248,249,250,269,270]
            weiss = [107,310,313]
            orange = [26,27,28,29,45,46,47,48,49,50,65,66,67,68,69,70,84,85,86,87,88,89,90,91,99,103,104,105,106,109,110,111,118,123,124,125,126,129,130,131,132,143,144,145,146,149,150,151,152,165,166,167,168,169,170,171,172,173]
            orange2 = [178,188,189,191,192,193,197,198,210,211,212,213,216,217,231,232,233,234,236,251,252,253,254,271,272,273,291,292,311,312]
            self.orange(orange)
            self.black(schwarz)
            self.black(schwarz2)
            self.red(rot)
            self.white(weiss)
            self.yellow(gelb)
            self.orange(orange2)
