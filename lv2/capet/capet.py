def solution(brown, yellow):
    total = brown + yellow  # 갈색과 노란색 격자 수를 합해서 총 격자 수를 구합니다.

    # 카펫의 가로와 세로 크기를 찾는 반복문
    for width in range(total, 2, -1):  # 총 격자 수부터 2까지 1씩 감소하는 범위에서 반복합니다.
        if total % width == 0:  # 현재 가로 크기로 총 격자 수를 나누어 떨어지면 유효한 가로 크기입니다.
            height = total // width  # 가로 크기로 총 격자 수를 나눈 몫을 세로 크기로 설정합니다.

            # 노란색 격자의 수와 카펫의 크기를 비교하여 일치하면 해당 가로와 세로 크기는 유효한 카펫의 크기입니다.
            if (width - 2) * (height - 2) == yellow:
                return [width, height]  # 유효한 가로와 세로 크기를 리스트로 묶어서 반환합니다.

    # 반복문을 모두 검사하고도 유효한 카펫의 크기를 찾지 못하면 None을 반환합니다.
    return None

print(solution(10, 2))