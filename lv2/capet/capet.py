def solution(brown, yellow):
    
    total = brown + yellow                          # 갈색과 노란색 격자 수를 합해서 총 격자 수를 구합니다.

    for width in range(total, 2, -1):               
        if total % width == 0:
            height = total // width 
        
            if (width - 2) * (height -2) == yellow:
                return [width, height]
    return None