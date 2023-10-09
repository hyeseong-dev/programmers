def solution(n):
    # 초기 피보나치 수를 설정합니다.
    prev_fibo, current_fibo = 0, 1

    # n번째 피보나치 수를 계산합니다.
    for _ in range(2, n+1):
        next_fibo = (prev_fibo + current_fibo) % 1234567
        prev_fibo, current_fibo = current_fibo, next_fibo

    # n번째 피보나치 수를 반환합니다.
    return current_fibo
