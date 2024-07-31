
def twoStrings(s1, s2):
    s1 = set(s1)
    s1 = set(s1)
    return 'YES' if s1.intersection(s2) else 'NO'

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
        print(result)

"""
2
hello
world
hi
world
"""