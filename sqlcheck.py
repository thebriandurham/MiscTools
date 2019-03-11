# sqlchecker.py
# Reads in a dict of reserved SQL keywords and scans the provided input to determine whether or not a SQL keyword is present
# Useful for PCAP analysis to determine validity of SQLi security events

# Import packages

def run():
	# Define Colors for reformatting
	C_RED = '\033[1;31;40m'
	C_BLUE = '\033[1;34;40m'

	# Init vars to store keywords from CSV
	sql_keywords = None
	words_file = '#pathToSQLWordsFile'

	# Open the CSV file and store it as a list
	with open(words_file, 'rb') as csv_file:
		file_reader = csv.reader(csv_file, delimiter=',')
		file_reader = list(file_reader)

	# Get user input to parse for reserved words
	check_string = raw_input('\nEnter string to parse for SQL reserved words: ').lower()

	# Check for presence of each keyword
	words_list = []
	for item in file_reader:
		for word in item:
			if word in check_string:
				words_list.append(word)
				check_string = check_string.replace(word,C_RED word + C_BLUE)

	# Print results
	print('\n' + check_string)
	print('\nKeywords found: ' + str(words_list))