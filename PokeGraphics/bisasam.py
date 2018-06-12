from tkinter import *
top = Tk()
c = Canvas(top,width=500,height=500,bg = "white")
c.pack()
graphic = list()
colors = list()
hellgruen = [56,58,78,131,152,153,154,173,174,175,176,193,194,196,199,215,216,217,218,219,220,221,222,223,236,237,238,240,241,242,243,255,256,257,258,260,263,264,277,278,279,280,285,299,300,301,305]
schwarz = [35,36,37,55,57,59,74,75,76,80,93,94,96,98,100,102,103,110,113,116,119,121,125,130,132,133,134,136,140,143,147,151,156,157,160,165,168,172,179,181,186,189,192,201,202,203,207,209,212]
schwarz2 = [213,224,227,228,229,233,234,244,246,247,248,252,254,261,262,270,273,275,281,287,289,291,292,293,297,302,307,311,319,320,327,332,342,343,344,345,346,347,348,349,353,371,372,373]
dunkelgruen = [77,79,95,97,99,101,114,115,117,118,120,122,123,124,135,137,138,139,141,142,144,145,146,155,158,159,161,162,163,164,166,167,177,178,180,182,183,184,185,187,188,195,197,198,200,204,205,206]
dunkelgruen2 = [208,214,225,226,230,235,239,245,249,250,251,259,265,266,267,268,269,271,272,276,286,288,290,298,306,308,309,310,311,321,322,323,324,325,326,328,329,330,331,351]
rot = [282,303]
def graphics(groesse):
    if groesse == 1:
        for q in range(0,20):
            for i in range(0,21):
                id1 = c.create_rectangle(i*5+3,q*5+3,i*5+8,q*5+8,fill="white",outline="white")
                graphic.append(id1)
    elif groesse == 2:
        for q in range(0,32):
            for i in range(0,32):
                id1 = c.create_rectangle(i,q,i+1,q+1,fill="white",outline="white")
                graphic.append(id1)
    elif groesse == 3:
        for q in range(0,64):
            for i in range(0,64):
                id1 = c.create_rectangle(i,q,i+1,q+1,fill="white",outline="white")
                graphic.append(id1)
def lightgreen(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'lime green', outline = 'lime green')
        colors.append(x[i]-1)
def black(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'black', outline = 'black')
        colors.append(x[i]-1)
def darkgreen(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'forest green', outline = 'forest green')
        colors.append(x[i]-1)
def red(x):
    for i in range(len(x)):
        c.itemconfig([x[i]-1], fill = 'red', outline = 'red')
        colors.append(x[i]-1)
def norm():
    black(schwarz)
    black(schwarz2)
    lightgreen(hellgruen)
    darkgreen(dunkelgruen)
    darkgreen(dunkelgruen2)
    red(rot)
graphics(1)
norm()
top.mainloop()
