n, k = map(int, input().split())
v = list(map(int, input().split()))

i = 0
sum_value = 0

v.sort()

for j in range(n):
    sum_value += v[j] * i
    if i < k:
        i += 1

print(sum_value)
