from collections import defaultdict

adj_list = defaultdict()
adj_list['a'] = ['d']
adj_list['b'] = ['d']
adj_list['c'] = ['e']
adj_list['d'] = ['e']
adj_list['e'] = []
print(adj_list)
visited = defaultdict()
visited['a'] = False
visited['b'] = False
visited['c'] = False
visited['d'] = False
visited['e'] = False
print(visited)
output = []

def topology_sort(v):
    if not visited[v]:
        visited[v] = True
        for n in adj_list[v]:
            topology_sort(n)
        output.insert(0,v)
for v in visited:
    print(v)
    topology_sort(v)

print(output)