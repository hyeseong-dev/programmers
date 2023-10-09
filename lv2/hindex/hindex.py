import math

def custom_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def solution(citations):
    n = len(citations)
    h = custom_round(sum(citations) / n)


    dic_citations = {idx: value for idx, value in enumerate(citations)}
    
    dic_gte = {idx: val for idx, val in dic_citations.items() if val >= h}
    dic_lte = {idx: val for idx, val in dic_citations.items() if idx not in dic_gte}

    result = False
    if len(dic_gte) >= h and dic_lte :
        for val in dic_lte.values():
            if val <= h:
                result = True
        return h if result is True else 0
    else:
        return h 


citations =  [5, 6, 7, 8, 9, 10]

result = solution(citations)
print(result)
