def solution(myString):
    return myString.upper()


params = [
["aBcDeFg",	"ABCDEFG"],
["AAA",	"AAA"],
]

for param in params:
    result = solution(param[0])
    assert result == param[1]
    print(result)


"""
위 코드의 시간 복잡도는 입력된 문자열의 길이에 비례합니다. 
따라서 O(n)입니다. 공간 복잡도는 추가적인 데이터 구조나 메모리 사용 없이 주어진 문자열을 대문자로 변환하여 반환하기 때문에 O(1)입니다.

위 코드는 이미 간단하고 효율적이기 때문에 개선할 수 있는 부분이 없습니다. 이미 대문자로 변환하는 내장 함수인 upper()를 사용하고 있으며, 
시간 복잡도와 공간 복잡도도 최적화되어 있습니다.
"""