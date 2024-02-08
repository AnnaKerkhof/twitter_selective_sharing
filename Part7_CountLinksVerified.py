import csv
import urllib.parse
import http.client
import time
import socket
import ssl

from unshortenit import UnshortenIt
import unshortenit.exceptions



def unshortenit_url(zdf_url):

	# source: https://stackoverflow.com/questions/22734464/unicodeencodeerror-ascii-codec-cant-encode-character-xe9-when-using-ur
	scheme_e, netloc_e, path_e, query_e, fragment_e = urllib.parse.urlsplit(zdf_url)
	path_e = urllib.parse.quote(path_e, safe='/', encoding='utf-8', errors=None)
	zdf_url = urllib.parse.urlunsplit((scheme_e, netloc_e, path_e, query_e, fragment_e))
	print("Link after UTF-8 decoding: " + str(zdf_url))
	
	parsed_utf = urllib.parse.urlparse(zdf_url)

	try:
		print("Starting UnshortenIt with URL: " + str(zdf_url))

		unshortener = UnshortenIt()
		finallink = unshortener.unshorten(zdf_url)

		print("Link UnshortenIt: " + str(finallink))		
		return finallink


	except unshortenit.exceptions.NotFound:

		print("!!! 404 Not Found (UnshortenIt) !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except unshortenit.exceptions.UnshortenFailed:

		print("!!! Unshorten Failed (UnshortenIt)")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except OSError:

		print("!!! OSError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except socket.gaierror:

		print("!!! socket.gaierror !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except TimeoutError:

		print("!!! TimeoutError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except ssl.CertificateError:

		print("!!! CertificateError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except ssl.SSLError:

		print("!!! ssl.SSLError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except ConnectionResetError:

		print("!!! ConnectionResetError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except ConnectionRefusedError:

		print("!!! ConnectionRefusedError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

	except UnicodeDecodeError:

		print("!!! UnicodeDecodeError !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"


politicians = {}

results = {'AfD': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'CDU': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'CSU': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'FDP': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'fraktionslos': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'GRÜNE': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'LINKE': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}, 'SPD': {'bild.de': 0, 'spiegel.de': 0, 'focus.de': 0, 'n-tv.de': 0, 'welt.de': 0, 'zeit.de': 0, 'sueddeutsche.de': 0, 'stern.de': 0, 'faz.net': 0, 'taz.de': 0, 'tagesschau.de': 0, 'zdf.de/nachrichten': 0, 'deutschlandfunk.de': 0}}


with open('..\Accounts MdBs\Ergebnisse\Accountdaten_2018_05_07BraunKesslerChanged.csv', newline='', encoding='utf-8') as Accountfile:
	accountreader = csv.reader(Accountfile, delimiter=';', quotechar='"')

	for line in accountreader:

		pol_handle = line[1]
		verified = line[10]

		politicians[pol_handle] = verified

	print(politicians)


with open('CSV_Sublime\LinksCOMPLETE.csv', newline='', encoding='utf-8') as csvfile:
	linereader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in linereader:

		handle = row[1]
		party = row[2]
		url = row[9]
		expanded_url = row[7]

				
		if politicians[handle] == 'True':

			if url == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":
				url = row[8]

			if party == 'AfD':

				if '.bild.de' in url or url == 'bild.de':
					results['AfD']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['AfD']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['AfD']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['AfD']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['AfD']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['AfD']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['AfD']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['AfD']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['AfD']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['AfD']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['AfD']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['AfD']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['AfD']['deutschlandfunk.de'] += 1

			
			if party == 'CDU':

				if '.bild.de' in url or url == 'bild.de':
					results['CDU']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['CDU']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['CDU']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['CDU']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['CDU']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['CDU']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['CDU']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['CDU']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['CDU']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['CDU']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['CDU']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['CDU']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['CDU']['deutschlandfunk.de'] += 1

			
			if party == 'CSU':

				if '.bild.de' in url or url == 'bild.de':
					results['CSU']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['CSU']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['CSU']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['CSU']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['CSU']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['CSU']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['CSU']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['CSU']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['CSU']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['CSU']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['CSU']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['CSU']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['CSU']['deutschlandfunk.de'] += 1

			
			if party == 'FDP':

				if '.bild.de' in url or url == 'bild.de':
					results['FDP']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['FDP']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['FDP']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['FDP']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['FDP']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['FDP']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['FDP']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['FDP']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['FDP']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['FDP']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['FDP']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['FDP']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['FDP']['deutschlandfunk.de'] += 1

			
			if party == 'fraktionslos':

				if '.bild.de' in url or url == 'bild.de':
					results['fraktionslos']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['fraktionslos']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['fraktionslos']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['fraktionslos']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['fraktionslos']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['fraktionslos']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['fraktionslos']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['fraktionslos']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['fraktionslos']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['fraktionslos']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['fraktionslos']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['fraktionslos']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['fraktionslos']['deutschlandfunk.de'] += 1

			
			if party == 'GRÜNE':

				if '.bild.de' in url or url == 'bild.de':
					results['GRÜNE']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['GRÜNE']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['GRÜNE']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['GRÜNE']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['GRÜNE']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['GRÜNE']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['GRÜNE']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['GRÜNE']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['GRÜNE']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['GRÜNE']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['GRÜNE']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['GRÜNE']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['GRÜNE']['deutschlandfunk.de'] += 1


			if party == 'LINKE':

				if '.bild.de' in url or url == 'bild.de':
					results['LINKE']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['LINKE']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['LINKE']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['LINKE']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['LINKE']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['LINKE']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['LINKE']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['LINKE']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['LINKE']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['LINKE']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['LINKE']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['LINKE']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['LINKE']['deutschlandfunk.de'] += 1


			if party == 'SPD':

				if '.bild.de' in url or url == 'bild.de':
					results['SPD']['bild.de'] += 1

				if  '.spiegel.de' in url or url == 'spiegel.de':
					results['SPD']['spiegel.de'] += 1

				if '.focus.de' in url or url == 'focus.de':
					results['SPD']['focus.de'] += 1

				if '.n-tv.de' in url or url == 'n-tv.de':
					results['SPD']['n-tv.de'] += 1

				if '.welt.de' in url or url == 'welt.de':
					results['SPD']['welt.de'] += 1

				if '.zeit.de' in url or url == 'zeit.de':
					results['SPD']['zeit.de'] += 1

				if '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
					results['SPD']['sueddeutsche.de'] += 1

				if '.stern.de' in url or url == 'stern.de':
					results['SPD']['stern.de'] += 1

				if '.faz.net' in url or url == 'faz.net':
					results['SPD']['faz.net'] += 1

				if '.taz.de' in url or url == 'taz.de':
					results['SPD']['taz.de'] += 1

				if '.tagesschau.de' in url or url == 'tagesschau.de':
					results['SPD']['tagesschau.de'] += 1

				if '.zdf.de' in url or url == 'zdf.de':
					control_url = unshortenit_url(expanded_url)
					if 'zdf.de/nachrichten' in control_url:
						results['SPD']['zdf.de/nachrichten'] += 1

				if '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
					results['SPD']['deutschlandfunk.de'] += 1

		else:
			continue

	print (results)


resultlist = [['Partei', 'bild.de', 'spiegel.de', 'focus.de', 'n-tv.de', 'welt.de', 'zeit.de', 'sueddeutsche.de', 'stern.de', 'faz.net', 'taz.de', 'tagesschau.de', 'zdf.de/nachrichten', 'deutschlandfunk.de']]

AfD = results['AfD'].items()
AfD_list = ['AfD']

CDU = results['CDU'].items()
CDU_list = ['CDU']

CSU = results['CSU'].items()
CSU_list = ['CSU']

FDP = results['FDP'].items()
FDP_list = ['FDP']

fraktionslos = results['fraktionslos'].items()
fraktionslos_list = ['fraktionslos']

GRÜNE = results['GRÜNE'].items()
GRÜNE_list = ['GRÜNE']

LINKE = results['LINKE'].items()
LINKE_list = ['LINKE']

SPD = results['SPD'].items()
SPD_list = ['SPD']

for tupel in AfD:
	AfD_list.append(tupel[1])

for tupel in CDU:
	CDU_list.append(tupel[1])

for tupel in CSU:
	CSU_list.append(tupel[1])

for tupel in FDP:
	FDP_list.append(tupel[1])

for tupel in fraktionslos:
	fraktionslos_list.append(tupel[1])

for tupel in GRÜNE:
	GRÜNE_list.append(tupel[1])

for tupel in LINKE:
	LINKE_list.append(tupel[1])

for tupel in SPD:
	SPD_list.append(tupel[1])


resultlist.append(LINKE_list)
resultlist.append(GRÜNE_list)
resultlist.append(SPD_list)
resultlist.append(FDP_list)
resultlist.append(CDU_list)
resultlist.append(CSU_list)
resultlist.append(AfD_list)

# resultlist.append(fraktionslos_list)






with open("CSV_Sublime\Auswertung\Python\SharingPerPartyVERIFIED01.csv", "w", newline="", encoding="utf-8") as ResultCSV:

	resultwriter = csv.writer(ResultCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in resultlist:

		resultwriter.writerow(row)

