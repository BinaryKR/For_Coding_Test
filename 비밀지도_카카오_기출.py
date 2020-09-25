def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        if len(arr1[i]) < n or len(arr2[i]) < n:
            while (len(arr1[i]) < n):
                arr1[i] = '0' + arr1[i]
            while (len(arr2[i]) < n):
                arr2[i] = '0' + arr2[i]
        stri = ""
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                stri = stri + " "
            else:
                stri = stri + '#'
        answer.append(stri)

    print(answer)

    return answer