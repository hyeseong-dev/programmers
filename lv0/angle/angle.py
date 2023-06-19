# 솔루션1
# 코드 개발시 문제점 : assert 문에 대해 어떻게 사용해야 하는지 몰랐음. 
def solution(angle):
    acute_angle = (0 < angle < 90)
    right_angle = (90 == angle)
    obtuse_angle = (90 < angle < 180)
    flat_angle = (180 == angle)
    
    if acute_angle:
        return 1
    elif right_angle:
      return 2   
    elif obtuse_angle:
        return 3
    elif flat_angle:
        return 4

angle1 = 70
answer1 = 1

angle2 = 91
answer2 = 3

angle3 = 180
answer3 = 4

assert solution(angle1) == answer1, f"Expected {answer1}, but got {solution(angle1)}"
assert solution(angle2) == answer2, f"Expected {answer2}, but got {solution(angle2)}"
assert solution(angle3) == answer3, f"Expected {answer3}, but got {solution(angle3)}"
