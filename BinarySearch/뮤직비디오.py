
# 9 3 
# 123456789

# 1+2+3+4+5+6+7+8+9 -> 45 각 노래들의 길이의 모든 합
#  1 ~ 45  사이의 값이 정답 -> 이분탐색

# 1 ~ 45 중앙값 : 23 (정답 가능 -> res에 저장)
# rt = mid-1
# 1 ~ 22 중앙값 : 11 (정답 불가능 , 3개를 초과해버림 최소 5장이 필요함)
# lt = mid+1
# 12 ~ 22 중앙값 : 17 (정답 -> res에 저장)


def Count(capacity):
    # 필요한 dvd 개수
    cnt  = 1
    # dvd에 노래를 저장할 때 곡들의 누적된 시간들 
    sum = 0
    for x in minute:
        if sum + x > capacity:
            # 더이상 저장할수없어서 용량이 초과함
            # 새로운 dvd 필요함
            cnt +=1
            # 새로운 dvd에 x곡을 저장해야함, 새롭게 x로 초기화 
            sum = x
        else:
            sum += x 
    return (cnt)


N, M = map(int, input().split())
minute = list(map(int, input().split()))

# all_minute = 0
# for i in range(N+1):
#     all_minute += i
# print(all_minute)

lt = 1
rt = sum(minute)
res=0
# rt = all_minute



while lt<= rt :
    mid = (lt+rt // 2)
    #  원소들을 더해가면서 <= mid
    # 필요한 dvd개수가 M 이하여야만 한다 
    # 주의 : 용량이 3개 짜리인데 2가 리턴되어서 와도 답이 될수있음 , 2장만에 저장이 되면 3장만에 되는것임
    #if Count(mid) ==  M:
    if Count(mid) <=  M:
        res = mid
        rt = mid-1
    # if 더한 묵음이 > M :
    #elif Count(mid ) > M :
    else:
        lt = mid+1

print(res)
    
