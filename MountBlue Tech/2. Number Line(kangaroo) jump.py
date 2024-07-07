x1,v1,x2,v2 = 0,3,4,2

# x1,x2 starting pos of kangaro
# v1,v2 is steps of kangaro

if v1>v2:
    if (x2-x1) % (v2-v1) == 0:
        return 'YES'
return 'NO'