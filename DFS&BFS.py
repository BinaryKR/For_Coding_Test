graph = { 1:[2,3,4],2:[5],3:[5],4:[],5:[6,7],6:[],7:[3]}
print(graph)

def DFS(vertax, visited=[]):        #### 인접 리스트 / 재귀
    visited.append(vertax)
    for i in graph[vertax]:
        if not i in visited:
            visited = DFS(i,visited)
    return visited

print(DFS(1))

def DFS_STACK(start):               #### 인접 리스트 / 스택
    visitied = []
    stack = [start]
    while stack:
        vertax = stack.pop()
        if vertax not in visitied:
            visitied.append(vertax)
            for i in graph[vertax]:
                stack.append(i)
    return visitied

print(DFS_STACK(1))

def BFS_QUEUE(start):               #### 인접 리스트 / 큐
    visitied = [start]
    queue = [start]
    while queue:
        vertax = queue.pop(0)
        for i in graph[vertax]:
            if i not in visitied:
                visitied.append(i)
                queue.append(i)
    return visitied

print(BFS_QUEUE(1))

#### BFS는 재귀로 구현 불가 -> ONLY QUEUE##