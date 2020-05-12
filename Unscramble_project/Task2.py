"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
max_time = 0
record_dictionary = {}
for call in calls:
	record_dictionary[call[0]] = 0
	record_dictionary[call[1]] = 0

for record in record_dictionary:
	for call in calls:
		if record == call[0]:
			temp_var = record_dictionary[record]
			record_dictionary[record] = int(temp_var) + int(call[3])
		if record == call[1]:
			temp_var = record_dictionary[record]
			record_dictionary[record] = int(temp_var) + int(call[3])


maximum = max(record_dictionary, key = record_dictionary.get)
print ("{} spent the longest time, {} seconds, on the phone during September 2016".format(maximum,record_dictionary[maximum]))