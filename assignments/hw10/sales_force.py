"""
Name: Lindy Mayes

File Name: sales_force.py

Problem: create a sales force class

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
from sales_person import SalesPerson
def create_sales_people(line):
    employee_id, name, sale_amounts = line.split(",")
    return employee_id, name, float(sale_amounts)

class SalesForce:
    def __init__(self):
        self.sales_people = ""

    def add_data(self, file_name):
        file = open(file_name, "r")
        for line in file:
            current_seller = create_sales_people(line)
        return current_seller

    def quota_report(self, quota):
        return "{0}, {1}, {2}, {3},".format(SalesPerson.get_id(), SalesPerson.get_name(),
                                            SalesPerson.total_sales(), SalesPerson.met_quota())
    def top_seller(self):
        top_seller = create_sales_people(file.readline())
        if curent_seller < top_seller:
            top_seller = current_seller
            return top_seller
        if current_seller == top_seller:
            return curent_seller, top_seller

    def individual_sales(self, employee_id):
        return SalesPerson.get_id()






