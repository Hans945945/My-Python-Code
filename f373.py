n = int(input())
a = n- n//2000*200
b = n- n//1000*100
print(f"{b} 1" if b<a else f"{a} 0")
