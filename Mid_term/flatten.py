"""
Exercise 6:

Write a function to flatten a list. The list contains other lists, strings,
or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened
into [1,'a','cat',2,3,'dog',4,5] (order matters).
"""

def flatten(aList):
    newlist = []
    for i in aList:
        if type(i) == list:
           newlist = newlist + flatten(i)
        else:
            newlist.append(i)
    return newlist

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5] ))
print(flatten([1, [2, 3]]))
print(flatten([]))

# code 2
def flatten(aList):
    '''
    aList: a list
    Returns: a copy of aList, which is a flattened version of aList
    '''

    if aList == []:
        return []
    else:
        for elem in aList:
            if type(elem) == list:
                aList.remove(elem)
                return flatten(elem) + flatten(aList)
            else:
                aList.remove(elem)
                return [elem] + flatten(aList)
