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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

"""

lst_of_receivers = []
for call in calls:
	if call[0].startswith('(080)'):
		lst_of_receivers.append(call[1])
total_number_of_receiver = len(lst_of_receivers)


def area_code(lst_of_receivers):
	area_code_lst = []
	for i in lst_of_receivers:
		if i.startswith('('):
			end = i.find(')')+1
			code = i[:end]
			if code not in area_code_lst:
				area_code_lst.append(code)
	area_code_lst.sort()
	print('The numbers called by people in banglore have codes:')
	for numbers in area_code_lst:
		print(numbers)


def mobile_prefixes(lst_of_receivers):
	mobile_list = []
	for call in lst_of_receivers:
		if " " in call:
			end = call.find(" ")
			prefix = call[:end]
			if prefix not in mobile_list:
				mobile_list.append(prefix)
	mobile_list.sort()
	print('The numbers called by people in banglore have prefixes:')
	for numbers in mobile_list:
		print(numbers)


def percentage(lst_of_receivers, length):
	banglore_itself = []
	for i in lst_of_receivers:
		if i.startswith('(080)'):
			banglore_itself.append(i)
	reveived_in_banglore = len(banglore_itself)
	percentage = round(reveived_in_banglore/length * 100,2)
	print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentage))


area_code(lst_of_receivers)
mobile_prefixes(lst_of_receivers)
percentage(lst_of_receivers, total_number_of_receiver)