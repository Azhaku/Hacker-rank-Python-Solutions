
#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    uniarr = set(arr[0])
    
    res = uniarr
    
    for i in range(1, len(arr)):
        res = res.intersection(arr[i])
    return len(res)
    
    


n = int(input().strip())

arr = []

for _ in range(n):
    arr_item = input()
    arr.append(arr_item)

print(gemstones(arr))
