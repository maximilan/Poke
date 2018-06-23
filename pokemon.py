class Key():
    def __init__(self):
        self.current_key = None
    def change_key(self, key):
        self.current_key = key
    def return_current_key(self):
        return self.current_key
#########################################################################
kastengröße = 25
kastengröße = 25
trainerblack = [185,186,187,188,189,190,209,216,233,242,258,267,282,283,284,291,292,293,307,308,310,311,312,313,314,315,317,318,331,333,342,344,356,361,364,369,382,383,386,389,392,393,407,408,409,416,417,418,431,434,435,436,437,438,439,440,441,444,456,459,460,461,462,463,464,465,466,469,482,483,484,487,488,491,492,493,508,510,511,514,515,517,533,537,538,542,559,560,561,564,565,566]
trainerhaut = [316,332,334,335,336,337,338,339,340,341,343,357,358,359,360,362,363,365,366,367,388,384,385,387,388,390,391,410,411,414,415,432,433,442,443,457,458,467,468]
trainerweiss = [286,287,288,289]
trainergreen4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,150,301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425,426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450]
trainergreen2 = [451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625,151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300]
trainerrot = [210,211,212,213,214,215,234,235,236,237,238,239,240,241,259,260,261,262,263,264,265,266,285,290,412,413,485,486,489,490,509,512,513,516,534,535,536,539,540,541]
id1 = list()
colors = list()
from random import randint
from time import sleep
import tkinter as tk
from tkinter import*
from pokegraphics import *
#Pokedex wird eingelesen
dateihandler = open('pokedex.csv')
#Master (für Dateienaustausch zuständig) wird erstellt


inhalt = dateihandler.read()

tabelle  = []
pokemon = []
zeilen = inhalt.split('\n')
for i in range(len(zeilen)-1):
    del pokemon[:]
    spalten = zeilen[i].split(',')
    tabelle.append(spalten)
#Pokedex wrd gespeichert
pokedex = tabelle
        
class Tile():
    def __init__(self, canvas, x, y,module):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'grey')
        self.design = [id1]
        self.coordinates = [x, y]
        self.x = x
        self.y = y
        self.directions = []
        self.neighbor_tiles = {}
        self.person = None
        self.function = None
        self.module = module
    #Koordinaten wiedergeben
    def return_coordinate(self):
        return self.coordinates
    #Tile mit Richtungsvermerk an benachbarten Tile linken
    def link_tile(self, direction, tile):
        self.neighbor_tiles[direction] = tile
    #eigene Koordinaten verändern und wiedergeben
    def dif_coords(self, x, y):
        tupel = self.return_coordinate()
        return [tupel[0]+x, tupel[1]+y]
    #Mit benachbarten Tiles verbinden
    def get_function(self, coordinates, tileslist):
        if self.dif_coords(kastengröße, 0) in coordinates:
            self.directions.append("Right")
            i = coordinates.index(self.dif_coords(kastengröße, 0))
            self.link_tile("Right", tileslist[i])
        if self.dif_coords(-kastengröße, 0) in coordinates:
            self.directions.append("Left")
            i = coordinates.index(self.dif_coords(-kastengröße, 0))
            self.link_tile("Left", tileslist[i])
        if self.dif_coords(0, kastengröße) in coordinates:
            self.directions.append("Down")
            i = coordinates.index(self.dif_coords(0, kastengröße))
            self.link_tile("Down", tileslist[i])
        if self.dif_coords(0, -kastengröße) in coordinates:
            self.directions.append("Up")
            i = coordinates.index(self.dif_coords(0, -kastengröße))
            self.link_tile("Up", tileslist[i])
    #mögliche Richtungen wiedergeben
    def return_directions(self):
        return self.directions
    def return_linked_tile(self, direction):
        return self.neighbor_tiles[direction]
    def add_person(self, speech):
        self.person = Person(self.canvas, self.x, self.y,self.module)
        self.person.set_speech(speech)
    def return_persons(self):
        return self.person
    def persons(self):
        if self.person != None:
            return True
        else:
            return False
    def return_function(self):
        return self.function
    def return_pokemon_level(self):
        return int(self.pokemon_level)
    def check_pokemon(self,posibpoke):
        pokemon = None
        for i in range(len(pokedex)):
            if pokedex[i][0] in posibpoke:
               if randint(1, int(pokedex[i][2])) == 1:
                   pokemon = pokedex[i][0]
                   break
        return pokemon
                   
        

