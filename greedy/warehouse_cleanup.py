from os import spawnl
import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/greedy/warehouse_cleanup.txt", "r")
n = int(input())
box = list(map(int, input().split()))
m = int(input())
box.sort()
for i in range(m):
    box[0] += 1
    box[n-1] -= 1
    box.sort()
print(box[n-1] - box[0])
