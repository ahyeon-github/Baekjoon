# 28개의 입력을 한줄씩 받는다
# 1~30까지 없는 숫자를 판별해야함
#1부터 30이 들어간 배열에 원소가 없으면 출력


check_list = [i for i in range (1,31)]
for _ in range(28):
    n = int(input())
    #배열에 원소가 없으면 출력
    # for r in range (n):
    #     if r not in check_list:
    #         print(r)
    check_list.remove(n)
print(min(check_list))
print(max(check_list))