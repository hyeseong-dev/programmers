def solution(left, right):
    answer = 0
    yaksu_list = []
    for num in range(left, right + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                yaksu_list.append(i)
        if len(yaksu_list) % 2 ==0:
            answer += num
        else:
            answer -= num
        yaksu_list = []
    return answer


parameters = [
    13,	17,	43,
]

result = solution(parameters[0], parameters[1])
print(result)