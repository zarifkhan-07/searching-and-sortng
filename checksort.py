arr = [3, 4, 5, 1, 2]
n = len(arr)
count = 0

for i in range(1, n):
    if(arr[i-1] > arr[i]):
        count += 1

if(arr[n-1] > arr[0]):
    count += 1

print(count <= 1)