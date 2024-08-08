N, K = input().split()
N = int(N)
K = int(K)

C = sorted([int(i) for i in input().strip().split()],reverse=True)

result = 0
p = 1

for num,i in enumerate(C,start=1):
    result+=p*i
    if num%K==0: p+=1
print(result)