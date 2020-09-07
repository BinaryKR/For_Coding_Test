import collections

nums = [1,1,1,2,2,3]
k = 2
answer = []
counter = collections.Counter(nums)
for i,value in counter.items():
    if value >= k:
        answer.append(i)

print(answer)


