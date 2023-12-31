def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if int(num**0.5)**2 == num:  # 제곱수의 판별
            answer -= num
        else:
            answer += num
    return answer


parameters = [
    13,	17,	43,
]

result = solution(parameters[0], parameters[1])
print(result)

# 먼저, 주어진 문제는 각 숫자의 약수의 개수가 짝수인지 홀수인지를 판단하는 것이 중요한 포인트입니다. 자연수의 약수는 일반적으로 쌍으로 존재합니다. 예를 들어 12의 약수는 1, 2, 3, 4, 6, 12로, 이 중 1과 12, 2와 6, 3과 4는 서로 쌍을 이룹니다.

# 하지만 제곱수의 경우에는 약수의 개수가 홀수가 됩니다. 예를 들어 9의 약수는 1, 3, 9로 1과 9는 쌍을 이루지만 3은 쌍을 이루지 않습니다. 따라서 이를 활용하면 시간 복잡도를 줄일 수 있습니다.

# 이렇게 개선하면, 시간 복잡도는 O(n)으로 줄어들고 공간 복잡도는 O(1)이 됩니다. 
# 여기서 n은 'right' - 'left'의 값입니다. 이는 각 숫자에 대해 한 번씩만 연산을 수행하기 때문입니다. 또한, 추가적인 저장 공간을 사용하지 않기 때문에 공간 복잡도도 줄어듭니다.


# num**0.5에서 0.5는 제곱근을 구하는 연산입니다. 
# num**0.5는 'num'의 제곱근을 의미합니다. 예를 들어, 만약 num이 9라면, num**0.5는 3이 됩니다.
# 다음으로 int(num**0.5)**2에서 2는 제곱을 의미합니다. 따라서 int(num**0.5)**2는 'num'의 제곱근을 구한 뒤에 그 결과를 정수로 만든 것을 다시 제곱한 것을 의미합니다. 이렇게 하는 이유는 'num'이 제곱수인지를 판단하기 위함입니다.
# 예를 들어, 만약 num이 9(제곱수)라면, int(num**0.5)는 3이고, int(num**0.5)**2는 다시 9가 되어 원래의 num과 같습니다. 따라서 이렇게 연산한 결과가 원래의 num과 같으면 num은 제곱수라는 것을 알 수 있습니다.
# 하지만, 만약 num이 8(제곱수가 아님)이라면, int(num**0.5)는 2이고, int(num**0.5)**2는 4가 되어 원래의 num과 다릅니다. 따라서 이런 경우 num은 제곱수가 아님을 알 수 있습니다.