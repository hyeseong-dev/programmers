def next_square_if_square(n):
    root = n ** 0.5
    return (root + 1) ** 2 if root.is_integer() else -1

# 시간 공간 복잡도를 개선할 수 있는 방법:

# 함수의 가독성을 약간 향상시킬 수 있습니다. 함수의 이름을 is_integer_sqrt에서 보다 명확한 이름으로 변경하고, 코드의 몇 부분을 간결하게 만들 수 있습니다.