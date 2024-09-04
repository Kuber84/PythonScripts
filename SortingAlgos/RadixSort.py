def countingSort(arr,x):
    k = 0
    countLst = [0,0,0,0,0,0,0,0,0,0]
    digitDir = {
    for i in range(len(arr)):
        (arr[i]%(10**x))/(10**(x-1))
    for i in range(len(countLst)):
        for j in range(countLst[i]):
            arr[k] = min+i
            k+=1
    print(arr)
    return arr
def RadixSort(arr):
    max = max(arr)
    noofPasses = 0
    while max > 0:
        noofPasses+=1
        max=max//10
    for i in range(noofPasses):
        arr = countingSort(arr,i+1)