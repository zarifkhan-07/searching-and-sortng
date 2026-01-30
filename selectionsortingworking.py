a=[64,25,12,22,11]
for i in range (len(a)):
    min_id=i
    for j in range(i+1,len(a)):
        if a[min_id]>a[j]:
            min_id=j
    
    a[min_id],a[j]=a[min_id],a[j]

print("Sorted array")
for i in range(len(a)):
    print("%d" %a[i],end="")