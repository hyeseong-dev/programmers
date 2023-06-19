def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

test_cases = [
    (70, 1),
    (91, 3),
    (180, 4)
]

for angle, expected in test_cases:
    assert solution(angle) == expected, f"Expected {expected}, but got {solution(angle)}"

