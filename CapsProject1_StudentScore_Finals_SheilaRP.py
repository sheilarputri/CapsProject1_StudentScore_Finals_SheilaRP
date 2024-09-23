#STUDENT UNIVERSITY DATA DICTIONARY
student_dictionary = {
    101 : {'Student Name': 'Camila Wood', 'University': 'Stanford University', 'Program': 'Finance', 'General Score': 93, 'Domain Score': 88},
    102 : {'Student Name': 'Alexander Thompson', 'University': 'Stanford University', 'Program': 'Information Technology', 'General Score': 95, 'Domain Score': 90},
    201 : {'Student Name': 'Liam Taylor', 'University': 'Harvard University', 'Program': 'Communication', 'General Score': 90, 'Domain Score': 75},
    103 : {'Student Name': 'Evelyn Jenkins', 'University': 'Stanford University', 'Program': 'Art', 'General Score': 78, 'Domain Score': 88},
    202 : {'Student Name': 'Michael Jackson', 'University': 'Harvard University', 'Program': 'Art', 'General Score': 80, 'Domain Score': 92},
    104 : {'Student Name': 'Chloe Moore', 'University': 'Stanford University', 'Program': 'Communication', 'General Score': 79, 'Domain Score': 84},
    203 : {'Student Name': 'Nicholas Clark', 'University': 'Harvard University','Program': 'Finance', 'General Score': 88, 'Domain Score': 49,'Total Score': 98},
    105 : {'Student Name': 'Olivia Richardson', 'University': 'Stanford University','Program': 'Finance', 'General Score': 77, 'Domain Score': 93},
    106 : {'Student Name': 'Aiden Rivera', 'University': 'Stanford University', 'Program': 'Information Technology', 'General Score': 89, 'Domain Score': 95},
    204 : {'Student Name': 'Harper Turner', 'University': 'Harvard University','Program': 'Communication', 'General Score': 92, 'Domain Score': 90},
    107 : {'Student Name': 'Madison Lee', 'University': 'Stanford University','Program': 'Information Technology', 'General Score': 77, 'Domain Score': 85},
    205 : {'Student Name': 'Carter Hall', 'University': 'Harvard University', 'Program': 'Finance', 'General Score': 85, 'Domain Score': 77},
    206 : {'Student Name': 'Mia Thomas', 'University': 'Harvard University','Program': 'Art', 'General Score': 95, 'Domain Score': 90},
    108 : {'Student Name': 'Lucas Evans', 'University': 'Stanford University','Program': 'Communication', 'General Score': 87, 'Domain Score': 91},
    207 : {'Student Name': 'Abigail Bailey', 'University': 'Harvard University', 'Program': 'Information Technology', 'General Score': 90, 'Domain Score': 83}
}

#Average Score
for key,value in student_dictionary.items():
    average = int((student_dictionary[key]['General Score']+student_dictionary[key]['Domain Score']) / 2)
    student_dictionary[key]['Total Score']=average

#Sort By Total Score
def mySort(n):
    key, value = n
    return int(value["Total Score"])

#Main Menu
def menu_options():
    menu_options = (1, 2, 3, 4, 5, 6)

