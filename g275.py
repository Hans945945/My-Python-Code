N = int(input())
for _ in range(N):
    list1 = list(input().split())
    list2 = list(input().split())
    r = ""
    if not(list1[1] != list1[3] and list1[1] == list1[5] and list2[1] != list2[3] and list2[1] == list2[5]):
        r = r+"A"
    if not(list1[-1] == "1" and list2[-1] == "0"):
        r = r+"B"
    for i in range(1,len(list1),2):
        if list1[i] == list2[i]:
            r = r+"C"
            break
    if r == "":
        r = "None"
    print(r)
