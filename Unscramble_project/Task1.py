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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

total_list = []

for text in texts:
	total_list.append(text[0])
	total_list.append(text[1])

for call in calls:
	total_list.append(call[0])
	total_list.append(call[1])

corrected_list=[]

for i in total_list:
	if i not in corrected_list: 
	    corrected_list.append(i) 

print("There are {} different telephone numbers in the records.".format(len(corrected_list)))