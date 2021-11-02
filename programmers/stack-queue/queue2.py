from collections import deque

# 내가 작성한 코드
def solution(priorities, location):
    count = 0
    priorities = deque(priorities)
    while True:
        value = priorities.popleft()
        location -= 1
        if len(priorities) == 0:
            default = value
        else:
            default = max(priorities)
        if default <= value:
            count += 1
            if location == -1:
                return count
        else:
            priorities.append(value)
            if location == -1:
                location = len(priorities) - 1

#다른분의 코드 
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

