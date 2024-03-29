# Problem 4
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
#     '''
#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     '''
#     # Your code here

#For example,
# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0


def closest_power(base, num):
    if base > num:
        return 0
    else:
        exp_max = num//base
        exp_min = 0
        while abs(exp_max - exp_min) > 1:
            exponent = (exp_min + exp_max) // 2
            epliso = base ** exponent - num
            if epliso == 0:
                return exponent
            elif epliso > 0:
                exp_max = exponent
            else:
                exp_min = exponent
        else:
            if abs(base ** exp_max - num) < abs(base ** exp_max - num):
                value = exp_max
            elif abs(base ** exp_max - num) >= abs(base ** exp_max - num):
                value = exp_min
        return value

print(closest_power(3,19586032))

def closest_power(base, num):
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result

print(closest_power(3,19586032))