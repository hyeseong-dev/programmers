from typing import List

def solution(numbers: List[int]) -> int:
    max_val: int = max(numbers)
    numbers.remove(max_val)
    second_max_val: int = max(numbers)
    return max_val * second_max_val