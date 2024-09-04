def selsort(arr):
    for i in range(len(arr)):
        minIn = i
        for j in range(i+1,len(arr)):
            if arr[minIn] > arr [j]:
                minIn = j
        arr[i], arr[minIn] = arr[minIn], arr[i]
arr = [int(x) for x in input("Enter list separated by space:").split()]
selsort(arr)
print(arr)