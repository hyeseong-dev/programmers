
def solution(array, height):
    answer = 0
    array.sort()
    for friend_height in array:
        if friend_height > height:
            answer += 1
        elif friend_height == height:
            break
    return answer


params = [
[[149, 180, 192, 170], 167, 3],
[[180, 120, 140], 190, 0],
]

for param in params:
    result = solution(param[0], param[1])
    print(result)
