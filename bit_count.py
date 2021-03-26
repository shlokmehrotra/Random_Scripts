def bitcount(x):
    bits = 0
    while(x):
        bits += x & 1 #checks if last digit if bitmap "overlaps" with 1
        x >>= 1
    return(bits)
print(bitcount(2)) #10
print(bitcount(8)) #1000
print(bitcount(7)) #111