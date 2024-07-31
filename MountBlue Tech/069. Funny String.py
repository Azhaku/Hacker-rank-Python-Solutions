def funnyString(s):
    res = []
    for i in range(1, len(s)):
        res.append(abs(ord(s[i-1]) - ord(s[i])))
    if res == res[::-1]:
        return 'Funny'
    return 'Not Funny'

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)
