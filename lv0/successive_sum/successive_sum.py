def solution(common):
    is_arith, diff = is_arithmetic_sequence(common)
    if is_arith and diff is not None:
        return common[-1] + diff
    
    is_geo, ratio = is_geometric_sequence(common)
    if is_geo and ratio is not None:
        return common[-1] * ratio

# 등차 수열 확인
def is_arithmetic_sequence(sequence):
    difference = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i-1] != difference:
            return False, None
    return True, difference

def is_geometric_sequence(sequence):
    if sequence[0] == 0:
        return False, None
    ratio = sequence[1] / sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] / sequence[i-1] != ratio:
            return False, None
    return True, ratio
            

# 등비 수열 확인
params = [1, 2, 3, 4],	5
params = [2, 4, 8],	16
result = solution(params[0])
print(result)
assert result == result