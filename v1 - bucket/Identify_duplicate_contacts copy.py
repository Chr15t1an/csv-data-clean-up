import csv
import re
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def name_fix(a_input):
    if 'nmls_id:' in a_input:
        a_input=''
        return a_input 
    else:
        a_input=re.sub("[^a-zA-Z]", " ", a_input)
        a_input = a_input.lower()
        a_input = a_input.capitalize()
        return a_input
    
#Read file 
input_file = open('all-contacts.csv','r',encoding='utf-8')
csv_obj = csv.reader(input_file)


#Collect data we want
new_list =[]

for row in csv_obj:     
    #Fname - Lname - Email
    fnam = row[14]
    lnam = row[17]
    email = row[0]

    new_list.append([fnam,lnam,email])
input_file.close()
#print(new_list)

#format first + last names
a = 0
for row in new_list:
    a=a+1 #Skip first row.
    if a > 1 :
        row[0] = name_fix(row[0])
        row[1] = name_fix(row[1])


#list of fname + lname + email
new_list
prep_forcomp =[]


entries = set()
dup = [['First Name','Last Name','Email']]
for row in new_list:
    key = (row[0], row[1]) # instead of just the last name
    if key not in entries:
        entries.add(key)
    else:
        dup.append([row[0],row[1],row[2]])

print(dup)



#Write to new file 
out = open('duplicate_contacts_new_data.csv', 'w', newline='',encoding='utf-8')
output=csv.writer(out)

for row in dup:
    output.writerow(row)

out.close()