def saveThePrisoner(n, m, s):
    sweet_per = m%n
    res = s+sweet_per
    if (res-1) % n == 0:
        return n
    return (res-1) % n 


print(saveThePrisoner(5,1,1))
print(saveThePrisoner(5,2,2))
print(saveThePrisoner(5,2,4))
print(saveThePrisoner(5,2,5))
print(saveThePrisoner(5,9,1))