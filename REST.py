import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)
print(response.json())
# print(response.json()[0]["id"])

payload = {}  # empty dictionary

flag = 1
while flag:
    resp = input("Would you like to submit another profile?")
    if resp == "yes":
        # Employee ID Case
        id = input("Please enter employee ID: ")
        flagID = True
        while flagID:
            try:
                id = int(id)
                payload["id"] = id
                flagID = False
            except ValueError:
                print("Error. ID must be a number")
                id = input("Please enter employee ID: ")

        # Employee Name Case
        employee_name = input("Please enter employee name: ")
        flagName = True
        while flagName:
            if employee_name.isdigit():
                print("Must enter a name")
                employee_name = input("Please enter employee name")
            else:
                payload["employee_name"] = employee_name
                flagName = False

        # Emplyee Salary Case
        employee_salary = input("Please enter employee salary: ")
        flagSalary = True
        while flagSalary:
            try:
                employee_salary = int(employee_salary)
                payload["employee_salary"] = employee_salary
                flagSalary = False
            except ValueError:
                print("Error. Salary must be a number.")
                employee_salary = input("Please enter employee salary")

        # Employee Age Case
        employee_age = input("Please enter employee's age: ")
        flagAge = True
        while flagAge:
            try:
                employee_age = int(employee_age)
                payload["employee_age"] = employee_age
                flagAge = False
            except ValueError:
                print("Error. Age must be a number.")
                employee_age = input("Please enter employee's age")

        # Profile Image
        profile_image = input("Please enter employee image link: ")
        payload["profile_image"] = profile_image
    else:
        flag = 0

# print(payload)
url = "http://dummy.restapiexample.com/api/v1/create"
putthing = requests.post(url, json = payload)
print("Post Code:", putthing)


# Name Lookup
flag2 = False
flag = 1

while flag:
    quest = input("Want to look someone up by name?")
    if quest == "yes":
        name = input("What is the name?")
        for x in range(len(response.json())):
            if response.json()[x]["employee_name"] == name:
                flag2 = True
        if flag2:
            print("Person exists!")
        else:
            print("Nah")
    else:
        flag = 0

# Employee ID Lookup
flag2 = False
flag = 1

while flag:
    quest = input("Want to look someone up by employee ID?")
    if quest == "yes":
        idd = input("What is the ID?")
        for x in range(len(response.json())):
            if response.json()[x]["id"] == idd:
                flag2 = True
        if flag2:
            print("ID exists!")
        else:
            print("Nah")
    else:
        flag = 0

# Salary Lookup
flag2 = False
flag = 1

while flag:
    quest = input("Want to look someone up by salary")
    if quest == "yes":
        idd = input("What is the salary?")
        for x in range(len(response.json())):
            if response.json()[x]["employee_salary"] == idd:
                flag2 = True
        if flag2:
            print("salary exists!")
        else:
            print("Nah")
    else:
        flag = 0

# Age Lookup
flag2 = False
flag = 1
while flag:
    quest = input("Want to look someone up by age?")
    if quest == "yes":
        idd = input("What is the age?")
        for x in range(len(response.json())):
            if response.json()[x]["employee_age"] == idd:
                flag2 = True
        if flag2:
            print("Employee exists!")
        else:
            print("Nah")
    else:
        flag = 0