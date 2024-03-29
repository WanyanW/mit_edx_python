def oddTuples(aTup):
    odd = ()
    for i in range(0,len(aTup),2):
        odd = odd + (aTup[i],)
    print(odd)

oddTuples(('I', 'am', 'a', 'test', 'tuple'))


# answer1 from Edx
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

oddTuples(('I', 'am', 'a', 'test', 'tuple'))


# answer2 from Edx
def oddTuples2(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]