def solution(num_list, n):
    answer = []
    for idx in range(0, len(num_list), n):
        item = num_list[idx]
        answer.append(item)
    return answer

params = [
[[4, 2, 6, 1, 7, 6],	2,	[4, 6, 7]],
[[4, 2, 6, 1, 7, 6],	4,	[4, 7]],
]

for param in params:
    result = solution(param[0], param[1])
    assert result == param[2]
    print(result)

"""
위 코드의 시간 복잡도는 O(N), 공간 복잡도는 O(N)입니다. N은 num_list의 길이를 나타냅니다.

코드를 개선하여 시간 복잡도를 개선할 수 있습니다. 현재 코드에서는 매 반복마다 answer 리스트에 append 연산을 수행하고 있으므로, 
이 과정에서 리스트의 크기가 커질수록 성능 저하가 발생할 수 있습니다. 
대신에 리스트 컴프리헨션을 사용하여 한 번에 요소를 생성하는 방식으로 개선할 수 있습니다. 이를 통해 추가적인 반복문이 없이도 원하는 결과를 얻을 수 있습니다.
"""
