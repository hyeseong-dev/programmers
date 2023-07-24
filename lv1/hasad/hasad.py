def solution(x):
    arr = [int(num) for num in str(x)]
    divisor = sum(arr)
    return x % divisor == 0

    


print(solution(18))