def solution(my_string, letter):
    answer = ''.join([char for char in my_string if char != letter])   
    return answer


params = [
    ["abcdef","f","abcde"],
    ["BCBdbe","B","Cdbe"]
]
for case in params:
    display = solution(case[0], case[1])
    assert display == case[2]
    print('성공했습니다.')
