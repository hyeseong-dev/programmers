def solution(word):
    count_p = 0
    count_y = 0

    for char in word:
        char_lower = char.lower()
        if char_lower == 'p':
            count_p += 1
        if char_lower == 'y':
            count_y += 1
    return count_p == count_y
    
    
