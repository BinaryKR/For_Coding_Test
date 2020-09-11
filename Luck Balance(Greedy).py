def luckBalance(k, contests):
    dic = {1:[],0:[]}
    for L,T in contests:
        if T == 1:
            dic[1].append(L)
        else:
            dic[0].append(L)
    n = len(dic[1]) - k
    if n<0:
        n=0
    dic[1].sort()
    dic[0].sort()
    summ = sum(dic[1][n:])+sum(dic[0]) - sum(dic[1][:n])
    print(summ)
    return summ