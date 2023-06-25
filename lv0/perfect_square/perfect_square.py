def is_square(n):
    if n < 0:
        return False
    sqrt = n ** 0.5
    return sqrt == int(sqrt)

# 테스트
print(is_square(16))  # True
print(is_square(15))  # False