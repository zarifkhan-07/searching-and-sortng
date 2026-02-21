def rotations(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):
    temp=a[0]
    for i in range(a_size-1):
        a[i]=a[i+1]
    a[a_size-1]=temp
def printArray(a,a_size):
    for i in range(a,a_size):
        print("% d" % a[i], end="")
    print("\n")
a=[21,3,56,7,88,12,67,5432]
print(a,len(a))
rotations(a,2,len(a))
printArray(a,len(a))