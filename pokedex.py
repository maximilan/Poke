dateihandler = open('pokedex.csv')

inhalt = dateihandler.read()

tabelle  = []

zeilen = inhalt.split('\n')
for i in range(len(zeilen)):
    spalten = zeilen[i].split(',')
    tabelle.append(spalten)



