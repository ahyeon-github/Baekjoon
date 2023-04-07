n=int(input())

#세 수중 최댓값 찾기
# for i in range(3):
#     r= int(input())
#     record.append(r)
    
#     m = max(record)
# 나머지 점수/최대점수 * 100 적용
# print(m)

# 세 수들의 평균을 출력
# a, b, c = map(int, input().split())
# record.append(a)
# record.append(b)
# record.append(c)

# for i in record:
#     m = max(record)
    
# result = ( m + record[0]/m * 100 + record[1]/m*100 ) / n
# print(result)

#점수들 리스트로 받기 
score_list = list(map(int,input().split()))
max = max(score_list)
result =[]

for r in score_list:
    result.append(r/max * 100 )

avg = sum(result)/n
print(avg)