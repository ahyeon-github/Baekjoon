a = int(input())
b= int(input())


print(a*(b%10)) # B 세자릿 수를 10으로 나눈 나머지 -> 일의자리 
print( a*((b%100)//10)) # B 수를 100으로 나눈 나머지 -> 십의 자리수 그 값에 //10 -> 몫
print((a*(b//100))) #100으로 나눈 몫
print((a*b)) # 전체 곱한 수
 
 
 
#문자열 이용한 방법
A = int(input())
B= int(input())

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B)) 