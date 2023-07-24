def soulution(s):
    answer = [0, 0]

    bin_str = s

    while len(bin_str) > 1:
        answer[1] += bin_str.count('0') # 제거할 0의 개수
        a = bin_str.replace('0', '')    # 0을 제거한 이진수 문자
        len_a = len(a)                  # 0을 제거한 이진수 문자의 수
        bin_str = bin(len_a)[2:]                  # prefix로 붙은 OB를 제거하고 0을 제거한 이진수 문자의 십진수를 다시 이진수로 만듬
        answer[0] += 1

    return answer


soulution('110010101001')