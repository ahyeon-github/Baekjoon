#생각정리 
# - 큐 문제이므로 deque를 사용, 시간복잡도가 더 적어서
# 문제에서 시간복잡도가 O(1) 이어야 한다고 제시, 연결리스트로 [] 큐 구현은 O(n)
#시간을 단축하기 위해서 input() 보다는 sys.stdin.readline() 사용

#deque함수를 사용하면 기존에 list로 큐를 구현하는 것보다 시간복잡도를 대폭 줄일 수 있다.
# 리스트의 경우 pop()하면 뒤의 원소들이 이동하기 때문에 시간복잡도가 O(n)인데,
#Deque의 경우 리스트 하나하나가 객체로 이루어진 Double linked list로 구현되어 있기 때문에
# 양 끝의 추가, 삭제 (큐,스택)가 시간복잡도 O(1)을 만족하게 된다.


import sys
from collections import deque

# 시간을 단축하기 위해서 input() 보다는 sys.stdin.readline() 사용
n = int(sys.stdin.readline())
#큐 문제이므로 deque를 사용
queue = deque()
for i in range(n):
    order = sys.stdin.readline().split()
    #명령어를 하나씩 받아서 요구대로 처리해주어 구현
    if order[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif order[0] == "push":
        queue.append(order[1])