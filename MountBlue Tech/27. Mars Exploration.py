def marsExploration(s):
    res = 0 
    msg = "SOS"
    count = 0
    while count<len(s):
        if s[count] != msg[count%3]:
            res += 1
        count += 1
    return res

s = 'SSSSOPSSP'
print(marsExploration(s))