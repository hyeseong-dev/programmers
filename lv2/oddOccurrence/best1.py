def solution(A):
    unpaired_elements = set()
    
    for number in A:
        # 숫자가 세트에 있으면 제거, 없으면 추가
        if number in unpaired_elements:
            unpaired_elements.remove(number)
        else:
            unpaired_elements.add(number)
    
    # 세트에 남아있는 원소가 짝이 없는 원소
    return unpaired_elements.pop()

# 예제로 주어진 배열을 사용하여 함수 테스트
A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))  # 결과: 7
