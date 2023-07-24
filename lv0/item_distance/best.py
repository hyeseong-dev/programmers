def solution(num_list, n):
    return [num_list[idx] for idx in range(0, len(num_list), n)]

"""
이 개선된 코드는 여전히 시간 복잡도가 O(N)이며, 공간 복잡도도 O(N)입니다. 하지만 리스트에 접근하고 요소를 생성하는 과정이 간결해졌으므로, 좀 더 효율적인 구현이라고 할 수 있습니다.
"""
