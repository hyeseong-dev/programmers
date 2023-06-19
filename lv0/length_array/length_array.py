def solution(strlist):
    answer = []
    for item in strlist:
        answer.append(len(item))
    return answer

example1 = ["We", "are", "the", "world!"]
print(solution(example1))