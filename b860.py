c,w = map(int, input().split())
print(0 if w == 0 or c+w < 12 else (c+w-2)//11)
