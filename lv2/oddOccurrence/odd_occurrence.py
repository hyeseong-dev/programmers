def solution(A):
    # 배열을 정렬
    A.sort()

    # 2칸씩 건너뛰며 짝이 없는 요소를 찾음
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i+1]:
            return A[i]
    
    # 모든 쌍을 확인한 후에도 짝이 없는 요소를 찾지 못한 경우, 배열의 마지막 요소가 짝이 없는 요소
    return A[-1]

# 예제로 주어진 배열을 사용하여 함수 테스트
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))  # 결과: 7
