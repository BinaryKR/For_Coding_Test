table = [2,3,6,7]
k = 7

result = []

def DFS(summ, idx, path):
    print(summ,idx,path)
    if summ <0:
        return
    if summ == 0:
        result.append(path)
        return
    for i in range(idx,len(table)):
        DFS(summ - table[i], i, path + [table[i]])


DFS(k,0,[])

print(result)