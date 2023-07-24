def solution(x, n):
    answer = []
    while len(answer) < n:
        answer.append(x)
        x+=answer[0]
    return answer



params = [
    [2,	5,	[2,4,6,8,10]]
]

for param in params:
    result = solution(param[0], param[1])
    print(result)


# 주어진 solution 함수의 시간 복잡도는 O(n)입니다. while 루프는 len(answer)가 n보다 작은 동안 반복하므로 최대 n번 반복합니다. 
# 각 반복에서 answer.append(x) 연산은 O(1)의 시간 복잡도를 가지며, x += answer[0] 연산도 O(1)의 시간 복잡도를 가집니다. 
# 따라서 전체 시간 복잡도는 O(n)입니다. 
# 
# 공간 복잡도는 answer 리스트에 n개의 요소를 저장하므로 O(n)입니다.