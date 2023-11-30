import sys
import heapq

input = sys.stdin.readline

heap_arr = []
N = int(input())
# 우선순위를 -x로 지정하면 최대힙 구현이 가능
# 힙 : 요소를 꺼낼때 가장 작은 값부터 뽑아옴 
for i in range(N):
    num = int(input())
    if num == 0:
        if heap_arr:
        # 가장 큰값부터 뽑아오게 하기 위해 요소에 -를 붙여서 
        # 가장 큰값을 가장 작은 값으로 변환하여 힙에 넣는다.
            print(-heapq.heappop(heap_arr))
        else:
            print(0)
    else:
        # 뺄 때는 - 부호를 붙여서 양수로 뽑히게끔 만들었다.
        heapq.heappush(heap_arr, -num)
