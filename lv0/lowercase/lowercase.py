def to_lowercase(string):
    result = ""
    for char in string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def solution(myString):
    
    return to_lowercase(myString)


# Python에서 lower() 함수를 직접 구현하려면 ASCII 값에 대한 이해가 필요합니다. 
# 대문자 A-Z의 ASCII 값은 65-90이며, 소문자 a-z의 ASCII 값은 97-122입니다. 
# 따라서 대문자를 소문자로 바꾸려면 각 문자의 ASCII 값에 32를 더하면 됩니다.

# 이 코드에서 ord() 함수는 문자의 ASCII 값을 반환하며, chr() 함수는 주어진 ASCII 값을 문자로 변환합니다. 
# 따라서 대문자인 경우 (즉, ASCII 값이 65-90 사이인 경우), 32를 더해서 대응하는 소문자로 바꾸고, 그렇지 않은 경우에는 원래 문자를 그대로 사용합니다.