class Wildnis(Tile):
    def __init__(self, canvas, x, y, pokemon, pokemon_level,module):
        self.module = module
        super().__init__(canvas, x, y,module)
        self.function = "Wildnis"
        self.pokemon = pokemon
        self.pokemon_level = pokemon_level
        
        for i in range(len(self.design)):
            self.canvas.itemconfig(self.design, fill = 'green')
        self.canvas.create_rectangle(x,y,x+25,y+6,fill="green4",outline="green4")
        self.canvas.create_rectangle(x,y+6,x+25,y+12,fill="green2",outline="green2")
        self.canvas.create_rectangle(x,y+12,x+25,y+18,fill="green4",outline="green4")
        self.canvas.create_rectangle(x,y+18,x+25,y+25,fill="green2",outline="green2")

class Hindernis(Tile):
    def __init__(self, canvas, x, y,module):
        super().__init__(canvas, x, y,module)
        self.function = "Hindernis"
        for i in range(len(self.design)):
            self.canvas.itemconfig(self.design, fill = 'grey')
        for i in range(0,5):
            self.canvas.create_oval(x+i*5,y-2,x+i*5+5,y+3,fill="green4",outline="green4")
            self.canvas.create_oval(x+i*5,y+23,x+i*5+5,y+28,fill="green4",outline="green4")
        for i in range(0,5):
            self.canvas.create_oval(x-2,y+i*5,x+3,y+i*5+5,fill="green4",outline="green4")
            self.canvas.create_oval(x+27,y+i*5,x+22,y+i*5+5,fill="green4",outline="green4")
        self.canvas.create_rectangle(x,y,x+25,y+25,fill="green4",outline="green4")
class Tür(Tile):
    def __init__(self, canvas, x, y, linked_setting,module):
        self.module = module
        super().__init__(canvas, x, y,module)
        self.linked_setting = linked_setting
        self.function = "Tür"
    def return_setting(self):
        return self.linked_setting
class Player():
    def haut(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'papaya whip', outline = 'papaya whip')
            colors.append(x[i]-1)
    def rot(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'red', outline = 'red')
            colors.append(x[i]-1)
    def schwarz(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'black', outline = 'black')
            colors.append(x[i]-1)
    
    def weiss(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'white', outline = 'white')
            colors.append(x[i]-1)
    def green2(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'green2', outline = 'green2')
            colors.append(x[i]-1)
    def green4(self,x):
        for i in range(len(x)):
            self.canvas.itemconfig(id1[x[i]-1], fill = 'green4', outline = 'green4')
            colors.append(x[i]-1)
    def __init__(self, canvas, x, y,current_tile, pokemon, window):
        global id1
        del id1[:]
        colors = list()
        self.canvas = canvas
        for q in range (0,25):
            for i in range (0,25):
                id2 = self.canvas.create_rectangle(x+i*1,y+q*1,x+i*1+1,y+q*1+1,fill="red",outline="red")
                id1.append(id2)
        self.green4(trainergreen4)
        self.green2(trainergreen2)
        self.schwarz(trainerblack)
        self.haut(trainerhaut)
        self.weiss(trainerweiss)
        self.rot(trainerrot)
        self.design = id1
        self.current_tile = current_tile
        self.posibpoke = pokemon
        self.pokemon = []
        self.window = window
    def beweg(self, x, y):
        for design in self.design:
            self.canvas.move(design, x, y)
    def move(self, direction):
        if direction in self.current_tile.return_directions():
            self.current_tile = self.current_tile.return_linked_tile(direction)
            if direction == 'Up':
                self.beweg(0, -kastengröße)
            elif direction == 'Down':
                self.beweg(0, kastengröße)
            elif direction == 'Left':
                self.beweg(-kastengröße, 0)
            elif direction == 'Right':
                self.beweg(kastengröße, 0)
            self.window.update()
            #Pokemon suchen und bekämpfen
            pokemon = self.current_tile.check_pokemon(self.return_posibpoke())
            if pokemon != None:
                print("Ein wildes "+pokemon+" (Level "+str(self.current_tile.return_pokemon_level())+") erscheint.")
                self.pokemon[0].fight(pokemon, self.current_tile.return_pokemon_level())
            #Mit Personen reden
            if self.current_tile.persons() == True:
                self.current_tile.return_persons().speak(self)
    def return_current_tile(self):
        return self.current_tile
    def return_posibpoke(self):
        return self.posibpoke
    def return_pokemon(self):
        return self.pokemon
    def return_pokemon_names(self):
        names = []
        for pokemon in self.pokemon:
            names.append(pokemon.return_name())
        return names
    def add_pokemon(self, name, level, hp):
        self.pokemon.append(Pokemon(name, level, hp))
    def add_new_pokemon(self, name, level):
        for pokemon in pokedex:
            if name in pokemon:
                self.pokemon.append(Pokemon(name, level, pokemon[1]))
        self.write()
    
    #Pokemon speichern
    def write(self):
         dateihandler = open("PlayerPoke", "w")
         dateihandler.write("")
         for pokemon in self.pokemon:
             dateihandler.write(pokemon.return_name()+";"+str(pokemon.return_level())+";"+str(pokemon.return_hp()))
             dateihandler.write("\n")
    def load_pokemon(self):
        dateihandler = open("PlayerPoke", "r")
        del self.pokemon[:]
        for line in dateihandler:
            id1 = line.rstrip()
            pokemon = id1.split(";")
            self.add_pokemon(pokemon[0], pokemon[1], pokemon[2])
