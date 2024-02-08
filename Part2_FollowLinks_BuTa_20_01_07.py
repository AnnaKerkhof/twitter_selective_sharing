# Change-Log:
# - Ergänzung der Spalte link_source in die Unshorten-Dokumentation
# - 07.01.2020: Ergänzung der Exception http.client.HTTPException

import csv
from datetime import datetime, timedelta
import urllib.parse
import http.client
import time
import socket
import ssl
import tweepy

from unshortenit import UnshortenIt
import unshortenit.exceptions


def unshorten_url(utf_url, counter):
	print("Beginn Unshortening: " + str(utf_url))
	

	if counter >= 1:

		scheme_e, netloc_e, path_e, query_e, fragment_e = urllib.parse.urlsplit(utf_url)
		path_e = urllib.parse.quote(path_e, safe='/', encoding='utf-8', errors=None)
		utf_url = urllib.parse.urlunsplit((scheme_e, netloc_e, path_e, query_e, fragment_e))

	# source: https://stackoverflow.com/questions/4201062/how-can-i-unshorten-a-url
	parsed = urllib.parse.urlparse(utf_url)


	if parsed.scheme == "http":

		time.sleep(0.3)
		print("Main-URL: " + str(parsed.netloc))
		h = http.client.HTTPConnection(parsed.netloc)
		resource = parsed.path
		if parsed.query != "":
			resource += "?" + parsed.query

		try:

			h.request('HEAD', resource)
			response = h.getresponse()

			if response.status//100 == 3 and response.getheader('Location'):

				print("Redirect-Versuch Nr. " + str(counter+1) + ", Redirect-Code: " +  str(response.status) + ", Redirect-URL: " + str(response.getheader('Location')))

				if counter <= 10:
					counter = counter + 1
					redirect_url = response.getheader('Location')
					redirect_parsed = urllib.parse.urlparse(redirect_url)

					if redirect_parsed.scheme and redirect_parsed.netloc and redirect_parsed.path:
						return unshorten_url(redirect_url, counter)		# return entfernt rückgängig gemacht

					else:
						redirect_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, redirect_parsed.path, parsed.query, parsed.fragment))
						print("Falscher Redirect. Scheme und Netloc aus bisheriger URL verwendet: " + str(redirect_url))
						return unshorten_url(redirect_url, counter)		# return entfernt rückgängig gemacht

				else:
					counter = 0
					return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

			else:
				counter = 0
				print("Endgültige URL bestimmt: " + str(utf_url))
				return utf_url

		except tweepy.error.TweepError:

			print("!!! tweepy.error.TweepError !!!")
			print("30 seconds timeout")
			time.sleep(15)
			print("15 seconds left")
			time.sleep(15)
			print("Restarting function")
			unshorten_url(utf_url, counter)

		
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

		except http.client.HTTPException:

			print("!!! http.client.HTTPException !!!")
			return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"
			#Exception ergänzt am 07.01.2020 nach Auftreten eines Fehlers nach Abrufen einer nicht mehr existenten Website


	elif parsed.scheme == "https":

		time.sleep(0.3)
		print(parsed.netloc)
		h = http.client.HTTPSConnection(parsed.netloc)
		resource = parsed.path
		if parsed.query != "":
			resource += "?" + parsed.query

		try:

			h.request('HEAD', resource)
			response = h.getresponse()

			if response.status//100 == 3 and response.getheader('Location'):

				print("Redirect-Versuch Nr. " + str(counter+1) + ", Redirect-Code: " +  str(response.status) + ", Redirect-URL: " + str(response.getheader('Location')))

				if counter <= 10:
					counter = counter + 1
					redirect_url = response.getheader('Location')
					redirect_parsed = urllib.parse.urlparse(redirect_url)

					if redirect_parsed.scheme and redirect_parsed.netloc and redirect_parsed.path:
						return unshorten_url(redirect_url, counter)		# return entfernt rückgängig gemacht

					else:
						redirect_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, redirect_parsed.path, parsed.query, parsed.fragment))
						print("Falscher Redirect. Scheme und Netloc aus bisheriger URL verwendet: " + str(redirect_url))
						return unshorten_url(redirect_url, counter)		# return entfernt rückgängig gemacht

				else:
					counter = 0
					return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"

			else:
				counter = 0
				print("Endgültige URL bestimmt: " + str(utf_url))
				return utf_url


		except tweepy.error.TweepError:

			print("!!! tweepy.error.TweepError !!!")
			print("30 seconds timeout")
			time.sleep(15)
			print("15 seconds left")
			time.sleep(15)
			print("Restarting function")
			unshorten_url(utf_url, counter)


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

		except http.client.HTTPException:

			print("!!! http.client.HTTPException !!!")
			return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"
			#Exception ergänzt am 07.01.2020 nach Auftreten eines Fehlers nach Abrufen einer nicht mehr existenten Website


	else:
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"


