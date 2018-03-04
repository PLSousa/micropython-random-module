"""
usage:
>>> from random import randint
>>> randint(1,100)
16
>>> from random import choice
>>> mylist = ['Paris','London','Roma','Rio']
>>> choice(mylist)
'Roma'
"""

# Pseudo-random number generator module

def _bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def _rescale(Nmin, Nmax, OldValue):
    NewRange = Nmax - Nmin  
    NewValue = OldValue * NewRange / 255 + Nmin
    return NewValue

# Return a random integer N such that Nmin <= N <= Nmax.
def randint(Nmin, Nmax):
    from uos import urandom
    Oldint = _bytes_to_int(urandom(1))
    N = round(_rescale(Nmin-0.5, Nmax+0.5, Oldint))
    return N

# Return a random element from a list.
def choice(mylist):
    index = randint(0,len(mylist)-1)
    return mylist[index]
