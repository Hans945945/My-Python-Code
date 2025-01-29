def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return m_data(left, right)
def m_data(left, right):
    r = []

    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            r.append(left[l_index])
            l_index += 1
        else:
            r.append(right[r_index])
            r_index += 1
    r += left[l_index:]
    r += right[r_index:]

    return r

N = int(input())
arr = list(map(int, input().split()))
arr = merge_sort(arr)
for i in range(N):
    print(arr[i], end = " ")
                
