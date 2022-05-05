def insertion_sort(a,n):
    for i in range(1,n):
        item = a[i]
        j=i-1
        # while j>=0 and a[j]<item: # assending
        while j>=0 and a[j]>item:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=item
    return a

a=[5,8,1,99,25]
print(insertion_sort(a,len(a)))