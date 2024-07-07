ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pairs = 0
fre_dic = {}
for i in ar:
    # print(i)

    if i in fre_dic:
        if fre_dic[i] == 1:
            pairs += 1
            fre_dic[i] =0

        else:
            fre_dic[i] = 1
    else:
        fre_dic[i] = 1
    # print(fre_dic[i])
print(fre_dic)
print(pairs)