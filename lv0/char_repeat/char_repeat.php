<?php
def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += (char * 3)
    
    return answer

params = [
    "hello",	3,	"hhheeellllllooo"
]

result = solution(params[0], params[1])
print(result)