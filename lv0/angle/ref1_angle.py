def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        raise ValueError("Angle must be between 0 and 180 degrees inclusive.")

test_cases = [
    (70, 1),
    (91, 3),
    (180, 4)
]

for angle, expected in test_cases:
    assert solution(angle) == expected, f"Expected {expected}, but got {solution(angle)}"

