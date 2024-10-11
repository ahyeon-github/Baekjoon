# board 이차원리스트 탐색하면서  익은 토마토(1)은 큐에 넣음
# dis 이차원 리스트 : 다 익는데 걸리는 날짜  -> 기본적으로 0으로 초기화

# 익은 토마토의 위치를 큐에 넣음
# Q
# (1,2)  (3,5)

#익은 토마토를 넣고, 그 다음 네방향 탐색
# 출발하면서  이제 거기서 네방향 탐색을 시작한다.

# Q
# (1,2)  (3,5)

# 큐에서 (1,2) pop 되어서 빠져나옴
# Q
# (3,5)
# 1,2 의 상하좌우를 본다  안익은 토마토가 있다면(0) -> 1로 바꿈 (1,3)

# 큐에 넣음
# Q
# (3,5) (1,3)
# dis 에는 부모값 + 1



# 그 다음 옆에 또 안익은 토마토 큐에 넣음
# Q
# (3,5) (1,3) (1,1)
# dis 에는 부모값 + 1



# pop
# Q
# (1,3) (1,1)
# (3,5)에서 네방향 탐색


# 큐에 넣음
# Q
# (1,3) (1,1) (2,5)
# (3,5)에서 네방향 탐색



# pop
# Q
# (1,1) (2,5) (0,3)
# dis + 1


from collections import deque

dx = [-1 , 0 , 1, 0]
dy = [0, 1, 0, -1]

# 열, 행
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
# 날짜 저장
dis = [[0]*n for _ in range(m)]


# 이미 익은 것들을 q에 append
# m 행
for i in range(m):
    for j in range(n):
        # 1 익은 토마토
        if board[i][j] == 1:
            # 해당 좌표를 Q에 넣음
            Q.append((i, j))


while Q:
    tmp=Q.popleft()
    for i in range(4):
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        # x가 행 번호  행(세로 위치) 인덱스 0<=xx< n 이 아님
        if 0<=xx< m   and 0<=yy<n and board[xx][yy]==0:
            # board[xx][yy]==1
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]]+1
            Q.append((xx,yy))


# 토마토가 모두 익지 못하는 상황이라면  -1 을 출력
flag = 1
for i in range(m):
    for j in range(n):
        # 거기까지 가지 못했다, 안익은 토마토가 존재한다
        if board[i][j] == 0 :
            flag = 0

# 최댓값 찾아야함
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                #dis[i][j] = result
                result = dis[i][j]
    print(result)

else:
    print(-1)

