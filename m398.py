import sys

a, b, c = map(int, sys.stdin.readline().split())
lines = sys.stdin.read().splitlines()
times = [
    sum(map(int, lines[0].split())) * 3 + (a - 1) * 2,
    sum(map(int, lines[1].split())) * 3 + (b - 1) * 2,
    sum(map(int, lines[2].split())) * 3 + (c - 1) * 2,
]

min_time = min(times)
min_counter = times.index(min_time) + 1

print(min_counter, min_time)
