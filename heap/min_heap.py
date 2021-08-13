import sys
import heapq as hq
sys.stdin = open("/Users/hyojinjeong/Algorithm/heap/heap.txt", "r")
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else: 
            print(hq.heappop(a))
    hq.heappush(a, n)