squad = input().split()
print(" ".join([squad[i] for i in range(len(squad)) if (i%3 == 0)]))
print(" ".join([squad[i] for i in range(len(squad)) if (i%3 == 1)]))
print(" ".join([squad[i] for i in range(len(squad)) if (i%3 == 2)]))
