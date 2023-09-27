def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)
    return answer

arr = [2,6,8,14]
result = solution(arr)
print(result)