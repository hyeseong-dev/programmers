def solution(polynomial):
    # 다항식을 각 항으로 분리합니다.
    terms = polynomial.split(' + ')

    # x의 계수와 상수항을 초기화합니다.
    x_coefficient, constant_term = 0, 0

    # 다항식의 각 항을 처리합니다.
    for term in terms:
        # 'x'가 있는 경우, x 항입니다.
        if 'x' in term:
            coefficient = term[:-1]
            # 계수가 없는 경우 1로 간주합니다.
            x_coefficient += int(coefficient) if coefficient else 1
        else:
            # 'x'가 없는 경우, 상수항입니다.
            constant_term = int(term)

    # 결과 문자열을 준비합니다.
    # x의 계수가 1인 경우와 그보다 큰 경우를 처리합니다.
    if x_coefficient > 1:    x_part = f'{x_coefficient}x'
    elif x_coefficient == 1: x_part = 'x'
    else:                    x_part = ''

    # 상수항이 0보다 큰 경우 상수항을 추가합니다.
    if constant_term > 0: constant_part = f' + {constant_term}'
    else:                 constant_part = ''

    # 최종 결과를 반환합니다.
    return x_part + constant_part


