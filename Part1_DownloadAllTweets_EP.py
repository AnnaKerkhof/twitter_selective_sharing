import tweepy
import csv
from datetime import datetime, timedelta
import pytz
import urllib.parse
import time

# Changelog zu vorheriger Version: Einfügen Fkt. retweet_contains_link, Abändern der Fkt. politician_tweet_contains_link, Abändern der Fkt. Datenabfrage passend zu den beiden vorher genannten Funktionen
# außerdem all_tweets eingefügt für Gesamtübersicht über alle Tweets


ergebnisse = []
counter = 0
BuTa_constitution = datetime.strptime("2018-12-28 00:01", "%Y-%m-%d %H:%M")		# angepasst an 199 Tage Zeitraum der ursprünglichen Daten
overview = []		# zweite Liste für Statistiken
all_tweets = []		# dritte Liste für Gesamtübersicht
error_list = []		# vierte Liste für Errors, die danach händisch geprüft werden


def politician_tweet_contains_link(tweet):

	if "retweeted_status" in tweet._json:
		return False

	else:
		if tweet._json["entities"]["urls"]:
			return True

		else:
			return False


def retweet_contains_link(tweet):

	if "retweeted_status" in tweet._json:

		if tweet._json["retweeted_status"]["entities"]["urls"]:
			return True

		else:
			return False

	else:
		return False


def politician_tweet_contains_quoted_link(tweet):

	if "quoted_status" in tweet._json:
		
		if tweet._json["quoted_status"]["entities"]["urls"]:
			return True

		else:
			return False

	else:
		return False


def retweet_contains_quoted_link(tweet):

	if "retweeted_status" in tweet._json:
		
		if "quoted_status" in tweet._json["retweeted_status"]:
			
			if tweet._json["retweeted_status"]["quoted_status"]["entities"]["urls"]:
				return True

			else:
				return False

		else:
			return False

	else:
		return False
		



