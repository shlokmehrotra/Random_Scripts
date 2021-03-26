#multiplication using bitwise operation

def multiply(x, y):
    def add(x, y):
        return x if y == 0 else add(x ^ y, (x & y) << 1)
    rv = 0
    while x:
        if x & 1:
            rv = add(rv, y) 
        x, y = x >> 1, y << 1
    return rv
           