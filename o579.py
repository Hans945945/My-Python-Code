t = int(input())
options = [t*3]
options.append(299+(t>300)*3*(t-300))
options.append(699+(t>750)*3*(t-750))
print(min(options))

