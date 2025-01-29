n = int(input())
a,b = map(int, input().split())
if n % 2 ==1:
    print("能")
    print(pow(a, n)+pow(b,n))
else:
    print("不能")
