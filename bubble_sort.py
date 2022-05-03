def bubble_sort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a = [5,98,54,75,2,35,7,]
print(bubble_sort(a,len(a)))