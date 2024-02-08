import tweepy
import csv
from datetime import datetime, timedelta
import pytz
import time


consumer_key = "K1nzE25udpghfkC3SkF9YcG9A"
consumer_secret = "NPquJXjSOQQIRzhLGgyDQw7ruNIxACuTOZ79uwD5DFlZgTqgr5"
access_token = "827098487951081472-PxNi0tPdTVVyAEwbSriM7tMmPQIGiZc"
access_token_secret = "ht4DKz3ueoUahJoijU4u8oIjDog3KGDU5Y0AGRcXhkawI"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


all_users = []
error_list = []

with open('AccountHandles\\NamesLT.csv', newline='', encoding='utf-8') as csvfile:
	namesreader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in namesreader:

		if row[1] != 'None':

			time.sleep(1)

			name = row[0]
			handle = row[1]
			party = row[2]
			landtag = row[3]

			print(str(name) + ": " + str(handle))

			try:

				account_request = api.get_user(handle)

				user_data = []

				user_data.append(name)		# Name in Excel-File
				user_data.append(handle) 	# @-Handle, das herausgesucht wurde
				user_data.append(party)		# NEU HINZUGEFÜGT am 02.05.2018
				user_data.append(account_request._json['id'])		# Eindeutige Account-ID
				user_data.append(account_request._json['name'])		# Auf Twitter angegebener Name
				user_data.append(datetime.strptime(account_request._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%d.%m.%Y'))		# Account erstellt am
				user_data.append(account_request._json['followers_count'])		# Anzahl der Follower
				user_data.append(account_request._json['friends_count'])		# Anzahl der Accounts, denen der Politiker folgt
				user_data.append(account_request._json['statuses_count'])		# Anzahl aller Tweets inkl. Antworten des Politiker-Accounts
				user_data.append(account_request._json['favourites_count'])		# Anzahl der "Gefällt-mir"-Angaben des Accounts
				user_data.append(account_request._json['verified'])				# blauer Haken am Account / verifiziert (False = Nein, True = Ja)
				user_data.append(landtag)


				all_users.append(user_data)

			except tweepy.error.TweepError as e:

				print("++FEHLER++")
				print("Tweepy Error: " + str(name) + ", " + str(handle) + ", " + str(party) + ", " + str(landtag))
				print(""

					"")

				print(e)

				print(""

					"")

				error_temp = []

				error_temp.append(name)
				error_temp.append(handle)
				error_temp.append(party)
				error_temp.append(landtag)

				error_list.append(error_temp)


		else:
			continue


with open("Results LT\\Part 6\\LP_Data_2019_07_13.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in all_users:

		ergebniswriter.writerow(row)


with open("Results LT\\Part 6\\LT_Errors_2019_07_13_Part6.csv", "w", newline="", encoding="utf-8") as ErrorsCSV:

	errors_writer = csv.writer(ErrorsCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in error_list:

		errors_writer.writerow(row)