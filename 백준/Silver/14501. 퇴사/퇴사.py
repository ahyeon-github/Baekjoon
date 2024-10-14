N= int(input())

# T, P = [list(map(int, input().split())) for _ in range(N)]
# 3 5
# 2 4
# T = [3, 5]
# P = [2, 4]

T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

# 3 5
# 2 4
# 6 7
# T = [3, 2, 6]
# P = [5, 4, 7]

def dfs(n, sm):
    # 전역변수
    global ans
    # [1] 종료 조건 처리 : 가능한 n을 종료하는 관려된 것으로 정의
    if n >= N:
        # 정답 ans, sm 중에
        ans= max(ans, sm)
    # return ans
        return

    # [2] 하부 함수 호출 : 화살표 개수만큼 호출
    if n + T[n] <= N: # 상담이 가능한 경우  (퇴사일전 완료 가능한 날)
        dfs (n + T[n], sm  + P[n])

    # 상담하지 않은 경우 (항상 가능)
    # 상담 안하는건 항상 가능, 조건을 붙일 필요가 없음
    # else:
    #     dfs(n+1, sm)
    dfs(n + 1, sm)


# 제일 위 함수
# n= 0, 합계 수익 0
ans = 0
dfs(0, 0)
print(ans)
