"""
Name: Lindy Mayes

File Name: sales_person.py

Problem: create a salesperson class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = 0

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales = sale

    def total_sales(self):
        acc = 0
        for total in self.get_sales():
            acc += total
        return self.sales

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        self.quota = quota
        if self.sales >= quota:
            return True
        else:
            return False

    def compare_to(other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        if other.total_sales() == self.total_sales():
            return 0
    def __str__(self):
        return "{0}, {1}, {2}".format(self.employee_id, self.name, self.sales)