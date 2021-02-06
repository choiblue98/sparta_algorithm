from collections import deque

c = 11
b = 2


# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직인다.
# 즉 증가하는 속도가 1초마다 1씩 증가.
# 속도
# 1 2 3 4 5 6 7 8 9
# 위치
# 3 4 6 9 13 18

# 브라운의 위치 변화
# B - 1, B + 1, 2 * B -> 변화무쌍
# 경우의 수가 너무 많고 쉽게 일반화되어지지 않을 것 같은 문제: '모든 경우의 수를 다 나열해야겠구나.'
# BFS를 써야겠구나

# 잡았다 = 똑같은 시간에 똑같은 위치에 존재
# 시간은 + 1, 위치는 코니도 브라운도 자유자재로 변화
# 규칙적 -> 배열, 자유자재 -> 딕셔너: 각 시간마다 브라운이 갈 수 있는 위치를 저장하자.
# [{}]


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    visited = [{} for _ in range(200001)]
    # visited[0] = {
    #     2: True
    # }
    # visited[1] = {
    #     1: True,
    #     3: True,
    #     4: True
    # }
    # visited[위치][시간] -> visited[3]에 5라는 키가 있냐 = 3 위치에 5초에 간 적이 있냐

    while cony_loc <= 200000:
        cony_loc += time  # 시간만큼 더해지니까
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

    # 구현해보세요!
    return - 1


print(catch_me(c, b))  # 5가 나와야 합니다!
