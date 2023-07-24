def solution(num_list):
    answer = 0
    odd = ""
    even = ""

    for number in num_list:
        if number % 2 == 0:
            even += str(number)
        else:
            odd += str(number)
    return int(odd) + int(even)




params = [
[[3, 4, 5, 2, 1],	393],
[[5, 7, 8, 3],	581],
]

for param in params:
    result = solution(param[0])
    assert result == param[1]
    print(result)


"""
위 코드의 시간 복잡도는 O(N), 공간 복잡도는 O(N)입니다. N은 num_list의 길이를 나타냅니다.

코드를 개선하여 시간 복잡도를 개선할 수 있습니다. 현재 코드에서는 odd와 even 문자열에 숫자를 문자열로 변환하여 붙이고, 
마지막에 정수로 변환하여 더해주는 방식을 사용하고 있습니다. 이 과정에서 문자열의 불변성으로 인해 반복문마다 새로운 문자열을 생성하고 연결하는 연산이 수행되므로 성능 저하가 발생할 수 있습니다. 

대신에 odd와 even을 정수형 리스트로 초기화하고, 짝수와 홀수를 각각 해당 리스트에 추가하여 더하는 방식으로 개선할 수 있습니다.

개선된 코드는 아래와 같습니다.
"""
