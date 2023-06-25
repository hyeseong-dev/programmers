def solution(s1, s2):
    answer = 0
    for s1_item in s1:
        if s1_item in s2:
            answer += 1
    return answer