
def binary_search(a,n,x):
        left=0
        right=n-1
        while left<=right:
                mid =(left+right)//2
                
                
                if a[mid]==x:
                        return mid
                elif a[mid]<x:
                        left=mid+1
                else:
                    right=mid-1
                    print(mid)
                    
        return -1

a=[25,35,45,55,65,75,85,95]
# print (len(a))
input=input("Enter the number to be searched: ")
index=binary_search(a,len(a),int(input))
print(index)
print(a[index])