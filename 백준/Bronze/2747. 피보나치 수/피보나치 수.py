N = int(input())

dy = [0] * (N+1)
dy[0] = 0
dy[1] = 1

for i in range(2, N+1):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[N])