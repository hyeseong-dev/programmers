def solution(sides):
    longest = max(sides)
    side1, side2, side3 = sides
    if side1 == longest and side1 < (side2 + side3):
        return 1
    elif side2 == longest and side2 < (side1 + side3):
        return 1
    elif side3 == longest and side3 < (side1 + side2):
        return 1
    else :
        return 2
