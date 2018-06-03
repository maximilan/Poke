from pokemon_data import Tile, Player, Wildnis, Hindernis, Setting, Tür
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
############
kastengröße = 25
current_key = None
player = None
############
window = tk.Tk()
c = Canvas(width = 500, height = 500, background = 'black')
c.pack()
q1 = [3,1,1,1,1,1,1,1,1,1,1,2]
q2 = [0,1,0,1,0,0,0,0,0,0,0,0]
q3 = [0,1,1,1,0,0,0,0,0,0,0,0]
q = [q1,q2,q3]
p1 = [0,0,0,0,0,0,1,0,0,0,0,0]
p2 = [0,0,0,0,0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0,0,0,0,0]
p = [p1,p2,p3]
speech = ["Hallo! Ich bin Tom"]
setting1 = Setting(q, p, speech)
q1 = [0,1,3,1,0,1,1,1]
q2 = [0,1,0,1,1,1,0,1]
q3 = [0,1,1,1,0,1,1,2]
q = [q1,q2,q3]
p1 = [0,0,0,0,0,0,1,0]
p2 = [0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0]
p = [p1,p2,p3]
speech = ["Hallo! Ich heiße Bob!"]
setting2 = Setting(q,p,speech)
setting1.link([setting2])
setting2.link([setting1])

def setting(liste):
    global player
    global setting2
    del tiles[:]
    del coordinates[:]
    y = 0
    playdata = []
    for i in range(len(liste[0])):
        x = 0
        for f in range(len(liste[0][i])):
            #Tile erzeugen
            if liste[0][i][f] == 1:
                id1 = Wildnis(c, x, y)
                tiles.append(id1)
                coordinates.append([x, y])
            #Hindernis erzeugen
            if liste[0][i][f] == 0:
                id1 = Hindernis(c,x,y)
            #Personen erzeugen
            if liste[1][i][f] == 1:
                person = liste[2].pop(0)
                id1.add_person(person)
                liste[2].append(person)
            if liste[0][i][f] == 2:
                print("Tür")
                print(liste[3][0])
                link = liste[3].pop(0)
                id1 = Tür(c, x, y, link)
                liste[3].append(link)
                tiles.append(id1)
                coordinates.append([x,y])
            if liste[0][i][f] == 3:
                id1 = Wildnis(c, x, y)
                tiles.append(id1)
                coordinates.append([x,y])
                playdata = [x, y, id1]
            x += 25
        y += 25
    player = Player(c, playdata[0], playdata[1], playdata[2])
    for tile in tiles:
        tile.get_function(coordinates, tiles)
        y += 25
print(setting1.return_all())
setting(setting1.return_all())
window.update()


def movement(event):
    global current_key
    key = event.keysym
    current_key = key
c.bind_all('<Key>', movement)
while True:
    if player.return_current_tile().return_function() == "Tür":
        c.delete("all")
        setting(player.return_current_tile().return_setting().return_all())
    player.move(current_key)
    current_key = None
    window.update()
    sleep(0.1)
