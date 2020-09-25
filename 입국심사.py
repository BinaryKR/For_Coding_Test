def solution(n, times):
    times.sort()
    l = 1
    r = times[-1]*n
    answer = r
    print(l,r)
    while(l<=r):
        mid = int((l+r)/2)
        sum = 0
        for i in range(len(times)):
            sum += int(mid/times[i])
        if(sum >= n):
            if(answer > mid):
                answer = mid;
            r = mid-1
        else:
            l = mid +1

    return answer

n =6
times=[7,10]
print(solution(n,times))

