def solution(dartResult):
    result = []
    k = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if (dartResult[i] == '0' and dartResult[i - 1] == '1'):
                continue
            result.append(dartResult[k:i])
            k = i
    result.append(dartResult[k:])
    result.pop(0)
    summ = []
    for i in result:
        if len(i) == 2:
            if i[1] == 'S':
                summ.append(int(i[0]))
            elif i[1] == 'D':
                summ.append(int(i[0]) ** 2)
            elif i[1] == 'T':
                summ.append(int(i[0]) ** 3)
        else:
            if i[1] == '0':
                if i[2] == 'S':
                    summ.append(10)
                elif i[2] == 'D':
                    summ.append(10 ** 2)
                elif i[2] == 'T':
                    summ.append(10 ** 3)
            else:
                if i[1] == 'S':
                    summ.append(int(i[0]))
                elif i[1] == 'D':
                    summ.append(int(i[0]) ** 2)
                elif i[1] == 'T':
                    summ.append(int(i[0]) ** 3)
                if (i[2] == '*'):
                    if len(summ) > 1:
                        summ[-2] = summ[-2] * 2
                    summ[-1] = summ[-1] * 2
                if (i[2] == '#'):
                    summ[-1] = -summ[-1]

    return sum(summ)