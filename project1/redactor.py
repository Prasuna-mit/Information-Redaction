#import
import sys
import main
import glob
import numpy
from nltk.corpus import wordnet

#a_list = []
#a_list = sys.argv
#i_path = [] 
#o_path = ''
#concept = ''
#flags = []
#stats_list = []
#for i in range(len(a_list)):
#    print(a_list[i])
#    if a_list[i] == '--input':
#        i_path.append(a_list[i+1])

 #   else:
 #       if a_list[i] == '--output':
 #       o_path = a_list[i+1]
 #   else:
 #       if a_list[i] == '--concept':
 #           concept = a_list[i+1]
#for path in i_pathi:
 #   file = glob.glob(paths)
  #  if n in flags 

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

#for i in range(len(user_arguments)):
 #   if user_arguments[i] == "--names":
  #      read_file = main.names_red(ls)
   #     print(read_file)

 #   else:
  #      if user_arguments[i] == "--dates":
  #          data = main.dates(read_file)
  #          print(data)
