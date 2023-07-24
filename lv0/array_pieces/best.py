def solution(arr, query):
    start = 0
    end = len(arr)
    for i, item in enumerate(query):
        if i % 2 == 0:
            end = start + item + 1
        else:
            start = start + item
    return arr[start:end]

params = [
    [[0, 1, 2, 3, 4, 5], [4, 1, 2], [1, 2, 3]]
]

for param in params:
    result = solution(param[0], param[1])
    print(f"결과값 : {result}     기대값: {param[2]}")

"""
시간복잡도와 공간복잡도 모두 O(1)

이 함수는 주어진 'arr' 배열에 대한 서브 배열을 반환합니다. 이 서브 배열은 'query' 배열의 각 요소에 따라 결정됩니다.

우리는 'start'와 'end' 두 개의 변수를 사용합니다. 이 변수들은 현재 서브 배열의 시작과 끝 인덱스를 나타냅니다. 초기에 'start'는 0으로, 'end'는 배열 'arr'의 길이로 설정됩니다.

그 후에, 'query'의 각 요소에 대해 다음을 수행합니다:

현재 요소의 인덱스가 짝수인 경우, 'end'를 'start' + 현재 'query' 요소의 값 + 1로 업데이트합니다. 즉, 'query' 요소의 값만큼 배열의 뒷부분을 잘라냅니다. 여기서 +1을 하는 이유는 배열의 인덱스가 0부터 시작하기 때문입니다.

현재 요소의 인덱스가 홀수인 경우, 'start'를 'start' + 현재 'query' 요소의 값으로 업데이트합니다. 즉, 'query' 요소의 값만큼 배열의 앞부분을 잘라냅니다.

최종적으로 'start'와 'end'가 표시하는 인덱스 사이의 배열을 반환합니다. 이 부분이 바로 'query'에 의해 결정된 서브 배열입니다.

이렇게 직접 배열을 수정하지 않고 'start'와 'end' 인덱스를 사용하여 배열의 일부를 추적하면, 시간복잡도와 공간복잡도를 모두 O(1)로 줄일 수 있습니다. 이는 실제로 배열을 수정하는 대신에 인덱스만 업데이트하기 때문입니다. 이러한 접근 방식은 매우 큰 입력에 대해 효율적입니다.
"""