def solution(num):
    count = 0
    while num !=1:
        if count > 500:
            return -1
        elif num % 2 ==0:
            num = num / 2
        else : 
            num = num * 3 + 1
        count += 1
    return count


# 이 함수의 시간 복잡도는 O(500)이며, 실질적으로는 O(1)로 간주될 수 있습니다. 이는 루프가 최대 500회만 반복되기 때문입니다. 공간 복잡도는 O(1)입니다. 이 함수는 입력 크기에 상관없이 상수 개수의 변수만을 사용하므로 공간 복잡도는 상수입니다.