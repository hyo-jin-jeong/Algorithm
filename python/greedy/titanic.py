import sys
from collections import deque
sys.stdin = open("/Users/hyojinjeong/Algorithm/greedy/titanic.txt", "r")
n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
cnt = 0
weight = deque(weight)
while weight:
    cnt += 1
    if len(weight) == 1:
        break
    else:
        weight.popleft()
    weight.pop()
print(cnt)