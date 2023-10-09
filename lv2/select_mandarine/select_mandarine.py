from collections import Counter
from itertools import accumulate

def solution(k, tangerine):
    # 각 귤의 크기별로 개수를 카운트
    counter = Counter(tangerine)   # Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1})
    sizes = list(counter.values()) # [1, 2, 2, 2, 1]
    
    sizes.sort(reverse=True)  # 내림차순 정렬  [2, 2, 2, 1, 1]
    acc_sizes = list(accumulate(sizes))  # 누적합 리스트 생성 # [2, 4, 6, 7, 8]
    
    # k개를 포함할 수 있는지 확인하며 최소 크기 종류 계산
    for i in range(len(acc_sizes)):
        if acc_sizes[i] >= k:
            return i + 1  # 0-based index이므로 1을 더해줌
    
    return len(sizes)  # 모든 크기의 귤을 다 사용해도 k개를 못 채울 경우

# 테스트 케이스
# print(solution(2, [1, 3, 2, 5, 4, 5, 2, 3]))  # 결과: 3
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 결과: 2
# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # 결과: 1
print(solution(6, [1, 1, 1, 1, 1, 1, 1, 1]))  # 결과: 1
