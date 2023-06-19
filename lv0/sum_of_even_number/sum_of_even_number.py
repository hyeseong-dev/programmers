def solution(n):
    answer = 0
    for i in range(1, n+1) :
        if i % 2 == 0:
            answer += i
            
    return answer

assert solution(10) == 30, f"solution(10) == 30은 틀립니다. solution(10)의 반환 값은 {solution(10)}"