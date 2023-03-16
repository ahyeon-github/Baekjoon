A, B = input().split()
print(int(A) + int(B))


#map 함수를 활용하면 한 줄의 코딩으로 모든 자료형 각각에 함수를 적용할 수 있다.
A, B = map(int, input().split())
print(A+B)