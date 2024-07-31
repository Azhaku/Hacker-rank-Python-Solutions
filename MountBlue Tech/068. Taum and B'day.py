def taumBday(b, w, bc, wc, z):
    res = 0
    res += min(b*bc,(wc+z)*b)
    res += min(w*wc,(bc+z)*w)
    return res


t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    b = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    bc = int(second_multiple_input[0])

    wc = int(second_multiple_input[1])

    z = int(second_multiple_input[2])

    print(taumBday(b, w, bc, wc, z))
