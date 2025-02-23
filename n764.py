import sys
data = sys.stdin.readlines()
idx = 0
Dict = {}
for s in data:
    if s.strip() == "":
        break
    e, b = s.split()
    Dict[b] = e
    idx += 1
sys.stdout.write("\n".join(Dict.get(s.strip(),"eh") for s in data[idx+1:])+"\n")
    

    
