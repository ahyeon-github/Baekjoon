import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    minH, maxH = [], []
    # False면 두 힙 중 하나 이상에 존재하지 않은 상태
    # visited[node] = False => 삭제된 노드
    visited = [False] * k 
    for i in range(k):
        cmd, x = input().split()
        if cmd == "I":
            # 힙은 기본적으로 최소힙 : 오름차순 정렬
            heapq.heappush(minH, (int(x), i))
            # 최대힙(내림차순 정렬)을 위해 입력값에 -를 붙인다
            heapq.heappush(maxH, (-int(x), i))
            # True면 두 힙 모두에 존재하는 상태
            # visited[node] = True => 존재하는 노드
            visited[i] = True 
        else:
            # 최소값 제거
            if x == '-1':
                # 최소힙과 최대힙의 싱크로율을 맞추는 과정
                # 이미 삭제된 노드를 삭제하는 과정
                # minH이 비거나 minH이 두 힙 모두에 존재할 때까지 while문 반복
                while minH and not visited[minH[0][1]]:
                    # 최솟값 pop
                    heapq.heappop(minH)
                # 최소힙이 비어있지 않다면
                if minH:
                    # 최솟값 삭제
                    visited[minH[0][1]] = False
                    heapq.heappop(minH)
            # 최댓값 제거
            else:
                # 최소힙과 최대힙의 싱크로율을 맞추는 과정
                # maxH이 비거나 maxH이 두 힙 모두에 존재할 때까지 while문 반복
                while maxH and not visited[maxH[0][1]]:
                    # 최댓값 pop
                    heapq.heappop(maxH)
                # 최대힙이 비어있지 않다면
                if maxH:
                    # 최댓값 삭제
                    visited[maxH[0][1]] = False
                    heapq.heappop(maxH)
    # 최소힙과 최대힙의 싱크로율을 맞추기 위해 위에서 한 짓을 반복
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)

    # 최소힙과 최대힙 둘 다 안 비어있는 경우
    if maxH and minH:
        # 위에서는 최대힙과 최소힙을 맞추기 위해 인덱스 i를 기준으로 계산했지만
        # 입력값인 x을 출력해야하니까 -maxH[0][0], minH[0][0] 출력
        print(-maxH[0][0], minH[0][0])
    # 비어있는 경우
    else:
        print("EMPTY")