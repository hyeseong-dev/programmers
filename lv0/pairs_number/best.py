import math

def solution(n):
    answer = 0
    
    sqrt_n = int(math.sqrt(n))              # 입력값 n의 제곱근을 계산하고, 정수 형태로 변환하여 sqrt_n 변수에 저장합니다.

    for divisor in range(1, sqrt_n + 1):    # 1부터 sqrt_n까지의 범위에서 반복문을 실행합니다. divisor 변수는 각 약수를 나타냅니다.
        if n % divisor == 0:                # n을 divisor로 나누었을 때 나머지가 0인지 확인하여 약수인지 판별합니다.
            answer += 1                     # 약수인 경우, 결과값 answer를 1 증가시킵니다.
            if n // divisor != divisor:     # 약수가 제곱근이 아닌 경우를 판별하기 위해, n을 divisor로 나눈 몫과 divisor를 비교합니다.
                answer += 1                 # 약수가 제곱근이 아닌 경우, 결과값 answer를 추가로 1 증가시킵니다.
    return answer

solution(20)