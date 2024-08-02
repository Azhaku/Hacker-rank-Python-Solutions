import math
def kaprekarNumbers(p,q):
    li = []
    for n in range(p,q+1):
        square = n**2
        length = len(str(n))
        left = square // (10 **length)
        right = square % (10 ** length)
        print(right, left)
        if right + left == n:
            li.append(n)
    return li

if __name__ == '__main__':
    p = 1

    q = 500

    print(kaprekarNumbers(p, q))