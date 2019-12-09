"""
Exercise 3:
Write a recursive Python function, given a non-negative integer N,
to calculate the no. of occurrences of digit 7 in N.
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.
"""

def count7(N):
    residue = N % 10
    if N == 0:
        count = 0
    elif residue == 7:
        count = count7(N//10) + 1
    else:
        count = count7(N//10)
    return count

