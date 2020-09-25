import heapq
def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i] = -works[i]
    heapq.heapify(works)
    for k in range(n):
        works[0] += 1
        a = heapq.heappop(works)
        heapq.heappush(works,a)
    for j in works:
        if j <0:
            answer = answer + j*j
    return answer
print(solution(n=4,works=[4,3,3]))