  
import sys
read = sys.stdin.readline
n=int(read())  

graph = []
village_count=0
temp_count=0
house_count= []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def recursive_dfs(x, y):
    # 범위를 벗어난 경우 예외처리
    if(x < 0 or x >= n) or (y < 0 or y >=n ):
        return False
    
    # 현재 노드가 '1' 이면서 아직 미방문  -> 해당 지점 방문
    if graph[x][y] == 1:
        # 해당 지점 방문하고 '0' 처리
        graph[x][y] = 0
        global temp_count
        temp_count += 1
        # 상하좌우 탐색 
        # for i in range (len(dy))
        for i in range (len(dx)):
            recursive_dfs(x+dx[i], y+dy[i])
        return True
    # 방문을 했다면 더 이상 탐색하지 않음
    return False

for i in range(n):
    graph.append(list(map(int, read().rstrip())))
        
for i in range(n):
    for j in range(n):
        if recursive_dfs (i,j):
            village_count += 1
            house_count.append(temp_count)
            temp_count=0
house_count.sort()
print(village_count)
for count in house_count:
    print(count)

