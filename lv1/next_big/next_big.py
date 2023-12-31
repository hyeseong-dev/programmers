def solution(n):
    answer = 0
    len_n_bin = bin(n)[2:].count('1')
    for num in range(n+1, 1_000_000):
        if len_n_bin == bin(num)[2:].count('1'):    
            return num
        

solution(15)


# 시간 복잡도:
# 위의 코드는 n에서 1_000_000까지 순차적으로 반복하면서 각 숫자의 1의 개수를 세는 작업을 수행합니다. 
# 이때, 이진수 변환 및 1의 개수 세는 작업이 각 숫자에 대해 O(logM)의 시간이 걸립니다(M은 해당 숫자). 
# 따라서, 전체적인 시간 복잡도는 O(NlogM)으로 표현할 수 있습니다. 여기서 N은 1_000_000 - n입니다.

# 공간 복잡도:
# 위의 코드는 추가적인 배열이나 리스트를 사용하지 않으며, 변수 len_n_bin과 num만을 사용합니다. 따라서 공간 복잡도는 O(1)입니다.