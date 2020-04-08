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
print(len(read_file))
main_file = read_file
#names

for i in range(len(user_arguments)):
    if user_arguments[i] == "--names":
        redacted_names,n_count = main.san_names(main_file)
        print(redacted_names)
#main_file2 = redacted_names
#print(main_file)
print("namesd redaction is done")
print(n_count)

#Dates
for i in range(len(user_arguments)):
    if user_arguments[i] == "--dates":
        redacted_dates,d_count = main.red_dates(redacted_names)
main_file3 = redacted_dates
print(redacted_dates)
print("dates redacted")
print(d_count)


#Location
for i in range(len(user_arguments)):
    if user_arguments[i] == "--locations":
        redacted_loc,lcount = main.red_locations(main_file3)
main_file4 = redacted_loc
print(redacted_loc)
print(lcount)
print("locatiniedacted")

#gender
for i in range(len(user_arguments)):
    if user_arguments[i] == "--gender":
        redacted_gender = main.red_locations(main_file4)
main_file5 = redacted_gender
print(redacted_gender)
print("gender redacted")

#contact numbers


