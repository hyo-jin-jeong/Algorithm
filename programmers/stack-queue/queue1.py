# 내 접근법 
# 1. progresses, speeds를 deque로 만든다.
# 2. progresses를 한 번씩 돌면서 speeds의 해당 인덱스 값을 더한다. -> 값이 더해지는 한 턴에 모든 값들이 +를 해야한다고 생각함.
# 3. 인덱스 0번 값이 100 이상인지 체크한다. 
# 3. 100 이상인 경우 popleft 하고, count 한다. 
# 4. 100 미만이면 다시 2번 과정으로 돌아가서 progresses의 length가 0이 될 때까지 반복한다.
from collections import deque 

def solution(progresses, speeds): 
    answer = [] 
    progresses = deque(progresses) 
    speeds = deque(speeds) 
    count = 0
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses) > 0:
            if progresses[0] < 100:
                break
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count > 0:
            answer.append(count)
            count = 0 
        
    return answer


# 다른분들이 푼 접근법
# progresses에 speeds를 더해가는 방식이 아닌 100 - progresses 값을 speeds로 나눈 값을 비교해서 품
def solution1(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print(Q)
        if len(Q)==0 or Q[-1][0]<((100-p)//s):
            Q.append([((100-p)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution1([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 문제 푸는데 걸린 시간 40분
# => 문제를 풀때 하나하나의 조건을 다 표현하려 하기보단 역으로 생각하여 시간복잡도를 줄여나가야겠다. 