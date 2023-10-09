
n = 16                                      # 2진수 - '0b1111'

def solution(n):
    result = 0
    count_one = bin(n).count('1')           # 자연수 n을 2진수로 바꾸고 1의 개수를 파악한다. 
    
    for num in range(n+1, 1000000+1):       # `n의 다음 큰 숫자`는 n초과 1,000,000 이하의 범위를 순회하여 확인
                                            # 
        if count_one ==bin(num).count('1'): # 조건2 : `n`을 이진수로 바꾼 수의 1의 개수와 `n의 다음 큰 숫자`의 이진수에서 `1`의 개수가 같은지 확인 
            result = num
            break
    return result                           # 조건3 : `n의 다음 큰 숫자`는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

for n in 78, 15:
    print(solution(n))                          # 23(2진수 - '0b10111')


