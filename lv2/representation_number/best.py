def solution(n):
    answer = 0
    start = 1
    end = 1
    sum = 1

    while start <= end:
        if sum < n:
            end += 1
            sum += end
        elif sum > n:
            sum -= start
            start += 1
        else:
            answer += 1
            sum -= start
            start += 1

    return answer


result = solution(15)