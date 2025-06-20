'''
while 1:
    try:
        print(sum(map(int, input().split())))
    except EOFError:
        break
'''
import sys
for s in sys.stdin:
    print(sum(map(int, s.split())))
