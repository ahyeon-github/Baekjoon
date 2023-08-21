def solution(n):
    answer = [[0]*n for _ in range(n)]
    dr= [-1, 0 , 1, 0]
    dc= [0, 1, 0, -1]
    r, c = 0, -1
    see = 1
    cnt = 1
    
    while cnt <= n*n :
        nr = r + dr[see]
        nc = c + dc[see]
        if nr <0 or nr >= n or nc <0 or nc >=n or answer[nr][nc] != 0:
            # 격자 밖은 회전만
            see = (see+1) % 4
            continue
        answer[nr][nc] = cnt
        cnt += 1
        
        r=nr
        c=nc
    
    return answer