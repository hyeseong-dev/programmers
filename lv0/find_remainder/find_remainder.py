def solution(n):
    for num in range(3, n):
        if n % num == 1:
            return num

params = [
    [10,3],
    [12,11],
]
for param in params:
    result = solution(param[0])
    print(result, param[1])



