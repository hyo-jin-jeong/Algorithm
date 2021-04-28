
"""
Compare the distance between each coordinate and find the two coordinates with the closest distance.
"""

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    dis = -1
    x1, x2, y1, y2 = 0, 0, 0, 0
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            result = distance(coordinates[i], coordinates[j])
            if dis == -1 or result < dis:
                dis = result
                x1, x2, y1, y2 = coordinates[i][0], coordinates[j][0], coordinates[i][1], coordinates[j][1]
    return [(x1, y1), (x2, y2)]


test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
