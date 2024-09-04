def countingSort(arr):
    min = arr[0]
    max = arr[0]
    k = 0
    countLst = []
    for i in range(len(arr)):
        if (min>arr[i]): min=arr[i]
        if (max<arr[i]): max=arr[i]
    for i in range(min,max+1):
        countLst.append(0)
    print("max {} min {}".format(max,min))
    for i in range(len(arr)):
        countLst[(arr[i]-min)]+=1
    for i in range(len(countLst)):
        for j in range(countLst[i]):
            arr[k] = min+i
            k+=1
    print(arr)
    return arr
countingSort([1,3,1,1,2,4,3,2,9,5,8,1,3,5,4,-10])
