# micropython-random-module
This module implements pseudo-random number generators for Micropython. For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element.

## Functions for integers

    random.randint(Nmin, Nmax)

Return a random integer N such that Nmin <= N <= Nmax.
    
## Functions for sequences (list)

    random.choice(mylist)

Return a random element from the non-empty sequence.
