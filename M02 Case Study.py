# Sam Richardson
# Dean's List/Honor Roll Eligibility
# The program takes user input (last name, first name, and gpa) and determines if a student is on the Dean's List or Honor Roll.

Lname_list = []
Fname_list = []
gpa_list = []
# These lists store the information that users input

while True:
  
  Lname = input("Enter last name: ")
  if Lname.lower() == "zzz":
    break
  else:
    Lname_list.append(Lname)
    
  Fname = input("Enter first name: ")
  Fname_list.append(Fname)
  gpa = input("Enter GPA: ")
  gpa = float(gpa)
  gpa_list.append(gpa)

for x in range(2):
  print("\n")
# Two blank lines are printed to separate the input from the output

for i in range (len(Lname_list)): 
  if gpa_list[i] >= 3.5:
    print(f"{Fname_list[i]} {Lname_list[i]} is on the Dean's List")
  elif gpa_list[i] >= 3.25:
    print(f"{Fname_list[i]} {Lname_list[i]} is on the Honor Roll")
# This loop goes through the number of names that are stored in the last name list and determines if each person has qualified for the Dean's List or Honor roll