class Person():
    def __init__(self, canvas, x, y,module):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'purple')
        self.design = (id1)
        self.speech = None
        self.x = x
        self.y = y
        self.module = module
    def set_speech(self, speech):
        self.speech = speech
    def speak(self, player):
        print(self.speech)
        #self.module = module
        print("Möchtest du kämpfen?")
        fight = menu(["Ja", "Nein"])
        if fight == "Ja":
            self.canvas.delete("all")
            self.canvas.config(width=700,height=700)
            self.canvas.create_rectangle(0,0,700,700,fill="SpringGreen4",outline="SpringGreen4")
            
            self.canvas.create_line(0,57,700,607,fill="white")
            self.canvas.create_oval(290,290,460,420,fill="SpringGreen4",outline="white")
            self.canvas.create_polygon(610,0,700,0,700,70,fill="gray",outline="grey")
            self.module.update()
            allpoke = []
            for possesion in player.return_pokemon():
                allpoke.append(possesion.return_name())
            pokemon = menu(allpoke)
            print(pokemon)
            #Pokemon wird auf Besitz überprüft
            for possesion in player.return_pokemon():
                if possesion.return_name() == pokemon:
                    Pokedesign(pokemon, self.canvas)
            
            self.module.update()
        elif fight == "Nein":
            print("Ok. Vielleicht ein anderes mal!")
        else:
            print("Der Befehl existiert nicht")
class Setting():
    def __init__(self, tiles, persons, speech, pokemon, level):
        self.all = [tiles, persons, speech,pokemon, level]
    def return_all(self):
        return self.all
    def link(self, link):
        self.all.append(link)

