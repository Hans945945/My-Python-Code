import sys
from collections import deque
stack = deque()
data = sys.stdin.read().splitlines()
results = []
for command in data[1:]:
    if command.startswith("Sleep"):
        stack.append(command[6:])
    elif command.startswith("Kick") and stack:
        stack.pop()
    elif command.startswith("Test"):
        results.append(stack[-1] if stack else "Not in a dream")
sys.stdout.write("\n".join(results) + "\n")
