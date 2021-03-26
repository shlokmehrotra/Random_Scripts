def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
        print(result)
    print("----------------")
    return result

print(parity(15))