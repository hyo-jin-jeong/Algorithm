#최소힙에서 최대값을 삭제 해야하는 방법을 모르겠어서 max값의 index를 찾아서 지워주고
# heapq의 heapfy함수를 통해 queue를 다시 heap 구조로 만들어주었다.
import heapq
def solution(operations):
    answer = []
    queue = []
    for s in operations:
        if "I" in s:
            heapq.heappush(queue, int(s.split(" ")[1]))
        if len(queue) > 0:
            if "D 1" == s:
                index = queue.index(max(queue))
                del queue[index]
                heapq.heapify(queue)
            elif "D -1" == s:
                heapq.heappop(queue)
    if len(queue) > 0:
        answer.append(max(queue))
        answer.append(min(queue))
    else: 
        answer = [0, 0]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))