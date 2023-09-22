def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result

# 예제로 주어진 배열을 사용하여 함수 테스트
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))  # 결과: 7
