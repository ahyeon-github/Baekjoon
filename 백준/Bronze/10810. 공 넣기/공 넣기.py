n, m = map(int, input().split())

# 바구니 배열 n의 개수만큼
#k_list=[]
k_list =[0]*n

for r in range(m):
    i,j,k = map(int, input().split())
    
    # i.j 바구니에 k번 공을 넣는다
    # 가장 마지막에 넣는 공을 출력한다 아무것도 들어있지 않으면 0
    # i j 에 k 값 전부 대입
    for l in range(i,j+1):
        k_list[l-1]=k
for t in range(n):
    print(k_list[t], end= ' ')