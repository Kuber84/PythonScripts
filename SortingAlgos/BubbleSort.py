def bubblesort(arr):
    for i in range(len(arr)):
        j = len(arr)-1
        while j>i:
            if (arr[j]<arr[j-1]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j=j-1
arr = [int(x) for x in input("Enter list separated by space:").split()]
print(arr)
bubblesort(arr)
print(arr)