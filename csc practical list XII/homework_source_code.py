import sys
import random as r
import pickle as p
import zampy as zp
import csv
import mysql.connector
#Default functions:
def read_b(file_name):
    data = p.load(open(file_name, "rb"))
    print(data)
    return data



#⦁	Write a program using user defined function to find factorial of a number.
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

#⦁	Write a program using user defined function to accept two numbers as parameters, if num1 is less than num2 swap them and return the values otherwise return the numbers as is.

def swapnumbers(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    return num1, num2


#⦁	Write a program to generate a random number between 1 and 6 (simulates a dice).
def dice():
    return r.randint(1, 6)

#⦁	Write a user defined function EvenSum(numbers) to add those values from the list of NUMBERS which are at even positions.
def evensum(numbers):
    return sum([numbers[i] for i in range(len(numbers)) if i % 2 == 0])

#⦁	Write a program to read a text file line by line and display each word separated by '#'.
def read_file_return_hashes(file_name):
    return open(file_name).read().replace(" ", "#")

#print(read_file_return_hashes("sample.txt"))
#⦁	Write a program to read a text file and display the number of vowels, consonants, uppercase and lowercase in the file.
def vcul(file_name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vc, cc, uc, lc = 0, 0, 0, 0
    with open(file_name, "r") as f:
        data = f.read()
        for char in data:
            if char.isalpha():
                if char.islower():
                    lc += 1
                else:
                    uc += 1
                if char.lower() in vowels:
                    vc += 1
                else:
                    cc += 1
    return vc, cc, uc, lc

#print(vcul("sample.txt"))
#7.	Write a program to remove all the lines that contains the character 'a' in a file and write it to another textfile ‘OTHER.TXT’.
def disbanda(file_name):
    fmain = open(file_name, "r")
    main_data = fmain.readlines()
    fmain.close()
    fmain = open(file_name, "w")
    other = open("other.txt", "w")
    otherlines = []
    fmainlines = []
    #print(main_data)
    for line in main_data:
        if 'a' in line.lower():
            otherlines.append(line)
        else:
            fmainlines.append(line)
    other.writelines(otherlines)
    fmain.writelines(fmainlines)
    fmain.close()
    other.close()
#disbanda("sample.txt")
#8.	Write a method in python to read data from a text file INDIA.TXT, to count and display the occurrence of word ‘INDIA’.
def india(file_name):
    with open(file_name, "r") as fmain:
        return len([x for x in fmain.read().split() if x == "INDIA"])
#print(india("sample.txt"))
#9.	Write a program to input roll_no, name, marks & grade from the user and write it to a binary file Student.dat. The program must display the names of all the students who receive grade ‘A’.
def binary_file_maker_student():
    data = {}
    for i in range(int(input("Enter number of students: "))):
        roll_no = int(input(f"Enter roll number for student {i + 1}: "))
        marks = int(input(f"Enter marks for student {i + 1}: "))
        name = input(f"Enter name of student {i + 1}: ")
        grade = input("Enter grade: ").upper()
        data[roll_no] = (marks, name, grade)
    f_main = open("student.dat", "wb")
    p.dump(data, f_main)
    
    #data = p.load(open("student.dat", "rb"))
    #print(data)
    for key in data.keys():
        if data[key][2] == "A":
            print(data[key])

#binary_file_maker_student()
#10. Write a menu driven program to read employee data (EmpId,EmpName,EmpSal) and write it into a binary file emp.dat. Based on the user’s choice the program must search (), update (), delete () or read () more data into the file.
main_file_name = "employee_data.dat"

def write_employee_data(): #Items in the dictionary
    try:
        f_def = open(main_file_name, "rb")
        existing_data = p.load(f_def)
    except Exception as e:
        print("No existing data. Error:", e)
        existing_data = []
    else:
        f_def.close()
    new_data = []
    f_main = open("employee_data.dat", "wb+")
    for i in range(int(input("Enter number of employees: "))):
        new_data.append([int(input("Enter employee id: ")), input("Enter employee name: "), int(input("Enter employee salary: "))])
    p.dump(existing_data + new_data, f_main)
    f_main.close()

def search():
    name = input("Enter the employee name: ")
    try:
        data = p.load(open(main_file_name, "rb+"))
        for record in data:
            if name in record:
                print(record)
    except Exception as e:
        print("Some error occured:", e)
    
    

def update():
    name = input("Enter the employee name: ")
    f_main = open(main_file_name, "rb+")
    try:
        data = p.load(f_main)
        for record in data:
            if name in record:
                user_input = int(input(f"Record found.\n1 - Update employee ID\n2 - Update employee name\n3 - Update employee salary"))
                if user_input == 1:
                    new_data = int(input("Enter employee ID: "))
                    record[0] = new_data
                elif user_input == 2:
                    new_data = input("Enter employee name: ")
                    record[1] = new_data
                elif user_input == 3:
                    new_data = int(input("Enter employee salary: "))
                    record[2] = new_data
        f_new = open(main_file_name, "wb")
        p.dump(data, f_new)
        print("Updated successfully.")
    except Exception as e:
        print("Some error occured:", e)
    f_main.close()


def delete():
    name = input("Enter the employee name: ")
    f_main = open(main_file_name, "rb+")
    try:
        data = p.load(f_main)
        for record in data:
            if name in record:
                data.remove(record)
        f_new = open(main_file_name, "wb")
        p.dump(data, f_new)
        print("Deleted successfully.")
    except Exception as e:
        print("Some error occured:", e)
    f_main.close()

def read():
    try:
        print(p.load(open(main_file_name, "rb")))
    except Exception as e:
        print("Some error occured while trying to read:", e)

'''while True:
    user_input = int(input(f"1 - Write employee data\n2 - Read existing data\n3 - Search for a record\n4 - Update a record\n5 - Delete a record\n0 - Exit\nInput: "))
    if user_input == 1:
        write_employee_data()
    elif user_input == 2:
        read()
    elif user_input == 3:
        search()
    elif user_input == 4:
        update()
    elif user_input == 5:
        delete()
    elif user_input == 0:
        break
'''
'''data = dict()
for i in range(5):
    data[zp.random_number(2, False)] = [zp.random_name(1) + "'s Movie", zp.random_genre()]'''
#zp.create_file_with_data("cinema", ".dat", data)

def copyData():
    f_new = open("basket.dat", "wb")
    data = p.load(open("sport.dat", "rb"))
    dump_data = []
    count = 0
    for record in data:
        if "Basketball" in record:
            dump_data.append(record)
            count += 1
    p.dump(dump_data, f_new)
    f_new.close()
    return count

def findtype(mtype):
    f_main = open("cinema.dat", "rb")
    data = p.load(f_main)
    output_data = []
    for item in data.items():
        if mtype in item[1]:
            output_data.append(item)
    print(f"All records having {mtype}: {output_data}")

def expensiveProducts():
    f_main = open("inventory.dat", "rb")
    data = p.load(f_main)
    c = 0
    for record in data:
        if record[3] > 1000:
            c += 1
            print("Product ID:", record[0])
    print(f"Total expensive products: {c}")

def findBook(price):
    main_file = open("book.dat", "rb")
    data = p.load(main_file)
    main_file.close()
    for item in data.items():
        if item[1][2] >= price:
            print(item)

#findBook(4000)

#⦁	Write a program to search and display all those records of the students whose marks are 50 and above in a binary file Student.dat.
#   Assumed format: [StudentName, StudentRollNo, StudentMarks]
def show_top_students():
    return [x for x in p.load(open("Student.dat", "rb")) if x[2] > 50]

#print(show_top_students())
'''file_name = "Student"
data = list()
for i in range(10):
    data.append([zp.random_name(), i + 1, zp.random_number(1)])
zp.create_file_with_data(file_name, ".dat", data)
read_b(file_name + ".dat")'''

#⦁	Write a program to generate a csv file by reading rollno, name and marks from user. 
#The program must display the name when rollno is entered. If not found, displays appropriate message.

def csv_from_students_data():
    main_file = open("Students_Data.csv", "w", newline="")
    writer = csv.writer(main_file)
    writer.writerow(["Roll No", "Name", 'Marks'])
    while True:
        data = [int(input("Enter roll no: ")), input("Enter name: "), int(input("Enter marks: "))]
        writer.writerow(data)
        if input("Continue: ").lower() == 'n':
            break

def search_student_from_csv():
    main_file = open("Students_Data.csv", "r")
    reader = csv.reader(main_file)
    next(reader)
    roll_no = input("Roll no of student to be found: ")
    data = {}
    for record in reader:
        data[record[0]] = [record[1], record[2]]
    if roll_no in data.keys():
        for key in data.keys():
            if key == roll_no:
                print(data[key][0])
    else:
        print("No student with given roll number found.")

#search_student_from_csv()
#⦁	Create a CSV file by entering user-id and password, read and search the password for given userid.
def csv_with_id_pass():
    main_file = open("ID_password.csv", 'w', newline='')
    writer = csv.writer(main_file)
    writer.writerow(['User ID', 'Password'])
    while True:
        writer.writerow([input('Enter user id: '), input("Enter password: ")])
        if input('Continue: ').lower() == 'n':
            break
    
def search_id_pass_csv():
    main_file = open("ID_password.csv",'r')
    reader = csv.reader(main_file)
    next(reader)
    uid = input("Enter user id whose password you need: ")
    for record in reader:
        if record[0] == uid:
            print("Password:", record[1])
#search_id_pass_csv()
#Write a program to read the dictionary dict1= {“Dev”:45,” Ravi”:56,” tej”:78}
#Consisting of name and marks of students. Include a function to push name of those students into the stack 
#where marks are greater than 75. Display the contents of the stack
dict1 = {'Dev':45, 'Ravi':56, 'tej':78}
stack = []

def push(s, ele):
    s.append(ele)

for key, value in dict1.items():
    if value > 75:
        push(stack, key)

for item in stack:
    print(item)

#Sami has a list L1 containing 10 integers you need to help him create a program with separate functions 
#to push () those elements from list L1 which are at even positions 
#and pop() to empty the stack and print the contents.
L1 = [500, 900, 100, 700, 500, 300, 100, 200, 900, 500]
stack = []
def PUSH(s, ele):
    s.append(ele)

def POP(s):
    try:
        return s.pop()
    except:
        print("Some error occured while trying to pop.")

for index in range(len(L1)):
    if index % 2 == 0:
        PUSH(stack, L1[index])

while stack:
    print(POP(stack)) 

#1. Write a program to connect with database to read and store record of employees and display all
#   records

database = mysql.connector.connect(host='localhost', user='root', password='admin', database='hospital_main')
cursor = database.cursor()

def display_all_records():
    cursor.execute('select * from doctors;')
    return cursor.fetchall()

def add_new_record():
    doctorID = input('Enter emplyee ID: ')
    name = input('Enter name of employee: ')
    cursor.execute(f'insert into doctors (doctorID, name) values ("{doctorID}", "{name}")')

while True:
    option = int(input('Enter action:\n1. Read existing employees data\n2. Enter new employee record\n3. Exit\n'))
    if option == 1:
        data = display_all_records();
        for index in range(len(data)):
            print(f'{index + 1}. {data[index]}')
    elif option == 2:
        add_new_record()
    else:
        break

#2. Write a program to connect with database to search/update/delete employee records in the table
#employee depending upon user’s choice and display the records. If the employee number is not
#found, the program must display an appropriate message.