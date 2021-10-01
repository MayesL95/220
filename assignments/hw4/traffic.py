"""
Name: Lindy Mayes

File Name: traffic.py

Problem: Analyze traffic patterns

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""

def main():
    ttl = 0
    roads_surveyed = eval(input("How many roads were surveyed?"))
    for road in range(roads_surveyed):
        days_surveyed = eval(input("how many days was road " + str(road + 1) + " surveyed? "))
        acc = 0
        for day in range(days_surveyed):
            cars_traveled = eval(input("How many cars traveled on day " + str(day + 1) + "?"))
            acc = acc + cars_traveled
            ttl = ttl + cars_traveled
        print(" Road " + str(road +1) + " average vehicles per day ", acc / days_surveyed)
    print("Total number of vehicles traveled on all roads:", ttl)
    print("Average number of vehicles per road:", round(ttl / roads_surveyed, 2))

if __name__ == '__main__':
    main()





















