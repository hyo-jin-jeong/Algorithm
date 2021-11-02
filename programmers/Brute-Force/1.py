# 처음 생각했던 방식 solution1 
# 1. 정답으로 들어온 값을 for문 둘려서 하나씩 비교한다. 
# 2. 정답이 맞으면 sum += 1 
# 3. result라는 dic을 만들어서 max값이 나온 수포자 번호와 sum 값을 저장한다.
# 4. return 값인 answer에 sorted된 값을 넣어 return한다. 

# 결과
# 테스트 5,6,7,9~13 실패 
# 원인: answers을 기준으로 pattern을 돌렸을 때 맞는지 확인을 해야했는데 내가 한 방법은 
# pattern을 기준으로 answers가 맞는 경우를 생각하여 pattern이 answers보다 길다고 착각했다. 
# 문제이해를 잘못한것이 문제!!
def solution1(answers):
    answer = []
    pattern = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], 
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = {}
    
    for i in range(len(pattern)):
        sum = 0
        for j in range(len(answers)):
            if len(pattern[i]) - 1 < j:
                break 
            if pattern[i][j] == answers[j]:
                sum += 1 
        if len(result) == 0 or max(result.values()) < sum:
            result = {i+1: sum}
        elif len(result) != 0 and max(result.values()) == sum:
            result[i+1] = sum
    
    answer = sorted(result.keys())
    return answer

# 답을 참고
# answers을 기준으로 pattern을 비교하여 푸는 방식으로 변경
def solution2(answers):
    result = []
    pattern = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5], 
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    sums = [0, 0 ,0]
    for idx, answer in enumerate(answers):
        if answer == pattern[0][idx%len(pattern[0])]:
            sums[0] += 1
        if answer == pattern[1][idx%len(pattern[1])]:
            sums[1] += 1
        if answer == pattern[2][idx%len(pattern[2])]:
            sums[2] += 1 
            
    for idx, sum in enumerate(sums):
        if max(sums) == sum:
            result.append(idx + 1)
    return result     

print(solution1([0,0,0,0,0,0,0,0,0,0,1]))
print(solution2([1,3,2,4,2]))