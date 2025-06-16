w,h = map(int, input().split())
paper = []
for _ in range(h):
    temp = input().split()
    paper.append(' '.join(temp+temp[::-1]))
print("\n".join(paper + paper[::-1]))
