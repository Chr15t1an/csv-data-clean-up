#CSV Lib
import csv
#Form libs
import re
from difflib import SequenceMatcher


#State - library
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}






#Functions
#Strips all but #s
def num_only(a_input):
    #Removes all non ints from NMLS ID 
    a_input=re.sub("[^0-9]", "", a_input)
    return a_input

def phone_fix(a_input):
    if a_input.startswith('1'): 
        #print('rah')
        a_input = a_input[1:]
        
    if len(a_input)> 10:
        a_input = ' X '.join([a_input[:10],a_input[10:]])
        #print('blah')
        
    if a_input: 
        a_input = '-'.join([a_input[:3], a_input[4:7], a_input[6:]])

    return a_input


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


def state_fix(a_input):
    if len(a_input) > 2:
        for name, code in us_state_abbrev.items():
            a_input = a_input.capitalize()
            if a_input == name:
                return code
           
    else:
        return a_input.upper()
       









#End_functions


#Read file 
input_file = open('all-contacts-2017-03-25.csv','r',encoding='utf-8')
csv_obj = csv.reader(input_file)


#Collect data we want
new_list =[]

for row in csv_obj:    
    
    # 224 => Email - #01 => Last name - #00 First Name - #169 NMLS - #23 phone # - #22 Mobile  -- state

    email = row[0]
    lnam = row[17]
    fnam = row[14]
    nmls = row[18]
    phone = row[23]
    mobile = row[22]
    state = row[41]

    new_list.append([email,lnam,fnam,nmls,phone,mobile,state])

input_file.close()


#Format

a = 0 

for row in new_list:
    a=a+1 #Skip first row.
    if a > 1 :
        
        #Sanitise last name
        row[1] = name_fix(row[1])
        
        # #Sanitise first name
        row[2] = name_fix(row[2])
        
        #Removes all non ints from NMLS ID 
        row[3] = num_only(row[3])
       
        #Formats phone 4
        row[4] = num_only(row[4])
        row[4] = phone_fix(row[4])
        
        #Formats phone 5
        row[5] = num_only(row[5])
        row[5] = phone_fix(row[5])
    
        
        #Formats State
        
        row[6] = state_fix(row[6]) 
        
        
        
        
        
        #print(row[7])       
        #print(row[4],row[5],row[6])



#Write to new file 
out = open('clean_contacts_new_data.csv', 'w', newline='',encoding='utf-8')
output=csv.writer(out)

for row in new_list:
    output.writerow(row)
    
out.close()

