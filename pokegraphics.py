from tkinter import *
from time import sleep

class Pokedesign():
        def __init__(self, name, canvas, function, module):
                self.canvas = canvas
                self.module = module
                if name == "Bisasam":
                        id1 = Bisasam(canvas)
                elif name == "Bisaknosp":
                        id1 = Bisaknosp(canvas)
                elif name == "Bisaflor":
                        id1 = Bisaflor(canvas)
                elif name == "Glumanda":
                        id1 = Glumanda(canvas)
                elif name == "Schiggy":
                        id1 = Schiggy(canvas)
                elif name == "Raupy":
                        print("Hello World!")
                        id1 = Raupy(canvas)
                elif name == "Hornliu":
                        id1 = Hornliu(canvas)
                elif name == "Pikachu":
                        id1 = Pikachu(canvas)
                elif name == "Raichu":
                        id1 = Raichu(canvas)
                elif name == "Sandan":
                        id1 = Sandan(canvas)
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
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/001.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Bisaknosp(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/002.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Bisaflor(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/003.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Glumanda():
         def __init__(self,canvas):
             self.graphic = list()
             self.canvas = canvas
             global img
             img = PhotoImage(file = "Pokemonsprites/004.png")
             self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
             self.canvas.update()
class Glutexo(Pokedesign):
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
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'firebrick1', outline = 'firebrick1')
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
            for i in range(0,25):
                    for q in range(0,22):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [15,36,38,58,60,75,76,79,83,96,99,101,106,117,121,123,128,137,138,142,146,149,158,163,164,168,171,179,187,191,194,201,205,208,214,217,222,226,231,236,240,243,247,248,254,255,259,262]
            schwarz2 = [265,273,278,279,281,285,288,292,293,294,297,302,307,311,312,314,315,320,324,329,332,335,336,337,341,346,350,353,358,360,362,367,369,372,375,378,379,380,383,388,391,393,398,399,402,406,409,413,414,425,426,427,429,430,435,452,456,474,478,497,498,499]
            rot = [37,59,80,81,82,102,104,105,124,126,127,148]
            weiss = [227,249]
            grau = [354,377,403,405,475,477]
            gelb = [103,125,147,295,316,317,318,338,339,340,361]
            orange1 = [97,98,118,119,120,139,140,141,159,160,161,162,169,170,180,181,182,183,184,185,186,192,193,202,203,204,206,207,215,216,223,224,225,228,229,230,237,238,239,244,245,246,250,251,252,253,260,261,266,267,268,269,270,271,272,274,275,276,277,282,283,284,289,290,291,296,298,299,300,301]
            orange2 = [303,304,305,306,313,319,321,322,323,325,326,327,328,333,334,342,343,344,345,347,348,349,355,356,357,359,363,364,365,366,368,370,371,376,381,382,384,385,386,387,389,390,392,404,407,408,410,411,412,431,432,433,434,453,454,455,476]
            self.black(schwarz)
            self.black(schwarz2)
            self.red(rot)
            self.white(weiss)
            self.gray(grau)
            self.yellow(gelb)
            self.orange(orange1)
            self.orange(orange2)
class Schiggy(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/007.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Raupy(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/010.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Hornliu(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/013.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
class Pikachu(Pokedesign):
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            global img
            img = PhotoImage(file = "Pokemonsprites/025.png")
            self.image = self.canvas.create_image(20, 20, anchor = NW, image = img)
            self.canvas.update()
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
class Sandan(Pokedesign):
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
        def white(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'white', outline = 'white')
                colors.append(x[i]-1)
        def gray(self,x):
            for i in range(len(x)):
                self.canvas.itemconfig(self.graphic[x[i]-1], fill = 'gray64', outline = 'gray64')
                colors.append(x[i]-1)
        def __init__(self,canvas):
            self.graphic = list()
            self.canvas = canvas
            for i in range(0,18):
                    for q in range(0,20):
                            id1 = self.canvas.create_rectangle(540+q*5,110+i*5,540+q*5+5,110+i*5+5,fill="SpringGreen4",outline="SpringGreen4")
                            self.graphic.append(id1)
            schwarz = [4,23,25,26,27,28,29,30,43,51,52,62,69,73,82,88,90,94,99,101,110,115,118,120,121,122,135,136,137,140,141,147,156,160,161,166,167,170,171,176,179,182,188,189,197,199,203,204,205,210,217,218,226,231,232,237,238,247,257,266,268,276,287,288,289,290,295,296,311,312,314,315,331,335,352,353,354]
            weiss = [102,146,162,183,184,185,186,187,190,208,209,211,227,228,229,230,248,249,250,251,270,271,332,334]
            gelb = [24,44,45,46,47,48,49,50,63,64,65,66,67,68,70,71,72,83,84,85,86,87,89,91,92,93,103,104,105,106,107,108,109,111,112,113,114,119,123,124,125,126,127,128,129,130,131,132,133,134,138,139,142,143,144,145,148,149,150,151,152,153,154,155,157,158,159]
            gelb2 = [163,164,165,168,169,172,173,174,175,177,178,191,192,193,194,195,196,198,212,213,214,215,216,233,234,235,236,252,253,254,255,256,272,273,274,275,292,293,294,313,333]
            grau = [206,207,267,269,291]
            self.black(schwarz)
            self.white(weiss)
            self.yellow(gelb)
            self.yellow(gelb2)
            self.gray(grau)

