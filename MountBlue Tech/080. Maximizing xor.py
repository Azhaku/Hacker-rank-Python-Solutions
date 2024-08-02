# def maximizingXor(l, r):
#     xor = l ^ r
#     print(bin(l), bin(r))
    
#     #method 1
#     pow = len(bin(xor)[2:])
#     print(2**pow -1)
    
#     #method2
#     maxXor = 1
#     while xor > 0:
        
#         maxXor <<= 1
#         xor >>= 1
#         print(xor,maxXor)
#     return maxXor - 1

def maximizingXor(l, r):
    # maximum = 0
    # for i in range(l, r+1):
    #     for j in range(i, r+1):
    #         maximum = max(maximum, i ^ j)
    # return maximum
    
    xor = len(bin(l ^ r)[2:])
    return 2** xor -1

# Example usage
l = 1
r = 10
result = maximizingXor(l, r)
print(f"Max XOR between {l} and {r}: {result}")
