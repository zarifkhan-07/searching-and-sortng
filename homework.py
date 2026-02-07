n=int(input("Enter the elements"))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Shell Sort algorithm
gap = n // 2
while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = temp
    gap //= 2

# printing sorted array
print("Sorted array:")
for num in arr:
    print(num, end=" ")
