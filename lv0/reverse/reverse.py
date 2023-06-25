def solution(my_string):
    answer = ''
    for i in my_string:
        answer = i + answer
    return answer

params = [
    ["jaron","noraj"],
    ["bread","daerb"],
]

for i in params:
    result = solution(params[0][0])
    print(result, params[0][1])
    if result == params[0][1]:
        
        print('통과')
    else:
        
        print('실패')