

from tkinter import *
class Pikachu():
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
        def brown(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'brown', outline = 'brown')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,20):
                    for q in range(0,20):
                            id1 = self.canvas.create_rectangle(350+q*5,50+i*5,350+q*5+5,50+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [6,7,17,25,27,36,38,45,47,55,59,64,67,72,73,74,79,84,87,90,91,94,98,103,108,109,113,117,122,132,133,136,141,152,154,157,161,162,172,175,177,181,187,193,194,196,202,206,207,213,214,215]
            schwarz2 = [223,234,242,254,263,264,270,274,284,289,294,303,305,310,314,323,324,325,326,327,333,348,349,350,352,353,369,373,390,391,392,393]
            weiss = [142,186,283]
            rot = [208,209,228]
            grau = [26,92,93,112]
            braun = [232,233,273]
            gelb = [37,46,56,57,58,65,66,75,76,77,78,85,86,95,96,97,104,105,106,107,110,111,114,115,116,123,124,125,126,127,128,129,130,131,134,135,143,144,145,146,147,148,149,150,151,155,156,163,164,165,166,167,168,169,170,171]
            gelb2 = [176,182,183,184,185,188,189,190,191,192,195,203,204,205,210,211,212,224,225,226,227,229,230,231,243,244,245,246,247,248,249,250,251,252,253,265,266,267,268,269,271,272,285,286,287,288,290,291,292,293,304,306,307,308,309,311,312,313,328,329,330,331,332,351,370,371,372]
            self.black(schwarz)
            self.black(schwarz2)
            self.red(rot)
            self.white(weiss)
            self.gray(grau)
            self.brown(braun)
            self.yellow(gelb)
            self.yellow(gelb2)