def Datenabfrage(name, handle, party, BuTa_constitution, ergebnisse, latest_id, max_counter, tweet_counter, overview, all_tweets):

	consumer_key = "K1nzE25udpghfkC3SkF9YcG9A"
	consumer_secret = "NPquJXjSOQQIRzhLGgyDQw7ruNIxACuTOZ79uwD5DFlZgTqgr5"
	access_token = "827098487951081472-PxNi0tPdTVVyAEwbSriM7tMmPQIGiZc"
	access_token_secret = "ht4DKz3ueoUahJoijU4u8oIjDog3KGDU5Y0AGRcXhkawI"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	user_account_created = None
	statuses_count = None
	tweet_created = None

	time.sleep(1)

	try:

		twitterabfrage = api.user_timeline(handle, tweet_mode = 'extended', max_id = latest_id, count = 200)	# max_id nicht mit latest_id verwechseln! max_id ist Parameter von Tweepy, latest_id selbst definierter. Sie meinen aber das Selbe.

		for tweet in twitterabfrage:
			
			max_counter = max_counter + 1
			tweet_created = datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
			user_account_created = datetime.strptime(tweet._json['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
			statuses_count = tweet._json['user']['statuses_count']
			latest_id = tweet._json['id']
			tweetdaten = []
			all_tweets.append([name, handle, party, tweet_created, tweet._json['id'], tweet._json['full_text']])

			if tweet_created > BuTa_constitution:

				tweet_counter += 1
				
				if politician_tweet_contains_link(tweet):

					for entry in tweet._json['entities']['urls']:

						expanded_url = entry['expanded_url']
						tweetdaten.append(name)
						tweetdaten.append(handle)
						tweetdaten.append(party)
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%d.%m.%Y'))
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%H:%M'))
						tweetdaten.append(tweet._json['id'])
						tweetdaten.append(tweet._json['full_text'])
						tweetdaten.append(expanded_url)
						
						ergebnisse.append(tweetdaten)

						tweetdaten = []


				if retweet_contains_link(tweet):

					for entry in tweet._json['retweeted_status']['entities']['urls']:

						expanded_url = entry['expanded_url']
						tweetdaten.append(name)
						tweetdaten.append(handle)
						tweetdaten.append(party)
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%d.%m.%Y'))
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%H:%M'))
						tweetdaten.append(tweet._json['id'])
						tweetdaten.append(tweet._json['full_text'])
						tweetdaten.append(expanded_url)
						tweetdaten.append("RT-Link")		# Retweet-Link
						tweetdaten.append(tweet._json['retweeted_status']['user']['screen_name'])
						tweetdaten.append(tweet._json['retweeted_status']['id'])
						tweetdaten.append(tweet._json['retweeted_status']['full_text'])
						
						ergebnisse.append(tweetdaten)

						tweetdaten = []

						
				if politician_tweet_contains_quoted_link(tweet):

					for entry in tweet._json['quoted_status']['entities']['urls']:

						expanded_url = entry['expanded_url']
						tweetdaten.append(name)
						tweetdaten.append(handle)
						tweetdaten.append(party)
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%d.%m.%Y'))
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%H:%M'))
						tweetdaten.append(tweet._json['id'])
						tweetdaten.append(tweet._json['full_text'])
						tweetdaten.append(expanded_url)
						tweetdaten.append("Quoted-Link")
						tweetdaten.append(tweet._json['quoted_status']['user']['screen_name'])
						tweetdaten.append(tweet._json['quoted_status']['id'])
						tweetdaten.append(tweet._json['quoted_status']['full_text'])
												
						ergebnisse.append(tweetdaten)

						tweetdaten = []

				
				if retweet_contains_quoted_link(tweet):

					for entry in tweet._json['retweeted_status']['quoted_status']['entities']['urls']:

						expanded_url = entry['expanded_url']
						tweetdaten.append(name)
						tweetdaten.append(handle)
						tweetdaten.append(party)
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%d.%m.%Y'))
						tweetdaten.append(datetime.strptime(tweet._json['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC).strftime('%H:%M'))
						tweetdaten.append(tweet._json['id'])
						tweetdaten.append(tweet._json['full_text'])
						tweetdaten.append(expanded_url)
						tweetdaten.append("RT-Q-Link")		# Retweet-Quoted-Link
						tweetdaten.append(tweet._json['retweeted_status']['quoted_status']['user']['screen_name'])
						tweetdaten.append(tweet._json['retweeted_status']['quoted_status']['id'])
						tweetdaten.append(tweet._json['retweeted_status']['quoted_status']['full_text'])
						
						ergebnisse.append(tweetdaten)

						tweetdaten = []
						
				

			else: continue

	except tweepy.error.TweepError:

		print("++FEHLER++")
		print("Tweepy Error: " + str(name) + ", " + str(handle) + ", " + str(party))
		print(""

			"")

		error_temp = []

		error_temp.append(name)
		error_temp.append(handle)
		error_temp.append(party)

		error_list.append(error_temp)

		return ergebnisse


	print("latest_id: " + str(latest_id))
	print("tweet_created: " + str(tweet_created))
	print("max_counter: " + str(max_counter))
	print("tweet_counter: " + str(tweet_counter))

	if tweet_created != None and user_account_created != None and latest_id != None and max_counter > 0 and statuses_count > 0:

		if tweet_created > BuTa_constitution and tweet_created > user_account_created and max_counter < 3200 and max_counter < statuses_count:
			latest_id = latest_id - 1
			Datenabfrage(name = name, handle = handle, party = party, BuTa_constitution = BuTa_constitution, ergebnisse = ergebnisse, latest_id = latest_id, max_counter = max_counter, tweet_counter = tweet_counter, overview = overview, all_tweets = all_tweets)

		elif max_counter >= 3200:
			error_list.append([name, handle, party, "Reached Tweet Limit! Last tweet at: " + str(tweet._json['user']['created_at']), tweet_counter, latest_id])
			overview.append([name, handle, party, tweet_counter])
			return ergebnisse

		else:
			overview.append([name, handle, party, tweet_counter])
			return ergebnisse

	else:
		overview.append([name, handle, party, tweet_counter, "FAULT"])
		error_list.append([name, handle, party, "Fault other than Tweepy", tweet_counter])
		print(""

			"")
		print("++FEHLER++")
		print(twitterabfrage)
		print(""

			"")
		return ergebnisse



with open("AccountHandles\\NamesEP.csv", newline="", encoding="utf-8") as csvfile:
	namesreader = csv.reader(csvfile, delimiter=";", quotechar='"')

	for row in namesreader:

		if row[1] != 'None':
			
			name = row[0]
			handle = row[1]
			party = row[2]

			print("+++ " + str(name) + ", " + str(handle) + " +++")

			Datenabfrage(name = name, handle = handle, party = party, BuTa_constitution = BuTa_constitution, ergebnisse = ergebnisse, latest_id = None, max_counter = 0, tweet_counter = 0, overview = overview, all_tweets = all_tweets)

			

		else: continue




with open("Results EP\\Part 1\\EP_OnlyURL_2019_07_14.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisse:

		ergebniswriter.writerow(row)



with open("Results EP\\Part 1\\EP_Overview_2019_07_14.csv", "w", newline="", encoding="utf-8") as overviewCSV:

	overviewwriter = csv.writer(overviewCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in overview:

		overviewwriter.writerow(row)


with open("Results EP\\Part 1\\EP_All_Tweets_2019_07_14.csv", "w", newline="", encoding="utf-8") as AllCSV:

	all_tweets_writer = csv.writer(AllCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in all_tweets:

		all_tweets_writer.writerow(row)


with open("Results EP\\Part 1\\EP_Errors_2019_07_14.csv", "w", newline="", encoding="utf-8") as ErrorsCSV:

	errors_writer = csv.writer(ErrorsCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in error_list:

		errors_writer.writerow(row)