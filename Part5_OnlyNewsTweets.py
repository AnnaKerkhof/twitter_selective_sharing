import csv
import urllib.parse
import http.client
import time
import socket
import ssl

from unshortenit import UnshortenIt
import unshortenit.exceptions

onlynews = []

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



def newscheck(url):

	if '.bild.de' in url or url == 'bild.de':
		return True

	elif  '.spiegel.de' in url or url == 'spiegel.de':
		return True

	elif '.focus.de' in url or url == 'focus.de':
		return True

	elif '.n-tv.de' in url or url == 'n-tv.de':
		return True

	elif '.welt.de' in url or url == 'welt.de':
		return True

	elif '.zeit.de' in url or url == 'zeit.de':
		return True

	elif '.sueddeutsche.de' in url or url == 'sueddeutsche.de':
		return True

	elif '.stern.de' in url or url == 'stern.de':
		return True

	elif '.faz.net' in url or url == 'faz.net':
		return True

	elif '.taz.de' in url or url == 'taz.de':
		return True
		
	elif '.tagesschau.de' in url or url == 'tagesschau.de':
		return True

	elif '.zdf.de' in url or url == 'zdf.de':
		control_url = unshortenit_url(expanded_url)
		if 'zdf.de/nachrichten' in control_url:
			return True

	elif '.deutschlandfunk.de' in url or url == 'deutschlandfunk.de':
		return True

	else:
		return False


with open('CSV_Sublime\LinksCOMPLETE.csv', newline='', encoding='utf-8') as csvfile:
	linereader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in linereader:

		name = row[0]
		handle = row[1]
		party = row[2]
		date_day = row[3]
		date_time = row[4]
		tweet_id = row[5]
		tweet_text = row[6]
		expanded_url = row[7]
		url_own_short = row[8]
		url_unshortenit = row[9]

		if url_unshortenit == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":

			if newscheck(url_own_short):

				templist = []

				if len(row) > 13:

					quoted_handle = row[12]
					quoted_tweet_id = row[13]
					quoted_tweet_text = row[14]

					templist.append(name)
					templist.append(handle)
					templist.append(party)
					templist.append(date_day)
					templist.append(date_time)
					templist.append(tweet_id)
					templist.append(tweet_text)
					templist.append(expanded_url)
					templist.append(url_own_short)
					templist.append(url_unshortenit)
					templist.append(quoted_handle)
					templist.append(quoted_tweet_id)
					templist.append(quoted_tweet_text)

					onlynews.append(templist)

				else:

					templist.append(name)
					templist.append(handle)
					templist.append(party)
					templist.append(date_day)
					templist.append(date_time)
					templist.append(tweet_id)
					templist.append(tweet_text)
					templist.append(expanded_url)
					templist.append(url_own_short)
					templist.append(url_unshortenit)
					
					onlynews.append(templist)


		else:

			if newscheck(url_unshortenit):

				templist = []

				if len(row) > 13:

					quoted_handle = row[12]
					quoted_tweet_id = row[13]
					quoted_tweet_text = row[14]

					templist.append(name)
					templist.append(handle)
					templist.append(party)
					templist.append(date_day)
					templist.append(date_time)
					templist.append(tweet_id)
					templist.append(tweet_text)
					templist.append(expanded_url)
					templist.append(url_own_short)
					templist.append(url_unshortenit)
					templist.append(quoted_handle)
					templist.append(quoted_tweet_id)
					templist.append(quoted_tweet_text)

					onlynews.append(templist)

				else:

					templist.append(name)
					templist.append(handle)
					templist.append(party)
					templist.append(date_day)
					templist.append(date_time)
					templist.append(tweet_id)
					templist.append(tweet_text)
					templist.append(expanded_url)
					templist.append(url_own_short)
					templist.append(url_unshortenit)
					
					onlynews.append(templist)


with open("CSV_Sublime\OnlyNews_01.csv", "w", newline="", encoding="utf-8") as ResultCSV:

	resultwriter = csv.writer(ResultCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in onlynews:

		resultwriter.writerow(row)