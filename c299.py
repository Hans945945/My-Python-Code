data = list(map(int, input().split()[1:]))
smallest = min(data)
largest = max(data)
print(smallest, largest, "yes" if sum(data) == (largest - smallest + 1)*(smallest + largest)//2 else "no")
