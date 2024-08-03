n = int(input())
arr = list(map(int, input().split()))

li = [0]*100
for i in arr:
    li[i] += 1
print(" ".join(map(str, li)))