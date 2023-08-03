def solution(n):
    if n == 1:
        return 1
    answer = 0
    start = 1
    end = 1
    temp = 1

    while start <= n//2 + 1:
        if temp < n:
            end += 1
            temp += end
        elif temp == n:
            answer += 1
            end += 1
            temp += end 
        else :
            temp -= start
            start += 1

    return answer + 1 # 자기 자신을 더함

result = solution(1)
print(1)