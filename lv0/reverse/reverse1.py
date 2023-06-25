
'''
하나. 위 코드의 시간 복잡도와 공간 복잡도는 다음과 같습니다:

시간 복잡도: O(n^2). 이는 각 문자열이 문자 하나씩 역순으로 새로운 문자열에 추가될 때마다 문자열 전체를 복사하기 때문입니다. 
여기서 n은 입력 문자열의 길이입니다.
공간 복잡도: O(n). 새로운 문자열 'answer'이 입력 문자열과 같은 크기의 메모리를 사용하기 때문입니다.

둘. 위 코드를 최적화하기 위해 Python의 문자열 슬라이싱을 이용하여 문자열을 역순으로 만들 수 있습니다. 
이는 시간 복잡도를 O(n)으로 줄이며, 공간 복잡도 역시 O(n)으로 유지됩니다.
'''

def solution(my_string):
    return ''.join(reversed(my_string))

params = [
    ["jaron","noraj"],
    ["bread","daerb"],
]

for original, reversed_str in params:
    result = solution(original)
    print(f'결과: {result}, 예상결과: {reversed_str}')
    print('통과' if result == reversed_str else '실패')