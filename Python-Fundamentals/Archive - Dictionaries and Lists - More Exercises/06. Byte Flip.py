import codecs
import binascii
import random

data = [i for i in input().split() if len(i) == 2]
data = list(reversed([i[::-1] for i in data ]))

for i in data:    
    print(bytes.fromhex(i).decode("ASCII"), end="")
