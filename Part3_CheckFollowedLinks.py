# Change-Log:
# - link_source hinzugefügt
# - Fail-Liste vervollständigt
# - both_fail hinzugefügt
# - len(row) angepasst auf 12


import csv

ergebnisliste_both_fail = []
ergebnisliste_fb = []
ergebnisliste_other = []
ergebnisliste_fail = []


with open('CSV_Sublime\LinksCOMPLETE.csv', newline='', encoding='utf-8') as csvfile:
	namesreader = csv.reader(csvfile, delimiter=';', quotechar='"')

	for row in namesreader:

		zwischenliste_both_fail = []
		zwischenliste_fb = []
		zwischenliste_other = []
		zwischenliste_fail = []

		name = row[0]
		handle = row[1]
		party = row[2]
		date_day = row[3]
		date_time = row[4]
		tweet_id = row[5]
		tweet_text = row[6]
		expanded_url = row[7]
		main_url_own_code = row[8]
		main_url_unshortenit = row[9]
		similar = row[10]
		link_source = row[11]

		if main_url_own_code == main_url_unshortenit == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":

			# Falls beide Tools versagt haben

			zwischenliste_both_fail.append(name)
			zwischenliste_both_fail.append(handle)
			zwischenliste_both_fail.append(party)
			zwischenliste_both_fail.append(date_day)
			zwischenliste_both_fail.append(date_time)
			zwischenliste_both_fail.append(tweet_id)
			zwischenliste_both_fail.append(tweet_text)
			zwischenliste_both_fail.append(expanded_url)
			zwischenliste_both_fail.append(main_url_own_code)
			zwischenliste_both_fail.append(main_url_unshortenit)
			zwischenliste_both_fail.append(link_source)

			if len(row) > 12:
				
				quoted_handle = row[11]
				quoted_tweet_id = row[12]
				quoted_tweet_text = row[13]

				zwischenliste_both_fail.append(quoted_handle)
				zwischenliste_both_fail.append(quoted_tweet_id)
				zwischenliste_both_fail.append(quoted_tweet_text)

			ergebnisliste_both_fail.append(zwischenliste_both_fail)


		if main_url_unshortenit == "FEHLER BEIM HERAUSFINDEN DER MAIN_URL":

			# Wenn hat UnshortenIt versagt hat.

			zwischenliste_fail.append(name)
			zwischenliste_fail.append(handle)
			zwischenliste_fail.append(party)
			zwischenliste_fail.append(date_day)
			zwischenliste_fail.append(date_time)
			zwischenliste_fail.append(tweet_id)
			zwischenliste_fail.append(tweet_text)
			zwischenliste_fail.append(expanded_url)
			zwischenliste_fail.append(main_url_own_code)
			zwischenliste_fail.append(main_url_unshortenit)
			zwischenliste_fail.append(link_source)

			if len(row) > 12:
				
				quoted_handle = row[11]
				quoted_tweet_id = row[12]
				quoted_tweet_text = row[13]

				zwischenliste_fail.append(quoted_handle)
				zwischenliste_fail.append(quoted_tweet_id)
				zwischenliste_fail.append(quoted_tweet_text)

			ergebnisliste_fail.append(zwischenliste_fail)


		if similar == "!NO!":

			
			if "facebook.com" in main_url_unshortenit:
				# Alle Facebook-Link heraussuchen, da fb.me am öftesten für Unterschiede sorgt (kann von eigenem Tool nicht ausgelesen werden)
		
				zwischenliste_fb.append(name)
				zwischenliste_fb.append(handle)
				zwischenliste_fb.append(party)
				zwischenliste_fb.append(date_day)
				zwischenliste_fb.append(date_time)
				zwischenliste_fb.append(tweet_id)
				zwischenliste_fb.append(tweet_text)
				zwischenliste_fb.append(expanded_url)
				zwischenliste_fb.append(main_url_own_code)
				zwischenliste_fb.append(main_url_unshortenit)
				zwischenliste_fb.append(link_source)

				if len(row) > 12:
					
					quoted_handle = row[11]
					quoted_tweet_id = row[12]
					quoted_tweet_text = row[13]

					zwischenliste_fb.append(quoted_handle)
					zwischenliste_fb.append(quoted_tweet_id)
					zwischenliste_fb.append(quoted_tweet_text)

				ergebnisliste_fb.append(zwischenliste_fb)

			else:
				# Alle anderen Unterschiede werden hier erfasst

				zwischenliste_other.append(name)
				zwischenliste_other.append(handle)
				zwischenliste_other.append(party)
				zwischenliste_other.append(date_day)
				zwischenliste_other.append(date_time)
				zwischenliste_other.append(tweet_id)
				zwischenliste_other.append(tweet_text)
				zwischenliste_other.append(expanded_url)
				zwischenliste_other.append(main_url_own_code)
				zwischenliste_other.append(main_url_unshortenit)
				zwischenliste_other.append(link_source)

				if len(row) > 12:

					quoted_handle = row[11]
					quoted_tweet_id = row[12]
					quoted_tweet_text = row[13]

					zwischenliste_other.append(quoted_handle)
					zwischenliste_other.append(quoted_tweet_id)
					zwischenliste_other.append(quoted_tweet_text)

				ergebnisliste_other.append(zwischenliste_other)


			



with open("CSV_Sublime\DoubleShortenCheck\Check_both_fail_01.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisliste_both_fail:

		ergebniswriter.writerow(row)


with open("CSV_Sublime\DoubleShortenCheck\Check_fail_01.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisliste_fail:

		ergebniswriter.writerow(row)


with open("CSV_Sublime\DoubleShortenCheck\Check_fb_01.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisliste_fb:

		ergebniswriter.writerow(row)

with open("CSV_Sublime\DoubleShortenCheck\Check_other_01.csv", "w", newline="", encoding="utf-8") as ergebnisCSV:

	ergebniswriter = csv.writer(ergebnisCSV, delimiter=";", quotechar = '"', quoting=csv.QUOTE_MINIMAL)

	for row in ergebnisliste_other:

		ergebniswriter.writerow(row)




