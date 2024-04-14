N, K = map(int, input().split())
# list = []
count = 0
for i in range(1, N+1):

    if N % i == 0:
        # list.append(i)
        # sorted(list)
        count += 1
    if count == K:
        print(i)
        break


else:
    print(0)

# print(list[K - 1])

