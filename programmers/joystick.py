def solution(name):
    answer = 0
    name = list(name)
    idx = 0
    while True:
        right_move = 1  # 오른쪽으로 이동
        left_move = 1  # 왼쪽으로 이동

        # 문자를 바꿔야 한다면 더 적은 횟수로 바꾼후 A로 업데이트
        if name[idx] != "A":
            answer += min(ord(name[idx]) - ord("A"), ord("Z") - ord(name[idx]) + 1)
            name[idx] = "A"

        # name의 모든 문자가 A로 업데이트 됐다면 while loop 종료
        if name == ["A"] * len(name):
            break

        # 바꿔야 할 문자가 남았다면 현재 위치에서
        # 좌우로 'A'가 아닌 곳을 가장 빠르게 만나는 위치를 비교(A문자는 바꿀 필요가 없으므로)
        else:
            for i in range(1, len(name)):
                if name[idx + i] == "A":
                    right_move += 1
                else:
                    break

                if name[idx - i] == "A":
                    left_move += 1
                else:
                    break

            if right_move > left_move:
                answer += left_move
                idx -= left_move
            else:
                answer += right_move
                idx += right_move

    return answer


name = input()
print(solution(name))