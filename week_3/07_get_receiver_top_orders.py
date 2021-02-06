top_heights = [6, 9, 5, 7, 4]


# for idx in range((5-1), -1, -1):
# 강의에서 "우리가 비교할 거는 결국 인덱스부터 시작이기 때문이에요."
# 라고 했는데 이게 무슨 말이지?


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights: # O(N) -> O(N^2)
        height = heights.pop()  # heights에서 하나 뺏으니까 지금 len(heights)는 4
        for idx in range(len(heights) - 1, -1, -1): #O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
