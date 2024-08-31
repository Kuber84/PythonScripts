def heapsortInplace(arr):
    arr.insert(0, -1)
    heapfix(arr, len(arr) - 1)
    arr.pop(0)
    return arr

def heapfix(arr, i):
    if i <= 1:
        return
    j = i
    while i > 1:
        parent = i // 2
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
        i -= 1
    arr[1], arr[j] = arr[j], arr[1]
    heapfix(arr, j - 1)

arr = [6, 4, 3, 8, 1, 5, 2, 7, -1000, 205, 15, 17, 16, 19, 21, 18, -306, 152]
res = heapsortInplace(arr)
print(res)