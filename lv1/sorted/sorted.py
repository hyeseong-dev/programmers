def solution(s):
    return int(''.join(reversed(sorted(str(s)))))


# 시간 복잡도(Time Complexity): 이 함수의 복잡도는 주로 sorted() 함수에 의해 결정됩니다. sorted() 함수는 팀소트 알고리즘을 사용하며, 이는 O(n log n)의 시간 복잡도를 가집니다. 
# 여기서 n은 입력 문자열의 길이입니다. reversed()와 join()은 각각 O(n)의 시간을 소요합니다. 
# 그러나 이들은 sorted()에 비해 무시할 수 있는 수준의 시간을 소요하므로, 
# 
# 전체 시간 복잡도는 O(n log n)입니다.

# 공간 복잡도(Space Complexity): sorted() 함수는 새로운 리스트를 반환하므로 O(n)의 공간을 사용합니다. 
# reversed() 함수는 반복 가능한 객체를 반환하며, 추가적인 공간을 필요로 하지 않습니다. join() 함수는 결합된 문자열을 반환하며, 
# 이는 입력 문자열의 크기와 같으므로 O(n)의 공간을 사용합니다. 따라서 
# 
# 전체 공간 복잡도는 O(n)입니다