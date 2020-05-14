'''
Implement a function which behaves like the uniq command in UNIX.

It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

Example:

['a','a','b','b','c','a','b','c'] --> ['a','b','c','a','b','c']
'''

def uniq(seq): 
    i = 0
    while i < len(seq)-1:
        if seq[i] == seq[i+1]:
            seq.pop(i+1)
        else:
            i += 1
    return seq

