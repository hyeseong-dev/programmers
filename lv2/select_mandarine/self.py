def solution(k, tangerine):
    mandarin_count = {}

    for size in tangerine:
        if size not in mandarin_count:
            mandarin_count[size] = 1
        else:
            mandarin_count[size] += 1

    sorted_mandarin = sorted(mandarin_count.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for i, (size, amount) in enumerate(sorted_mandarin):
        count += amount
        if count >= k:
            return i + 1

    return len(mandarin_count)


# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 결과: 3
print(solution(2, [1, 1, 2, 2, 3, 3, 4, 4]))  # 결과: 1