def solution(s):    
    word = s
    left = 0
    right = 1

    temp = ''
    while len(word) > 0:
        if right >= len(word):
            if len(temp) > 0:
                word = temp
                left = 0
                right = 1
                temp = ''
            else:
                break

        elif word[left] == word[right]:
            word = f"{temp}{word[right+1:]}"
            left = 0
            right = 1
            temp = ''
        else:
            temp += word[left]
            left += 1
            right += 1
    return 0 if len(word) > 0 else 1



print(solution('baabaa'))
print(solution('cdcd'))
