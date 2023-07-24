def solution(a, b):
    return (a + b) * (abs(a - b) + 1) // 2


result = solution(3,5)
print(result)