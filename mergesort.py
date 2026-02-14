def mergeSorting(A):
    if len(A) > 1:

        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        mergeSorting(left)
        mergeSorting(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
