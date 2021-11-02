from collections import deque
from typing import Deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    truck_on_bridge = Deque()
    truck_location = Deque()
    count = 0 
    total_weight = 0
    while len(truck_weights) > 0 or len(truck_on_bridge) > 0:
        count += 1
        if len(truck_location) > 0 and truck_location[0] == bridge_length:
            truck_weight = truck_on_bridge.popleft()
            truck_location.popleft()
            total_weight -= truck_weight
        if len(truck_weights) > 0 and total_weight + truck_weights[0] <= weight: 
            truck_weight = truck_weights.popleft()
            truck_on_bridge.append(truck_weight)
            total_weight += truck_weight
            truck_location.append(0)
            
        for i in range(len(truck_location)):
            truck_location[i] += 1
    return count 

print(solution(2, 10, [7,4,5,6]))