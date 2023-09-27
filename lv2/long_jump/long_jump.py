def solution(n):
    MOD = 1234567 # MOD 값을 상수로 정의하여 코드 가독성 향상
    if n == 1:
        return 1 # 1칸일 때는 1가지 방법만 존재
    if n == 2:
        return   # 2칸일 때는 2가지 방법이 존재
    
    ways = [0] * (n+1) # n까지 도달하는 방법의 수를 저장할 리스트
    ways[1], ways[2] = 1, 2
    
    for i in range(3, n+1):
        # 이전 칸과 그 이전 칸에서 현재 칸으로 도달하는 방법의 수를 합하고, MOD로 나눈 나머지를 저장
        ways[i] = (ways[i - 1] + ways[i - 2]) % MOD
    return ways[n]  # 최종 결과 반환

solution(6)