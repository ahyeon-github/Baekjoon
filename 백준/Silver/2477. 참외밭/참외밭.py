melon = int(input()) 
widths = [input().split() for _ in range(6)] 

 # 방향, 길이 저장
directions = [int(n[0]) for n in widths] 
lengths = [int(n[1]) for n  in widths]
# 큰 직사각형의 길이, 작은 직사각형의 길이를 담을 배열
maxRec_lengths, minRec_lengths = [], [] 

for i in range(1, 5):
    if directions.count(i) == 1: # direction이 한번만 존재 == 큰 직사각형의 변
        maxRec_lengths.append(lengths[directions.index(i)]) # 큰 직사각형의 변 길이 저장
        # 큰 직사각형 가로 혹은 세로 길이의 변에서, 세 번째 이동하는 변 
        # directions + 3 == 작은 직사각형의 변
        temp = directions.index(i) + 3 
        if temp >= 6:
             temp -= 6 # cycle을 위해 6 이상일 경우 -6
        minRec_lengths.append(lengths[temp]) 

area = maxRec_lengths[0] * maxRec_lengths[1] - minRec_lengths[0] * minRec_lengths[1]
print(melon * area)
