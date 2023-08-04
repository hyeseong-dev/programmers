def solution(N, A, B):
    round = 0
    while A != B:
        temp_a = (A+1)
        process_a = temp_a // 2
        A = process_a

        temp_b = (B+1)
        process_b = temp_b // 2
        B = process_b
        round += 1
    return round


result = solution(8, 4, 7)
print(result)