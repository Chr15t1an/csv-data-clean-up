#CSV Lib
import csv
import re

######Functions

def name_fix(a_input):
    if 'nmls_id:' in a_input:
        a_input=''
        return a_input
    else:
        a_input=re.sub("[^a-zA-Z]", " ", a_input)
        a_input = a_input.lower()
        a_input = a_input.capitalize()
        return a_input

    # Strips all but #s
def num_only(a_input):
        # Removes all non ints from NMLS ID
        a_input = re.sub("[^0-9]", "", a_input)
        return a_input

######Functions---END

#Read file
input_file = open('x.csv','r',encoding='utf-8')
csv_obj = csv.reader(input_file)


# Collect data we want
new_list = []

email = 15
fname = 13
lname = 14
nmls_id = 12
course_name = 16
course_medium = 3
year = "2016"


for row in csv_obj:
    new_list.append([row[email], row[fname], row[lname], row[nmls_id], row[course_name],row[course_medium]])
input_file.close()


a = 0

# Format

a = 0
output_list=[]
for row in new_list:
    a = a + 1  # Skip first row.
    if a > 1:

        #Email
        email = row[0]

        # Sanitise first name
        fname_c = name_fix(row[1])

        # #Sanitise last name
        lname_c = name_fix(row[2])

        # Removes all non ints from NMLS ID
        nmls_id_c = num_only(row[3])

        # COURSE NAME
        #2016 Online Self-Study {course title}
        #2016 Classroom {course title}

        course_title = row[4]
        course_medium = row[5]

        tag = ";"+year+" "+course_medium+" "+course_title

        output_list.append([email,fname_c, lname_c, nmls_id_c, tag])


    else:
        output_list.append(["Email","First Name", "Last Name", "NMLS ID", "Categories Bought"])


print(output_list)



    # Write to new file
out = open('nmls_contacts_new_data.csv', 'w', newline='', encoding='utf-8')
output = csv.writer(out)

for row in output_list:
    output.writerow(row)

out.close()