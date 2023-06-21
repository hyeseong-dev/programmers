# 시간 복잡도 O(n)
# 공간 복잡도 O(1)

def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

