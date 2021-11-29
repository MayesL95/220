def encode():
    x = input("Enter a message")
    key = eval(input("Enter a number value"))
    acc = " "
    for c in x:
        i = ord(c)
        new_chc = chr(key + i)
        acc = acc + new_chc
    print(acc)


def encode_better():
    m = input("Enter message")
    k = input("Enter key")
    acc = " "
    for i in range(len[m]):
        c = ord(m[i])
        key = ord(k[i])
        new_chrc = c + key - 97
        acc = acc + chr(new_chrc)
    print(acc)
