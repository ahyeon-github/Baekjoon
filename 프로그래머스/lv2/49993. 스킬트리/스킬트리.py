from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        dq = deque(skill)
        for x in tree:
            if x in dq:
                if x !=dq.popleft():
                    break
        else:
            answer +=1
            
                    
    return answer