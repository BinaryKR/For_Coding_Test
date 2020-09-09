table = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]

def DFS(i,j):
    if i<0 or i>= len(table) or j<0 or j>=len(table[0]) or table[i][j] != 1:
        return
    table[i][j] = 0

    DFS(i+1,j)
    DFS(i-1, j)
    DFS(i, j+1)
    DFS(i, j-1)

cnt = 0
for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 1:
            DFS(i,j)

            cnt += 1

print(cnt)
