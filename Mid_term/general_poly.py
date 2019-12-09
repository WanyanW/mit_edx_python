"""
Exercise 7:

L, a list of numbers (n0, n1, n2, ... nk)
Returns a function, which when applied to a value x, returns the value
n0 * x^k + n1 * x^(k-1) + ... nk * x^0
If L = [1, 2, 3, 4]
Invoking function with list L and value of x = 10 -
general_poly(L)(10)
result should be 1234
i.e. 1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0
"""

def general_poly(L):
    def newFunc(x):
        value = 0
        for i in range(len(L)):
            value = value + L[i] * (x**(len(L) - 1 - i))
        return value
    return newFunc

L = [1,2,3,4]
print(general_poly(L)(10))