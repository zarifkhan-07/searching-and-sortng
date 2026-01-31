def sortArray(a):
    if len(a) <= 1:
        return

    x = -1
    y = -1
    prev = a[0]

    for i in range(1, len(a)):
        if prev > a[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i

        prev = a[i]

    swap(a, x, y)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == '__main__':
    a = [3, 5, 6, 9, 8, 7]
    print("Original Array:", a)
    sortArray(a)
    print("Sorted Array:", a) 