n,m = map(int, input().split())
#리스트 n 만큼 
#list = [1,2,3,4,5]
list = [l for l in range(1, n+1)]
for r in range(m):
    i,j = map(int, input().split())
    # j는 i, i는 j에 값을 대입
    list[i-1] , list[j-1] = list[j-1] , list[i-1]
#print(list)
for i in range(n):
    print(list[i], end=' ')