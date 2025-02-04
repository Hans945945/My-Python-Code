import sys
def process(a, b):
    if int(a) % (1<<int(b)) == 0:
        return f"YA!!終於算出{a}可被2的{b}次整除了!!"
    else:
        return f"可惡!!算了這麼久{a}竟然無法被2的{b}次整除"
data = sys.stdin.read().splitlines()
r = [process(a, b) for a, b in (s.split() for s in data)]
sys.stdout.write("\n".join(r) + "\n")
