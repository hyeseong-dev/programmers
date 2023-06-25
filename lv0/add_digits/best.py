def solution(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum


"""
위 개선된 코드에서는 주어진 숫자 n을 10으로 나눈 나머지를 구하여 각 자리 숫자를 더하고 있습니다.
 그 후 n을 10으로 나눈 몫으로 갱신하여 다음 자리 숫자를 처리합니다.
 이를 반복하여 모든 자리 숫자를 처리하고, 자릿수의 합을 반환합니다.

개선된 코드는 시간 복잡도는 여전히 O(d)이지만, 리스트를 생성하고 저장하는 공간을 사용하지 않아 공간 복잡도가 O(1)로 개선됩니다. 
또한 반복문 없이 수학적으로 처리하기 때문에 약간의 성능 개선을 기대할 수 있습니다.
"""