import sys
from itertools import groupby
data = sys.stdin.read().split()
spell = data[1].strip()
new = "".join(f"{len(list(v))}{k}" for k,v in groupby(spell))
sys.stdout.write(spell+"\n" if len(spell) <= len(new) else new+"\n")
