import sys
from collections import deque

sys.stdin = open("/Users/hyojinjeong/Algorithm/queue/emergency.txt", "r")
n, m= map(int, input().split(","))
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split(","))))]
Q = deque(Q)
cnt = 0 

while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
        cnt += 1
    else:
        cnt += 1
        if cur[0] == m:
            break
        
print(cnt)