class Pokemon():
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.attackennamen = []
        self.attacken = {}
        for i in range(len(pokedex)):
            if self.name in pokedex[i]:
                if hp == None:
                    self.hp = int(pokedex[i][1])
                else:
                    self.hp = int(hp)
                for q in range(3, len(pokedex[i]), +2):
                    self.attackennamen.append(pokedex[i][q])
                    self.attacken[pokedex[i][q]] = pokedex[i][q+1]
    def return_attackennamen(self):
        return self.attackennamen
    def return_attackenstärke(self, name):
        return int(self.attacken[name])
    def change_hp(self, change):
        self.hp += int(change)
    def return_name(self):
        return self.name
    def return_hp(self):
        return self.hp
    def return_level(self):
        return int(self.level)
    def angriff(self, attacke, pokemon):
        if attacke in self.attackennamen:
            stärke = int(self.return_attackenstärke(attacke))
            stärke += round(self.return_attackenstärke(attacke)/10) * self.return_level()
            print(self.name+" wendet "+str(attacke)+ " an.")
            sleep(0.5)
            pokemon.change_hp(-stärke)
            print(pokemon.return_name()+" besitzt noch "+str(pokemon.return_hp())+ " HP.")
            sleep(0.5)
            if pokemon.return_hp() <= 0:
                print(pokemon.return_name()+" wurde ohnmächtig.")
                return True
            else:
                return False
    def randattack(self, pokemon):
        attack = randint(0, len(self.attackennamen)-1)
        attack = self.attackennamen[attack]
        return self.angriff(attack, pokemon)
                  
    def fight(self, pokemon, level):
        pokemon = Pokemon(pokemon, level, None)
        print("Folgende Attacken stehen dir zur Verfügung:")
        for i in range(len(self.attackennamen)):
            print(self.attackennamen[i])
        kill = False
        while kill != True:
            attacke = input("Welche Attacke soll "+str(self.name)+" anwenden: ")
            kill = self.angriff(attacke, pokemon)
            sleep(1)
            if kill != True:
                  kill = pokemon.randattack(self)
        if self.return_hp() <= 0:
              print("Du hast verloren!")    

class Choice():
    def __init__(self, optionen, canvas,module):
        global current_key
        self.canvas = canvas
        self.design = self.canvas.create_rectangle(0, 550, 700, 700, fill = 'white')
        self.module = module
        self.current_choice = None
        while len(optionen) < 6:
            optionen.append("")
        choices = list()
        coords = list()
        for i in range(2):
            for q in range(3):
                coordinates = [0 + q*220+140, 550+i*50+50]
                text = str(optionen.pop(0))
                if i == 0 and q == 0:
                    id2 = self.canvas.create_text(coordinates,text = text, fill = 'red', font = ('Lato Black', 17))
                else:
                    id2 = self.canvas.create_text(coordinates,text = text, fill = 'black', font = ('Lato Black', 17))
                id1 = Option(id2, self.canvas, coordinates, text)
                coords.append(coordinates)
                choices.append(id1)
        for i in range(len(choices)):
            choices[i].link(coords, coords[i], choices)
        self.current_choice = choices[0]
        while True:
            self.module.update()
            key = current_key
            current_key = None
            if key in ["Left", "Right", "Up", "Down"]:
                self.current_choice = self.current_choice.switch(key)
            if key == "z":
                break
            sleep(0.1)
        for choice in choices:
            choice.delete_design()
        self.canvas.delete(self.design)
    def return_choice(self):
        return self.current_choice.return_text()
class Option():
    def __init__(self, design, canvas, coordinates, text):
        self.design = design
        self.canvas = canvas
        self.coordinates = coordinates
        self.directions = []
        self.links = {}
        self.text = text
    def change_coords(self, x, y):
        id1 = self.coordinates[0]+x
        id2 = self.coordinates[1]+y
        return[id1, id2]
    def return_design(self):
        return self.design
    def link(self, liste, position, objects):
        coords = self.change_coords(220, 0)
        if coords in liste:
            self.directions.append("Right")
            self.links["Right"] = objects[liste.index(coords)]
            
        coords = self.change_coords(-220, 0)
        if coords in liste:
            self.directions.append("Left")
            self.links["Left"] = objects[liste.index(coords)]

        coords = self.change_coords(0, 50)
        if coords in liste:
            self.directions.append("Down")
            self.links["Down"] = objects[liste.index(coords)]

        coords = self.change_coords(0, -50)
        if coords in liste:
            self.directions.append("Up")
            self.links["Up"] = objects[liste.index(coords)]
    def switch(self, direction):
        if direction in self.directions:
            self.canvas.itemconfig(self.design, fill = 'black')
            new_choice = self.links[direction]
            self.canvas.itemconfig(new_choice.return_design(), fill = 'red')
            return new_choice
        else:
            return self
    def return_text(self):
        return self.text
    def delete_design(self):
        self.canvas.delete(self.design)