while True:
    print()
    print('WELCOME TO --UNIVERSITY STUDENT-- DATA')
    print(1, 'Create Student Data')
    print(2, 'Search Student')
    print(3, 'Update Student Score')
    print(4, 'Delete Student')
    print(5, 'Sorting Score')
    print(6, 'EXIT')

    print()
    menu_options = int(input("Enter the number you want to run: "))
    if menu_options == 1: #-Create Student Data-#
        input1 = int(input("STUDENT ID : "))
        if input1 in student_dictionary:
            print("Your Student ID Already Exist, Input Another One")
            break
        else:
            input2 = input("NAME OF THE STUDENT : ")
            input3 = input("UNIVERSITY : ")
            input4 = input("PROGRAM : ")
            input5 = 0
            input6 = 0
            input7 = 0
            student_dictionary[input1]= {'Student Name': input2, 'University': input3, 'Program': input4, 'General Score': input5, 'Domain Score': input6, 'Total Score': input7}
            print("Student Data Saved")
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            print(f"{student_dictionary[input1]['Student Name']:<18} | {input1:<14} | {student_dictionary[input1]['University']:<19} | {student_dictionary[input1]['Program']:<22} | {student_dictionary[input1]['General Score']:<17} | {student_dictionary[input1]['Domain Score']:<16} | {student_dictionary[input1]['Total Score']:<19}")
            
    elif menu_options == 2: #-Search Student-#
        menu_options = input("ALL or SPECIFIC: ")
        if menu_options == 'ALL':
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            for key,value in student_dictionary.items():
                print(f"{student_dictionary[key]['Student Name']:<18} | {key:<14} | {student_dictionary[key]['University']:<19} | {student_dictionary[key]['Program']:<22} | {student_dictionary[key]['General Score']:<17} | {student_dictionary[key]['Domain Score']:<16} | {student_dictionary[key]['Total Score']:<19}")
            break
        elif menu_options == 'SPECIFIC':
            menu_options = int(input('STUDENT ID: '))
            if menu_options not in student_dictionary:
                print("NO STUDENT WITH THE ID")
                break
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            print(f"{student_dictionary[menu_options]['Student Name']:<18} | {menu_options:<14} | {student_dictionary[menu_options]['University']:<19} | {student_dictionary[menu_options]['Program']:<22} | {student_dictionary[menu_options]['General Score']:<17} | {student_dictionary[menu_options]['Domain Score']:<16} | {student_dictionary[menu_options]['Total Score']:<19}")
            break
    
        else:
            print()
            print('NO OPTION, BACK TO MAIN MENU')

    elif menu_options == 3: #-Update Student Score-#
        menu_options = int(input("Enter Student ID for Change: "))
        if menu_options in student_dictionary:
            new_general = int(input("Enter New General Score: "))
            new_domain = int(input("Enter New Domain Score: "))
            new_total = (int(new_general+new_domain) / 2)
            student_dictionary[menu_options]['General Score'] = new_general
            student_dictionary[menu_options]['Domain Score'] = new_domain
            student_dictionary[menu_options]['Total Score'] = new_total
            print("Score Change Has Been Saved")
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            print(f"{student_dictionary[menu_options]['Student Name']:<18} | {menu_options:<14} | {student_dictionary[menu_options]['University']:<19} | {student_dictionary[menu_options]['Program']:<22} | {student_dictionary[menu_options]['General Score']:<17} | {student_dictionary[menu_options]['Domain Score']:<16} | {student_dictionary[menu_options]['Total Score']:<19}")
            break  
        else:
            print("Student ID not available")

    elif menu_options == 4: #-Delete Student-#
        menu_options = int(input('Student ID you want to Delete: '))
        menu_options2 = input('Enter Student Name to Confirm: ')
        menu_options3 = input('Enter University to Confirm: ')
        menu_options4 = input('Enter Program to Confirm: ')
        if menu_options2 == student_dictionary[menu_options]['Student Name'] and menu_options3 == student_dictionary[menu_options]['University'] and menu_options4 == student_dictionary[menu_options]['Program']:
            del student_dictionary[menu_options]
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            for key,value in student_dictionary.items():
                print(f"{student_dictionary[key]['Student Name']:<18} | {key:<14} | {student_dictionary[key]['University']:<19} | {student_dictionary[key]['Program']:<22} | {student_dictionary[key]['General Score']:<17} | {student_dictionary[key]['Domain Score']:<16} | {student_dictionary[key]['Total Score']:<19}")
            break

    elif menu_options == 5: #-Sorting by Score-#
        print(1, 'ALL')
        print(2, 'FILTER BY UNIVERSITY')
        print(3, 'FILTER BY PROGRAM')
        menu_options = int(input("Enter Sort You Want to Run (1/2/3: )"))
        student_dictionary = dict(sorted(student_dictionary.items(), key=mySort, reverse=True))
        if menu_options == 1:
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            for key,value in student_dictionary.items():
                print(f"{student_dictionary[key]['Student Name']:<18} | {key:<14} | {student_dictionary[key]['University']:<19} | {student_dictionary[key]['Program']:<22} | {student_dictionary[key]['General Score']:<17} | {student_dictionary[key]['Domain Score']:<16} | {student_dictionary[key]['Total Score']:<19}")
            break
        elif menu_options == 2:
            user_input = input("UNIVERSITY NAME: ")
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            for key,value in student_dictionary.items():
                if user_input.lower() in value["University"].lower():
                    print(f"{student_dictionary[key]['Student Name']:<18} | {key:<14} | {student_dictionary[key]['University']:<19} | {student_dictionary[key]['Program']:<22} | {student_dictionary[key]['General Score']:<17} | {student_dictionary[key]['Domain Score']:<16} | {student_dictionary[key]['Total Score']:<19}")
                else:
                    continue
            break
        elif menu_options == 3:
            user_input = input("PROGRAM NAME: ")
            print('UNIVERSITY STUDENT DATA'.center(140,' '))
            print('-'*140)
            print('   Student Name    |   Student ID   |     University      |         Program        |   General Score   |   Domain Score   |   Total Score   ')
            print('_'*140)
            for key,value in student_dictionary.items():
                if user_input.lower() in value["Program"].lower():
                    print(f"{student_dictionary[key]['Student Name']:<18} | {key:<14} | {student_dictionary[key]['University']:<19} | {student_dictionary[key]['Program']:<22} | {student_dictionary[key]['General Score']:<17} | {student_dictionary[key]['Domain Score']:<16} | {student_dictionary[key]['Total Score']:<19}")
                else:
                    continue
            break
        break

    elif menu_options == 6: #-EXIT-#
        print()
        print("EXIT STUDENT DATA")
        exit
        break

    else:
        print()
        print('OPTIONS NOT AVAILABLE')