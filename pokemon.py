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
current_pokemon = []
############
kastengröße = 25
current_key = None
player = None
############
window = tk.Tk()
c = Canvas(width = 500, height = 500, background = 'black')
c.pack()
q1 = [3,1,1,1,1,1,1,1,1,1,2,0]
q2 = [0,1,0,1,0,0,0,0,0,0,0,0]
q3 = [0,1,1,1,0,0,0,0,0,0,0,0]
q = [q1,q2,q3]
p1 = [0,0,0,0,0,0,1,0,0,0,0,0]
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
                id1 = Wildnis(c, x, y, current_pokemon, current_level)
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
            #Portale erzeugen    
            if liste[0][i][f] == 2:
                link = liste[len(liste)-1].pop(0)
                id1 = Tür(c, x, y, link)
                liste[len(liste)-1].append(link)
                tiles.append(id1)
                coordinates.append([x,y])
            #Daten für Spieler speichern
            if liste[0][i][f] == 3:
                id1 = Wildnis(c, x, y, current_pokemon, current_level)
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
        
setting(setting1.return_all())
window.update()


def movement(event):
    global current_key
    key = event.keysym
    current_key = key
c.bind_all('<Key>', movement)
player.add_new_pokemon("Glurak", 20)
while True:
    if player.return_current_tile().return_function() == "Tür":
        c.delete("all")
        player.write()
        setting(player.return_current_tile().return_setting().return_all())
        player.load_pokemon()
    player.move(current_key)
    current_key = None
    window.update()
    sleep(0.1)
