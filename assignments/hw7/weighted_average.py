"""
Name: Lindy Mayes

File Name: weighted_average.py

Problem: read and write files and solving averages

Certification of Authenticity:
I certify that this assignment is entirely my own work
    but I did use the internet for help
"""

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        student_and_grades_seperated = line.split(":")
        grades_and_weights = student_and_grades_seperated[1]
        grades_and_weights_seperated = grades_and_weights.split(" ")
        acc = 1
        for i in range(len(grades_and_weights_seperated)):
            grades = grades_and_weights_seperated[1::2]
            weights = grades_and_weights_seperated[2::2]
            acc = 0
            for x, y in zip(grades, weights):
                acc += x * y
                student_average = acc / sum(weights)
                if sum(weights) < 100:
                    print("Error: The weights are less than 100")
                if sum(weights) > 100:
                    print("Error: The weights are more than 100")
                    outfile.write(grades_and_weights_seperated[0] + print("averge:") +
                                  round(student_average, 1)

    infile.close()
    outfile.close()


def main():
    weighted_average(grades.txt, avg.txt)








