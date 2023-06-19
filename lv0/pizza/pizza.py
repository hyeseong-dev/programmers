def solution(n):
    answer = 0
    a = n //7 
    if n % 7 != 0:
        remain = 1
    else:
        remain = 0
    answer = a + remain
    return answer