def solution(l, r):
    answer = []
    for num in range(l, r+1):
        str_num = str(num)
        for num_char in str_num:
            if num_char not in ('0', '5'):
                break
        else:
            answer.append(num)
    if not answer:
        return [-1]
    return answer


params = [
    5,	555,	[5, 50, 55, 500, 505, 550, 555],
]

result = solution(params[0], params[1])
print(result)

"""
- 시간 복잡도: 이 알고리즘은 O(N * M)입니다, 여기서 N은 l과 r 사이의 숫자의 수 (즉, r - l + 1)이고, M은 각 숫자의 자릿수입니다. 
각 숫자에 대해 자릿수를 반복하므로 숫자의 수와 숫자의 자릿수 모두에 비례하는 복잡도가 있습니다.

- 공간 복잡도: 이 알고리즘은 O(N)입니다. 결과를 저장하는 데 필요한 공간이 입력 크기에 비례하기 때문입니다. 
최악의 경우에는 l과 r 사이의 모든 숫자가 "0"과 "5"로만 구성되어 있을 수 있으므로, 이들 모두를 저장해야 합니다.

"""