#import
import sys
import main
import glob
import numpy
from nltk.corpus import wordnet

#for getting arguments
user_arguments = sys.argv
#print(user_arguments)        

for i in range(len(user_arguments)):
    if user_arguments[i] == "--input":
        read_file = main.read_arg(user_arguments[i+1])
#print(len(read_file))
main_file = read_file
#names

for i in range(len(user_arguments)):
        if user_arguments[i] == "--names":
            redacted_names,n_count = main.san_names(main_file)
main_file = redacted_names
#print(redacted_names)
print("namesd redaction is done")
print(n_count)

#Dates
for i in range(len(user_arguments)):
        if user_arguments[i] == "--dates":
            redacted_dates,d_count = main.red_dates(main_file)
main_file = redacted_dates
#print(redacted_dates)
print("dates redacted")
print(d_count)


#Location

for i in range(len(user_arguments)):
        if user_arguments[i] == "--locations":
            redacted_loc,lcount = main.red_locations(main_file)
main_file = redacted_loc
print(lcount)
print("locatiniedacted")

#contact numbers

def redact_phones(ptext):
    red = deepcopy(ptext)
    phone = re.compile(r'''((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))''')
    phones = re.findall(phone,ptext)
    for j in phones:
        b1 = "█"*(len(j))
        red = red.replace(j,b1)
    return red
phone_red_file = redact_phones(ptext)
phone_red_fil
