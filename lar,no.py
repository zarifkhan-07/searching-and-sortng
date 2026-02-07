A1 = [1, 2, 4, 5, 6, 8, 10]
A2 = [2, 3, 5, 7, 10, 15]

m = len(A1)
n = len(A2)

i, j = 0, 0
while i < m and j < n:
    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        print(A2[j], end=" ")
        j += 1
        i += 1
