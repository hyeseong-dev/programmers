# 시간복잡도 O(n) -> 더 개선 불가. 그렇지만 리스트 컴프리헨션으로 리팩토링 가능 

def solution(strlist):
    return [len(item)for item in strlist]


example1 = ["We", "are", "the", "world!"]
print(solution(example1))

# lambda 함수 
# solution = lambda strlist: list(map(len, strlist))
