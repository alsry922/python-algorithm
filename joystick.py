from string import ascii_uppercase

alphabet = list(ascii_uppercase)

name = input()


def get_count(i, start, end):
    mid = (start + end) // 2

    if i < alphabet[mid]:
        return get_count(i, start, mid)
    elif i > alphabet[mid]:
        return get_count(i, mid + 1, end)
    else:
        return mid


def solution(name):
    mid = (len(alphabet) // 2) - 1
    count_a = 0
    move_next = len(name) - 1
    answer = 0

    for i in name:
        if i == "A":
            count_a += 1
            continue

        if i < alphabet[mid]:
            count = get_count(i, 0, mid)
            answer += count
        elif i > alphabet[mid]:
            count = len(alphabet) - get_count(i, mid + 1, len(alphabet) - 1)
            answer += count
        else:
            answer += mid
    answer += move_next

    if count_a >= len(name) // 2:
        answer -= count_a
    else:
        answer += count_a

    return answer


print(solution(name))
