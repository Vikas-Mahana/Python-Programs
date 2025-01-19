'''
create a python function called make_id that accepts a string parameter. the passed in string is the full name of a person which is meant to contain words that all start with a letter.
the output of the function is an id that comprises of the first character of the first two words of the full name passed in (both capitalised) followed by the current timestamp (in seconds) and three random digits.
if the name is incomplete, replace the bad character(s) with x for example make_id("sachin tendulkar")= st1617628389348, make_id("kerala 22") = kx1617628389199. you can use the modules random, time and/or datetime.
'''
import random
from datetime import datetime
import sys
#Three digit random generator
randomNumber = random.randint(100,900)
#Gtting current time
now = datetime.now()
current_time = now.strftime("%H%M%S")

#Catching the exception for no entry , one Entry or more than one name entry

try: 
    while(True):
        #Enter full name
        fullName = input('Please enter your full name:-')
        if not fullName:
            #please enter valid name
            print("Name can't be blank")
        else:
            break
    #consider first space split only, if name is more then two string long
    firstName , lastname = fullName.split(' ',1)

except ValueError:

    firstName = fullName
    lastname = "x"


print(f'{firstName[0]}{lastname[0]}{randomNumber}{current_time}'.upper())