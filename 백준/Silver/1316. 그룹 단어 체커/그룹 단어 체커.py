word_count =int(input())
count = word_count
for i in range(word_count):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break
        
print(count) 
'''
단어들이 계속 연속하여 등장하는지 확인을 하기 위해 자료구조 스택을 사용
각 문자들이 들어올 때 스택에 넣어준다. 

'''