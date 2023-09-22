def solution(s):    
    word = list(s)
    left = 0
    right = 1

    while right < len(word):
        # 같은 문자를 찾았을 경우
        if word[left] == word[right]:
            # left와 right 포인터가 가리키는 문자를 제거
            word[left] = word[right] = ''

            # left 포인터를 왼쪽으로 이동시키며, 비어있는 곳을 찾지 않도록 한다.
            left -= 1
            while left >= 0 and word[left] == '':
                left -= 1

            # left가 -1이면 왼쪽 끝으로 이동한 것이므로 right 바로 앞으로 이동
            if left == -1:
                left = right - 1

            # right는 다음 위치로 이동
            right += 1
        else:
            # 같은 문자를 찾지 못했을 경우, 포인터들을 이동
            left = right
            right += 1

    # 남은 문자들 중 빈 문자열이 아닌 것이 있으면 0, 아니면 1을 반환
    return 0 if any(word) else 1

print(solution('baabaa'))
