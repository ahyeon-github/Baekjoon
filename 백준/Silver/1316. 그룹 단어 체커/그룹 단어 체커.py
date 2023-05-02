n = int(input())
#count = 0
count = n
for i in range(n):
    word = input()
    # 단어들을 하나씩 보면서
    # 그룹단어인지 체크한다
    # 단어들을 하나씩 보고 원소들 중에 뒤에 중복된 원소가 나오면 그룹단어가 아님
    # 단어 각 원소들 바로 이어지는 것이면 그룹체커 , 단어들이 띄어져 있으면 그룹 체커가 아님
    for j in range(0, len(word)-1):
        if word [j] == word[j+1]:
            pass
        
        elif word[j] in word[j+2:]:
            count-=1
            break
print(count)
        



