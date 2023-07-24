def solution(minefield):
    field_size = len(minefield)
    danger_zones = set()
    
    for row_index, row_content in enumerate(minefield):
        for column_index, cell_content in enumerate(row_content):
            if not cell_content:
                continue
            danger_zones.update((row_index + delta_row, column_index + delta_column) for delta_row in [-1,0,1] for delta_column in [-1, 0, 1])
    
    safe_zones = field_size * field_size - sum(0 <= row < field_size and 0 <= column < field_size for row, column in danger_zones)
    
    return safe_zones





"""
하나.    field_size = len(minefield)
field_size라는 변수에 지뢰밭의 한 변의 크기를 저장합니다. minefield는 정사각형 배열이므로 한 변의 길이만 알아도 전체 크기를 알 수 있습니다.

둘. danger = set()
'danger'라는 이름의 빈 집합을 만듭니다. 이 집합은 위험 지역의 좌표를 담을 용도로 사용됩니다.


셋. for i, row in enumerate(board):
보드의 각 행에 대해 반복합니다. 'i'는 현재 행의 인덱스를 나타내고, 'row'는 현재 행의 내용을 나타냅니다.

넷. for j, x in enumerate(row):
현재 행의 각 열에 대해 반복합니다. 'j'는 현재 열의 인덱스를 나타내고, 'x'는 현재 셀의 내용을 나타냅니다.

다섯. if not x: continue
만약 현재 셀의 내용이 0(즉, 지뢰가 없다면), 이 반복문의 나머지 부분을 건너뛰고 다음 셀로 넘어갑니다.

여섯. danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
현재 셀이 지뢰를 포함하므로, 현재 셀 주변의 8개 셀(위, 아래, 왼쪽, 오른쪽, 그리고 대각선 방향)을 위험 지역으로 추가합니다.

일곱. return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

마지막으로, 전체 셀의 수(n*n)에서 위험 지역의 수를 뺀 값을 반환합니다. 위험 지역의 수는 보드의 범위 내에 있는 위험 지역의 좌표 수로 계산됩니다.

"""