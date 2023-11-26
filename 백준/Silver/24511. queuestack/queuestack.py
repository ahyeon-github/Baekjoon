# 생각정리
# 오답 : 시간초과
# 연결리스트 사용해서 단순 구현 -> 2중 포문에 if문까지 써서 시간복잡도가 올라감


import sys
# deque
from collections import deque
# 시간복잡도 개선을 위한 명령어
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

# deque 선언
queStack = deque()

for i in range(n):
    # 만약 a[i] 값이 queue일경우
    # stack은 입력과 출력이 일어나도 변수의 변경이 없으므로 생략해준다.
    if a[i] == 0:
        # deque에 b[i] 값을 차례대로 append 해준다.
        queStack.append(b[i])
# 반복문이 종료 된 후 바로 실행되는 else 명령어.
else:
    # 만약 b 리스트 내부가 모두 스택이여서 len(b)의 값이 0일경우
    if len(b) == 0:
        # 그냥 c에 입력된 수열을 다시 출력해준다.
        # stack 자료형에 들어간 수는 어차피 pop을 해도 다를게 없기 때문에
        print(*c)
        # 코드를 즉시 종료
        sys.exit()

#  입력한 수열의 값을 queStack에 넣어 pop해준다.
for i in range(m):
    # queStack 내부 가장 왼쪽에 수열의 값을 넣어준다.
    queStack.appendleft(c[i])
    # queStack 마지막 자료를 pop 해주고 출력.
    print(queStack.pop(), end=" ")