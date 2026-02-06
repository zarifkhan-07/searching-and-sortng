A = [1, 2, 3, 4, 5, 6]

start = 0
end = len(A) - 1

while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

print("Reversed array is")
print(A)
