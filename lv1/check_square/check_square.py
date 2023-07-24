def solution(n):
    check_square = n ** 0.5
    if (check_square).is_integer():
        return (check_square + 1) ** 2
    return -1

# 시간 복잡도(Time Complexity): 이 함수는 제곱근 계산과 정수 판별, 그리고 선택적으로 제곱 계산을 수행합니다. 이러한 모든 연산들은 상수 시간을 소요하므로, 이 함수의 시간 복잡도는 O(1)입니다.

# 공간 복잡도(Space Complexity): 이 함수는 입력 n 및 check_square를 저장하는 데에 공간을 사용합니다. 이러한 변수들은 고정된 크기를 가지며, 입력 크기에 따라 변하지 않습니다. 따라서 이 함수의 공간 복잡도 역시 O(1)입니다.