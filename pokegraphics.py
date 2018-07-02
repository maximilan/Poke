from tkinter import *

from time import sleep

class Pokedesign():
        def __init__(self, name, canvas, function, module):
                self.canvas = canvas
                self.module = module
                if name == "Bisasam":
                       id1 = Bisasam(canvas)
                elif name == "Glumanda":
                        id1 = Glumanda(canvas)
                elif name == "Schiggy":
                        id1 = Schiggy(canvas)
                elif name == "Raupy":
                        id1 = Raupy(canvas)
                elif name == "Hornliu":
                        id1 = Hornliu(canvas)
                elif name == "Pikachu":
                        id1 = Pikachu(canvas)
                elif name == "Raichu":
                        id1 = Raichu(canvas)
                self.graphic = id1.return_design()
                if function == "self":
                        for graphic in self.graphic:
                                self.canvas.move(graphic, -400, 300)
        def return_design(self):
                return self.graphic
        def delete(self):
                for graphic in self.graphic:
                        self.canvas.delete(graphic)
                self.module.update()

class Bisasam(Pokedesign):
        global colors
        colors = list()
        def lightgreen(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'lime green', outline = 'lime green')
                colors.append(x[i]-1)
        def black(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'black', outline = 'black')
                colors.append(x[i]-1)
        def darkgreen(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'forest green', outline = 'forest green')
                colors.append(x[i]-1)
        def red(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'red', outline = 'red')
                colors.append(x[i]-1)
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,20):
                    for q in range(0,21):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            hellgruen = [56,58,78,131,152,153,154,173,174,175,176,193,194,196,199,215,216,217,218,219,220,221,222,223,236,237,238,240,241,242,243,255,256,257,258,260,263,264,277,278,279,280,285,299,300,301,305]
            schwarz = [35,36,37,55,57,59,74,75,76,80,93,94,96,98,100,102,103,110,113,116,119,121,125,130,132,133,134,136,140,143,147,151,156,157,160,165,168,172,179,181,186,189,192,201,202,203,207,209,212]
            schwarz2 = [213,224,227,228,229,233,234,244,246,247,248,252,254,261,262,270,273,275,281,287,289,291,292,293,297,302,307,311,319,320,327,332,342,343,344,345,346,347,348,349,353,371,372,373]
            dunkelgruen = [77,79,95,97,99,101,114,115,117,118,120,122,123,124,135,137,138,139,141,142,144,145,146,155,158,159,161,162,163,164,166,167,177,178,180,182,183,184,185,187,188,195,197,198,200,204,205,206]
            dunkelgruen2 = [208,214,225,226,230,235,239,245,249,250,251,259,265,266,267,268,269,271,272,276,286,288,290,298,306,308,309,310,311,321,322,323,324,325,326,328,329,330,331,351]
            weiss = [283,284,304,350,352]
            rot = [282,303]
            self.black(schwarz)
            self.black(schwarz2)
            self.lightgreen(hellgruen)
            self.darkgreen(dunkelgruen)
            self.darkgreen(dunkelgruen2)
            self.red(rot)
            self.white(weiss)
class Glumanda(Pokedesign):
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
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
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
class Schiggy(Pokedesign):
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
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def brown(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'brown', outline = 'brown')
                colors.append(x[i]-1)
        def brown2(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'sienna3', outline = 'sienna3')
                colors.append(x[i]-1)
        def blue(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'dodger blue', outline = 'dodger blue')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,18):
                    for q in range(0,22):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [4,5,6,7,17,18,19,20,25,30,31,38,43,47,54,55,59,66,68,76,78,79,81,88,90,102,108,110,111,125,129,132,133,139,147,151,153,155,160,169,172,173,174,178,182,187,192,193,194]
            schwarz2 = [201,202,207,208,214,223,225,226,227,228,236,246,247,250,254,258,270,273,274,275,276,280,291,293,299,301,314,315,316,317,321,323,339,340,341,343,344,362,366,385,386,387]
            weiss = [138,165,188,211,233,255]
            braun = [77,99,101,124,161,183,191,212,213,234,235,256,257,278,279]
            grau = [277,300,322]
            gelb = [248,249,271,272,294,295,296,297,298,318,319]
            braun2 = [100,122,123,144,145,146,167,168,189,190]
            blau = [26,27,28,29,39,40,41,42,48,49,50,51,52,53,60,61,62,63,64,65,69,70,71,72,73,74,75,82,83,84,85,86,87,91,92,93,94,95,96,97,98,103,104,105,106,107,109,112,113,114,115,116,117,118,119,120,121]
            blau2 = [126,127,128,130,131,134,135,136,137,140,141,142,143,148,149,150,152,156,157,158,159,162,163,164,166,170,171,179,180,181,184,185,186,203,204,205,206,209,210]
            blau3 = [224,229,230,231,232,251,252,253,292,320,342,363,364,365]
            self.black(schwarz)
            self.black(schwarz2)
            self.white(weiss)
            self.brown(braun)
            self.gray(grau)
            self.yellow(gelb)
            self.brown2(braun2)
            self.blue(blau)
            self.blue(blau2)
            self.blue(blau3)
