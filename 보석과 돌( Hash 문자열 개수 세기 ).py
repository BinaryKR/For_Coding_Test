freqs = {}
count = 0
J = "aA"      ##보석
S = "aAAbbbb" ## 돌

for char in S:
    if char not in freqs:
        freqs[char] = 1
    else:
        freqs[char] += 1

for char in J:
    if char in freqs:
        count += freqs[char]


print(freqs)
print(count)

##########################
import collections
freqs = collections.defaultdict(int)
count = 0

for char in S:
    freqs[char] +=1

for char in J:
    count += freqs[char]
print(freqs)
print(count)

############################

print(sum(s in J for s in S))