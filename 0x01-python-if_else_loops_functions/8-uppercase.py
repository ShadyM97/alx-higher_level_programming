#!/usr/bin/python3
def uppercase(str):
    for x in range(len(string)):
        if ord(string[x]) < ord('a'):
            c = ord(string[x]) - 32
	    print('{}'.format(chr(c)), end="")
        else:
            print('{}'.format(string[x], end="")
