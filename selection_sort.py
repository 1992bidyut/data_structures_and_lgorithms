def selection_sort(a,n):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]
    return a

a=[5,9,1,88,32,6,9]

x= selection_sort(a,len(a))
print(x)