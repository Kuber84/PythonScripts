#creates 2 aux lists
def mergesort(arr):
    count=len(arr)
    if count<=1:
        return arr
    mid=len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    mergesort(arr1)
    mergesort(arr2)
    i=j=k=0
    while i<len(arr1) or j<len(arr2):
        if i == len(arr1):
            arr[k]=arr2[j]
            j+=1
        elif j == len(arr2):
            arr[k]= arr1[i]
            i+=1
        elif arr1[i]<=arr2[j]:
            arr[k]=arr1[i]
            i+=1
        elif arr1[i]>arr2[j]:
            arr[k]=arr2[j]
            j+=1
        k+=1
    return arr
print([6,4,3,8,1,5,2,7,100,-102,1023,100,5,7])
print(mergesort([6,4,3,8,1,5,2,7,100,-102,1023,100,5,7]))

#creates only 1 aux list for saving result, passes original array wid indices
def mergesort2(arr):
    print(arr)
    count=len(arr)
    if count<=1:
        return arr
    merge(arr,0,count)
    return arr
def merge(arr,start,end):
    length = end-start
    if end == start:
        return arr
    if length < 2 :
        return arr
    mid = (length//2) + start
    arr=merge(arr,start,mid)
    arr=merge(arr,mid,end)
    i=start
    j=mid
    k=0
    res=[]
    while i<mid or j<end:
        if i == mid:
            res.append(arr[j])
            j+=1
        elif j == end:
            res.append(arr[i])
            i+=1
        elif arr[i]<=arr[j]:
            res.append(arr[i])
            i+=1
        elif arr[i]>arr[j]:
            res.append(arr[j])
            j+=1
        k+=1
    i=start
    for k in range(len(res)):
        arr[i]=res[k]
        i+=1
    return arr
print(mergesort2([6,4,3,8,1,5,2,7,-9,-5,-105,134,-1023,1023]))
