def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += (char * 3)
    
    return answer

params = [
    "hello",	3,	"hhheeellllllooo"
]

result = solution(params[0], params[1])
print(result)


"""
위 코드의 시간 복잡도는 O(M * N)입니다. 여기서 M은 입력 문자열 my_string의 길이이고, N은 반복 횟수입니다.
반복문을 통해 문자열의 각 문자를 순회하고, 각 문자를 N번 반복하여 결과 문자열에 추가하기 때문에 시간 복잡도는 입력 크기에 선형적으로 비례합니다.

공간 복잡도는 O(M * N)입니다. 코드에서는 결과 문자열을 생성하는 데 필요한 공간을 사용하고 있습니다.
입력 문자열의 길이가 M이고 반복 횟수가 N이므로, 결과 문자열의 길이는 M * N이 될 수 있습니다.
따라서 결과 문자열을 저장하기 위해 M * N 크기의 공간이 필요하게 됩니다.

위 코드의 시간 복잡도를 개선하기 위해 리스트 컴프리헨션을 사용하여 문자열을 구성하는 방법을 사용할 수 있습니다.
이 방법을 사용하면 반복문을 사용하지 않고도 간단하게 문자열을 구성할 수 있습니다.
이를 통해 시간 복잡도를 O(M)으로 개선할 수 있습니다.
"""