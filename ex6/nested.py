#!/usr/bin/env python3

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_info(self):
            return f"{self.name} the {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_info() for employee in self.employees]

company = Company("Krusty Krab")

company.add_employee("Spongebob", "Cook")
company.add_employee("Eugene", "Manager")
company.add_employee("Squidward", "Cashier")

for employee in company.list_employees():
    print(employee)

company2 = Company()

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

for employee in company2.list_employees():
    print(employee2)