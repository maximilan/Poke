#column 1[index 0] = name
#column 2[index 1] = attacks
#column 3[index 2] = Hitpoints

dateihandler = open('pokedex.csv')

inhalt = dateihandler.read()

tabelle  = []

zeilen = inhalt.split('\n')
for i in range(len(zeilen)-1):
    spalten = zeilen[i].split(',')
    tabelle.append(spalten)




