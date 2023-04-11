s = str(input())

alphabet ='abcdefghijklmnopqrstuvwxyz'

# 입력받은 문자열 인덱스
# 문자열 하나씩 보면서 알파벳이 등장하는 인덱스 
# 최종 24개 알파벳 인덱스 출력

for i in alphabet:
    
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')
        
    



# 0 1 2 3 4 5 6 7
# b a e k j o o n

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 1 0     2         4 3     7 5 