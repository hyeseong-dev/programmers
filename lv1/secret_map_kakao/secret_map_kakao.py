from typing import List

def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    answer = []
    for i in range(n):
        # Use Python's format string to generate a binary number of n bits
        bin_num1 = format(arr1[i], f'0{n}b')
        bin_num2 = format(arr2[i], f'0{n}b')

        temp = ''
        for bin1, bin2 in zip(bin_num1, bin_num2):
            if bin1 == '1' or bin2 == '1':
                temp += '#'
            else:
                temp += ' '

        answer.append(temp)
    return answer

parameter = [
    5, 
    [9, 20, 28, 18, 11],
    [30, 1, 21, 17, 28]
]

result = solution(parameter[0],parameter[1],parameter[2])
