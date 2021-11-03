def solution(array, commands):
    answer = []
    for value in commands:
        result = sorted(array[value[0] - 1:value[1]])
        answer.append(result[value[2] - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


