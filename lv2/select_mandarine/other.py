def solution(k, tangerine):
    answer = 0
    
    ###1###
#    typeOfTangerine = list(set(tangerine))
    typeNumber = {}
    
    ###2###
    for i in tangerine:
        if i in typeNumber:
            typeNumber[i] += 1
        else:
            typeNumber[i] = 1
 
    ###3###
    sortedTypeNumber = sorted(typeNumber.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sortedTypeNumber)):
        k -= sortedTypeNumber[i][1]
        answer += 1
        if k >= 0:
            break
 
    return answer