def solution(my_string, n):
    return ''.join([char *n for char in my_string])

params = [
    "hello",	3,	"hhheeellllllooo"
]

result = solution(params[0], params[1])
print(result)

"""
개선된 코드에서는 리스트 컴프리헨션을 사용하여 문자열을 구성하고, join() 함수를 통해 리스트 요소들을 하나의 문자열로 합칩니다. 이를 통해 반복문을 사용하지 않고도 문자열을 구성할 수 있으며, 시간 복잡도를 개선할 수 있습니다.

개선된 코드의 시간 복잡도는 O(M)이며, 공간 복잡도는 O(M * N)으로 동일합니다. 문자열을 구성하는 데 필요한 공간은 여전히 M * N 크기입니다.
"""