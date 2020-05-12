import csv
from itertools import chain

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
telephone_numbers_in_texts = list(chain.from_iterable(
    [(sender, reciever) for sender, reciever, _ in texts]))

texters = set(telephone_numbers_in_texts)

callers = set()
call_recievers = set()

for caller, reciever, _, _ in calls:
    callers.add(caller)
    call_recievers.add(reciever)

# telemarkerters don't text or revicieve callers
possible_telemarkerters = callers - (texters | call_recievers)

print("These numbers could be telemarketers:")

for tel_number in sorted(possible_telemarkerters):
    print(tel_number)
