kastengröße = 25
kastengröße = 25
trainerblack = [1,2,3,4,5,6,7,8,9,10]
id1 = list()
colors = list()
class Tile():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'black')
        self.design = [id1]
        self.coordinates = [x, y]
        self.x = x
        self.y = y
        self.directions = []
        self.neighbor_tiles = {}
        self.person = None
        self.function = None
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
        self.person = Person(self.canvas, self.x, self.y)
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

class Wildnis(Tile):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.function = "Wildnis"
        for i in range(len(self.design)):
            self.canvas.itemconfig(self.design, fill = 'green')
        self.canvas.create_rectangle(x,y,x+25,y+6,fill="green4",outline="green4")
        self.canvas.create_rectangle(x,y+6,x+25,y+12,fill="green2",outline="green2")
        self.canvas.create_rectangle(x,y+12,x+25,y+18,fill="green4",outline="green4")
        self.canvas.create_rectangle(x,y+18,x+25,y+25,fill="green2",outline="green2")

class Hindernis(Tile):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
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
    def __init__(self, canvas, x, y, linked_setting):
        super().__init__(canvas, x, y)
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
    
    def __init__(self, canvas, current_tile):
        global id1
        colors = list()
        self.canvas = canvas
        for i in range (0,25):
            for q in range (0,25):
                id2 = self.canvas.create_rectangle(0+i*1,0+q*1,0+i*1+1,0+q*1+1,fill="red",outline="red")
                id1.append(id2)
        self.schwarz(trainerblack)
        self.design = id1
        self.current_tile = current_tile
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
        if self.current_tile.persons() == True:
            self.current_tile.return_persons().speak()
    def return_current_tile(self):
        return self.current_tile
class Person():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'purple')
        self.design = (id1)
        self.speech = None
        self.x = x
        self.y = y
    def set_speech(self, speech):
        self.speech = speech
    def speak(self):
        print(self.speech)

class Setting():
    def __init__(self, tiles, persons, speech, links):
        self.all = [tiles, persons, speech, links]
    def return_all(self):
        return self.all