##########################################################################

#from pokemon_data import *
from tkinter import *
import tkinter as tk
from time import sleep


##########
setting1 = None
setting2 = None
setting3 = None
##########
tiles = list()
coordinates = list()
current_pokemon = []
############
kastengröße = 25
current_key = None
player = None
############
window = tk.Tk()
c = Canvas(width = 700, height = 700, background = 'black')
c.pack()
q1 = [3,1,1,1,1,1,1,1,1,1,2,0]
q2 = [0,1,0,1,0,0,0,0,0,0,0,0]
q3 = [0,1,1,1,0,0,0,0,0,0,0,0]
q = [q1,q2,q3]
p1 = [0,1,0,0,0,0,0,0,0,0,0,0]
p2 = [0,0,0,0,0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0,0,0,0,0]
p = [p1,p2,p3]
pokemon = ["Schiggy"]
speech = ["Hallo! Ich bin Tom"]
setting1 = Setting(q, p, speech, pokemon, 2)
q1 = [0,1,3,1,0,1,1,1]
q2 = [0,1,0,1,1,1,0,1]
q3 = [0,1,1,1,0,1,1,2]
q = [q1,q2,q3]
p1 = [0,0,0,0,0,0,1,0]
p2 = [0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0]
p = [p1,p2,p3]
speech = ["Hallo! Ich heiße Bob!"]
pokemon = ["Schiggy", "Glurak"]
setting2 = Setting(q,p,speech, pokemon, 3)
setting1.link([setting2])
setting2.link([setting1])
######################
def setting(liste):
    global player
    global setting2
    del tiles[:]
    del coordinates[:]
    y = 0
    playdata = []
    #Pokemon aufnehmen
    current_pokemon = liste[3]
    current_level = liste[4]
    for i in range(len(liste[0])):
        x = 0
        for f in range(len(liste[0][i])):
            #Tile erzeugen
            if liste[0][i][f] == 1:
                id1 = Wildnis(c, x, y, current_pokemon, current_level,window)
                tiles.append(id1)
                coordinates.append([x, y])
            #Hindernis erzeugen
            if liste[0][i][f] == 0:
                id1 = Hindernis(c,x,y,window)
            #Personen erzeugen
            if liste[1][i][f] == 1:
                person = liste[2].pop(0)
                id1.add_person(person)
                liste[2].append(person)
            #Portale erzeugen    
            if liste[0][i][f] == 2:
                link = liste[len(liste)-1].pop(0)
                id1 = Tür(c, x, y, link,tk)
                liste[len(liste)-1].append(link)
                tiles.append(id1)
                coordinates.append([x,y])
            #Daten für Spieler speichern
            if liste[0][i][f] == 3:
                id1 = Wildnis(c, x, y, current_pokemon, current_level,window)
                tiles.append(id1)
                coordinates.append([x,y])
                playdata = [x, y, id1]
            x += 25
        y += 25
    #Spieler erstellen
    player = Player(c, playdata[0], playdata[1], playdata[2], current_pokemon,window)
    for tile in tiles:
        tile.get_function(coordinates, tiles)
        y += 25
################
def menu(optionen):
    id1 = Choice(optionen, c, window)
    return id1.return_choice()
################
setting(setting1.return_all())
window.update()


def movement(event):
    global current_key
    key = event.keysym
    current_key = key
    keysaver.change_key(key)
c.bind_all('<Key>', movement)


player.add_new_pokemon("Pikachu", 13)
player.add_new_pokemon("Raupy",5)
player.add_new_pokemon("Schiggy", 5)
player.add_new_pokemon("Raichu", 4)
#Tastenspeicehr wird initialisiert
keysaver = Key()
#Hauptschleife
while True:
    player.load_pokemon()
    if player.return_current_tile().return_function() == "Tür":
        c.delete("all")
        player.write()
        setting(player.return_current_tile().return_setting().return_all())
        player.load_pokemon()
    player.move(current_key)
    current_key = None
    window.update()
    sleep(0.1)












