#!/usr/bin/env python3

# ----------------------------------
# projects/python/collatz/Collatz.py
# Copyright (C) 2017
# Glenn P. Downing
# ----------------------------------

from typing import IO, List

# ------------
# collatz_read
# ------------

def collatz_read (s: str) -> List[int] :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i: int, j: int) -> int :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert i > 0
    assert j > 0
    assert j >= i
    max = 0
    for num in range(i, j):
        cycle_length = get_cycle_length(num)
        if (cycle_length > max):
            max = cycle_length    
    return max

def get_cycle_length (i: int) -> int :
    count = 1
    while (i != 1):
        if (i % 2 == 1):
            i = (3 * i + 1) / 2
            count = count + 2
        else:
            i = i / 2
            count = count + 1
    return count
# -------------
# collatz_print
# -------------

def collatz_print (w: IO[str], i: int, j: int, v: int) -> None :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r: IO[str], w: IO[str]) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
