def solution(a, b, c, d):
    answer = 0
    if a == b and b == c and c == d:
        return 1111 * a
    elif (answer := condition2(a,b,c,d)) is not False:
        return answer
    elif (answer := condition3(a,b,c,d)) is not False:
        return answer
    elif (answer := condition4(a,b,c,d)) is not False:
        return answer
    elif (answer := condition5(a,b,c,d)) is not False:
        return answer


def condition2(a, b,c, d):
    if   (a == b == c) and a != d: return ((10*a) + d) ** 2
    elif (a == c == d) and a != b: return ((10*a) + b) ** 2
    elif (b == c == d) and a != b: return ((10*a) + b) ** 2
    else :                         return False
    
def condition3(a, b, c, d):
    if (a == b) and (c == d)  : return (a+c) * abs(a-c)
    elif (a == c) and (b == d): return (a+b) * abs(a-b)
    elif (a == d) and (b ==c ): return (a+b) * abs(a-b)
    elif (b == c) and (a == d): return (b+a) * abs(b-a)
    elif (b == d) and (a == c): return (b+a) * abs(b-a)
    elif (c == d) and (a == b): return (c+a) * abs(c-a) 
    else                      : return False
    
def condition4(a, b, c, d):
    pair1 = a, b
    pair2 = a, c
    pair3 = a, d
    pair4 = b, c 
    pair5 = b, d
    pair6 = c, d

    if pair1[0] == pair1[1] and c!=d and c != a:    return c * d
    elif pair2[0] == pair2[1] and b!=d and b != a:  return b * d
    elif pair3[0] == pair3[1] and b!=c and b != a:  return b * c
    elif pair4[0] == pair4[1] and a!=d and c != a:  return a * d
    elif pair5[0] == pair5[1] and a!=c and c != a:  return a * c
    elif pair6[0] == pair6[1] and a!=b and c != a:  return a * b
    else                                         :  return False

def condition5(a,b,c,d):
    array = [a,b,c,d]
    if len(set(array)) == 4:return min(array)
    else :False

"""
채점 결과
정확성: 85.7
합계: 85.7 / 100.0
"""