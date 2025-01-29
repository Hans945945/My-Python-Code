def change_array(w,a1,a2):
    if w ==1:
        arr = a1
    else:
        arr = a2
    if arr[0] % 3 == 0:
        r = max(arr)
        print(r)
        for i in range(5):
            if arr[i] == r:
                arr[i] = int(arr[i]/2)
    else:
        r = min(arr)
        smallest = 1001
        if r == 0:
            for i in range(5):
                if arr[i] < smallest and arr[i]!= 0:
                    smallest = arr[i]
                r = smallest
        print(r)
        for i in range(5):
            if arr[i] == r:
                arr[i] -= 1
    if w ==1:
        a1 = arr
    else:
        a2 = arr
    return r , a1, a2
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
which = 1
result = -1
while result != 0:
    result, a1,a2 = change_array(which,a1,a2)
    if result % 2 == 0:
        which = 2
    else:
        which = 1

