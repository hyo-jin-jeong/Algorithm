"""
I want to know how much rainwater can hold between buildings.
I am going to write a function trapping_rain that calculates it.

The function trapping_rain takes a list of buildings that store building height information as a parameter,
and returns the total amount of rainwater contained.
"""


def trapping_rain(buildings):
    amount = 0
    # 총 담기는 빗물의 양을 변수에 저장
    for i in range(1, len(buildings) - 1):
        left = max(buildings[:i])
        # 현재 건물보다 왼쪽에 있는 건물들 중 가장 높은 건물의 층 수 저장
        right = max(buildings[i:])
        # 현재 건물보다 오른쪽에 있는 건물들 중 가장 높은 건물의 층 수 저장

        result = min(right, left)
        # 선택된 두 건물 중 더 낮은 건물 층 수 저장
        if result > buildings[i]:
            # 저장 된 층 수 보다 현재 건물이 더 낮을 경우에만 물이 찰 수 있다.
            amount += result - buildings[i]
            # 저장된 층수에서 현재 건물의 층수를 뺀 나머지 부분을 물로 채운다. -> amount 변수에 나머지 층 수 값 저장

    return amount


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
