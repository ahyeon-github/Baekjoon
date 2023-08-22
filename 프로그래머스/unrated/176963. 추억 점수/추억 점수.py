# default = 0
from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    sH = defaultdict(int)
    
    for i in range(len(name)):
        sH[name[i]] = yearning[i]
    for i in photo:
        sum = 0
        for j in i:
            sum += sH[j]
        answer.append(sum)
                   
    return answer