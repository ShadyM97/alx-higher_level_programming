#!/usr/bin/python3
def uppercase(str):
    for x in range(len(string)):
        if ord(string[x]) < ord('a'):
            c = ord(string[x]) - 32
        else:
            c = ord(string[x])
        print('{}'.format(chr(c)), end="")
    print('\n')
