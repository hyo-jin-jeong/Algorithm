from collections import deque

def queue(n, k):
    queue = list(range(1, n+1))
    queue = deque(queue)
    count = 0
    while(len(queue) != 1):
        count += 1
        if count == k:
            queue.popleft()
            count = 0
        else:
            queue.append(queue[0])
            queue.popleft()
        
    return queue[0]
    
print(queue(8, 3))