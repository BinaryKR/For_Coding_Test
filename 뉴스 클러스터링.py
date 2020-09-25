import re
from collections import Counter
p = re.compile("[A-Z]{2}")
def Lee(str):
    tmp = []
    for i in range(len(str)-1):
        if p.match(str[i:i+2]):
            tmp.append(str[i:i+2])
    return tmp
def solution(str1, str2):
    str1 = Lee(str1.upper())
    str2 = Lee(str2.upper())
    if (len(str1) == 0 and len(str2) == 0):
        return 65536
    p1 = Counter(str1)
    p2 = Counter(str2)
    qq = list((p1 & p2).elements())
    sumlen = len(str1) + len(str2) - len(qq)
    return int(len(qq)/sumlen *65536)