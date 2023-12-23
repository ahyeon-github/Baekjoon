import sys; input = sys.stdin.readline

def dfs(i, j): # DFS
    result = 0
    for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]: # 상하좌우
        # 다음 위치가 범위 안이며 방문하지 않은 위치이며 병사의 종류가 시작 위치와 같아야 한다.
        if 0 <= ii < M and 0 <= jj < N and not visited[ii][jj] and matrix[m][n] == matrix[ii][jj]:
            visited[ii][jj] = True # 방문 체크
            result += 1 # 결과에 1 더하고
            result += dfs(ii, jj) # 다음 위치 DFS
    return result # 결과 반환

N, M = map(int, input().split())
matrix = [input().strip() for _ in range(M + 1)]
visited = [[False] * N for _ in range(M + 1)] # 방문 체크할 행렬도 전쟁터의 크기와 똑같이 만든다.
W = B = 0
for m in range(M):
    for n in range(N):
        if not visited[m][n]: # 만약 방문하지 않은 위치라면
            visited[m][n] = True # 방문 체크 후
            result = 1 + dfs(m, n) # 그 위치의 1명 + DFS 결과값이 뭉쳐있는 병사 수가 된다.
            exec('%s += result ** 2' % matrix[m][n]) # 병사들이 속해있는 국가의 위력에 뭉쳐있는 병사 수의 제곱만큼 더해준다.
print(W, B) # 정답 출력