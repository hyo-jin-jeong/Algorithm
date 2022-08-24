import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/greedy/wrestler.txt", "r")
n = int(input())
player = []
for i in range(n):
    t, w = map(int, input().split())
    player.append((t, w))
player.sort(reverse=True)
largest = 0
cnt = 0
for t, w in player:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)
