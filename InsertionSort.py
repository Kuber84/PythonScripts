def insertSort(arr):
    for i in range(1,len(arr)):
        j = i
        temp = arr[i]
        while j > 0 and temp < arr[j-1] :
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=temp
count = int(input("Enter the count:"))
arr = []
for i in range(count):
    arr.append(int(input(f"Enter the number {i}:")))
print(arr)
insertSort(arr)
print(arr)