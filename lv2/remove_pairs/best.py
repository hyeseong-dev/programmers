raw_data = 'cdbaabdc'

def solution(raw_data):
    stack = []

    for char in raw_data:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        return 1
    else:
        return 0


print(solution(raw_data))