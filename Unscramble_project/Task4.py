"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers_list = []
for numbers in calls:
	for number in numbers:
		if number.startswith('140') and len(number) == 10:
			telemarketers_list.append(number)

no_duplicate_list = []
for i in telemarketers_list:
	if i not in no_duplicate_list:
		no_duplicate_list.append(i)

print("These numbers could be telemarketers: ")
no_duplicate_list.sort()
for i in no_duplicate_list:
	print(i)