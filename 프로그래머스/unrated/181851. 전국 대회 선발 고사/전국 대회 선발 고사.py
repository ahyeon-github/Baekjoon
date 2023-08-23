def solution(rank, attendance):
    answer = 0
    temp = []
    for i in range(len(rank)):
        index = rank.index(i+1)
        if attendance[index]:
            temp.append(index)
        if len(temp) == 3:
            break



    return 10000*temp[0]+100*temp[1]+temp[2]