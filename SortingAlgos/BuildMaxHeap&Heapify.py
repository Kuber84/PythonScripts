def buildheap(arr):
    # arr = [-1] + [int(x) for x in input("Enter list separated by space:").split()]
    arr.insert(0, -1)
    i = len(arr) - 1
    while i > 1:
        parent = i // 2
        if arr[parent] < arr[i]:
            arr[i], arr[parent] = arr[parent], arr[i]
        arr = heapify(arr, i)
        i -= 1
    printheap(arr)
    return arr


def heapify(arr, i):
    child1 = i * 2
    child2 = i * 2 + 1
    noc = 2
    if (child1 >= len(arr)):
        return arr
    if (child2 >= len(arr)):
        noc = 1
    # print("index i {} children {} {}".format(arr[i],arr[child1],arr[child2]))
    if noc == 1:
        if arr[i] >= arr[child1]:
            return arr
    elif noc == 2:
        if arr[i] >= arr[child1] and arr[i] >= arr[child2]:
            return arr
    if noc == 2:
        if arr[child1] >= arr[child2]:
            arr[i], arr[child1] = arr[child1], arr[i]
            arr = heapify(arr, child1)
        else:
            arr[i], arr[child2] = arr[child2], arr[i]
            arr = heapify(arr, child2)
    else:
        arr[i], arr[child1] = arr[child1], arr[i]
        arr = heapify(arr, child1)
    return arr


def extractMax(arr):
    result = arr[1]
    arr[1] = arr[len(arr) - 1]
    arr.pop()
    heapify(arr, 1)
    # printheap(arr)
    return result


def heapsort(arr):
    buildheap(arr)
    res = [extractMax(arr) for i in reversed(range(1, len(arr)))]
    return res[::-1]

def printheap(arr):
    i = 1
    n = 1
    list = ""
    while i < len(arr):
        if i < 2 ** n:
            list += str(arr[i]) + " "
        else:
            n += 1
            print(list)
            list = str(arr[i]) + " "
        i += 1
    print(list)

arr = [6, 4, 3, 8, 1, 5, 2, 7, -1000, 205, 15, 17, 16, 19, 21, 18, -306, 152]
res = heapsort(arr)
print(res)