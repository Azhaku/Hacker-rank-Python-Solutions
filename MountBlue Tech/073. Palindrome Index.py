#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# edge case: s =>'abca' ,expected op => -1

def palindromeIndex(s):
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -=1
        # if its a last check, or middle values you can remove left one, else -1
        elif s[left + 1] == s[right] and (left + 1 == right or s[left + 2] == s[right - 1]):
            return left
        elif s[left] == s[right - 1]: # and (left == right - 1 or s[left + 1] == s[right - 2]):
            return right
        else:
            return -1
    return -1

            
            

q = 1

for q_itr in range(q):
    s = 'abca'

    result = palindromeIndex(s)
    print(result)
