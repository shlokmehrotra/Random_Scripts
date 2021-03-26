#taking x ^ y but... optimally?
def  power(x, y):
    rv = 1
    while y:
        if y & 1:
            rv *= x
        x = x * x
        y >> 1
    return rv
    