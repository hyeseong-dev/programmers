def solution(want, number, discount):
    DAYS = 10
    required_items = dict(zip(want, number))
    match_days = 0

    for i in range(len(discount) - DAYS + 1):
        items_in_period = discount[i:i+DAYS]
        if required_items == count_items(items_in_period):
            match_days += 1
    return match_days
    
def count_items(want, arr):
    return {name: arr.count(name) for name in want}