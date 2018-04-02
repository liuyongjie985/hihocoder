# 6 2
# 1 2 3 5 7 9
# 2 6
# 1 4

def fromMidToSide(i,nums):
    


N, M = (int(x) for x in raw_input().strip().split(' '))

nums = []

for x in xrange(N):
    temp = int(raw_input().strip())
    nums.append(temp)

for x in xrange(M):
    start, end = (int(x) for x in raw_input().strip().split(' '))


