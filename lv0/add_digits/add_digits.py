def solution(n):
    return sum([int(i) for i in str(n)])

print(solution(123))

'''
주어진 코드의 시간 복잡도는 O(d), 공간 복잡도는 O(d)입니다. 여기서 d는 입력된 숫자 n의 자릿수입니다.

 주어진 코드는 입력된 숫자 n을 문자열로 변환한 후, 각 자리 숫자를 정수로 변환하여 리스트에 저장하고 있습니다. 
이후 리스트의 모든 원소를 합산하여 반환하고 있습니다. 따라서 자릿수에 비례하여 각 자리 숫자를 처리하는 시간이 소요되며, 
리스트를 생성하여 저장하기 때문에 공간 복잡도도 자릿수에 비례합니다.

개선할 수 있는 부분이 있다면, 숫자의 각 자리 수를 더하는 과정을 반복문 없이 수학적으로 처리하는 방법을 사용할 수 있습니다.
'''