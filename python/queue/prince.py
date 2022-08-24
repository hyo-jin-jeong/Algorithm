from collections import deque

def queue_fun(n, k):
    dq = list(range(1, n+1))
    dq = deque(dq)
    count = 0
    while(len(dq) != 1):
        count += 1
        if count == k:
            dq.popleft()
            count = 0
        else:
            dq.append(dq[0])
            dq.popleft()
        
    return dq[0]
    
print(queue_fun(8, 3))