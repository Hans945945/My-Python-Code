import heapq
import sys

primes = [2, 3, 5, 7]
humble = [1]
seen = set(humble)
heap = [1]

while len(humble) < 5842:
    now = heapq.heappop(heap)
    for p in primes:
        n = now * p
        if n not in seen:
            seen.add(n)
            heapq.heappush(heap, n)
    if now != humble[-1]:
        humble.append(now)
r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)
    ans = humble[n-1]
    temp = "th" if 10 <= (n % 100) <= 20 else "st" if n%10 == 1 else "nd" if n%10 == 2 else "rd" if n%10 == 3 else "th"
    r.append(f"The {n}{temp} humble number is {ans}.")
sys.stdout.write("\n".join(r)+"\n")


