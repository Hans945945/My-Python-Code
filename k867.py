import sys
people = sys.stdin.readline().strip().split()
nums = list(map(int, sys.stdin.readline().strip().split()))
data = {num: person for person, num in zip(people, nums)}
sys.stdout.write(" ".join(data[i] for i in range(1, len(people) + 1)) + "\n")
