import sys
import heapq
sys.stdin = open('11279.txt','r')
input = sys.stdin.readline

# 최대힙 활용
#todo 배열에 자연수 x를 넣는다.
#todo 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 처음에 비어있는 배열에서 시작
#todo 입력에서 0이 주어진 회수만큼 답을 출력한다. 
# 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
            
        else:
            print(0)
            
    else:
        heapq.heappush(heap,-x)
        