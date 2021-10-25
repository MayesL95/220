"""
Name: Lindy Mayes
Functions.py
"""
from encryption import encode, encode_better
def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(i + " " + word + "\n")
            i += 1
    infile.close()
    outfile.close()

def hourly_wages (in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts = line.split()
        wage = int(parts[2])
        wage += 1.65
        wage = wage * int(parts[2])
        outfile.write(parts[0] + parts[1] + wage + "\n")

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn[:] * pos)
    return acc

def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".text", "w+")
    for line in infile:
        outfile.write(line)

def send_secret_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".text", "w+")
    for line in infile:
        outfile.write(encode(line,key))

def send_uncrackable_meessage(file, friend, pad):
    pad_file = open(pad, "r")
    key = pad_file.read()
    infile = open(file, "r")
    outfile = open(friend + ".text", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    hourly_wages(hourly_wages.txt, hourly_wages.txt)
    calc_check_sum(0072946520)
    send_message(message.txt, bob)
    send_secret_message(secret_message.txt, bob, 5)
    send_uncrackable_meessage(safest_message.txt, bob, pad.txt)



main()
