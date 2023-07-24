def solution(A, B):
    if A == B:
        return 0
    if A[-1] + A[:-1] == B:
        return 1
    return -1

params = [
    ["hello",	"ohell", 1],
    ["apple",	"elppa",- 1],
    ["atat",	"tata",	 1],
    ["abc",	"abc",	 0],
]

for param in params:
    result = solution(param[0], param[1])
    assert result == param[2]