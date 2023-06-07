#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) < ord('a'):
            c = ord(str[x]) - 32
        else:
            c = ord(str[x])
        print('{}'.format(chr(c)), end="")
    print('\n')
