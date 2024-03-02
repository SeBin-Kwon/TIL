from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    sum_weight = 0
    while truck:
        time += 1
        sum_weight -= bridge.popleft()
        
        if sum_weight + truck[0] <= weight:
            sum_weight += truck[0]
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
    time += bridge_length    

    return time
b = 100
w = 100
t = [10]
b1 = 2
w1 = 10
t1 = [7,4,5,6]
print(solution(b, w, t))