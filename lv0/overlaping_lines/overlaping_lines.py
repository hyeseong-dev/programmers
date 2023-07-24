def solution(lines):
    # 선분들의 시작과 끝 좌표를 기록할 리스트를 생성합니다.
    coordinates = []
    
    # 선분들의 시작과 끝 좌표를 coordinates 리스트에 추가합니다.
    for line in lines:
        start, end = line
        coordinates.append((start, "start"))
        coordinates.append((end, "end"))
    
    # 겹치는 부분의 길이를 계산합니다.
    overlapping_length = 0
    
    # coordinates 리스트를 오름차순으로 정렬합니다.
    coordinates.sort()
    
    # 선분이 겹치는 개수를 기록하는 변수를 생성합니다.
    overlap_count = 0
    
    # coordinates 리스트를 순회하면서 겹치는 부분의 길이를 계산합니다.
    # coordinates를 순회하면서 각 좌표의 유형을 확인합니다. 시작 좌표인 경우 'start', 끝 좌표인 경우 'end'로 표시합니다.
    for i in range(len(coordinates)):

        #시작 좌표인 경우 overlap_count를 1 증가시킵니다. 
        # 시작 좌표는 새로운 선분이 시작되는 지점을 의미합니다.
        if coordinates[i][1] == "start":
            overlap_count += 1

        #끝 좌표인 경우 overlap_count를 1 감소시킵니다. 
        # 끝 좌표는 선분이 끝나는 지점을 의미합니다.
        else:
            overlap_count -= 1
            
#overlap_count가 2 이상이고, 현재 좌표가 coordinates의 마지막이 아닌 경우에만 겹치는 부분의 길이를 계산합니다. 
#겹치는 부분의 길이는 다음 좌표의 값에서 현재 좌표의 값을 빼서 구할 수 있습니다. 
        if overlap_count >= 2 and i < len(coordinates) - 1:
# 따라서 coordinates[i+1][0] - coordinates[i][0]를 겹치는 부분의 길이에 더합니다.
            overlapping_length += coordinates[i + 1][0] - coordinates[i][0]
    
    return overlapping_length

params = [
    [[[0, 1], [2, 5], [3, 9]],	2],
    [[[-1, 1], [1, 3], [3, 9]],	0],
    [[[0, 5], [3, 9], [1, 10]],	8],
]
for param in params:
    result = solution(param[0])
    print(result)

    print('성공했습니다.')
