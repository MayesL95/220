"""
Name: Lindy Mayes

File Name: interest.py

Problem: Calculate the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

def main():
    print("This program calculates the monthly interest charge on a credit card account")
    net_balance = eval(input("input your previous net balance"))
    billing_cycle = eval(input("input number of days in your billing cycle"))
    net_payment = eval(input("input the payment amount"))
    day_of_payment = eval(input("input the day of the billing cycle the payment was made"))
    days_left_in_cycle = billing_cycle - day_of_payment
    annual_interest_rate = eval(input("input your interest rate for the year"))
    monthly_balance = net_balance * billing_cycle
    payment_during_month = net_payment * days_left_in_cycle
    new_monthly_total = monthly_balance - payment_during_month
    avg_daily_balance = new_monthly_total / billing_cycle
    print("your average daily balance is $", round(avg_daily_balance, 2))
    monthly_interest_rate = annual_interest_rate / 12
    decimal_monthly_interest_rate = monthly_interest_rate / 100
    monthly_interest_charge = avg_daily_balance * decimal_monthly_interest_rate
    print("the monthly interest charge is $", round(monthly_interest_charge, 2))

if __name__ == '__main__':
    main()



