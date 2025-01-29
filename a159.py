from sys import stdin, stdout
map_odd = {str(i): int(x) for i, x in enumerate('0246813579')}
li = [0] * 10000
for k in range(10000):
    s = f'{k:04}'
    li[k] = (map_odd[s[0]] + map_odd[s[2]] + int(s[1]) + int(s[3])) % 10
lines = stdin.read().splitlines()[1:]
results = []
for line in lines:
    nums = map(int, line.split())
    if sum(li[num] for num in nums) % 10 == 0:
        results.append("Valid\n")
    else:
        results.append("Invalid\n")
stdout.writelines(results)