class Raupy(Pokedesign):
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
        def lightgreen(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'lime green', outline = 'lime green')
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
            for i in range(0,17):
                    for q in range(0,14):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [4,17,19,21,22,31,33,34,37,45,47,51,58,62,63,64,66,72,74,75,81,85,89,92,95,99,105,106,109,114,118,123,125,129,130,131,132,136,138,140,144,147,148,149,150,152,154,158,164,165,166,168,173,177,179,181,188,189,190,194,195,203,207,208,218,219,220]
            weiss = [91]
            gelb = [59,73,77,78,90,93,104,107,119,120]
            rot = [18,32,35,36,46,48,49,50,60,61]
            hellgruen = [88,100,101,103,115,117,139,145,146,153,159,160,161,162,167,174,175]
            self.black(schwarz)
            self.white(weiss)
            self.yellow(gelb)
            self.red(rot)
            self.lightgreen(hellgruen)
class Hornliu(Pokedesign):
        global colors
        colors = list()
        def black(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'black', outline = 'black')
                colors.append(x[i]-1)
        def gray(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'gray64', outline = 'gray64')
                colors.append(x[i]-1)
        def pink(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'maroon1', outline = 'maroon1')
                colors.append(x[i]-1)
        def brown(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'orange2', outline = 'orange2')
                colors.append(x[i]-1)
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,18):
                    for q in range(0,16):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [4,5,20,22,23,24,36,39,41,42,51,52,55,59,67,69,70,75,82,92,98,99,104,108,113,116,119,120,124,129,133,139,146,149,155,163,164,169,170,174,176,159,181,182,183,184,187,189,192]
            schwarz2 = [197,203,205,207,214,218,220,222,231,232,233,238,248,253,254,264,268,269,281,282,283]
            rosa = [114,115,130,131,132,147,148,198,201,266]
            weiss = [103]
            grau = [21,37,38,53,54,175,190,191,206]
            braun = [40,56,57,58,68,71,72,73,74,83,84,85,86,87,88,89,90,91,100,101,102,105,106,107,117,118,121,122,134,135,136,123,137,138,150,151,152,153,154,165,166,167,168,185,186,199,200,202,215,216,217]
            braun2 = [219,221,234,235,236,237,249,250,251,252,265,267]
            self.black(schwarz)
            self.black(schwarz2)
            self.pink(rosa)
            self.white(weiss)
            self.gray(grau)
            self.brown(braun)
            self.brown(braun2)
class Pikachu(Pokedesign):
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
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [6,7,17,25,27,36,38,45,47,55,59,64,67,72,73,74,79,84,87,90,91,94,98,103,108,109,113,117,122,132,133,136,141,152,154,157,161,162,172,175,177,181,187,193,194,196,202,206,207,213,214,215]
            schwarz2 = [223,234,242,254,263,264,270,274,284,289,294,303,305,310,314,323,324,325,326,327,333,348,349,350,352,353,369,373,390,391,392,393]
            weiss = [142,186]
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
class Raichu(Pokedesign):
        global colors
        colors = list()
        def lightyellow(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'yellow', outline = 'yellow')
                colors.append(x[i]-1)
        def black(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'black', outline = 'black')
                colors.append(x[i]-1)
        def yellow(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'gold', outline = 'gold')
                colors.append(x[i]-1)
        def brown(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'brown', outline = 'brown')
                colors.append(x[i]-1)
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def orange(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'orange', outline = 'orange')
                colors.append(x[i]-1)
        def lightbrown(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'chocolate3', outline = 'chocolate3')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,24):
                    for q in range(0,25):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [7,31,32,55,57,80,82,89,90,91,92,93,96,104,107,112,113,117,120,122,129,131,136,141,145,147,154,155,156,157,158,160,165,170,173,178,179,184,189,195,198,202,209,215,216,220,224,227,234,235,239,241,243,244,245,249,251,260,261,262,263]
            schwarz2 = [268,270,275,276,283,289,294,298,300,302,307,308,314,319,322,324,325,328,340,345,347,352,354,360,365,371,372,377,379,383,384,391,397,403,404,405,407,416,422,423,430,432,436,441,448,455,458,459,460,466,467,473,479,481,482,483,490,492,493,497,498,504,505,506,507]
            schwarz3 = [509,514,518,519,520,521,522,535,536,537,540,559,564,585,586,587,588]
            weiss = [282,380,381,406,431,457,484,485]
            braun = [56,81,105,106,114,115,116,130,137,138,161,162,185,186,210,211,236,237,364,408,415,433,434,439,440,480,560,561,562,563]
            gelb = [139,212,180,181,182,183,203,204,205,206,207,208,228,229,230,231,232,233,252,253,254,255,256,258,259,269,271,277,279,280,281,284,285,286,287,288,295,296,303,304,305,306,311,312,313,320,321,331,332,333,336,337,338,346,355,356,357,358,359]
            gelb2 = [361,362,363,382,385,386,387,409,410,411,435]
            hellgelb = [121,140,146,163,164,171,172,187,188,196,197,213,214,221,222,223,238,246,247,248,272,273,274,297,299,309,310,334,335]
            orange1 = [257,329,330,339,353,378,388,389,390,412,413,414,437,438,456,461,462,463,464,486,487,488,489,510,511,512,538,539]
            hellbraun = [278,465,513]
            self.black(schwarz)
            self.black(schwarz2)
            self.black(schwarz3)
            self.white(weiss)
            self.brown(braun)
            self.yellow(gelb)
            self.yellow(gelb2)
            self.orange(orange1)
            self.lightyellow(hellgelb)
            self.lightbrown(hellbraun)
