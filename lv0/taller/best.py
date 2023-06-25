def solution(array, height):
    count = 0
    for h in array:
        if h > height:
            count += 1
    return count

params = [
    ([149, 180, 192, 170], 167, 3),
    ([180, 120, 140], 190, 0),
]

for param in params:
    result = solution(param[0], param[1])
    print(result)