n_list = []
for i in range(10):
    n = int(input())
    # 42로 나눈 나머지를 담을 리스트
    m = n % 42
    n_list.append(m)
    #리스트 중에 서로 다른 값 찾기
    
# 중복을 제거하기 위한 집합 자료형
n_list = set(n_list)
print(len(n_list))