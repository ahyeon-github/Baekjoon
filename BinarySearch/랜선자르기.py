# 현재 가지고 있는 랜선, 필요한 랜선 개수 입력받음 
K, N = map(int, input().split())
# K 만큼 돌면서 가지고 있는 랜선 길이들을 입력받음

# 리스트로 저장
Line=[]
# 찾은 중앙값 중에 가장 큰 값을 res에 저장 
res = 0
# 입력받은 것 중에 가장 큰 랜선 찾아야함 
largest = 0

for i in range(K):
# 줄바꿔서 입력받음 , 줄바꿈 하나하나 인풋
#     a = list(map(int,input().split()))
    tmp = int(input())
    Line.append(tmp)
    # 큰 값을 largest에 넣어줌 , 기존값과 새로운 값을 비교해서 갱신해준다.
    largest = max(largest, tmp)   
 
# lt = 0
# rt = small_line


# Count 함수
# len : 랜선의 길이
def Count(len):
    cnt = 0
    # 리스트 원소(x)에 하나하나 접근하면서
    for x in Line:
        cnt += (x//len)
    return cnt
        
        

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt) // 2
    # 찾은 mid
    # 각 Line에 있는 랜선 길이들과 //mid 
    # 계산 후 나온 몫들의합    < 11
    # 답이 아님 mid - 1 로 바꿈
    # 계산 후 나온 몫들의합    >= 11
    if Count(mid) >= N:
        res= mid
        lt=mid+1
    else:
        rt = mid-1
    # res에 저장
    # 그 다음 이어서 작을    lt 를 mid+1 로 바꿈
print(res)
    
