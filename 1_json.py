import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open(r'C:\Users\rabin\OneDrive\Pictures\Documents\assignment edyoda\assignment_6\employee.json', 'r') as json_file:
    data = json.load(json_file)
    for employee_data in data:
        name = employee_data["name"]
        dob = employee_data["DOB"]
        height = employee_data["height"]
        city = employee_data["city"]
        state = employee_data["state"]
        
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")