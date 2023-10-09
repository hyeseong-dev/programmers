def solution(n, left, right):
    answer = []

    for index in range(left, right+1):
        row = index // n
        col = index % n
        answer.append(max(row, col) + 1)

    return answer


# n = 3
# left = 2
# right = 5

n = 4
left = 7
right = 14
print(solution(n, left, right))