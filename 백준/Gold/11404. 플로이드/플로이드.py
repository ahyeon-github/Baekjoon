# 점화
import sys

if __name__=="__main__":
    # 정점노드의 개수 , 간선의 개수
    # 첫 번째 줄에서 도시의 개수 n 입력받기
    n = int(input())

    # 두 번째 줄에서 버스의 개수 m 입력받기
    m = int(input())

    # 이차원 테이블 , 가장 큰 값으로 초기화
    INF = sys.maxsize
    dis = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        # 자기자신으로 가는 건 0으로 초기화
        dis[i][i]=0

        # i -> j 로 가는데, 중간 노드 거치지 않고 바로 직행하는 것
    for i in range(m):
        a, b, c=map(int, input().split())
        # dis[a][b]=c
        dis[a][b] = min(dis[a][b], c)
        
# k 1~ n 까지 돌면서
    for k in range(1, n+1):
        # 이중for문
        for i in range(1, n+1):
            for j in range(1, n+1):
                # i -> k -> j
                dis[i][j] = min(dis[i][j], dis[i][k] +dis[k][j])

                #플로이드와샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

        # 결과 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == INF:
                print(0, end=' ')  # 갈 수 없는 경우 0 출력
            else:
                print(dis[i][j], end=' ')
        print()