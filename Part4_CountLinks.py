# Change-Log:
# - Wenn UnshortenIt Fehler hat (row[9]), greift Skript automatisch auf Spalte mit eigenen Ergebnissen (row[8]) zurück
# - Speicherort verändert
# - ergebnisliste.append Reihenfolge verändert
# - ergebnisliste.append fraktionslos deaktiviert


import csv

ergebnisse = {'AfD': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'CDU': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'CSU': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'FDP': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'fraktionslos': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'GRÜNE': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'LINKE': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}, 'SPD': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'heute.de': 0, 'deutschlandfunk.de': 0}}

with open('CSV_Sublime\LinksCOMPLETE.csv', newline='', encoding='utf-8') as csvfile:
	linereader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in linereader:

		party = row[2]
		url = row[9]

		if url == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":
			url = row[8]

		if party == 'AfD':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['AfD']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['AfD']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['AfD']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['AfD']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['AfD']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['AfD']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['AfD']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['AfD']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['AfD']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['AfD']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['AfD']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['AfD']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['AfD']['deutschlandfunk.de'] += 1

		
		if party == 'CDU':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['CDU']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['CDU']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['CDU']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['CDU']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['CDU']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['CDU']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['CDU']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['CDU']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['CDU']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['CDU']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['CDU']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['CDU']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['CDU']['deutschlandfunk.de'] += 1

		
		if party == 'CSU':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['CSU']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['CSU']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['CSU']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['CSU']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['CSU']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['CSU']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['CSU']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['CSU']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['CSU']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['CSU']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['CSU']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['CSU']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['CSU']['deutschlandfunk.de'] += 1

		
		if party == 'FDP':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['FDP']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['FDP']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['FDP']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['FDP']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['FDP']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['FDP']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['FDP']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['FDP']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['FDP']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['FDP']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['FDP']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['FDP']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['FDP']['deutschlandfunk.de'] += 1

		
		if party == 'fraktionslos':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['fraktionslos']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['fraktionslos']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['fraktionslos']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['fraktionslos']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['fraktionslos']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['fraktionslos']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['fraktionslos']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['fraktionslos']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['fraktionslos']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['fraktionslos']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['fraktionslos']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['fraktionslos']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['fraktionslos']['deutschlandfunk.de'] += 1

		
		if party == 'GRÜNE':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['GRÜNE']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['GRÜNE']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['GRÜNE']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['GRÜNE']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['GRÜNE']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['GRÜNE']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['GRÜNE']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['GRÜNE']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['GRÜNE']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['GRÜNE']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['GRÜNE']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['GRÜNE']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['GRÜNE']['deutschlandfunk.de'] += 1


		if party == 'LINKE':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['LINKE']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['LINKE']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['LINKE']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['LINKE']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['LINKE']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['LINKE']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['LINKE']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['LINKE']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['LINKE']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['LINKE']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['LINKE']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['LINKE']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['LINKE']['deutschlandfunk.de'] += 1


		if party == 'SPD':

			if '.bild.de' in url or url == 'bild.de':
				ergebnisse['SPD']['bild.de'] += 1

			if  '.spiegel.de' in url or url == 'spiegel.de':
				ergebnisse['SPD']['spiegel.de'] += 1

			if '.focus.de' in url or url == 'focus.de':
				ergebnisse['SPD']['focus.de'] += 1

			if '.n-tv.de' in url or url == 'n-tv.de':
				ergebnisse['SPD']['n-tv.de'] += 1

			if '.welt.de' in url or url == 'welt.de':
				ergebnisse['SPD']['welt.de'] += 1

			if '.zeit.de' in url or url == 'zeit.de':
				ergebnisse['SPD']['zeit.de'] += 1

			if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
				ergebnisse['SPD']['sueddeutsche.de'] += 1

			if '.stern.de' in url or url == 'stern.de':
				ergebnisse['SPD']['stern.de'] += 1

			if '.faz.net' in url or url == 'faz.net':
				ergebnisse['SPD']['faz.net'] += 1

			if '.taz.de' in url or url == 'taz.de':
				ergebnisse['SPD']['taz.de'] += 1

			if '.tagesschau.de' in url or url == 'tagesschau.de':
				ergebnisse['SPD']['tagesschau.de'] += 1

			if '.heute.de' in url or url == 'heute.de':
				ergebnisse['SPD']['heute.de'] += 1

			if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
				ergebnisse['SPD']['deutschlandfunk.de'] += 1

	print (ergebnisse)

ergebnisliste = [['Partei', 'bild.de', 'spiegel.de', 'focus.de', 'n-tv.de', 'welt.de', 'zeit.de', 'sueddeutsche.de', 'stern.de', 'faz.net', 'taz.de', 'tagesschau.de', 'heute.de', 'deutschlandfunk.de']]

AfD = ergebnisse['AfD'].items()
AfD_liste = ['AfD']

CDU = ergebnisse['CDU'].items()
CDU_liste = ['CDU']

CSU = ergebnisse['CSU'].items()
CSU_liste = ['CSU']

FDP = ergebnisse['FDP'].items()
FDP_liste = ['FDP']

fraktionslos = ergebnisse['fraktionslos'].items()
fraktionslos_liste = ['fraktionslos']

GRÜNE = ergebnisse['GRÜNE'].items()
GRÜNE_liste = ['GRÜNE']

LINKE = ergebnisse['LINKE'].items()
LINKE_liste = ['LINKE']

SPD = ergebnisse['SPD'].items()
SPD_liste = ['SPD']

for tupel in AfD:
	AfD_liste.append(tupel[1])

for tupel in CDU:
	CDU_liste.append(tupel[1])

for tupel in CSU:
	CSU_liste.append(tupel[1])

for tupel in FDP:
	FDP_liste.append(tupel[1])

for tupel in fraktionslos:
	fraktionslos_liste.append(tupel[1])

for tupel in GRÜNE:
	GRÜNE_liste.append(tupel[1])

for tupel in LINKE:
	LINKE_liste.append(tupel[1])

for tupel in SPD:
	SPD_liste.append(tupel[1])


ergebnisliste.append(LINKE_liste)
ergebnisliste.append(GRÜNE_liste)
ergebnisliste.append(SPD_liste)
ergebnisliste.append(FDP_liste)
ergebnisliste.append(CDU_liste)
ergebnisliste.append(CSU_liste)
ergebnisliste.append(AfD_liste)

# ergebnisliste.append(fraktionslos_liste)






with open("CSV_Sublime\Auswertung\Python\SharingPerParty03.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisliste:

		ergebniswriter.writerow(row)

