bricks = []

N = int(input())
# 각 벽돌의 정보 입력받기
for i in range(N):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c, i + 1))  # 벽돌 번호를 추가하여 튜플에 저장

# 밑면 넓이(a)를 기준으로 내림차순 정렬
bricks.sort(reverse=True)

dy = [0] * N  # 각 벽돌까지 쌓은 탑의 최대 높이 저장
track = [-1] * N  # 각 벽돌이 어디서 왔는지 추적 (이전 벽돌 인덱스 저장)
dy[0] = bricks[0][1]  # 첫 번째 벽돌의 높이로 초기화
res = dy[0]
max_index = 0  # 가장 높은 탑을 쌓은 벽돌의 인덱스

# DP로 가장 높은 탑 쌓기
for i in range(1, N):
    max_h = 0
    for j in range(i - 1, -1, -1):
        # 무게와 밑면 넓이 조건을 만족해야 위에 쌓을 수 있음
        if bricks[i][2] < bricks[j][2] and dy[j] > max_h:
            max_h = dy[j]
            track[i] = j  # 벽돌 i 위에 j를 쌓았다는 것을 추적
    dy[i] = max_h + bricks[i][1]

    # 가장 높은 탑을 쌓을 수 있는 경우 갱신
    if dy[i] > res:
        res = dy[i]
        max_index = i

# 사용된 벽돌의 수 계산
brick_stack = []
current = max_index
while current != -1:
    brick_stack.append(bricks[current][3])  # 벽돌 번호를 기록
    current = track[current]  # 추적 배열을 따라가며 벽돌 번호를 추가

# 결과 출력
print(len(brick_stack))  # 사용된 벽돌의 수
for brick in brick_stack:  # 벽돌을 위에서 아래 순서로 출력
    print(brick)