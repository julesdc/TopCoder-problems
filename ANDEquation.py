__author__ = 'Jules'


list = [191411,256951,191411,191411,191411,256951,195507,191411,192435,191411,
 191411,195511,191419,191411,256947,191415,191475,195579,191415,191411,
 191483,191411,191419,191475,256947,191411,191411,191411,191419,256947,
 191411,191411,191411]


def restoreY(A):
    top = A[len(A) - 1] & A[0]
    for x in range(0, len(A)):
        if x != 0 & x != (len(A) - 1):
            top = A[len(A) - 1] & A[0]
        elif 0 == x:
            if 1 == len(A) - 1:
                return -1
            else:
                top = A[1] & A[len(A) - 1]
        elif (len(A) - 1) == x:
            if 1 == len(A) - 1:
                return -1
            top = A[0] & A[len(A) - 2]
        for i in range(x + 1, len(A) - 1):
            top = top & (A[i] & A[i + 1])
        for j in range(0, x):
            top = top & (A[j] & A[j + 1])
        if top == A[x]:
            return A[x]
    return -1


print(restoreY(list))

