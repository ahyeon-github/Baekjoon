bricks = []

N = int(input())
# a,b,c = [list(map(int, input().split())) for _ in range (N)]
# 각 벽돌의 정보 입력받기
for i in range(N):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c, i+1)) # # 벽돌 번호를 추가하여 튜플에 저장


# 내림차순
# 튜플 첫번째 자료 A 밑면의 넓이에 의해서 내림차순
# 튜플자료가 (a,b,c) 최초 a 에 대해서 내림차순 첫번째 자료 기준
# 밑면 넓이(a)를 기준으로 내림차순 정렬
bricks.sort(reverse=True)

dy = [0]*N   # 각 벽돌까지 쌓은 탑의 최대 높이 저장
# 각 벽돌이 어디서 왔는지 추적 (이전 벽돌 인덱스 저장)
#i번째 벽돌이 그 위에 쌓인 경우, 그 밑에 있는 벽돌의 인덱스를 저장
# -1로 초기화 :  “현재 이 벽돌은 다른 벽돌 위에 쌓이지 않았다
# ex. track[2] = 0. 벽돌 2가 벽돌 0 위에 쌓였다. 
track = [-1] * N # 각 벽돌이 어디서 왔는지 추적 (이전 벽돌 인덱스 저장)
# 0번 벽돌의 높이  벽돌의 번호
# 초기화 가장 작은것 초기화 해놓음 , 첫 번째 벽돌의 높이로 초기화
dy[0] =  bricks[0][1]

max_index = 0  # 가장 높은 탑을 쌓은 벽돌의 인덱스
#정답 리턴하는 값도 초기화
res=bricks[0][1]

# 만들고자 하는 i 가장 상단의 벽돌
# DP로 가장 높은 탑 쌓기
for i in range(1, N):
    # 앞으로 가면서 찾아야함 0번까지 가면서
    # 현재 i 번째 바로 밑의 벽돌들[j]을 찾는것
    max_h=0
    #j는 I의 바로 밑
    for j in range(i-1,-1,-1):
        # 현재 무게가 더 작아야지 위에 쌓을 수 있음, 앞에 것들 중에 큰 높이 값
        # 무게와 밑면 넓이 조건을 만족해야 위에 쌓을 수 있음
        if bricks[i][2]<bricks[j][2] and dy[j] > max_h:
            max_h=dy[j]
            # 벽돌 i 위에 j를 쌓았다는 것을 추적
            track[i] = j
    # dy[i] = dy[j][1]+dy[i][1]
    # max+자기자신 j에 i 번째 벽돌 높이를 더함
    dy[i] = max_h + bricks[i][1]

    # dy 배열에서 가장 큰 거 찾기, 기존보다 dy[i]가 더 크다면 바꿔줌
    # res = max(res, dy[i])
    # 가장 높은 탑을 쌓을 수 있는 경우 갱신
    if dy[i]> res:
        res = dy[i]
        max_index = i
# 사용된 벽돌의 수 계산
brick_stack = []
current = max_index
# 벽돌은 더 이상 그 아래에 쌓인 벽돌이 없다는 의미 그 벽돌이 탑의 가장 아래에 있는 벽돌
while current != -1:
    brick_stack.append(bricks[current][3])# 벽돌 번호를 기록
    current = track[current] # 추적 배열을 따라가며 벽돌 번호를 추가

print(len(brick_stack)) # 사용된 벽돌의 수
for brick in brick_stack: # 벽돌을 위에서 아래 순서로 출력
    print(brick)