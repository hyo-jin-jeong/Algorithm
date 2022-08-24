from collections import deque
import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/queue/education.txt", "r")
need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)

    for x in plan:
        if x in dq and x!= dq.popleft():
            print("No", x)
            break
    else:
        if len(dq) == 0:
            print("Yes")
        else:
            print("No")
        
        

