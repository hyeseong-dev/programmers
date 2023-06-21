def solution(numbers):
    a = b = 0
    max_item = max(numbers)
    max_index = numbers.index(max_item)
    a = numbers.pop(max_index)
    max_item = max(numbers)
    max_index = numbers.index(max_item)
    b = numbers.pop(max_index)
    
    return a * b

print(solution([1,2,3,4,5]))