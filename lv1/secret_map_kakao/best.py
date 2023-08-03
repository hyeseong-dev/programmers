from typing import List

def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    answer = []
    for i in range(n):
        # Apply binary OR operation and then convert it to binary number
        # Convert the binary number to the string of n bits
        # Replace 1 with '#' and 0 with ' '
        row = format(arr1[i] | arr2[i], f'0{n}b').replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer

parameter = [
    5, 
    [9, 20, 28, 18, 11],
    [30, 1, 21, 17, 28]
]

result = solution(parameter[0],parameter[1],parameter[2])
