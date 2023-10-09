def solution(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return 1 + solution((n-1) // 2)
    return solution(n // 2)



# # 테스트
print(solution(5))  # 2
print(solution(6))  # 2
print(solution(7))  # 3
print(solution(8))  # 1
print(solution(9))  # 2
print(solution(10))  #2
print(solution(11))  #3
print(solution(5000))  # 5