def unshortenit_url(utf_url):

	try:
		print("Start UnshortenIt mit URL: " + str(utf_url))

		unshortener = UnshortenIt()
		shortlink = unshortener.unshorten(utf_url)

		print("Link UnshortenIt: " + str(shortlink))		
		return shortlink


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

	except http.client.HTTPException:

		print("!!! http.client.HTTPException !!!")
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"
		#Exception ergänzt am 07.01.2020 nach Auftreten eines Fehlers nach Abrufen einer nicht mehr existenten Website		




def parse_main_url(link):

	if link == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":
		return "FEHLER BEIM HERAUSFINDEN DER MAIN_URL"
	
	else:
		main_url = urllib.parse.urlparse(link).netloc
		return main_url



ergebnisliste = []
row_counter = 0

with open('Results BuTaNew\Part 1\BuTaNew_OnlyURL_2019_07_14_P5.csv', newline='', encoding='utf-8') as csvfile:
	namesreader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in namesreader:

		zwischenliste = []

		name = row[0]
		handle = row[1]
		party = row[2]
		date_day = row[3]
		date_time = row[4]
		tweet_id = row[5]
		tweet_text = row[6]
		expanded_url = row[7]


		if expanded_url == "None":
			continue

		else:
			print(""

				"")
			print("+++ " + str(handle) + ", ID: " + str(tweet_id) + ": " + str(expanded_url))

			# source: https://stackoverflow.com/questions/22734464/unicodeencodeerror-ascii-codec-cant-encode-character-xe9-when-using-ur
			scheme_e, netloc_e, path_e, query_e, fragment_e = urllib.parse.urlsplit(expanded_url)
			path_e = urllib.parse.quote(path_e, safe='/', encoding='utf-8', errors=None)
			utf_url = urllib.parse.urlunsplit((scheme_e, netloc_e, path_e, query_e, fragment_e))
			print("Link nach UTF-8-Codierung: " + str(utf_url))
			
			parsed_utf = urllib.parse.urlparse(utf_url)

			if parsed_utf.netloc == "twitter.com":
				print("!Twitter-Link! Link: " + str(expanded_url))
				continue

			else:

				url_own_code = unshorten_url(utf_url, 0)
				url_unshortenit = unshortenit_url(utf_url)

				main_url_own_code = parse_main_url(url_own_code)
				print(url_own_code)
				print(main_url_own_code)
				main_url_unshortenit = parse_main_url(url_unshortenit)
				print(url_unshortenit)
				print(main_url_unshortenit)

				if main_url_own_code == main_url_unshortenit:
					similar = "yes"

				else:
					similar = "!NO!"

				print(similar)				

				if len(row) > 10:

					link_source = row[8]
					quoted_handle = row[9]
					quoted_tweet_id = row[10]
					quoted_tweet_text = row[11]

					zwischenliste.append(name)
					zwischenliste.append(handle)
					zwischenliste.append(party)
					zwischenliste.append(date_day)
					zwischenliste.append(date_time)
					zwischenliste.append(tweet_id)
					zwischenliste.append(tweet_text)
					zwischenliste.append(expanded_url)
					zwischenliste.append(link_source)
					zwischenliste.append(quoted_handle)
					zwischenliste.append(quoted_tweet_id)
					zwischenliste.append(quoted_tweet_text)
					zwischenliste.append(url_own_code)
					zwischenliste.append(url_unshortenit)
					zwischenliste.append(main_url_own_code)
					zwischenliste.append(main_url_unshortenit)
					zwischenliste.append(similar)


					ergebnisliste.append(zwischenliste)
					

				else:

					zwischenliste.append(name)
					zwischenliste.append(handle)
					zwischenliste.append(party)
					zwischenliste.append(date_day)
					zwischenliste.append(date_time)
					zwischenliste.append(tweet_id)
					zwischenliste.append(tweet_text)
					zwischenliste.append(expanded_url)
					zwischenliste.append("own")
					zwischenliste.append("own")
					zwischenliste.append("own")
					zwischenliste.append("own")
					zwischenliste.append(url_own_code)
					zwischenliste.append(url_unshortenit)
					zwischenliste.append(main_url_own_code)
					zwischenliste.append(main_url_unshortenit)
					zwischenliste.append(similar)

					ergebnisliste.append(zwischenliste)

		row_counter = row_counter + 1

		if row_counter == 1000:

			row_counter = 0

			with open("Results BuTaNew\Part 2\LinksUnshortened_2020_01_04_BuTa_P5.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

				ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

				for row in ergebnisliste:

					ergebniswriter.writerow(row)



with open("Results BuTaNew\Part 2\LinksUnshortened_2020_01_04_BuTa_P5.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

				ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

				for row in ergebnisliste:

					ergebniswriter.writerow(row)