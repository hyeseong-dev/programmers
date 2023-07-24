def solution(n):
    sum_of_divisors = 0  # 약수의 합을 저장할 변수 초기화
    
    for divisor in range(1, int(n**0.5) + 1):  # 1부터 n의 제곱근까지 반복
        if n % divisor == 0:  # n을 divisor로 나누었을 때 나머지가 0이면 divisor는 n의 약수
            sum_of_divisors += divisor  # divisor를 약수의 합에 더함
            if divisor != n // divisor:  # divisor와 n // divisor가 서로 다른 경우에만 n // divisor도 약수로 추가
                sum_of_divisors += n // divisor
    
    return sum_of_divisors



# 위 코드의 시간 복잡도는 O(√n)입니다. 
# for 루프의 반복 횟수는 n의 제곱근에 비례하며, 약수를 찾기 위해 1부터 n의 제곱근까지 반복합니다. 
# 따라서 시간 복잡도는 O(√n)입니다.

# 공간 복잡도는 O(1)입니다. 
# 추가적인 공간을 사용하지 않고, 정수 변수 하나만을 사용하여 약수의 합을 계산하므로 공간 복잡도는 상수입니다.