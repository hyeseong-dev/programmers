def solution(arr, query):
    for item in query:
        if (item % 2) == 0: 
            arr = arr[:item+1]
        else:
            arr = arr[item:]
    return arr

params = [
    [[0, 1, 2, 3, 4, 5],	[4, 1, 2],	[1, 2, 3]]
]

for param in params:
    result = solution(param[0], param[1])
    print(f"결과값 : {result}     기대값: {param[2]}")