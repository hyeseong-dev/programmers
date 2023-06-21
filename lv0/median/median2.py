def solution(array):
    median_idx = len(array) // 2
    return sorted(array)[median_idx]

params = [
    [[1, 2, 7, 10, 11],	7],
    [[9, -1, 0],	0]
]
for case in params:
    result = solution(case[0])
    print(result)
    assert result == case[1]
    print('성공했습니다.')
