N=int(input())
A = list(map(int, input().split()))
V=int(input())
count = 0

for i in A:
    if(i==V):
        count+=1
print(count)





# N=int(input())
# A_list = list(map(int, input().split()))
# V=int(input())

# print(A_list.count(V))