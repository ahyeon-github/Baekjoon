import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
  filename, extension = input().rstrip().split(".")
  dic[extension] += 1

sortedDict = sorted(dic.items())

for i in sortedDict:
  print(*i)