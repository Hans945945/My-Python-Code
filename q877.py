from collections import defaultdict

parent = {}
siblings = defaultdict(list)

for _ in range(int(input())):
    line = input()
    if "之父曰" in line:
        child, father = line.split("之父曰")
        parent[child] = father
    elif "之子曰" in line:
        father, child = line.split("之子曰")
        parent[child] = father
    else:
        eldest, *others = line.split("，次曰")
        eldest_name = eldest[:eldest.index("弟")]
        father = parent.get(eldest_name)
        siblings_list = [eldest_name] + others
        siblings[father] = siblings_list
        for name in siblings_list:
            parent[name] = father

def get_depth(p, depth=0):
    if p not in parent:
        return depth
    return get_depth(parent[p], depth + 1)

a, b = input().split()
depth_a = get_depth(a)
depth_b = get_depth(b)

if depth_a < depth_b:
    print(a)
elif depth_b < depth_a:
    print(b)
else:
    pa = parent.get(a)
    pb = parent.get(b)
    if pa == pb:
        print(min(a, b, key=lambda name: siblings[pa].index(name)))
    else:
        grandpa_a = parent.get(pa)
        grandpa_b = parent.get(pb)
        print(min(a, b, key=lambda name: siblings[grandpa_a].index(parent[name])))

        
