# def solution(l, r):
#     answer = []
#     for num in range(l, r+1):
#         str_num = str(num)
#         for num_char in str_num:
#             if num_char not in ('0', '5'):
#                 break
#         else:
#             answer.append(num)
#     if not answer:
#         return [-1]
#     return answer


# params = [
#     5,	555,	[5, 50, 55, 500, 505, 550, 555],
# ]

# result = solution(params[0], params[1])
# print(result)

"""
1. 시간 복잡도: 이 알고리즘은 O(N * M)입니다, 여기서 N은 l과 r 사이의 숫자의 수 (즉, r - l + 1)이고, M은 각 숫자의 자릿수입니다. 
각 숫자에 대해 자릿수를 반복하므로 숫자의 수와 숫자의 자릿수 모두에 비례하는 복잡도가 있습니다.

2. 공간 복잡도: 이 알고리즘은 O(N)입니다. 결과를 저장하는 데 필요한 공간이 입력 크기에 비례하기 때문입니다. 
최악의 경우에는 l과 r 사이의 모든 숫자가 "0"과 "5"로만 구성되어 있을 수 있으므로, 이들 모두를 저장해야 합니다.


3. 시간 복잡도 개선: 시간 복잡도는 이미 입력 크기에 비례하므로 이를 더욱 개선하는 것은 어렵습니다. 하지만 코드를 다소 최적화하여 약간의 성능 향상을 얻을 수 있습니다.


4. `if set(str(num)) <= {'0', '5'}:`
이 부분의 코드는 set(str(num))이 {'0', '5'}의 부분집합인지 확인합니다.

여기서 str(num)은 num의 문자열 표현을 만듭니다. 이 문자열 표현을 set()에 전달하면, 각 자릿수(문자)를 요소로 하는 집합이 만들어집니다.

예를 들어, num이 505라면 str(num)은 '505'가 되고, set(str(num))은 {'5', '0'}이 됩니다.

<= 연산자는 집합의 부분집합 여부를 확인하는데 사용됩니다. 즉, A <= B는 "A가 B의 부분집합인가?"를 의미합니다.

따라서 set(str(num)) <= {'0', '5'}은 num의 각 자릿수가 '0' 또는 '5'인지 확인하는 것과 동일합니다. 즉, 이 코드는 num이 '0'과 '5'로만 이루어진 숫자인지 확인합니다.
"""

def solution(l, r):
    # answer = [num for num in range(l, r+1) if set(str(num)) <= {'0', '5'}]
    answer = []
    for num in range(l, r+1):
        if set(str(num)) <= {'0', '5'}:
            answer.append(num)
    if answer:
        return answer
    else :
        return [-1]


params = [
    5,	555,	[5, 50, 55, 500, 505, 550, 555],
]

result = solution(params[0], params[1])
print(result)  # [5, 50, 55, 500, 505, 550, 555]



