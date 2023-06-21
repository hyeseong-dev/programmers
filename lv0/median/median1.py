def solution(array):
    answer = 0
    median_idx = (len(array) // 2)
    sorted_array = sorted(array)
    answer = sorted_array[median_idx]
    return answer


params = [
    [[1, 2, 7, 10, 11],	7],
    [[9, -1, 0],	0]
]
for case in params:
    result = solution(case[0])
    print(result)
    assert result == case[1]
    print('성공했습니다.')
