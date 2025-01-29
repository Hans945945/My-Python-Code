queue = []
Max = 10
def enqueue(data):
    queue.append(data)
def dequeue():
    data = queue.pop(0)
    return data
def isFull():
    if len(queue) >= Max:
        return True
    else:
        return False
def empty():
    if len(queue) == 0:
        return True
    else:
        return False
def front():
    return queue[0]
def rear():
    return queue[len(queue)-1]

for i in range(int(input())):
    a = input().split()
    k = a[0]
    if k == "1":
        enqueue(a[1])
    elif k == "2":
        if empty():
            print(-1)
        else:
            print(front())
    elif k == "3":
        if not empty():
            dequeue()
