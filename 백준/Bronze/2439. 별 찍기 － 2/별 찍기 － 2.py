N=int(input())
for i in range(1,  N+1):
    # 공백찍기
    for j in range(N-i):
        print(" ",end="")
        # 별 찍기
    for k in range(i):
        print('*', end='')
    print()
    


# a=int(input())
# for i in range(1,a+1):
#     print(" "*(a-i) + "*"*i)