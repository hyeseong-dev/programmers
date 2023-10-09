def solution(want, number, discount):
    DAYS = 10 # 10일 동안 
    temp = dict(zip(want, number))
    total = 0

    period = len(discount)- DAYS + 1
    for i in range(period):
        item_checks = discount[i:DAYS+i]
        if temp == filter_items(item_checks):
            total += 1
        else:
            pass
    return total
    
def filter_items(arr):
    result = {}
    for name in arr:
        if name not in result:
            result[name] = 1
        else:
            result[name] += 1
    return result

            
want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
result = solution(want, number, discount)
print(result == 0)

